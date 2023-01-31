import requests
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.dispatch import receiver
from django.conf import settings
from . import models
from MyResume.task_bg import Loop, Task

loop = Loop()


@receiver(post_save, sender=models.Contact)
def send_notification(sender, instance, created, **kwargs):
    if created:
        date_time_create = instance.date_time_create.strftime(settings.DATETIME_FORMAT)
        TITLE_NOTIFICATION = 'پیام جدید از سایت رزومه'
        TEXT_CONTENT = """
                 <h4 style="text-align:right;">
                     {name} | <b>{email}</b>
                 </h4>
                 <p>
                     {message}
                 </p>
                 <span style="font-size:90%">
                     {date_time_send}
                 </span>
             """.format(name=instance.name, email=instance.email, message=instance.message,
                        date_time_send=date_time_create)
        models.MessageNotif.objects.create(title=TITLE_NOTIFICATION, description=TEXT_CONTENT)
        if settings.USING_EMAIL_FOR_NOTIFICATION == True:
            send_with_email(TITLE_NOTIFICATION, TEXT_CONTENT)
        telegram_obj = models.TelegramBot.objects.first()
        if telegram_obj:
            TEXT_CONTENT = """
*{name}* | *{email}*

------------------------

{message}

------------------------

{date_time_send}
            """.format(name=instance.name, email=instance.email, message=instance.message,
                       date_time_send=date_time_create)
            send_with_telegram(telegram_obj, TEXT_CONTENT)


def send_with_email(subject, content):
    task_send_email = Task(send_mail, (subject, content, settings.EMAIL_HOST_USER, [settings.EMAIL_USER_RECEIVE]))
    loop.add(task_send_email)
    loop.start()

def send_with_telegram(telegram_obj, content):
    def send(content):
        bot_token = telegram_obj.token_bot
        bot_chatID = telegram_obj.chat_id
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + content
        response = requests.get(send_text)

    if telegram_obj.is_active == True:
        try:
            send(content)
        except:
            pass

