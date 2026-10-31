from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
]

# Persian (default) has no prefix: /resume ; English: /en/resume
urlpatterns += i18n_patterns(
    path('', include('Public.urls', namespace='public')),
    prefix_default_language=False,
)

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
