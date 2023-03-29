from django.shortcuts import render
from django.views.generic.list import ListView
from student.models import StudentDetails
from silk.profiling.profiler import silk_profile
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.


class StudentList(ListView):
    model = StudentDetails
    template_name = "student/home.html"

    @silk_profile(name='View All Students')
    def get(self, request, *args, **kwargs):
        students = StudentDetails.objects.all()
        return render(request, template_name=self.template_name, context={"students": students})
