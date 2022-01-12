from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from main.models import Topic, Webpage, AccessRecord
from . import forms
import json
# Create your views here.


def index(request):
    now = timezone.localtime(timezone.now())
    content = {'datetime': now}
    return render(request, 'main/index.html', context=content) 

def main_index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}

    return render(request, 'main/main.html', context=date_dict)


def send_suggestion_page(request):
    form = forms.SuggestionForm()
    validation_dict = {'success': None}
    if request.POST:
        form = forms.SuggestionForm(request.POST)

        if form.is_valid():
            validation_dict['success'] = True
            return HttpResponse(json.dumps(validation_dict))
        else:
            validation_dict['success'] = False
            return HttpResponse(json.dumps(validation_dict))

    return render(request, 'main/suggestion.html', {'form': form})
