
from django.shortcuts import render


def student_dashboard(request):
    return render(request, 'student/sdashboard.html')
def student_requestform(request):
    return render(request,'student/requestform.html')

def reviews(request):
    return render(request,'student/reviews.html')
def available(request):
    return render(request,'student/availablebook.html')