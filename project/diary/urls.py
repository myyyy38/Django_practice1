from django.urls import path,include
from . import views

app_name = 'diary'
urlpatterns = [
    #/diary 以降が空のとき、index.html
    #.as_view() 汎用ビュー
    path('',views.IndexView.as_view(),name = 'index'),
    path('add/',views.AddView.as_view(),name = 'add'), #/diary/add
    path('update/<int:pk>',views.UpdateView.as_view(), name = 'update'), #diary/update/pk
    path('delete/<int:pk>',views.DeleteView.as_view(), name = 'delete'), #diary/delete/pk

    path('detail/<int:pk>',views.DetailView.as_view(), name = 'detail') #diary/detail/pk
]
