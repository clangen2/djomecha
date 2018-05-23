from django.db import models
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length = 50)
    slug = models.SlugField(blank = True)
    attributes = models.TextField(blank = True)
    description = RichTextField(blank = True)
    file = models.FileField(upload_to = "media/")
    url = models.URLField(blank = True)
    date_created = models.DateField(auto_now_add = True)
    last_modified = models.DateField(auto_now_add = False, auto_now= True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.title)

        super(Item, self).save(*args, **kwargs)
class rsvp(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    note = RichTextField(blank=True)

    def __str__(self):
       return self.name
