from django.contrib import admin

from news_feed_bookmarks.users import models


@admin.register(models.Bookmarks)
class BookmarksAdmin(admin.ModelAdmin):
    list_display = ("id", "content", "user")
