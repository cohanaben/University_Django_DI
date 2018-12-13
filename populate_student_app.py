import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','student_project.settings')
import django
django.setup()


import random
from faker import Faker
from student_app.models import Student, Note
from faker import Faker


fakegen = Faker()
matieres = ["Espagnol", "Philosophie", "SVT", "Sorcelerie"];

def populate():
	for i in range(2):
		newStudent = Student.objects.get_or_create( prenom=fakegen.first_name(), nom=fakegen.last_name(), date_naissance=fakegen.date());
		note = Note.objects.get_or_create( student=newStudent[0], matiere=random.choice(matieres),
		note = fakegen.random_int(min=0, max=20), coefficient=fakegen.random_int(min=1, max=10))


if __name__ == '__main__': 
	print('populate script...') 
	populate()
	print('done populating.')
