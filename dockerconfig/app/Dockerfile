FROM python:alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFRED 1
ENV DJANGO_SUPERUSER_PASSWORD admin

RUN mkdir /app
ADD requirments.txt /app
WORKDIR /app

RUN apk update
RUN apk add --no-cache gcc python3-dev musl-dev mariadb-dev libffi-dev

# install prerequisites for Pillow
RUN apk add --no-cache tiff-dev jpeg-dev openjpeg-dev zlib-dev freetype-dev lcms2-dev \
    libwebp-dev tcl-dev tk-dev harfbuzz-dev fribidi-dev libimagequant-dev \
    libxcb-dev libpng-dev

RUN pip install --upgrade pip --no-cache-dir
RUN pip install -r requirments.txt --no-cache-dir

RUN apk del gcc python3-dev musl-dev

# check if any user not exist create admin user
# install with requirments.txt from ../volumes/app/requirments.txt

CMD while ! python3 manage.py sqlflush > /dev/null 2>&1; do sleep 1; done && \ 
    python3 manage.py makemigrations --noinput && \
    python3 manage.py migrate --noinput && \
    python3 manage.py collectstatic --noinput && \
    python3 manage.py createsuperuser --user admin --email admin@admin.admin --noinput; \
    gunicorn -b 0.0.0.0:8000 config.wsgi