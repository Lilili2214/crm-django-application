from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Record


def home(request):
    return render(request, 'webapp/index.html')


def register(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sign In Successfully!')
            return redirect("login")
        else:
            messages.error(request, 'Please try again later!')
    else:
        form = CreateUserForm()   
    context = {'form': form}
    return render(request,"webapp/register.html", context=context)


# -Login a user 
def my_login(request):
    form = LoginForm()
    if request.method=='POST':
        form= LoginForm(request, data= request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password= request.POST.get("password")
            user = authenticate(request, username=username, password= password)
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Log In Successfully!')
                return redirect("dashboard")

    context = {'form2':form}
    return render(request, 'webapp/my-login.html', context= context)


def user_logout(request):
    auth.logout(request)
    return redirect("login")

@login_required(login_url='login')
def dashboard(request):

    my_records= Record.objects.all()
    context= {'records': my_records}
    return render(request, 'webapp/dashboard.html', context= context)


@login_required(login_url="login")
def create_record(request):
    form = CreateRecordForm()
    if request.method == "POST":
        form = CreateRecordForm(request.POST )
        if form.is_valid():
            form.save()
            messages.success(request, 'Create New Record Successfully!')
            return redirect("dashboard")
    context= {'formcreaterecord': form}
    return render(request, 'webapp/create-record.html', context=context)


@login_required(login_url="login")
def udpate_record(request, pk):
   
    record = Record.objects.get(id=pk)
    form = UpdateRecordForm(instance=record)
    if request.method=="POST":
        form = UpdateRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('view-record', pk=pk)
    context= {'formupdaterecord': form}
    return render(request, 'webapp/update-record.html', context=context)


@login_required(login_url="login")
def view_singular(request, pk):
    record = Record.objects.get(id=pk)
    context= {'record': record}
    return render(request, 'webapp/view-record.html', context=context)

@login_required(login_url="login")
def delete_record(request, pk):
    record = Record.objects.get(id=pk)
    if record:
        messages.success(request, 'Delete Successfully!')
        record.delete()
    else:
        messages.error(request, 'Please try again later!')
    return redirect("dashboard")
