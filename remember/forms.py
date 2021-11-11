from django import forms
from remember.models import RememberPlaceFB


class RememberForm(forms.Form):
    location = forms.CharField(label='Location', max_length=5000, widget=forms.TextInput(
        attrs={'rows': '1', 'cols': '5', 'class': 'form-control',
               'placeholder': 'Location...'},
    ))
    text_comment = forms.CharField(label='Comment', max_length=5000, widget=forms.Textarea(
        attrs={'rows': '5', 'cols': '5', 'class': 'form-control',
               'placeholder': 'Say Something...'},
    ))

    class Meta:
        model = RememberPlaceFB
        fields = '__all__'
