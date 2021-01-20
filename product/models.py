import uuid
from time import time

from django.db import models

from pytils.translit import TRANSTABLE, slugify


def gen_slug(s):
    slug = slufify(s)
    return slug + '-' + str(int(time()))


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, primary_key=True, blank=True)
    parent = models.ForeignKey('self',
                                related_name='children',
                                on_delete=models.CASCADE,
                                null=True,
                                blank=True)

    def __str__(self):
        return self.name
    
    def save(self):
        if not self.slug:
            self.slug = gen.slug(self.name)
        super().save()


    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    uuid = models.UUIDField(primary_key=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.uuid:
            self.uuid = str(uuid.uuid4())
        super().save(*args, **kwargs)
    
    class Meta:
        ordering = ('price',)


class ProductImage(models.Model):
    image = models.ImageField(upload_to='products')
    product = models.ForeignKey(Product,
                                related_name='images',
                                on_delete=models.CASCADE)