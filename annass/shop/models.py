from django.db import models

# Create your models here.
from django.db.models import ImageField


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    price = models.IntegerField()
    image = ImageField(upload_to="shop/product-images", blank=True)
    is_active = models.BooleanField(default=True, verbose_name='Aktiv?')

    def __str__(self):
        return self.name

    def to_array(self):
        ret = {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
        }
        if self.image:
            ret['image'] = self.image.url
        else:
            ret['image'] = None

        return ret


class ProductCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=255, verbose_name="Beschreibung", blank=True)
    products = models.ManyToManyField(Product, blank=True)
    is_active = models.BooleanField(default=True, verbose_name='Aktiv?')

    def __str__(self):
        return self.name


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return self.product.name


class ShoppingCart(models.Model):
    products = models.ManyToManyField(CartItem, blank=True)

    def __str__(self):
        return "Einkaufswagen" + str(self.id)

    def calculate_price(self):
        price = 0
        for product in self.products.all():
            price += product.product.price * product.amount
        return price

    def to_array(self):
        products = []
        for product in self.products.all():
            products.append(product)
        print(products)
        return products
