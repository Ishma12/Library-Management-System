
from django.shortcuts import render

def student_dashboard(request):
    return render(request, 'student/sdashboard.html')
def student_requestform(request):
    return render(request,'student/requestform.html')