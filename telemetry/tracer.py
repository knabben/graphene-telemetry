from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchExportSpanProcessor


def init_tracer():
    from opentelemetry.ext.jaeger import JaegerSpanExporter

    exporter = JaegerSpanExporter(
        service_name="basic", agent_host_name="localhost", agent_port=6831
    )

    trace.set_tracer_provider(TracerProvider())
    span_processor = BatchExportSpanProcessor(exporter)
    trace.get_tracer_provider().add_span_processor(span_processor)


def get_tracer():
    return trace.get_tracer(__name__)
