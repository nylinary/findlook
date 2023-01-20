from django.shortcuts import render
from django.views.generic import View
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import *

# Create your views here.


class IndexView(View):
    template_name = 'closet/index.html'

    data = HoodiesImages.objects.all()
    image_names = data.values('image_name')
    def get(self, request):
        return render(request, self.template_name, {'image_names':self.image_names})


def get_images(request):
    data = HoodiesImages.objects.all().values('image_name')
    images_names = data.image_name.all().objects.all()
    paginator = Paginator(images_names, 1)

    page = request.GET.get('page')
    try:
        typesets = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        typesets = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        typesets = paginator.page(paginator.num_pages)

    return render(request, 'closet/index.html', {'typesets': typesets})
