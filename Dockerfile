FROM python:3.12.1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
# Устанавливаем системные зависимости
RUN apt-get update \
    && apt-get install -y gcc python3-dev musl-dev \
    && apt-get install -y libpq-dev
    
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /code/