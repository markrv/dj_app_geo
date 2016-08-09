from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from geo.models import Geo
from django.utils.translation import ugettext as _

class GeoPluginPublisher(CMSPluginBase):
    module = _("Geo")
    name = _("Geo Plugin")
    render_template = "geo/geo_plugin.html"

    def render(self, context, instance, placeholder):
        geo = Geo.objects.order_by('id')
        context['geo'] = geo
        return context

plugin_pool.register_plugin(GeoPluginPublisher)
