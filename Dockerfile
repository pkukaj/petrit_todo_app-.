# Använd en officiell Python-runtime som en grund
FROM python:3.8-slim

# Sätt arbetskatalogen till /app
WORKDIR /app

# Kopiera kraven och koden till containern
COPY requirements.txt .
COPY app.py .

# Installera Flask och andra beroenden
RUN pip install --no-cache-dir -r requirements.txt

# Exponera port 5000 för Flask-appen
EXPOSE 5000

# Ange kommandot som ska köras när containern startas
CMD ["python", "app.py"]
