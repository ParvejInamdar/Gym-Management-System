from django.db import models

# Create your models here.
class Enquiry(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    emailid = models.CharField(max_length=30)
    age = models.CharField(max_length=5)
    gender = models.CharField(max_length=7)
    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    unit = models.CharField(max_length=30)
    date = models.CharField(max_length=10)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Plan(models.Model):
    name = models.CharField(max_length=100)
    amount = models.CharField(max_length=10)
    duration = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Member(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    emailid = models.CharField(max_length=30)
    age = models.CharField(max_length=5)
    gender = models.CharField(max_length=7)
    plan = models.CharField(max_length=50)
    joindate = models.CharField(max_length=50)
    expireddate = models.CharField(max_length=50)
    initialamount = models.CharField(max_length=50)

    def __str__(self):
        return self.name
