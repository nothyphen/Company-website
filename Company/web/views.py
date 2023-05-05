from django.shortcuts import render
from . import models
# Create your views here.
def HomePage(request):
    services = models.Service.objects.all()
    about = models.AboutCompany.objects.all()
    project = models.Project.objects.all()
    category = models.Category.objects.all()
    managers = models.Managers.objects.all()
    contact = models.ContactUs.objects.all()

    context = {
        'services' : services,
        'about' : about,
        'projects' : project,
        'category' : category,
        'managers' : managers,
        'category_name' : models.Project.category_return,
        'contacts' : contact,
    }
    return render(request, 'index.html', context=context)