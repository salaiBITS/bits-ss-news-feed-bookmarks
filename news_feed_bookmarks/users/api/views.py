from rest_framework import viewsets, permissions

from news_feed_bookmarks.users import models
from news_feed_bookmarks.users.api import serializers


class BookmarksViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.BookmarksSerializer
    http_method_names = ["post", "get", "delete"]

    def get_queryset(self):
        return models.Bookmarks.objects.filter(user=self.request.user)
