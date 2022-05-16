FROM python:3.9
RUN apt-get update -y
RUN apt-get install libgirepository1.0-dev gcc libcairo2-dev pkg-config python3-dev gir1.2-gtk-3.0 -y
RUN apt-get install libjpeg62 -y

WORKDIR /app
COPY . .


RUN pip install -r requirements.txt

ENV PORT 8080

# For environments with multiple CPU cores, increase the number of workers
CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 myproject:app
