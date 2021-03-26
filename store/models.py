from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.CharField(max_length=400, null=True, blank=True)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name
