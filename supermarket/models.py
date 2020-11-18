from django.db import models
from django.template.defaultfilters import slugify
import uuid

# Create your models here.


stocks = [
    ("in-stock", "In Stock"),
    ("stock-out", "Out of Stock"),
]
specials = [
    ("hot-offer", "Hot Offer"),
    ("featured-product", "Featured Product")
]
catego = [
    ("visible", "Visible"),
    ("hidden", "Hidden")
]

class Students(models.Model):
    id = models.AutoField(primary_key=True, max_length=50)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=255, default=None)
    mobile = models.CharField(max_length=100, null=True, default=None)
    password = models.CharField(max_length=255, default=None)

    def __str__(self):
        return self.student
    
    class Meta:
        db_table = 'students'




class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True, editable=False)
    status = models.CharField(max_length=100, choices=catego, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'categories'


class Units(models.Model):
    id = models.AutoField(primary_key=True)
    unit = models.CharField(max_length=50)

    def __str__(self):
        return self.unit

    class Meta:
        db_table = 'units'


class Products(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True, editable=False)
    image = models.ImageField()
    description = models.TextField(null=True, blank=True)
    category_id = models.ForeignKey(Categories, db_column='category_id', on_delete=models.CASCADE)
    unit_id = models.ForeignKey(Units, db_column='unit_id', null=True, blank=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=catego, null=True, blank=True)
    stock = models.CharField(max_length=100, choices=stocks, null=True, blank=True)
    final_price = models.IntegerField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)+'-'+uuid.uuid4().hex[:6]
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'products'