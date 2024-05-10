from django import forms

# class UserRegisterForm(UserCreationForm) :
#     input_classes = "bg-transparent text-white px-2 border-b-4 w-full sm:w-2/3 my-4  px-4 border-orange-600"
#     username = forms.CharField(widget=forms.TextInput(attrs={"placeholder" : "username", "class" : f"{input_classes}"}))
#     email = forms.CharField(widget=forms.EmailInput(attrs={"placeholder" : "Email adress", "class" : f"{input_classes}" }))
#     password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder" : "Password", "class" : f"{input_classes}"}))
#     password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder" : "Password confirmation", "class" : f"{input_classes}"}))

#     class Meta :
#         model = User
#         fields = ['username','email']




# class CreateRating(forms.ModelForm) :
#     input_classes = "bg-transparent text-white px-2 border-b-4 w-full sm:w-2/3 my-4  px-4 border-orange-600"
    
#     user = forms.CharField(widget=forms.TextInput(attrs={"placeholder " : "" }))
    
#     restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     rating = models.IntegerField(default=0)
#     comment = models.TextField()