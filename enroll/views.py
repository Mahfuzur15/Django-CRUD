from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
from . import forms

# Create your views here.

# def form_name_view(request):
#  form = forms.FormName()
#  if request.method == "POST":
#   form = forms.FormName(request.POST)
#   # Then we check to see if the form is valid (this is an automatic  validation by Django)
#   if form.is_valid():
#    # if form.is_valid == True then do something
#    s = sigtracker()
#    s.nm = form.cleaned_data['name']
#    s.em = form.cleaned_data['email']
#    s.txt = form.cleaned_data['text']
#    s.save()

# #    reg = forms(name=nm, email=em, text=txt)
# #    reg.save()
#    print("Form validation successful! See console for information:")
# #    print("Name: "+form.cleaned_data['name'])
# #    print("email: "+form.cleaned_data['email'])
# #    print("message: "+form.cleaned_data['text'])
#  return render(request, 'enroll/index.html', {'form': form})

def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form': fm, 'stu' : stud})


# Delete 
def deleted_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
    
def update_data(request, id):
        if request.method == 'POST':
            pi = User.objects.get(pk=id)
            fm = StudentRegistration(request.POST, instance=pi)
            if fm.is_valid():
                 fm.save()
        else:
                pi = User.objects.get(pk=id)
                fm = StudentRegistration(instance=pi)
        return render(request, 'enroll/updatestudent.html', {'form':fm})
