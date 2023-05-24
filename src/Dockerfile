FROM python:3.8-slim

COPY . /depend
WORKDIR /depend
RUN mkdir logging
RUN pip3 install -r requirements.txt  
EXPOSE 5000
CMD ["gunicorn" ,"--bind", "0.0.0.0:5000", "wsgi:app"]


