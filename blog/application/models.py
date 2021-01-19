from django.db import models
from django.dispatch import receiver
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    STATUS = (('public', 'Public'), ('private', 'Private'),)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS, default='private')

    def get_absolute_url(self):
        return reverse('detailPost', args=[self.slug])

    def get_absolute_url_update(self):
        return reverse('updatePost', args=[self.slug])

    def get_absolute_url_delete(self):
        return reverse('deletePost', args=[self.slug])

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title


@receiver(post_save, sender=Post)
def insert_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify({instance.title})
        return instance.save()