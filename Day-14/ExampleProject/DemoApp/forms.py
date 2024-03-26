from django import forms
from .models import Employee

class EForm(forms.ModelForm):
	class Meta:
		model = Employee
		fields = ["epid","ename","esal","edesg"]
		widgets = {
		"epid":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Employee Id",
			}),
		"ename":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Employee Name",
			}),
		"esal":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"min":"15000",
			"max":"60000",
			}),
		"edesg":forms.Select(attrs={
			"class":"form-control my-2",
			})
		}
