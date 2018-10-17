import uuid
from django.conf import settings
from django.contrib.gis.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Budget(models.Model):
    """
    A User has many Budgets but an Budget has only one User.
    """

    id = models.UUIDField(_("id"), primary_key=True, default=uuid.uuid4, editable=False)
    amount = models.DecimalField(_("amount"), max_digits=10, decimal_places=2)
    name = models.CharField(_("name"), max_length=25)
    order = models.IntegerField(_("order"), blank=True, null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("user")
    )
    date_created = models.DateTimeField(_("date created"), default=timezone.now)

    class Meta:
        verbose_name_plural = "budgets"

    def __str__(self):
        return self.name.title()

    @staticmethod
    def has_read_permission(request):
        return True

    def has_object_read_permission(self, request):
        return request.user == self.user

    @staticmethod
    def has_write_permission(self):
        return True

    def has_object_write_permission(self, request):
        return request.user == self.user
