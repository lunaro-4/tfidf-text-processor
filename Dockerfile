# Используем базовый образ Python
FROM python:3.10.12

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /app

#COPY requirements.txt /app/
#COPY build.sh /app/

COPY . /app/

#RUN pip install -r requirements.txt
RUN bash ./build.sh

EXPOSE 8000

CMD ["python", "/app/manage.py", "runserver", "0.0.0.0:8000"]
