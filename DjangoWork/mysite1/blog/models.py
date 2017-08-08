# coding=utf-8
from django.db import models
from django.contrib import admin

# Create your models here.


class BlogPost(models.Model):

    class Meta:
        ordering = ('-timestamp',)  # 这个逗号至关重要,他表明这是一个单元素的元组

    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()
    # authors = models.ForeignKey("BlogAuthor")
    # 这是一个完整的model，代表了一个有三个变量的 "BlogPost" 对象。
    # 严格来说有四个，django会为每一个model自动的加上一个自增的，唯一的 id变量
    # 他是强大的django对象关系映射ORM系统的核心。
    # 此外，每一个比那里那个都和普通的类属性一样被定义在一个特定变量类（field class)的实例
'''

class BlogAuthor(models.Model):
    author = models.CharField(max_length=100)

'''
class Author(models.Model):
    name = models.CharField(max_length=100)

'''
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignObject(Author)
    length = models.IntegerField()

'''


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'timestamp')

admin.site.register(BlogPost, BlogPostAdmin)
# admin.site.register(BlogAuthor)
# admin.site.register(Author, Book)
