from django import forms

class FeedBackForm(forms.Form):
    email = forms.EmailField(required=False)
    message = forms.CharField()