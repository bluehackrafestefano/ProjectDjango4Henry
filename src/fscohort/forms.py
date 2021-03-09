from django import forms
from fscohort.models import Student

# class StudentForm(forms.Form):
#     first_name = forms.CharField(max_length=50)
#     last_name = forms.CharField(max_length=50)
#     number = forms.IntegerField()

from .models import Student

class StudentForm(forms.ModelForm):
    
    first_name = forms.CharField(label="Your Name")
    
    class Meta:
        model = Student
        # fields = ("first_name", "last_name")
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['first_name'].label = "My Name"