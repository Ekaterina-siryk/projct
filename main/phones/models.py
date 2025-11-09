from django.db import models


from django.utils.text import slugify

class Phone(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=False, verbose_name='id')
    name = models.CharField(max_length=100, verbose_name='name')
    price = models.IntegerField(verbose_name='price')
    image = models.URLField(max_length=200, verbose_name='image')
    release_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name='release_date')
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=150, unique=True)

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name