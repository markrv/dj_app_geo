from django.contrib import admin
from .models import Geo

class GeoAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    class Media:
        js = ('js/jquery.min.js', 'http://api-maps.yandex.ru/2.1/?lang=ru_RU', 'js/yandexmodel.js',)

admin.site.register(Geo, GeoAdmin)

# https://tech.yandex.ru/maps/jsbox/2.1/polygonEditor