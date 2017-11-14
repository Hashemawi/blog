from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save, post_save

class Post(models.Model):
	title = models.CharField(max_length=150)
	slug = models.SlugField(unique=True)
	content = models.TextField()
	updated=models.DateTimeField(auto_now=True)
	img = models.ImageField(null=True, blank=True, upload_to="post_images")


	def __str__(self):
		return self.title

	def get_detail_url(self):
		return reverse("detail",kwargs={"post_slug":self.slug})

	class Meta:
		ordering = ["-updated"]

def create_slug(instance, new_slug=None):
	slug_value = slugify(instance.title)
	if new_slug is not None:
		slug_value = new_slug
	query = Post.objects.filter(slug=slug_value)
	if query.exists():
		slug_value = "%s-%s"%(slug_value, query.last().id)
		return create_slug(instance, new_slug=slug_value)
	return slug


def pre_save_post_function(*args, **kwargs):
	instance = kwargs['instance']
	if not instance.slug:
		slug_value = create_slug(instance)


pre_save.connect(pre_save_post_function, sender=Post)