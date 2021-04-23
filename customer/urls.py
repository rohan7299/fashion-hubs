from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import homepage
urlpatterns = [
    path('',homepage),
] + static(settings.STATIC_URL,document_root=settings.MEDIA_ROOT)