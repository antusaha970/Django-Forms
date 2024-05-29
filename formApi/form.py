from django import forms
from .models import Student


class TestForm(forms.Form):
    name = forms.CharField(required=False)
    about = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Say something about you'}), max_length=200)
    email = forms.EmailField(help_text="Enter an unique email address")
    trams = forms.BooleanField(
        label="Agreed to our trams and conditions", initial=True)
    birthday = forms.DateField(
        widget=forms.NumberInput(attrs={'type': 'date'}))
    techStack = forms.MultipleChoiceField(
        choices=[("C++", "C++"), ("Java", "Java"),], widget=forms.CheckboxSelectMultiple)
    hobby = forms.ChoiceField(choices=[("google", "Google"), ("play", "Play")])
    fav_color = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=[
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('black', 'Black'),
    ])


class TestModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
