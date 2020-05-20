# py-suruga-13-slackbot-handson

Python駿河 #13のSlackbotハンズオンの資料です

## 概要

今回のハンズオンは以下を扱います。

- SlackbotをSlackのEventAPI, WebAPIで作成する
- SlackbotでWEB APIで得られる結果を取得して返します
- SlackアプリをSlackに設定する方法
- Herokuへのデプロイ
- GitHub Actionsの基本的な扱い

時間内に終わらなくても、ドキュメントの内容を進めることで完走できます。

このハンズオン中にPythonの具体的なコードの解説はしない予定です。（ハンズオン後の懇親会やTwitterなどでお聞きください）

Pythonの実行環境は3.7以降を対象にしています。

## あるとよいツールの知識

- Gitの基礎知識:add, commit, push/pull, remote などの
- GitHubの基礎知識: 主にClone, GitHubのリポジトリへのpush/pull
- Web API/jsonの扱い, HTTPS経由のAPI操作

## ハンズオンに必要な環境

### 対象OS

- Windows 10
- （Mac, Linuxは動作しますが、詳しくサポートはしません）

### PCにインストールするもの

- Python 3.7: 公式版をおすすめします。
- エディター,IDE:基本的にお好きな物で
  - Visual Studio Code:講師が利用します
  - PyCharm
  - Visual Studio:
  - etc...
- ターミナル
  - Win:コマンドプロンプト（cmd.exe）
  - （Mac, Linuxはお好きなターミナルアプリで）
  - エディター, IDE内蔵のターミナルでも作業できます
- Git: なるべく最新
- Heroku Cli
  - [The Heroku CLI | Heroku Dev Center](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)


### 

## ハンズオン手順

### あらかじめ準備したほうが良いもの

利用する各サービスの登録, ログインをします

- Github
  - 登録 : https://github.com/join
  - ログイン : https://github.com/login
- Heroku
  - 登録 : https://signup.heroku.com/jp
  - ログイン : https://id.heroku.com/login
- Slack
  - 新規ワークスペース作成 : https://slack.com/get-started#/create

Slackbotを作る際には、開発用のSlackワークスペースを各自で用意することをおすすめします。（Slack側でもアナウンスされています）

サービスの登録については各サービスの案内に従ってください。

### 作業ディレクトリ

基本的にお好きな場所で構いません。わかりやすい位置としてホームフォルダのドキュメントを基準に操作します。

```cmd
cd ~\Documents
```

### ハンズオンのリポジトリをClone

このハンズオンのGitHubリポジトリからローカル環境にCloneします。

コマンドでの操作はこちらです。

```

git clone ***
git checkout 
```

VSCodeでの操作は


### ローカル開発環境の用意

Pythonはシステムにインストールされた実行環境以外に仮想環境を用意することができます。仮想環境を作ることでシステム側の環境を汚すこと無く開発環境の構築ができます。

仮想環境は以下のコマンドで作成します

```cmd
cd []
# cd 
python -m venv .venv
```

仮想環境を利用するときには、以下のコマンドを実行します

```
./venv/Scripts/activate.bat
(.venv) 
```


このハンズオンで利用するライブラリは以下になります。

- slackeventsapi
- slackclient
- requests
- Flask

また、Pipenvでの環境作成もできます。（此方については今回は扱いません。普段利用されている方はPipfileも同梱しているのでご利用ください）

- 全体図
- 環境構築
- Slackの必要な設定
- gitでコードを落とす
- herokuのサインアップ
- github actionsのデプロイ手段
- コードの概要