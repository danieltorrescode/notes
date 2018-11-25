from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tag(models.Model):
	tag = models.CharField(max_length=15)
	def __str__(self):
		return '{}'.format(self.tag)


class Category(models.Model):
	category = models.CharField(max_length=10)
	def __str__(self):
		return '{}'.format(self.category)

class Note(models.Model):
	VISIBILITY_TYPE = (
	(0, 'Private'),
	(1, 'Public'),
	)
	title = models.CharField(max_length=50)
	content = models.TextField()
	visibility = models.IntegerField(default=0 , choices=VISIBILITY_TYPE)
	tags =  models.ManyToManyField(Tag, blank=True)
	category = models.ForeignKey(Category, blank=True,
								null=True,on_delete=models.CASCADE)
	user = models.ForeignKey(User, null=True,on_delete=models.CASCADE)

	@property
	def visible_type(self):
		if self.visibility is 0:
			return 'Private'
		else:
			return 'Public'
			
	@property
	def all_tags(self):
		list=[]
		for item in self.tags.all():
			list.append(item.tag)
		return list
