from django import forms
from .models import Notice, Patron, Person, CommitteeMember,Book

class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ['title', 'content']
        widgets = {
        'title': forms.TextInput(attrs={'placeholder': 'Enter Notice Title', 'value': ''}),
        'content': forms.Textarea(attrs={'placeholder': 'Enter Notice Content', 'value': ''}),
    }
        
class PatronForm(forms.ModelForm):
    class Meta:
        model = Patron
        fields = ['name', 'since', 'designation']
        widgets = {
        'name': forms.TextInput(attrs={'placeholder': 'Enter the Name'}),
        'since': forms.TextInput(attrs={'placeholder': 'Enter the year'}),
        'designation': forms.Select(attrs={'placeholder': 'Select Designation'}),    
    }
        
class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'photo']

class CommitteeMemberForm(forms.ModelForm):
    class Meta:
        model = CommitteeMember
        fields = ['person', 'year', 'designation', 'order']
        widgets = {
            'year': forms.TextInput(attrs={'placeholder': 'Enter year (e.g., 2023)'}),
            'order': forms.NumberInput(attrs={'placeholder': 'Enter priority order'}),
        }


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'language', 'code', 'file_id']

        widgets = {
            'genre': forms.Select(choices=Book.GENRE_CHOICES),
            'language': forms.Select(choices=Book.LANGUAGE_CHOICES),
        }