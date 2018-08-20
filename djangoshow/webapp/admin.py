from django.contrib import admin
from webapp.models import *
import json
import logging

# Register your models here.

admin.site.site_header = "中国诗经管理"

logger = logging.getLogger('django')

def parse_shijing_to_mysql(modeladmin, request, queryset):
    with open('../chinese-poetry/shijing/shijing.json', 'r', encoding='utf-8') as f:
        sjlist = json.load(f)
        for sj in sjlist:
            sj = Shijing(title=sj['title'], chapter=sj['chapter'], section=sj['section'], content='\n'.join(sj['content']))
            sj.save()

        logger.info("import shijing to mysql successfullly.")

parse_shijing_to_mysql.short_description = '导入诗经到数据库'

class ShijingAmdin(admin.ModelAdmin):
    actions = (parse_shijing_to_mysql, )
    list_filter = ('chapter', 'section', 'title')
    list_display = ('title', 'chapter', 'section', 'content')

admin.site.register(Shijing, ShijingAmdin)