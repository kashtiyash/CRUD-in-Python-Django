import imp
from unicodedata import name
from django.urls import path
from .views import Add_Student, Delete_Studnet, EditStudent, Home


urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('add-student/', Add_Student.as_view(), name='add-student'),
    path('delete-student/', Delete_Studnet.as_view(), name="delete-student"),
    path('edit-studnet/<int:id>', EditStudent.as_view(), name='edit-student'),

]

