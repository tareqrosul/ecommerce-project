from django.db import models# Create your models here.
class Categories(models.Model):
  name = models.CharField(max_length = 300, null = False)
descript = models.TextField(max_length = 1000,
  default = 'Enter')

def __str__(self):
  return self.name

# this class represents brands of products
class Brand(models.Model):
  com_name = models.CharField(max_length = 300, null = False)
brand_description = models.TextField()
cat = models.ForeignKey(Categories, on_delete = models.PROTECT)

def __str__(self):
  return self.com_name

class Products(models.Model):
     prod_title = models.CharField(max_length = 300, null = False)
     prod_model = models.CharField(max_length = 300, )
     rating=models.FloatField()
     descr = models.TextField(max_length = 1000,
       default = 'give')
     brand = models.ForeignKey(Brand, on_delete = models.PROTECT)
     cat = models.ForeignKey(Categories, on_delete = models.PROTECT)

def __str__(self):
  return self.prod_title
