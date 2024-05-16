from django.contrib import admin
from django.urls import include, path
from surveys import views as surveys_views

urlpatterns = [
    path("", surveys_views.other_view, name="home"),
    path("admin/", admin.site.urls),
    path("surveys/", include("surveys.urls")),
]
