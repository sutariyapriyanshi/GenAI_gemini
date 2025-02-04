# Dockerfile
FROM python:3.12.2

WORKDIR /app

COPY requirement.txt requirement.txt
RUN pip install -r requirement.txt

COPY . .

CMD ["streamlit", "run", "app.py"]
