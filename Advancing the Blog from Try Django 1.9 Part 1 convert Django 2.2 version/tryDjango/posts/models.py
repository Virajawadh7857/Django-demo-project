from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.urls import reverse
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.utils import timezone



# Create your models here.
# MVC model view controller

#Post.objects.all()

class PostManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(PostManager, self).filter(draft=False).filter(publish__lte = timezone.now())

def upload_location(instance, filename):
    #return "%s/%s" %(instance.title, filename) # its make new folder with title name
    return "%s_%s" %(instance.title, filename) # its saved image title_filename

    #filebase, extension = filename.split(".")
    #return "%s/%s.%s" %(instance.title, instance.title,extension)  #its make a new folder with title name and change the filename

class Post(models.Model):
    user =models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    image = models.ImageField(null=True, blank=True, upload_to=upload_location)
    content = models.TextField()
    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False, auto_now_add=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    objects = PostManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={"slug": self.slug})
        #return reverse('posts:detail', kwargs={"id": self.id})
    class Meta:
        ordering = ["-timestamp", "-updated"]


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug=new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        #new_slug = "%s-%s" %(slug, qs.first().id)
        new_slug = "%s_%s" %(slug, qs.first().id)
        return create_slug(instance,new_slug=new_slug)
    return slug


'''
unique_slug_generator from Django Code Review #2 on joincfe.com/youtube/
'''
from .utils import unique_slug_generator

@receiver(pre_save, sender = Post)
def pre_save_post_receiver(sender, instance, *args, **kwargs):
   if not instance.slug:
       #instance.slug = create_slug(instance)
       instance.slug = unique_slug_generator(instance)# unique_slug_generator
       pre_save.connect(pre_save_post_receiver, sender=Post)
#pre_save.connect(pre_save_post_receiver, sender=Post)