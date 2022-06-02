from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"), name='home'),
    path("lettings/", include("lettings.urls"), name="lettings"),
    path("profiles/", include("profiles.urls"), name="profiles"),
    path('admin/', admin.site.urls),
] + static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )
