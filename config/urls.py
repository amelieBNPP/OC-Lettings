from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings


def trigger_error(request):
    division_by_zero = 1 / 0
    return division_by_zero


urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"), name='home'),
    path("lettings/", include("lettings.urls"), name="lettings"),
    path("profiles/", include("profiles.urls"), name="profiles"),
    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_error),
] + static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )
