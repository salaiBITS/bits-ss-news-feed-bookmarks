from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(
        _("Created At"), auto_now_add=True, help_text=_("Created Date and Time")
    )
    updated_at = models.DateTimeField(
        _("Updated At"), auto_now=True, help_text=_("Updated Date and Time")
    )

    class Meta:
        abstract = True


class Bookmarks(TimeStampModel):
    content = models.IntegerField(_("Content Primary Key"))
    user = models.ForeignKey(to=User, verbose_name=_("User Primary Key"), on_delete=models.CASCADE)

    class Meta:
        db_table = _("bookmarks")
        verbose_name = _("Bookmark")
        verbose_name_plural = _("Bookmarks")
        unique_together = ("content", "user")
