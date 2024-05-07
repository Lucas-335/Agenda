from faker import Faker
import os
import sys
from pathlib import Path
import django


DJANGO_BASE_DIR = Path(__file__).parent.parent

sys.path.append(str(DJANGO_BASE_DIR))
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'

django.setup()

if __name__ == '__main__':
    from contact.models import Contact
    import random

    Contact.objects.all().delete()

    fake  = Faker('pt-BR')
    
    for i in range(100):
        contato = Contact()
        subname = fake.name().split()

        contato.name = subname[0]
        contato.last_name = subname[1]
        contato.number = random.randrange(11111111,99999999)
        contato.email = f'{subname[0]}.{subname[1]}@gmail.com'
        contato.save()

