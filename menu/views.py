from django.shortcuts import render,redirect, get_object_or_404
from .forms import CreateDishForm
from .models import Category
from restaurants.models import Restaurant
# Create your views here.

def index(request) :
    return render(request,'foodief/index.html')


def create_dish(request):
    if request.method == 'POST':
        form = CreateDishForm(request.POST, request.FILES)
        if form.is_valid():
            dish = form.save(commit=False)
            dish.restaurant = request.user.restaurant
            dish.save()
            return redirect('admin.menu')
    else:
        form = CreateDishForm()
        form.fields['category'].queryset = Category.objects.all()
    
    return render(request, 'menu/create_dish.html', {'form': form})


# def add_dish(request):
#     if request.method == 'POST':
#         # Process submitted form data
#         dish_name = request.POST['dish_name']
#         selected_categories = request.POST.getlist('categories')

#         # Save new dish with associated category/ies
#         new_dish = Dish(name=dish_name)
#         new_dish.save()
        
#         for category_id in selected_categories:
#             category = Category.objects.get(id=category_id)
#             new_dish.categories.add(category)

#     else:
#         # Render add-dish template with available categories
#         categories = Category.objects.all()
    
#     return render(request, 'add-dish.html', {'categories': categories})



# If you're using Django forms, you can still achieve the desired functionality by customizing your form. Here's an example of how you can do it:

# 1. Define a Django form for adding new dishes (`forms.py`):

# ```python
# from django import forms
# from .models import Dish, Category

# class DishForm(forms.ModelForm):
#     categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple)

#     class Meta:
#         model = Dish
#         fields = ['name', 'categories']
# ```

# 2. In your view, create an instance of the form and pass it to the template (`views.py`):

# ```python
# from django.shortcuts import render
# from .forms import DishForm

# def add_dish(request):
#     if request.method == 'POST':
#         form = DishForm(request.POST)
        
#         if form.is_valid():
#             dish = form.save()
#             # dish.categories contains selected categories
            
#             # Additional processing or saving logic here
            
#             return redirect('success_url')
    
#     else:
#         form = DishForm()

#     return render(request, 'add-dish.html', {'form': form})
# ```

# 3. Render the form in your template (`add-dish.html`):

# ```html
# <form method="POST" action="{% url 'add_dish' %}">
#   {% csrf_token %}
  
#   {{ form.as_p }}
  
#   <button type="submit">Add Dish</button>
# </form>
# ```

# In this approach, we define a `ModelMultipleChoiceField` in our `DishForm`, which automatically generates checkboxes for each available category based on the queryset provided.

# When rendering the template with `{{ form.as_p }}`, it will display all fields of the `DishForm`, including checkboxes for selecting categories.

# Upon submission, Django will handle validating and saving data from the submitted POST request into a new instance of `Dish`. The selected categories are accessible through `dish.categories`.