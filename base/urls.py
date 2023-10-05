from django.urls import path

from . import views

urlpatterns = [
    # Your existing URL patterns
    path("fill/", views.populate_database_view, name="populate_database"),
]
