from django.db import models

class Category(models.Model):
    id = models.AutoField(primary_key=True)  # فیلد ID با auto-increment
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000, null=True, blank=True)
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.AutoField(primary_key=True)  # فیلد ID با auto-increment
    name = models.CharField(max_length=255)
    product_image = models.TextField(null=True, blank=True)  # تغییر به TextField برای مقادیر بزرگ
    description = models.TextField(null=True, blank=True)
    product_details = models.TextField(null=True, blank=True)
    price = models.BigIntegerField()
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    # ارتباط یک به چند با Category
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name
