from django.core.management.base import BaseCommand
from faker import Faker
from datetime import datetime
from django.contrib.auth.models import User
from todo.models import Task
import random



class Command(BaseCommand):
    help = "inserting dummy data"

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.fake = Faker()

    def handle(self, *args, **options):
        pass


        for _ in range(5):
            Task.objects.create(
                
                title=self.fake.paragraph(nb_sentences=1),
                description=self.fake.paragraph(nb_sentences=10),
                completed=random.choice([True, False]),
                created_at=datetime.now(),
                user=User.objects.create(username=self.fake.name(), password="Test@123456")
            )
