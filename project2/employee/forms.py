from django import forms
from .models import Club,Department


class SearchForm(forms.Form):
    #ModelChoiceField modelから選択肢を作成
    club = forms.ModelChoiceField(
        queryset = Club.objects, label='サークル', required=False
    )

    department = forms.ModelChoiceField(
        queryset = Department.objects, label='部署', required=False
    )

