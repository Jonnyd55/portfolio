from django.db import models
import tagulous

# Create your models here.
class Project(models.Model):
	title = models.CharField(max_length=256, blank=True, null=True)
	chatter = models.CharField(max_length=500, blank=True, null=True)
	spotlight_img = models.CharField(max_length=1000, blank=True, null=True)
	img = models.CharField(max_length=1000, blank=True, null=True)
	blurb = models.TextField(blank=True, null=True)
	tags = tagulous.models.TagField()

	def __str__(self):
		return self.title