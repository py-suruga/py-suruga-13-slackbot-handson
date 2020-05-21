# py-suruga-13-slackbot-handson

こちらはPython駿河 & Unagi.py合同勉強会 Slackbotハンズオンの資料です。

[Python駿河 勉強会 #13 〜オンラインSlack botハンズオン再び〜 - connpass](https://py-suruga.connpass.com/event/175942/)

[Unagi.py 勉強会29枚目～オンラインSlack botハンズオン再び～ - connpass](https://unagi-py.connpass.com/event/175956/)

## 概要

今回のハンズオンは以下を扱います。

- SlackbotをSlackのEventAPI, WebAPIで作成する
- SlackアプリをSlackに設定する方法
- GitHub Actionsの基本的な扱い
- Herokuへのデプロイ
- SlackbotからWeb APIを操作して結果をbotが答える

時間内に終わらなくても、ドキュメントの内容を進めることで完走できます。

このハンズオン中にPythonの具体的なコードの解説はしない予定です。（ハンズオン後の懇親会やTwitterなどでお聞きください）

Pythonの実行環境は3.7以降を対象にしています。

## あるとよいツールの知識

- Gitの基礎知識: add, commit, push/pull, remoteなどの操作コマンド
- GitHubの基礎知識: 主にClone, GitHubのリポジトリへのpush/pull
- Web API/jsonの扱い、HTTPS経由のAPI操作

## ハンズオンに必要な環境

### 対象OS

- Windows 10
- （Mac, Linuxは動作しますが、詳しくサポートはしません）

### PCにインストールするもの

- Python 3.7: 公式版をおすすめします。
- エディター,IDE:基本的にお好きな物で
  - Visual Studio Code: 講師が利用します
  - PyCharm
  - Visual Studio: Python拡張をおすすめします -> [Visual Studio を使用した Python 開発 - Visual Studio | Microsoft Docs](https://docs.microsoft.com/ja-jp/visualstudio/python/?view=vs-2019&fbclid=IwAR0U_6oJEYM8mJB-LcE7XAP6DNobZzlXpvPLNXoev2XiwJQi9gwy0JL0X_w)
  - etc...
- ターミナル
  - Win:コマンドプロンプト（cmd.exe）
  - （Mac, Linuxはお好きなターミナルアプリで）
  - エディター, IDE内蔵のターミナルでも作業できます
- Git: なるべく最新
- Heroku Cli
  - [The Heroku CLI | Heroku Dev Center](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)

## ハンズオン手順

### あらかじめ準備したほうが良いもの

利用する各サービスの登録, ログインをします

- GitHub
  - [登録](https://github.com/join)
  - [ログイン](https://github.com/login)
- Heroku
  - [登録](https://signup.heroku.com/jp)
  - [ログイン](https://id.heroku.com/login)
- Slack
  - [新規ワークスペース作成](https://slack.com/get-started#/create)

Slackbotを作る際には、開発用のSlackワークスペースを各自で用意することをおすすめします。（Slack側でもアナウンスされています）

サービスの登録については各サービスの案内にしたがってください。

### 作業ディレクトリ

基本的にお好きな場所で構いません。わかりやすい位置としてホームフォルダのドキュメントを基準に操作します。

```cmd
cd ~\Documents
```

### ハンズオンのリポジトリをフォークしてClone

このハンズオンのGitHubリポジトリを、参加者のGitHubのアカウントへフォークします。そのフォークしたリポジトリをローカル環境にCloneします。

GitHubのフォーク方法はヘルプを確認します。

[リポジトリをフォークする - GitHub ヘルプ](https://help.github.com/ja/github/getting-started-with-github/fork-a-repo)

コマンドでの操作はこちらです。

```cmd
// git clone https://github.com/[各参加者のgithubアカウント名]/py-suruga-13-slackbot-handson.git
```

エディター、IDEからのgit cloneはそれぞれのアプリの利用方法を参照してください。

### ローカル開発環境の用意

Pythonはシステムにインストールされた実行環境以外の仮想環境を用意できます。仮想環境を作ることでシステム側の環境を汚すこと無く開発環境の構築ができます。

仮想環境は以下のコマンドで作成します

```cmd
cd py-suruga-13-slackbot-handson
python -m venv .venv
```

仮想環境を利用するときには、以下のコマンドを実行します

```cmd
.\.venv\Scripts\activate.bat
(.venv) >
```

また、Pipenvでの環境作成もできます。このハンズオンでは利用しませんが、普段利用されている方はPipfileも同梱しているのでご利用ください。

---

Work in progress...

## システムの全体図

## Slackアプリの作成と設定

## GitHub Actionsのデプロイ手段

## ハンズオンのSlackbotの概要

## Slackbotの改造をしてみる
