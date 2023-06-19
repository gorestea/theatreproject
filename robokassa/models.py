# coding: utf-8

from django.utils.translation import gettext_lazy  as _
from robokassa import python_2_unicode_compatible
from django.db import models


@python_2_unicode_compatible
class SuccessNotification(models.Model):
    InvId = models.IntegerField(_(u'Номер заказа'), db_index=True)
    OutSum = models.CharField(_(u'Сумма'), max_length=15)

    created_at = models.DateTimeField(
        _(u'Дата и время получения уведомления'), auto_now_add=True)

    class Meta:
        verbose_name = _(u'Уведомление об успешном платеже')
        verbose_name_plural = _(
            u'Уведомления об успешных платежах (ROBOKASSA)')

    def __str__(self):
        return u'#%d: %s (%s)' % (self.InvId, self.OutSum, self.created_at)
