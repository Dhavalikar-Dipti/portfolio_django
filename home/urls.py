from django.contrib import admin
from django.urls import path,include
from home import views
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header="Login here"
admin.site.site_title="Welcome"
admin.site.index_title="welcome to the portal"

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('projects', views.projects, name='projects'),
    path('contact', views.contact, name='conatact'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)