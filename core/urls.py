from django.shortcuts import render
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from . import user_login
from django.utils.translation import gettext_lazy as _
def my_custom_404_view(request, exception):
    return render(request, 'errors/404.html', {}, status=404)
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
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)