from django.contrib import admin
from .models import Category, Service, AboutCompany, Project, Managers, ContactUs
# Register your models here.

admin.site.register(Category)
admin.site.register(Service)
admin.site.register(AboutCompany)
admin.site.register(Project)
admin.site.register(Managers)
admin.site.register(ContactUs)