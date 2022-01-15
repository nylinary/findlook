from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from main.models import AccessRecord
from .forms import (SuggestionForm, UserLoginForm, UserProfileInfoForm, UserForm)
import json
from django.contrib.auth.password_validation import validate_password
from django.urls import reverse
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate, login, logout
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
    return render(request, 'main/registration.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                  })


def user_login(request):

    if request.POST:
        login_form = UserLoginForm(data=request.POST)
        if login_form.is_valid():

            user = authenticate(username=login_form.cleaned_data['username'],
                                password=login_form.cleaned_data['password'])

            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('index'))
                
                else:
                    return HttpResponse("Not active.")
            else:
                print('User is not exist.')
                return HttpResponse("Data is not correct!")
        else:
            return HttpResponse("Data is not valid")
    else:
        login_form = UserLoginForm()
        return render(request, 'main/login.html', {'login_form': login_form})
    

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("You logged in.")