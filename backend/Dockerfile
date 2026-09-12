FROM python:3.13-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["sh", "-c", "python fix_db.py && python manage.py migrate && python seed_data.py && gunicorn maystudio_api.wsgi:application --bind 0.0.0.0:8000 --workers 2"]


