from django.urls import path
from student.views import StudentList

urlpatterns = [
    path("student-list", StudentList.as_view(), name="student_list")
]
