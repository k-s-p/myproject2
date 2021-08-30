# 初めてのアプリケーション

## 仮想環境の構築

仮想環境には、**venv**を使用する。
**venv**を使用することにより、仮想環境ごとに個別のライブラリをインストールすることができる。

以下のコマンドをコマンドラインに入力することで、仮想環境の構築、起動が可能。
(venv)が表示されたら、仮想環境内にいる。

```bash
hoge@LAPTOP-RNJHN4U2:~/myproject2$ python3 -m venv venv
hoge@LAPTOP-RNJHN4U2:~/myproject2$ source venv/bin/activate
(venv) hoge@LAPTOP-RNJHN4U2:~/myproject2$ 
```

## テンプレートhtmlの使用法

Djangoでは、共通のテンプレートhtmlを作成し、各ページで使用することができる。
これにより、個別のページで必要な部分以外を使いまわすことができて便利である。

base.html内の、`{% block content %}`から`{% endblock %}`で囲った部分が他のhtmlで置き換えることができる。
置き換えるhtmlでも、`{% block content %}`から`{% endblock %}`で囲む必要がある。

baseを使うhtmlでは、初めに`{% extends 'hoge/base.html' %`でbaseを継承する必要がある。

```html:base.html
<!DOCTYPE html>
<html lang="ja">
    <head>

    </head>
    <body>

        <h1>Base.htmlです</h1>
        {% block content %}
        {% endblock %}

    </body>
</html>
```

```html:index.html
{% extends 'mysite/base.html' %}

{% block content %}
    <h1>{{ title }}</h1>
    <h1>indexファイルですよ</h1>
{% endblock %}
```

## LivereLoadについて

LivereLoadとは、ホットリロードライブラリであり、プロジェクトに変更があった場合、自動でブラウザをリロードしてくれるライブラリである。

* 導入方法

1. `pip install django-livereload-server`
1. settings.pyのINSTALLED_APPSに`'livereload', #livereload`を追加
1. settings.pyのMIDDLEWAREに`'livereload.middleware.LiveReloadScript', #livereload`を追加
1. ターミナルで、`python manage.py livereload`を起動

## テンプレートの便利な使い方

base.htmlに色々書きすぎると、ごちゃごちゃしてくるので、個別のファイルに書くことができる。
その場合、`{% include 'hoge/snippets/header.html' %}`として、`include`を使用し、ファイルを読み込むことができる。