import email
from django.db import models
from pkg_resources import require

# Create your models here.
class TypeDocument(models.Model):
    description_type = models.CharField(max_length=20, unique=True)


class Persons(models.Model):
    type_document = models.ForeignKey(TypeDocument, on_delete=models.CASCADE)
    document_number = models.IntegerField(unique=True)
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    addres = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=20)

