from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
# from main.views import ProfileImageIndexView
from . import views

urlpatterns = [
    # url(r'^file/', views.ContactView.as_view(), name='index'),
    url(r'^file/', views.upload_file, name='index'),
    # url(r'^$', views.index, name='index'),
    # url(r'^$', ProfileImageIndexView.as_view(), name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
