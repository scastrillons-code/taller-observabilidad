from flask import Flask, Response
from prometheus_client import Counter, Gauge, generate_latest, CONTENT_TYPE_LATEST
import random

app = Flask(__name__)

visits = Counter('webapp_visits_total', 'Total visits to the homepage')
random_value = Gauge('webapp_random_value', 'Valor aleatorio de ejemplo')


@app.route("/")
def hello():
    visits.inc()
    random_value.set(random.randint(1, 100))
    return "Hello, Prometheus!"


@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)