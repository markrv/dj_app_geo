from django.db import models
from cms.models import CMSPlugin
from django.utils.translation import ugettext_lazy as _

class Geo(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('Title'))
    description = models.TextField(blank=True, null=True, verbose_name=_('Description'))
    pos = models.CharField(max_length=100, verbose_name=_('Pos'))

    class Meta:
        verbose_name = _('Geo')
        verbose_name_plural = _('Geo')

    def __unicode__(self):
        return unicode(self.title)