FROM python:3.8

COPY . /depend
WORKDIR /depend
RUN pip3 install -r requirements.txt  
EXPOSE 5000
CMD ["gunicorn" ,"--bind", "0.0.0.0:5000", "wsgi:app"]


