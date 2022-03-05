import imp
from django import views
from django.shortcuts import redirect, render
from django.views import View
from .models import Student
from .forms import AddStudentform

# Create your views here.
class Home(View):
    def get(self, request):
        stu_data = Student.objects.all()

        return render(request, "core/home.html", {'studata':stu_data})

class Add_Student(View):
    def get(self, request):
        fm = AddStudentform()
        return render(request, 'core/add-student.html', {'form': fm })
    
    def post(self, request):
        fm = AddStudentform(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        else:
            return render(request, 'core/add-student.html', {'form': fm })

class Delete_Studnet(View):
    def post(self, request):
        data = request.POST
        id = data.get('id')
        studata = Student.objects.get(id=id)
        print(studata)
        studata.delete()
        return redirect('/')

class EditStudent(View):
    def get(self, request, id):
        stu = Student.objects.get(id=id)
        fm = AddStudentform(instance=stu)
        return render(request, 'core/edit-student.html', {'form':fm})
    
    def post(self, request, id):
        stu = Student.objects.get(id=id)
        fm = AddStudentform(request.POST, instance=stu)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        else:
            return redirect('/')
