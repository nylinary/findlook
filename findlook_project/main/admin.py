from django.contrib import admin
from main.models import (Topic, Webpage, AccessRecord,
                         UserSuggested, UserProfileInfo, )  

# Register your models here.

admin.site.register([Topic, Webpage, AccessRecord,
                     UserSuggested, UserProfileInfo,])
