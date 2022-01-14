import profile
import re
from wsgiref import validate
from xml.dom import ValidationErr
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from main.models import (Topic, Webpage, AccessRecord,
                         UserSuggested)
from .forms import (SuggestionForm, UserProfileInfoForm, UserForm)
import json
from django.contrib.auth.password_validation import validate_password
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
    form = SuggestionForm()
    validation_dict = {'success': None}
    if request.POST:
        form = SuggestionForm(request.POST)

        if form.is_valid():
            form.save()
            validation_dict['success'] = True
            return HttpResponse(json.dumps(validation_dict))
        else:
            validation_dict['success'] = False
            return HttpResponse(json.dumps(validation_dict))

    return render(request, 'main/suggestion.html', {'form': form})


def register(request):
    
    error = False

    if request.POST:
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            # Get clean form data.
            user = user_form.save(commit=False)
            try:
                validate_password(user.password, user)           
                # Hash the password.
                user.set_password(user.password)
                # Save that hash.
                user.save() 

                profile = profile_form.save(commit=False)
                profile.user = user

                # Key 'profile_pic' defined in the models.
                if 'profile_pic' in request.FILES:
                    profile.profile_pic = request.FILES['profile_pic']
                
                profile.save()
                registered = True
            except Exception as e:
                error = True
        else:
            print(user_form.errors, profile_form.errors)
            error = True
        return HttpResponse(json.dumps({'error': error}))
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    # print(error)
    # if error:
    return render(request, 'main/registration.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                  })