from django import forms
from projects.models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Project Name',
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Simple Description'
            }),

            'project_participants': forms.CheckboxSelectMultiple()
        }

        labels = {
            'name': 'Project Name'
        }