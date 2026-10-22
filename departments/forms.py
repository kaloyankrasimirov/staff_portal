from django import forms
from departments.models import Department


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Finance-Bulgaria',
            }),
            'email_address': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'email@domain.com'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Sofia, Bulgaria'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '123456789'
            })
        }

        labels = {
            'name': 'Department Name',
        }

        error_messages = {
            'name': {
                'required': 'Please enter a valid department name.',
                'unique': 'A department with this name already exists.'
            },

            'email_address': {
                'required': 'Please enter a valid email address.',
                'unique': 'The email address already exists.'
            }
        }


