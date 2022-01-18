import os
from unicodedata import name
os.environ.setdefault('DJANGO_SETTINGS_MODULE','findlook_project.settings')

import django
django.setup()
     
import random
from main.models import Topic, Webpage, AccessRecord
from faker import Faker



fakegen = Faker()
topics = ['Search', 'Social Network', 'Marketplace', 'News', 'Games']


def add_topic():
    topic = Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
    topic.save()
    return topic


def populate(N=5):

    for _ in range(N):
        
        # Get the topic for the entry.
        topic = add_topic()

        # Create fake data for that entry.  
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # Create the new webpage entry
        # webpg = Webpage.objects.get_or_create(topic = topic,
        #                                       url=fake_url,
        #                                       name=fake_name)[0]
        webpg_list = list(Webpage.objects.all())
        webpg = random.choice(webpg_list)
        # Create a fake access record for that webpage.
        AccessRecord.objects.get_or_create(name=webpg,
                                                    date=fake_date)[0]
        
if __name__ == '__main__':
    print('Populating sctipt...')
    populate(22)
    print('Population completed.')