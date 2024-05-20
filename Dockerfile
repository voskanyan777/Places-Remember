FROM python:3.10


WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /app/djangoProject

ENV SOCIAL_AUTH_VK_OAUTH2_KEY 51926092
ENV SOCIAL_AUTH_VK_OAUTH2_SECRET bGdP8bxqTCzXJz5v8pU4
ENV NAME postgres
ENV USER postgres
ENV PASSWORD postgres
ENV HOST db
ENV PORT 5432