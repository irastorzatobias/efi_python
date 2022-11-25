FROM python:3.9.10-alpine3.14
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . /app
RUN chmod +x docker-entrypoint.sh
EXPOSE 5000
ENTRYPOINT ["sh", "./docker-entrypoint.sh"]
