from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=120)
    slug = AutoSlugField(populate_from='title', unique=True, editable=True, blank=True)

    class Meta:
        db_table = 'Category'
        verbose_name = 'Kategoriler'
        verbose_name_plural = 'Kategoriler'

    def __str__(self):
        return self.title



class Products(models.Model):
    title = models.CharField(max_length=155)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    detail = models.TextField()
    image = models.ImageField(upload_to='news_products_image/', default='products.jpg', verbose_name = 'Ürün')
    category = models.ForeignKey(Category,on_delete=models.CASCADE, verbose_name='Kategori')
    slug = AutoSlugField(populate_from='title', unique=True, editable=True, blank=True)

    class Meta:
        db_table = 'Products'
        verbose_name = 'Ürünler'
        verbose_name_plural = 'Ürünler'

    def __str__(self):
        return self.title


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField('Products', through='CartItem')

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey('Products', on_delete=models.CASCADE,db_column='product_id')
    quantity = models.PositiveIntegerField(default=1)




