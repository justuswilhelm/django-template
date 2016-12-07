"""Create abstract models and mixins."""
from django.conf import settings
from django.db.models import DateTimeField, ForeignKey, Model, CharField
from django.utils.translation import gettext_lazy as _


class TimestampModel(Model):
    """A model containing a timestamp."""

    created = DateTimeField(auto_now_add=True, editable=False,
                            verbose_name=_("Erstellt"))
    updated = DateTimeField(auto_now=True, editable=False,
                            verbose_name=_("Aktualisiert"))

    class Meta:
        """Declare as abstract."""

        abstract = True
        ordering = '-updated',


# XXX this should contain the name charfield Justus 2016-08-30
class StringNameModel(Model):
    """Return name as for string."""

    name = CharField(max_length=255)

    def __str__(self):
        """Return this objects name as string."""
        return self.name

    class Meta:
        """Abstract model."""

        abstract = True
        ordering = "name",


class UserModel(TimestampModel):
    """Model containing user submitted content."""

    user = ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Benutzer"))

    class Meta(TimestampModel.Meta):
        """Options."""

        abstract = True