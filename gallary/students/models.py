# coding=utf-8
from django.db import models
from tinymce.models import HTMLField
import datetime

# Create your models here.
class Student(models.Model):
	Gender_CHOICES = ( 
		('M', '男'), 
		('F', '女'),
	) 

	ZhongDui_CHOICES = (
		('09', '09中队'),
		('10', '10中队'),
		('11', '11中队'),
		('12', '12中队'),
	)

	QuDui_CHOICES = (
		('1', '一区队'),
		('2', '二区队'),
		('3', '三区队'),
		('4', '四区队'),
	)

	Catagory_CHOICES = (
		('0', '学习之星'),
		('1', '科技先锋'),
		('2', '训练标兵'),
		('3', '才艺明星'),
	)

	name = models.CharField(max_length=30)
	gender = models.CharField(max_length=1, choices=Gender_CHOICES, default='M')
	ZhongDui = models.CharField(max_length=10, choices=ZhongDui_CHOICES, default='09')
	QuDui = models.CharField(max_length=10, choices=QuDui_CHOICES, default='1')
	honor = models.TextField()
	detail = HTMLField()
	catagory = models.CharField(max_length=10, choices=Catagory_CHOICES, default='0')
	time = models.DateTimeField(default = datetime.datetime.now)
	image= models.ImageField(upload_to='static/photos/%Y/%m/%d', blank=True,null=True)

	def __unicode__(self):
		return self.name
