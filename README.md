# ai-chat

めちゃくちゃ単純なPythonとChatGPT APIを使ったチャットアプリケーションです。Python 3系（特に3.9や3.10ならまず大丈夫）が入っていればすぐ使えます。プログラムに詳しくなく、英語が苦手な人でも弄れるようにという思いを込めてさくっと作ってみました。

# セットアップ

Python3を事前にインストールしておいてください。

コマンドプロンプトで以下のように入力して、チャットアプリケーションで使っている`openai`ライブラリをインストールします。pipコマンドはPythonと一緒に入っていることが多いですがなければインストールしてください。

```console
pip install openai
```

# 実行

コマンドプロンプトで次のように実行します。OPENAI_API_KEYは「環境変数」と呼ばれますが詳しいことは知らなくても大丈夫です。OpenAIのサイトで発行された「APIキー」と呼ばれる文字の列を渡すだけでOKです。注意点としては「APIキー」があれば、他人があなたのアカウントでGPT APIを使えてしまう（＝自分のお金で他人が自由にAPIを使えてしまう）ので、「APIキー」は他の誰にも知られないようにしましょう。

```console
set OPENAI_API_KEY=OPENAIから発行されたAPIキー
python3 chat.py
```

# カスタマイズ

最初に'system'ロールに与えるキャラ設定はsystem.txtに書かれています。この内容を書き換えることで、自由にGPT-4 (あるいはGPT-3.5）のAIの人格や名前、性格や喋り方、好きなことや嫌いなことなどを自在に設定することができます。

初期設定では`system.txt`の中身は[こちら]([https://github.com/kuno-maichi/ai-chat/tree/main/system.txt](https://github.com/kuno-maichi/ai-chat/blob/master/system.txt))になっています。

# スクリーンショット

![ai-chat](https://user-images.githubusercontent.com/60324323/235350053-957ef235-e603-4044-aa83-3d77f3ce8564.png)
