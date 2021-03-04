FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine
RUN apk --update add bash nano 
RUN pip install --upgrade pip
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static
COPY ./requirements.txt /var/www/requirements.txt
RUN apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r /var/www/requirements.txt --no-cache-dir && \
 apk --purge del .build-deps