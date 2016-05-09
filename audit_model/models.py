from django.db import models
from django.utils.translation import ugettext_lazy as _
from .constants import AUTH_USER_MODEL, CREATED_BY, UPDATED_BY, CREATED_AT, UPDATED_AT


class AuditModel(models.Model):
    created_by = models.ForeignKey(AUTH_USER_MODEL, verbose_name=_(CREATED_BY))
    updated_by = models.ForeignKey(AUTH_USER_MODEL, verbose_name=_(UPDATED_BY))
    created_at = models.DateTimeField(_(CREATED_AT), auto_now_add=True)
    updated_at = models.DateTimeField(_(UPDATED_AT), auto_now=True)

    class Meta:
        abstract = True
