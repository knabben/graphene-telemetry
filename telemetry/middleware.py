from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchExportSpanProcessor
from opentelemetry.ext.jaeger import JaegerSpanExporter


# TODO - Make these settings configuration
exporter = JaegerSpanExporter(
    service_name="basic-middleware",
    agent_host_name="localhost",
    agent_port=6831,
)

trace.set_preferred_tracer_provider_implementation(lambda T: TracerProvider())
trace.tracer_provider().add_span_processor(BatchExportSpanProcessor(exporter))


def tracer_middleware(next, root, info, **args):
    tracer = trace.get_tracer(__name__)

    with tracer.start_as_current_span("graphene") as span:
        span.set_attribute("schema", str(info.schema))
        return next(root, info, **args)
