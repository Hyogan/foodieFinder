from django.shortcuts import render, redirect, get_object_or_404
from users.forms import UserRegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required
from restaurants.models import Restaurant
# Create your views here.


User = settings.AUTH_USER_MODEL
def index(request) :
    return render(request,'foodief/index.html')


def register_view(request) :
    if(request.method == "POST") :
        form = UserRegisterForm(request.POST or None)
        if form.is_valid() :
            new_user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Hey, {username} your account was created successfully") 
            new_user = authenticate(username=form.cleaned_data['email'],
                                    password= form.cleaned_data['password1']
                                )

            login(request,new_user)
            return redirect("index")
    else :
        form = UserRegisterForm()
    context = {
        'form' : form 
    }
    return render(request, 'users/signup.html',context=context)

    

def authenticate_view(request) :
    does_user_exist = False
    if request.method == "POST" :
        email = request.POST.get('email')
        password = request.POST.get('password')

        try :
            user = User.objects.get(email=email)
        except :
            # messages.warning(request, f"User width {email} does not exist")
            does_user_exist = False

        
        user = authenticate(request, email=email, password=password)

        if user is not None :
            login(request, user)
            messages.success(request, f"you have been successfully logged in > Bon appetit")
            return redirect("index")

        else :
            messages.warning(request, "Invalid credentials ");
    
        # if 

    context = {

    }
    return render(request, 'users/login.html',context)



def logout_user(request) :
    logout(request)
    return redirect('index')





# restaurants/views.py


# @login_required
# def add_admin(request, restaurant_id):
#     restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
#     # Check if the logged-in user is an admin of this restaurant
#     if request.user in restaurant.admins.all():
#         if request.method == 'POST':
#             email = request.POST.get('email')
#             # Check if the email belongs to an existing user
#             existing_user = User.objects.filter(email=email).first()
#             if existing_user:
#                 # Link existing user to the restaurant as admin
#                 restaurant.admins.add(existing_user)
#             else:
#                 # Create a new user account and link to the restaurant as admin
#                 new_user = User.objects.create_user(email=email, username=email)
#                 restaurant.admins.add(new_user)
#                 # Optionally, send an email invitation to the new user
#             return redirect('restaurant_detail', restaurant_id=restaurant.id)
#         else:
#             # Render the form to add a new admin
#             return render(request, 'add_admin.html', {'restaurant': restaurant})
#     else:
#         # If the logged-in user is not an admin of this restaurant, redirect or show an error message
#         return redirect('restaurant_detail', restaurant_id=restaurant.id)  # Redirect to restaurant detail page
