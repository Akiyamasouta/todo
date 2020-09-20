from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .models import Todo
from .forms import TodoForm
# Create your views here.

#Djangoであらかじめ用意されているListView, DetailView, CreateView, UpdateView, DeleteViewを利用

#一覧表示
class TodoListView(generic.ListView):
    """
    テンプレートを指定しないと、「モデル名_list.html」が使用される
    また、自動でページネーションもしてくれる
    """

    model = Todo
    paginate_by = 5

#詳細表示
class TodoDetailView(generic.DetailView):
    """
    Todoの詳細表示
    テンプレ指定しないと「モデル名_detail.html」が使用される
    """

    model = Todo

#新規作成
class TodoCreateView(generic.CreateView):
    """
    Todoの新規作成
    テンプレート指定しないと「モデル名_form.html」が使用される
    """
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy('todo:list')

#更新
class TodoUpdateView(generic.UpdateView):
    """
    Todoの更新
    テンプレートを指定しないと....
    """
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy('todo:list')

#削除
class TodoDeleteView(generic.DeleteView):
    """
    Todoの削除
    テンプレートを指定しないと...

    デフォルトの操作
    getリクエスト>>>確認ページへ遷移
    postリクエスト>>>削除を実行

    補足
    レコードを削除せず、有効フラグを消す場合
    deleteをオーバーライドしてその中に処理を描く
    """

    model = Todo
    success_url = reverse_lazy('todo:list')