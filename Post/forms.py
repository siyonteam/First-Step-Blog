from django import forms
from .models import Comment
from ckeditor.widgets import CKEditorWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body','author','email')
        widgets = {
            'author': forms.TextInput(attrs={'class': 'answerForm__name' , 'placeholder':'name' }),
            'email': forms.EmailInput(attrs={'class': 'answerForm__email' , 'placeholder':'email'}),
            'body': forms.Textarea(attrs={'class': 'answerForm__body' , 'placeholder':'Message....'}),
        }

