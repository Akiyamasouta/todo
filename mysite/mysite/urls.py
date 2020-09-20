"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #todo/でアクセスしたときはtodoのurl設定を参照
    path('todo/', include('todo.urls')),

    #urlが[admin/]の場合、管理画面(admin.site.urls)を返す(ブラウザに表示)
    path('admin/', admin.site.urls),

    #path('index/', include('mysite.urls', namespace='mysite')),
]

"""
[path関数]
第1引数: URL
第2引数: URLに対応するview関数
(クラスベースの場合、viewクラス名でas_viewメソッドを呼び出す)
name引数: テンプレート内で指定するURLの名称
(省略するとview関数の名前がそのまま利用される)

[include関数]
path関数の第2引数にview関数の代わりに指定することでURLを連結
path("", include("todo.urls"))
上ではtodo.urls.pyで設定したURLを連結
"""