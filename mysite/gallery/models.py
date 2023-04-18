from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

from users.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=400)
    likes = models.ManyToManyField(User, related_name='post_likes')

    def get_absolute_url(self):
        return reverse('gallery', args=[str(self.id)])

    def __str__(self):
        return str(self.id)

def get_image_filename(instance, filename):
    return 'post_images_{0}/{1}'.format(instance.post.id, filename)


class Images(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=None)
    image = models.ImageField(upload_to=get_image_filename,
                              verbose_name='Image')

