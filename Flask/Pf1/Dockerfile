FROM python:3.8-slim
WORKDIR /app
COPY . /app
RUN pip install --progress-bar off flask
EXPOSE 5050
CMD ["python3", "sample_app.py"]
