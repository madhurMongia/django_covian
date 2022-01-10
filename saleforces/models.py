from django.db import models

class User(models.Model):
    Id = models.CharField(max_length=255, primary_key=True)
    CompanyName = models.CharField(max_length=250)
    CreatedDate = models.DateTimeField()
    Email = models.CharField(max_length=100,null = True)
    FirstName = models.CharField(max_length=50,null = True)
    LastName = models.CharField(max_length=50,null = True)
    ProfileId = models.CharField(max_length=250,null = True)


class Account(models.Model):
    AccountNumber = models.CharField(max_length=250,null = True)
    Description = models.TextField(null = True)
    Name = models.CharField(max_length=250 ,null = True)
    Id = models.CharField(max_length=250,primary_key=True)
    Industry = models.CharField(max_length=250,null = True)
    OwnerId = models.CharField(max_length=250,null = True)
    Ownership = models.CharField(max_length=250,null = True)
    Website = models.URLField(max_length=250,null = True)

class Contact(models.Model):
    AccountId = models.CharField(max_length=250,null = True)
    Email = models.CharField(max_length=250,null = True)
    FirstName = models.CharField(max_length=250,null = True)
    LastName = models.CharField(max_length=250,null = True)
    Id = models.CharField(max_length=250,primary_key=True)
    Phone = models.CharField(max_length=250,null = True)