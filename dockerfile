FROM python:3.8.5

COPY . /word2vec
WORKDIR /word2vec

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "2", "--timeout", "600","application"]