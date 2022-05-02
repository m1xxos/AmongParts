FROM python:3.10

#
WORKDIR /app

#
COPY ./requirements.txt /app/requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt


#
CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host" , "0.0.0.0", "--port", "80", "--root-path=/api"]