FROM python:3.6

ENV APP_HOME=/app
WORKDIR $APP_HOME
COPY ./app $APP_HOME

RUN pip3 install -r requirements.txt
RUN ["chmod", "+x", "./start.sh"]

EXPOSE 8058
ENTRYPOINT ./start.sh

#CMD ["python", "src/main.py"]
#CMD ["gunicorn", "--workers=1", "-b 0.0.0.0:5000", "src.wsgi:app"]
