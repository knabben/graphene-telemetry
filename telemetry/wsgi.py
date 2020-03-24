from telemetry.tracer import init_tracer
from opentelemetry.ext.wsgi import OpenTelemetryMiddleware

init_tracer()


def get_telemetry_app(application):
    return OpenTelemetryMiddleware(application)
