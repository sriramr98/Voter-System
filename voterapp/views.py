from django.shortcuts import render
from django.http import request, HttpResponseRedirect
from voterapp.models import Voter
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    votes = Voter.objects.all()
    context = {'votes':votes}
    return render(request,'index.html',context=context)


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')

        if password != confirmPassword:
            context = {'failurePassword':"Passwords don't match"}
        else:
            print("Passwords are equal")
            try:
                userOne = User.objects.get(username = username)
            except User.DoesNotExist:
                userOne = None
            try:
                userTwo = User.objects.get(email= email)
            except User.DoesNotExist:
                userTwo = None
            if userOne:
                context = {'failureUsername':'Username already taken'}
            elif userTwo:
                context = {'failureEmail':"Email id taken. Login if you're already registered"}
            else:
                user = User.objects.create(username=username,first_name=username,email=email,password=password)
                context = {'success':'Registration success'}
        return render(request,'register.html',context=context)
    return render(request,'register.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is None:
             context = {'authError':'Could not authenticate you. Try again'}
             return render(request,'login.html',context=context)
        else:
            login(request,user)
            return HttpResponseRedirect(reverse('index'))
    return render(request,'login.html')

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
