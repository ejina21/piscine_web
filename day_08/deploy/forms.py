from django import forms

from deploy.models import Image


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'file')