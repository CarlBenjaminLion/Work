##Notes Of MySite1
***
###Django模板语言初探

    <h2>{{ post.title }}</h2>
    <p>{{ post.timestamp }}<p>
    <p>{{ post.body }}</p>

这是一个简单的blog帖子模板

	{% for post in posts %}
   	 	<h2>{{ post.title }}</h2>
   		 <p>{{ post.timestamp }}<p>
   		 <p>{{ post.body }}</p>
  	  {% endfor %}

**presentation** : 表示层
##Monday, 07. August 2017 08:24PM
##今天搞定django web开发一书中关于定义和使用模型中的知识点
==Web框架以来一个强大的数据访问层==
- 可移植性，一样的代码适用于不同的数据库
- 安全性，django框架本身具有还可以的安全特性
- 表现力，看起来好用又简单，因为SQL语言本身是看起来非常复杂的
###Django丰富的变量类型[model fields](file:///home/benjamin/Documents/Docs/django-docs-1.10-en/ref/models/fields.html#model-field-types)
CharField
TextField
AutoField
BigIntegerField
BinaryField
BooleanField
DateField
DateTimeField
EmailField
URLField
IPAddressField
***
###主键和唯一性primary key
primary key 通常是自增的整数来确保表里面记录的唯一值
指定主键的方法是在参数中写上  primary_key = True

==测试没有通过，我需要把关于模型和数据库的文档读一读==
