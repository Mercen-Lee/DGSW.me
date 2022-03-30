from django import forms

from .models import Shortener

class ShortenerForm(forms.ModelForm):
    
    long_url = forms.URLField(widget=forms.URLInput(
        attrs={"class": "name", "id": "urls", "placeholder": "단축할 URL을 입력하세요"}))

    class Meta:
        model = Shortener

        fields = ('long_url',)