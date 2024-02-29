"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.shortcuts import render
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from . import user_login

from django.utils.translation import gettext_lazy as _
def my_custom_404_view(request, exception):
    return render(request, '404.html', {}, status=404)
urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n',)),
]
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('rosetta/', include('rosetta.urls')),
    # apps urls
    path("", include("apps.settings.urls")),
    path("courses/", include("apps.courses.urls")),
    path('lessons/', include('apps.lessons.urls')),
    path('ent/', include('apps.ent.urls')),
    path(_('accounts/'), include('django.contrib.auth.urls')),
    # accounts
    path('accounts/register', user_login.REGISTER, name='register'),
    path('doLogin', user_login.DO_LOGIN, name='doLogin'),
    path('view_profile/', user_login.VIEW_PROFILE, name='view_profile'),
    path('accounts/profile', user_login.PROFILE, name='profile'),
    path('accounts/profile/update', user_login.PROFILE_UPDATE, name='profile_update'),
    
)
handler404 = my_custom_404_view
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
