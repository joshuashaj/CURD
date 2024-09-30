from django.db import models

# Create your models here.

class Employee(models.Model):
    eid = models.CharField(max_length=20)
    ename = models.CharField(max_length=30)
    eemail = models.EmailField(max_length=50)
    econtact = models.CharField(max_length=20)

    class Meta:
        db_table = "employee"