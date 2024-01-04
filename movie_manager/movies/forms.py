from django.forms import ModelForm
from . models import MovieInfo

class Movieform(ModelForm):
    class Meta:
        model=MovieInfo
        fields='__all__'
    