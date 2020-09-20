from django.db import models

# Create your models here.
class Todo(models.Model):

    #タイトル(空白禁止)
    title = models.CharField('タイトル', max_length=100, blank=False)

    #本文
    text = models.TextField('本文')

    #投稿日時
    #DateTimeFieldは時間を保存するフィールド
    #auto_now_add: データの登録日時を自動保存するか
    create_at = models.DateTimeField('投稿日時', auto_now_add=True)

    #最終更新日時
    #auto_now: データの更新日時を自動保存するかどうか
    updated_at = models.DateTimeField('最終更新日時', auto_now=True)

    def __str__(self):
        return self.title


"""
    「使い方」
    作成するデータベースのテーブルごとにmodels.Modelクラスを継承したクラスを作成
    今回はTodo
    
    
    「カラム(フィールド）」
    テーブル内のカラム(フィールド）をクラス変数として定義
    ToDo(todo)
    作成日時(created_at)
    更新日時(updated_at)

    
    「データベースの構築」
    モデルを構築したら以下のコマンド実行
    1. python manage.py makemigrations
    2. python manage.py migrate

    #1: models.pyの更新チェック
    #2: データベースファイルを作成更新

    「主キー(primary key)」
    主キーの設定を特にしなかった場合、自動的にモデルへの内部的にid=AutoField(primary_key=True)が追加され
    テーブルの主キーが追加される
"""