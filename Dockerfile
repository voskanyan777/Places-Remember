FROM python:3.10


WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /app/djangoProject

ENV SOCIAL_AUTH_VK_OAUTH2_KEY 51926092
ENV SOCIAL_AUTH_VK_OAUTH2_SECRET bGdP8bxqTCzXJz5v8pU4
ENV DB_NAME postgres
ENV DB_USER postgres
ENV DB_PASSWORD postgres
ENV DB_HOST db
ENV DB_PORT 5432