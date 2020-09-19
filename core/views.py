from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User 
from django.contrib.auth import login  ,logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin  
from django.contrib import messages


# Create your views here.

# @login_required
def home(request):

    total = User.objects.all().count

    return render(request , 'home.html' ,{'total':total} )

# class Home(LoginRequiredMixin,TemplateView):
#     template_name  =  'home.html'     


def signup(request):
    form = UserCreationForm()
    if request.method == 'POST':

        form = UserCreationForm(request.POST)
        if form.is_valid():

            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request ,'Signed up success by : ' + user)
            return redirect ('login')
    else:
        form = UserCreationForm()
    return render (request ,'registration/register.html',{'form':form} )  
      
# @login_required
def secret(request):
    return render (request , 'secret_page.html')    


# def login(request):
#     if request.method == 'POST':


#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request , username=username , password=password)
#         if user is not None:
            
#             login(request , user)

#             return redirect ('home')
#         else:
#               messages.info('Your user name or password is not coorect')
#     return render (request ,'registration/register.html',{'form':form} )    