from django.db import models

# Create your models here.

class Shijing(models.Model):
    title = models.CharField('标题', default='', max_length=100, help_text='标题')
    chapter = models.CharField('章名', default='',  max_length=100, help_text='章名')
    section = models.CharField('类名', default='',  max_length=100, help_text='类名')
    content = models.TextField('内容', default='',  help_text='内容')

    def __str__(self):
        return self.title + self.chapter + self.section
    
    class Meta:
        db_table = u'shijing'
        verbose_name = u'诗经'
        verbose_name_plural = u'诗经'
        ordering = ['id']