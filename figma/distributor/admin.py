from django.contrib import admin

# Register your models here.
from distributor.models import News, Legislation, ImageNews, LegislationCategory

admin.site.register(News)
admin.site.register(ImageNews)
admin.site.register(Legislation)
admin.site.register(LegislationCategory)
