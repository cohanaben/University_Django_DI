from django.shortcuts import render
from student_app.models import Student, Note

def index(request):
	students = Student.objects.all()
	return render(request, 'students/index.html', {'students':students})

def details(request, student_id):
	student = Student.objects.get(id=student_id)
	notes = Note.objects.filter(student=student)
	return render(request,'students/details.html',{'student':student,'notes':notes})