from django import forms
from .models import Day

# forms htmlのformタグみたいな？
class DayCreateForm(forms.ModelForm):
    class Meta:
        model = Day
        fields = '__all__' #('title','text')などで特定フィールド指定