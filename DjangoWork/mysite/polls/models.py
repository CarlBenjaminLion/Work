# coding=utf-8
import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin
# from django.utils.encoding import python_2_unicode_compatible


# @python_2_unicode_compatible  # only if you need to support Python 2
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    ass = models.CharField(max_length=100, default='aaa')

    def __str__(self):
        return self.question_text

    def a(self):
        return 123

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        # datetime.timedelta(days=1)  1 day, 0:00:00
        # 这个方法判断了是否是一天之内出版的


# @python_2_unicode_compatible  # only if you need to support Python 2
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


# Finally, note a relationship is defined, using ForeignKey.
# That tells Django each Choice is related to a single Question.
# 每一个Choice选择都关联一个Question问题
# Django supports all the common database relationships: many-to-one, many-to-many, and one-to-one.
# 下面这点很重要
# Run python manage.py makemigrations to create migrations for those changes
# Run python manage.py migrate to apply those changes to the database.
# 一个进入类ipython调试界面的方式
# To invoke the Python shell, use this command:
# $ python manage.py shell


admin.site.register(Question)
admin.site.register(Choice)
