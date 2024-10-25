# pdf-translator

## 仮想環境の作成

仮想環境を作成する
```bash
python -m venv pdf-translator
```

仮想環境を有効化する
```bash
# 仮想環境を有効化 (Linux/macOS)
source pdf-translator/bin/activate
```

依存関係のインストール

```bash
pip install -r requirements.txt
```

<!-- 依存関係の記録(requirements.txt を作成)
```bash
pip freeze > requirements.txt
``` -->

<!-- 仮想環境の無効化
```bash
deactivate
``` -->

## DEEPL API KEY の設定
ルートディレクトリに `.env` ファイルを作成し、以下の内容を記述する。

```bash
DEEPL_API_KEY={YOUR_DEEPL_API_KEY}
```


## sample の使い方

```bash
source sample/sample.sh
```

