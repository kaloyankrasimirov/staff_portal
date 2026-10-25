from django import forms
from records.models import EmployeeRecords, DepartmentRecords, ProjectRecords


class EmployeeRecordsForm(forms.ModelForm):
    class Meta:
        model = EmployeeRecords
        fields = '__all__'
        widgets= {
            'paid_leave_allowance': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'sick_leave_days': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'bonus_eligibility': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'manager_review': forms.Textarea(attrs={
                'class': 'form-control', 'rows': 3
            })

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'employee' in self.fields:
            self.fields['employee'].empty_label = 'Select Employee'
        if self.instance and self.instance.pk:
            if 'employee' in self.fields:
                self.fields['employee'].disabled = True



class DepartmentRecordsForm(forms.ModelForm):
    class Meta:
        model = DepartmentRecords
        fields = '__all__'
        widgets = {
            'annual_budget': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'headcount_target': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'strategic_goals': forms.Textarea(attrs={
                'class': 'form-control', 'rows': 3
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'department' in self.fields:
            self.fields['department'].empty_label = 'Select Department'
        if self.instance and self.instance.pk:
            if 'department' in self.fields:
                self.fields['department'].disabled = True


class ProjectRecordsForm(forms.ModelForm):
    class Meta:
        model = ProjectRecords
        fields = '__all__'
        widgets = {
            'allocated_budget': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'milestones': forms.Textarea(attrs={
                'class': 'form-control', 'rows': 3
            }),
            'targets': forms.Textarea(attrs={
                'class': 'form-control', 'rows': 3
            }),
            'status': forms.Select(attrs={
                'class': 'form-select'
            }),
            'completion_percentage': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'project' in self.fields:
            self.fields['project'].empty_label = 'Select Project'
        if self.instance and self.instance.pk:
            if 'project' in self.fields:
                self.fields['project'].disabled = True