from contextlib import redirect_stderr
from re import template
#from urllib import request
from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import DayCreateForm
from .models import Day

# Create your views here.
# generic.ListViewなどで引っ張るtemplate内のhtmlは、指定しない限り決まっている

class IndexView(generic.ListView):
    model = Day
    paginate_by = 3
    #template_name = 'diary/my_list.html'も可能


class AddView(LoginRequiredMixin,generic.CreateView):
    model = Day
    form_class = DayCreateForm
    #データ作成に成功したときにリダイレクトされるページ
    #reverse_lazy URLの文字列を返す　/diary
    success_url = reverse_lazy('diary:index')


class UpdateView(LoginRequiredMixin,generic.UpdateView):
    model = Day
    form_class = DayCreateForm
    success_url = reverse_lazy('diary:index')

class DeleteView(LoginRequiredMixin,generic.DeleteView):
    model = Day
    success_url = reverse_lazy('diary:index')

class DetailView(generic.DetailView):
    model = Day