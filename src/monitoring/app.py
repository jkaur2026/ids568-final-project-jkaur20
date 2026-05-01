from fastapi import FastAPI, Request
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from fastapi.responses import Response
import time
import random

app = FastAPI(title="Final Project Monitoring API")

REQUEST_COUNT = Counter("request_count", "Total API requests", ["endpoint"])
ERROR_COUNT = Counter("error_count", "Total API errors", ["endpoint"])
REQUEST_LATENCY = Histogram("request_latency_seconds", "Request latency in seconds", ["endpoint"])
INPUT_ANOMALY_COUNT = Counter("input_anomaly_count", "Input integrity anomalies")

@app.get("/")
def home():
    return {"message": "Monitoring API is running"}

@app.post("/predict")
async def predict(request: Request):
    start_time = time.time()
    endpoint = "/predict"
    REQUEST_COUNT.labels(endpoint=endpoint).inc()

    try:
        data = await request.json()
        user_input = data.get("text", "")

        if not user_input or len(user_input) < 3:
            INPUT_ANOMALY_COUNT.inc()

        if random.random() < 0.05:
            raise ValueError("Simulated model error")

        result = {
            "input": user_input,
            "prediction": "simulated_response",
            "latency_note": "Request processed successfully"
        }

        return result

    except Exception as e:
        ERROR_COUNT.labels(endpoint=endpoint).inc()
        return {"error": str(e)}

    finally:
        latency = time.time() - start_time
        REQUEST_LATENCY.labels(endpoint=endpoint).observe(latency)

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
