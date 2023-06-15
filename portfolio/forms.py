from django.forms import ModelForm, forms
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'forms-control', 'placeholder': 'Title'}),
            'description': forms.TextArea(attrs={'class': 'forms-control', 'placeholder': 'Content'}),
            'link': forms.TextInput(attrs={'class': 'forms-control', 'placeholder': 'Link'}),
            'image': forms.ImageField(attrs={'class': 'forms-control', 'upload_to': 'portfolio/'})
        }

        labels = {
            'title': 'Title',
            'description': 'Content of post',
            'link': 'Link',
            'image': 'Image'
        }
