FROM python:3.8.5

WORKDIR /word2vec
ADD ./requirements.txt /word2vec/requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install gunicorn
ADD . /word2vec
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "1", "--timeout", "600","application"]