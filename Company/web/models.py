from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

class Service(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    describtion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

class AboutCompany(models.Model):
    company_name = models.CharField(max_length=200, null=True, blank=True)
    describtion = models.TextField(null=True, blank=True)
    extra_describtion = models.CharField(max_length=450, null=True, blank=True)

    def __str__(self):
        return self.company_name

class Project(models.Model):
    category = models.ManyToManyField(Category)
    icon = models.ImageField(upload_to='static/imgs')
    describtion = models.TextField(null=True, blank=True)
    online_link = models.CharField(max_length=450, null=True, blank=True)

    def __str__(self):
        return self.describtion
    
    def category_return(self):
        return self.category

class Managers(models.Model):
    picture = models.ImageField(upload_to='static/imgs')
    name = models.CharField(max_length=200, blank=True, null=True)
    describtion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class ContactUs(models.Model):
    address = models.CharField(max_length=450, null=True, blank=True)
    phone = models.CharField(max_length=450, null=True, blank=True)
    company_email = models.EmailField()

    def __str__(self):
        return self.address