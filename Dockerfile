
FROM python:3.12-slim
WORKDIR /app
COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "app_streamlit.py", "--server.port=8501", "--server.address=0.0.0.0"]
