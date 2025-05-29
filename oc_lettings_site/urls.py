"""Configuration principale des URL pour le projet oc_lettings_site."""
from django.contrib import admin
from django.urls import path, include

from . import views


def trigger_error(request):
    division_by_zero = 1 / 0  # noqa: F841


urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls', namespace='lettings')),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('sentry-debug/', trigger_error),
    path('admin/', admin.site.urls),
]

handler404 = 'oc_lettings_site.views.custom_404'
handler500 = 'oc_lettings_site.views.custom_500'
