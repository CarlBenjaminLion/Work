# coding=utf-8

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import BlogPost

# Create your views here.


def archive(request):
    posts = BlogPost.objects.all()
    t = loader.get_template('archive.html')
    c = {'posts': posts}
    return HttpResponse('Hello World' + t.render(c))

# 每一个Django视图函数都将django.http.HttpRequest对象作为它的第一个参数，它还可以通过URLconf接受其他参数
# 当我们把BlogPost类作为django.db.model.Model的一个子类时，我们就过得了Django对象关系映射的全部能力
# 只需要模板的名字就能创建模板对象t，因为它保存在app下的templates下，无需更多只是就能找到它
# Django模板渲染的数据是由一个字典类的对象context提供的，这里的context c只是一个键值对
# 每个django视图函数都要返回一个django.http.HttpResponse对象。最简单的就是构造函数传递一个字符串，这里的模板的render方法返回的正是一个字符串
#####################################################
