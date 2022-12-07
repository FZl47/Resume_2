from django.urls import path
from . import views

app_name = 'Public'
urlpatterns = [
    path('',views.index,name='home'),
    path('resume',views.resume,name='resume'),
    path('ws',views.worksamples,name='worksamples'),
    path('ws/<slug>',views.worksample_detail,name='worksample_detail'),
    path('contact-me',views.contact.as_view(),name='contact_me'),
    path('review',views.review.as_view(),name='review'),
    path('clear-cache',views.clear_cache,name='clear_cache'),
]