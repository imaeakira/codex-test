# How to build & test

```bash
# 依存ライブラリのインストール
pip install -r requirements.txt

# Lint & フォーマッタ
ruff check .
black .

# 単体テスト
pytest -q
```

## ガイドライン

- PR には必ず **日本語で 1～2 行の要約** を書くこと  
- 新規・変更した関数／クラスには **Google-style Docstring** を付与すること  
- コーディング規約は **ruff + black（PEP8 準拠）** に従うこと  
- `main` への直接 push は禁止。必ず **feature/○○ → PR → Review** のフローでマージすること
