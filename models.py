from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name  = models.CharField(max_length = 50)
    category  = models.CharField(max_length = 100, default="")
    sub_category  = models.CharField(max_length = 100)
    price = models.IntegerField()
    desc  = models.CharField(max_length = 300)
    pub_date  = models.DateField()
    image  = models.ImageField(upload_to = "shop/images",default = "")

    def __str__(self):
        return self.product_name

class Order(models.Model):
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=5000)
    email = models.CharField(max_length=5000)
    address = models.CharField(max_length=5000)
    city = models.CharField(max_length=5000)
    state = models.CharField(max_length=5000)
    zip_code = models.CharField(max_length=5000)
    phone_no = models.CharField(max_length=5000)
