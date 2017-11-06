from django.db import models
from django.core.urlresolvers import reverse

class Post(models.Model):
	title = models.CharField(max_length=150)
	content = models.TextField()
	updated=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

	def get_detail_url(self):
		return reverse("detail",kwargs={"post_id":self.id})
