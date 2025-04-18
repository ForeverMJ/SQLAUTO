# SQLAUTO

SQLクエリの自動テスト生成と実行を行うツールです。

## 機能

- ✅ SQL構文チェック
- 🤖 GPTによるテストケース生成
- 🧠 SQLiteでのテスト実行
- 📊 テスト結果の要約

## インストール

1. リポジトリをクローン:
```bash
git clone https://github.com/ForeverMJ/SQLAUTO.git
cd SQLAUTO
```

2. 仮想環境を作成して有効化:
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate
```

3. 依存パッケージをインストール:
```bash
pip install -r requirements.txt
```

## 使用方法

1. Hugging Faceのトークンを取得:
   - https://huggingface.co/join でアカウント作成
   - https://huggingface.co/settings/tokens でトークン生成

2. アプリケーションを起動:
```bash
streamlit run ui/app.py
```

3. ブラウザで http://localhost:8501 にアクセス

4. Hugging Faceトークンを入力し、SQLクエリを入力してテストを実行

## ライセンス

MIT

## 作者

ForeverMJ
