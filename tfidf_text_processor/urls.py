from django.conf.urls.static import  static
# from django.templatetags.static import static
from django.urls import path, include

from app.settings import MEDIA_ROOT, MEDIA_URL
from .views import main_view

urlpatterns = [
        path( '', main_view, name='home')
        # path('', UploadView.as_view(), name= 'home'),

]
