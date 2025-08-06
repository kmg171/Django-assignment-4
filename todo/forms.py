from django import forms
from .models import Todo
from django_summernote.widgets import SummernoteWidget

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'start_date', 'end_date']  # image → start_date, end_date로 변경
        widgets = {
            'description': SummernoteWidget(),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '제목을 입력해주세요.'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'start_date', 'end_date', 'is_completed', 'completed_image']
        widgets = {
            'description': SummernoteWidget(),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '제목을 입력해주세요.'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'is_completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'completed_image': forms.FileInput(attrs={'class': 'form-control'}),
        }
