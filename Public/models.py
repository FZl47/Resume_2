from django.shortcuts import reverse
from django.db import models
from django.templatetags.static import static
from ckeditor.fields import RichTextField
from Public import mixins
from Public.cache import mixins as mixins_cache
from MyResume import Tools


def upload_image_src(instance,path):
    format_file = str(path).split('.')[-1]
    return f"images/{Tools.random_str()}.{format_file}"


class Information(mixins_cache.CacheMixin, models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    work_position = models.CharField(max_length=40)
    about = RichTextField()
    image = models.ImageField(upload_to=upload_image_src)
    phone_number = models.CharField(max_length=20,null=True,blank=True)
    email = models.CharField(max_length=100,null=True,blank=True)
    birthday = models.DateField(null=True,blank=True)
    location = models.CharField(max_length=200,null=True,blank=True)
    github_id = models.CharField(max_length=20,null=True,blank=True)
    telegram_id = models.CharField(max_length=20,null=True,blank=True)
    instagram_id = models.CharField(max_length=20,null=True,blank=True)
    linkdin_id = models.CharField(max_length=20,null=True,blank=True)


    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_image(self):
        return self.image.url



class Certificate(mixins_cache.CacheMixin, mixins.RemovePastFileWhenChangedMixin, models.Model):
    FIELDS_REMOVE_FILES = ('image',)

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=upload_image_src)
    link = models.CharField(max_length=100,null=True,blank=True)

    class Meta:
        ordering = '-id',

    def __str__(self):
        return self.title

    def get_image(self):
        return self.image.url


class Review(mixins_cache.CacheMixin, models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_showing = models.BooleanField(default=False)
    image = models.CharField(max_length=40)

    class Meta:
        ordering = '-id',

    def __str__(self):
        return self.name

    def get_image(self):
        return self.image


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class SkillManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('id','-linked')

class Skill(mixins_cache.CacheMixin, models.Model):
    title = models.CharField(max_length=50)
    percentage = models.IntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    is_showing = models.BooleanField(default=True)
    # this field makes object can be filtred or show as category
    linked = models.BooleanField(default=True)

    objects = SkillManager()

    def __str__(self):
        return self.title

    def get_slug_category(self):
        title = self.category.title.replace(' ','-')
        return f"{title}-{self.category.id}"



class WorkSampleManager(models.Manager):

    def get_by_slug(self,slug):
        id_obj = str(slug).split('-')[-1]
        try:
            return self.get_queryset().get(id=id_obj)
        except:return None


class WorkSample(mixins_cache.CacheMixin, models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField()
    views = models.BigIntegerField(default=0)
    skills = models.ManyToManyField('Skill')
    date_time_create = models.DateField(auto_now_add=True)
    gallery = models.ForeignKey('Gallery',on_delete=models.CASCADE)

    objects = WorkSampleManager()

    class Meta:
        ordering = '-id',

    def __str__(self):
        return self.title

    def get_cover(self):
        cover = self.gallery.image_set.first()
        if cover:
            return cover.image.url
        return static('images/default/no-image.png')

    def get_images(self):
        gallery = self.gallery
        images = gallery.image_set.all()
        return images

    def get_slug(self):
        title = str(self.title).replace(' ','-')
        return f"{title}-{self.id}"

    def get_absolute_url(self):
        return reverse('public:worksample_detail',args=(self.get_slug(),))



class Gallery(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return f"Gallery - {self.title}"


def upload_image_gallery_src(instance,path):
    format_image = str(path).split('.')[-1]
    return f"gallery/{Tools.random_str()}.{format_image}"


class Image(mixins.RemovePastFileWhenChangedMixin, models.Model):
    FIELDS_REMOVE_FILES = ('image',)
    gallery = models.ForeignKey('Gallery',on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_image_gallery_src)

    def __str__(self):
        return f"Image - {self.gallery.__str__()}"


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date_time_create = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = '-id',

    def __str__(self):
        return self.name


class Education(mixins_cache.CacheMixin, models.Model):
    title = models.CharField(max_length=100)
    date_range = models.CharField(max_length=100,null=True,blank=True)
    description = models.TextField(null=True,blank=True)

    class Meta:
        ordering = '-id',

    def __str__(self):
        return self.title


class Experience(mixins_cache.CacheMixin, models.Model):
    title = models.CharField(max_length=100)
    date_range = models.CharField(max_length=100,null=True,blank=True)
    description = models.TextField(null=True,blank=True)

    class Meta:
        ordering = '-id',

    def __str__(self):
        return self.title

class ExperienceSkill(mixins_cache.CacheMixin, models.Model):
    description = models.TextField(null=True,blank=True)

    class Meta:
        ordering = '-id',

    def __str__(self):
        return self.description[:20]


class TelegramBot(models.Model):
    chat_id = models.CharField(max_length=20)
    token_bot = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return 'Telegram Notification Bot'


class MessageNotif(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    date_time_send = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = '-id',

    def __str__(self):
        return self.title




