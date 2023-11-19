from django.shortcuts import render, redirect


def employee(request):
    print(request.user)
    if not request.user.is_authenticated:
        return redirect('library-login')
    return render(request, 'employee/edashboard.html')

def book(request):
    return render(request, 'employee/ebook.html')

def borrowedbook(request):
    return render(request, 'employee/eborrowedbook.html')

def changepw(request):
    return render(request, 'employee/changepw.html')

def addbook(request):
    return render(request, 'employee/addbook.html')

def editbook(request):
    return render(request, 'employee/editbook.html')

def deletebook(request):
    return render(request, 'employee/deletebook.html')

def addborrowedbook(request):
    return render(request, 'employee/addborrowedbook.html')

def editborrowedbook(request):
    return render(request, 'employee/editborrowedbook.html')

def deleteborrowedbook(request):
    return render(request, 'employee/deleteborrowedbook.html')



