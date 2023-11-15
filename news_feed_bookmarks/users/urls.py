from django.urls import include, path
from rest_framework.routers import DefaultRouter

from news_feed_bookmarks.users.api import views

app_name = "users"

# Create a router and register our viewsets with it.
router = DefaultRouter()

router.register("bookmarks", views.BookmarksViewSet, basename="bookmarks")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path("", include(router.urls)),
]
