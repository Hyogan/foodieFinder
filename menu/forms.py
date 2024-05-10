from django import forms
from .models import Dish, Category
from django import forms

class CreateDishForm(forms.ModelForm) :
    input_classes = "bg-transparent text-slate-600 px-2 border-b-4 w-full sm:w-2/3 my-4  px-4 border-orange-600"
    
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple)
# category = forms.CharField(required=True, widget=forms.Select(attrs={"label" : "Product category", "placeholder" : "Product Category", "class" : f"{input_classes}"}))
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder" : "Product name", "class" : f"{input_classes}"}))
    price = forms.FloatField(required=True, widget=forms.NumberInput(attrs={"placeholder" : "Product price", "class" : f"{input_classes}"}))
    slug = forms.SlugField(required=True, widget=forms.TextInput(attrs={"placeholder" : "Product slug", "class" : f"{input_classes}"}))
    description = forms.CharField(required=True, widget=forms.Textarea(attrs={"rows" : "4", "placeholder" : "Product description", "class" : f"{input_classes}"}))
    # thumbnail =  forms.ClearableFileInput(attrs={'class': f'{input_classes}'})
    

    # category =  forms.Select(attrs={'class': f'{input_classes}', 'placeholder' : "Product Category"}),
    # name =  forms.TextInput(attrs={'class': f'{input_classes}', 'placeholder' : "Product name "})
    # price =  forms(attrs={"class": f"{input_classes}", "placeholder" : "Product price"})
    # slug =  forms.TextInput(attrs={'class': f'{input_classes}', 'placeholder' : "Product slug. must not contains space"})
    # description =  forms.Textarea(attrs={'class': f'{input_classes}', 'placeholder' : "Product description"})
    thumbnail =  forms.ImageField(required=True)
    
    class Meta:
        model = Dish
        fields = ['category', 'name', 'price', 'slug', 'description', 'thumbnail']
        


    # name = forms.CharField(widget=forms.TextInput(attrs={"placeholder" : "Product name", "class" : f"{input_classes}"}))
    # price = forms.CharField(widget=forms.FloatField(attrs={"placeholder" : "Product price", "class" : f"{input_classes}"}))
    # # slug = forms.CharField(widget=forms.SlugField(attrs={"placeholder" : "Product price", "class" : f"{input_classes}"}))
    # description = forms.CharField(widget=forms.Textarea(attrs={"placeholder" : "Product Description", "class" : "bg-transparent text-white px-2 border-4 w-full sm:w-2/3 my-4  px-4 border-orange-600"}))
    # thumbnail = forms.ImageField(widget=forms.ImageField)
    # restaurant =  forms.Select(attrs={'class': f'{input_classes}', 'placeholder' : "}),
