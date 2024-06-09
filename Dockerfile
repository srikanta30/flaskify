FROM python:3.11.8-bookworm

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8000

COPY . /app

ENV MODULE_NAME="app"
ENV PORT="8000"

CMD ["python", "app.py"]