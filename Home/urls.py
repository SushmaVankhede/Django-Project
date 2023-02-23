from django.contrib import admin
from django.urls import path
from Home import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... the rest of your URLconf goes here ...
] 

urlpatterns = [
    path("", views.index, name = "Home"),
    path("aboutus", views.aboutus, name = "aboutus"),
    path("services", views.services, name = "services"),
    path("contactus", views.contactus, name = "contactus")
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()