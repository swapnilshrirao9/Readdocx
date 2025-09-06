# Use Python image
FROM python:3.11-slim

# Set environment
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV POSTGRES_DB readfile
ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD pgadmin
ENV POSTGRES_PORT 5432
ENV POSTGRES_HOST postgresdb
ENV DJANGO_SECRET_KEY EJ66PqygBtSEmcy3Fj2Hkblkeb12_pAotwe5w7L48ZK2SA8I8kD1qQCyhkzVx5EY3nU
# Set workdir
WORKDIR /app

# Install dependencies
COPY app/ /app/ 
RUN pip install --no-cache-dir -r requirements.txt
RUN chmod -R 755 /app/manage.py
RUN ls -al /app/manage.py
# Copy project files
#COPY /app /app/

# Collect static files
#RUN python manage.py makemigrations
#RUN python manage.py migrate
#RUN python manage.py collectstatic --noinput

# Expose port
EXPOSE 8000

# Start Gunicorn
#CMD ["gunicorn", "django_file_reader.wsgi:application", "--bind", "0.0.0.0:8000"]
