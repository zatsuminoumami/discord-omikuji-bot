# ベースイメージ
FROM python:3.11-slim

# 作業ディレクトリ
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN pip install python-dotenv

# コンテナ起動時に実行するコマンド
CMD ["python", "bot.py"]
