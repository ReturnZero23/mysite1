from django.db import models

# Create your models here.
class Publisher(models.Model):
	name = models.CharField(max_lengdh=30)
	address = models.CharField(max_lengdh=50)
	city = models.CharField(max_lengdh=60)
	stats_province = models.CharField(max_lengdh=30)
	country = models.CharField(max_lengdh=50)
	website = models.URLField()

class Author(models.Model):
	first_name = models.CharField(max_lengdh=30)
	last_name = models.CharField(max_lengdh=40)
	email = models.CharField()
class Book(models.Model):
	title = models.CharField(max_lengdh=100)
	author = models.ManyToManyField(Author)
	publisher = models.ForeignKey(Publisher)
	publication_date =  models.DateField()