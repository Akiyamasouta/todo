from django.urls import path
from . import views

app_name = 'todo'

"""
ユーザがアクセスするURL(http://www.example.jp/list/)と、
urlpatternsに格納したすべてのpath()の初めの引数('admin/'や'index/')を順に比較して
URLと引数が一致した場合、path()の2つ目の引数(views.TodoListView.as_view()など)を利用する
"""

urlpatterns = [
 #[list]のようなURLのとき、todo/views.pyのTodoListViewを利用
 path('list/', views.TodoListView.as_view(), name='list'),   

 #[detail/123] (123はint: 整数)のようなURLのとき、todo/views.pyのTodoDetailViewを利用
 path('detail//', views.TodoDetailView.as_view(), name='detail'),
 path('create/', views.TodoCreateView.as_view(), name='create'),
 path('update//', views.TodoUpdateView.as_view(), name='update'),
 path('delete//', views.TodoDeleteView.as_view(), name='delete'),
]

