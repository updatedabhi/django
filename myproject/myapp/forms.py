from .models import Blogpost
from django import forms
class Blogpostform(forms.ModelForm):
  class Meta:
    model = Blogpost
    fields = "__all__"