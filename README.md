# pdf-translator

## 使い方
### 仮想環境の作成

- 仮想環境を作成する
    ```bash
    python -m venv pdf-translator
    ```

- 仮想環境を有効化する (macOS)
    ```bash
    source pdf-translator/bin/activate
    ```

- 依存関係のインストール
    ```bash
    pip install -r requirements.txt
    ```

<!-- パッケージのインストール
```bash
python3 -m pip install xxx
``` -->

<!-- 依存関係の記録(requirements.txt を作成)
```bash
pip freeze > requirements.txt
``` -->

<!-- 仮想環境の無効化
```bash
deactivate
``` -->

### DEEPL API KEY の設定
- ルートディレクトリに `.env` ファイルを作成し、DEEPL API KEY を設定する.

    ```bash
    DEEPL_API_KEY={YOUR_DEEPL_API_KEY}
    ```

## 実行方法
- PDF ファイルを翻訳する

    ```bash
    python src/pdf_translator.py -i {path_to_pdf_file} -o {path_to_output_pdf_file} -l {language}
    ```

    - `path_to_pdf_file`: 翻訳対象の PDF ファイルのパス
    - `path_to_output_pdf_file`: 翻訳後の PDF ファイルのパス
    - `language`: 翻訳先の言語

## sample code

```bash
python src/pdf_translator.py -i sample/input/sample.pdf -o sample/output/sample.pdf -l JA
```



