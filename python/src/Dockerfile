FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

EXPOSE 8502

CMD streamlit run consumer.py --server.port 8501 & streamlit run producer.py --server.port 8502