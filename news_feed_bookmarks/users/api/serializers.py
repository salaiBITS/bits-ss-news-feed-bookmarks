import requests
from rest_framework import serializers
from rest_framework.authentication import get_authorization_header

from config import constants
from news_feed_bookmarks.users import models


class BookmarksSerializer(serializers.ModelSerializer):

    default_error_messages = {
        "invalid_content_id": "This content_id is invalid or does not exist.",
        "duplicate_bookmark": "This content was already bookmarked."
    }

    class Meta:
        model = models.Bookmarks
        fields = ("id", "content",)

    def validate(self, attrs):
        content_id = attrs["content"]
        user = self.context["request"].user

        if models.Bookmarks.objects.filter(content=content_id, user=user).exists():
            self.fail("duplicate_bookmark")

        resp = self.get_content(content_id=content_id)
        if resp.status_code != 200:
            self.fail("invalid_content_id")

        return attrs

    def get_content(self, content_id):
        url = f"{constants.CONTENT_SERVICE_URL}/api/contents/{content_id}/"
        auth_header = get_authorization_header(self.context["request"])
        headers = {
            "Authorization": auth_header
        }
        return requests.get(url=url, headers=headers)

    def create(self, validated_data):
        user = self.context["request"].user
        return self.Meta.model.objects.create(content=validated_data["content"], user=user)

    def to_representation(self, value):
        resp = self.get_content(content_id=value.content)
        if resp.status_code != 200:
            self.fail("invalid_content_id")

        return {
            "id": value.id,
            "content": resp.json()
        }
