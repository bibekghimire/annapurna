"""
URL configuration for annapurna project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import home
from person.views import more_view
from django.conf import settings
from django.conf.urls.static import static

from person.views import section_committee_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name='annapurnahome'),
    path('services',include("services.urls")),
    path('more',more_view,name="more_view"),
    path('person/',include("person.urls")),
    path('users/',include("users.urls")),
    path('committees/<int:type>/<int:pk>',section_committee_view,name='section_committee'),
    path("accounts/", include("django.contrib.auth.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)