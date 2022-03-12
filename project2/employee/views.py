from re import template
from django.shortcuts import render
from django.views import generic
from .models import Employee
from .forms import SearchForm
# Create your views here.


class IndexView(generic.ListView):
    #template_name = 'employee/employee_list.html'
    #model= employee_list.html
    model=Employee
    paginate_by = 1

    def get_context_data(self):
        #テンプレートに渡す辞書の作成
        context = super().get_context_data()
        #POSTにすると、検索時に選択が消える(毎回新規の検索になる)
        context['form'] = SearchForm(self.request.GET)
        if self.request.method == "POST":
            print(self.request)
        else:
            print('getだよ',self.request.POST)

        #print(context['form'])
        #print(context)
        return context
    
    def get_queryset(self):
        #テンプレートに渡すemployee_list変数の中身の作成
        formm = SearchForm(self.request.GET)
        formm.is_valid() #これがないとclean_dataができない

        #全社員を取得
        queryset = super().get_queryset()

        #部署が選択されていれば、部署で絞り込み
        department = formm.cleaned_data['department']
        if department:
            queryset = queryset.filter(department=department)
        
        club = formm.cleaned_data['club']
        if club:
            queryset = queryset.filter(club=club)
        return queryset
        