from telemetry.tracer import init_tracer, get_tracer

init_tracer()


class TelemetryMiddleware(object):
    """ Telemetry middleware integration. """

    def resolve(self, next, root, info, **args):
        tracer = get_tracer()
        self._set_query(info, tracer)

        with tracer.start_as_current_span(info.field_name) as span:
            promise = next(root, info, **args)
            promise_value = promise.get()

            try:
                return_type = info.return_type.name
            except AttributeError:
                return_type = info.return_type.of_type.name

            span.set_attribute("operation", str(info.operation.operation))
            span.set_attribute("source", str(info.operation.loc.source.body))
            span.set_attribute("parent_type", str(info.parent_type.name))
            span.set_attribute("return_type", str(return_type))
            span.set_attribute("value", str(promise_value))

        return promise

    def _set_query(self, info, tracer):
        parent_span = tracer.get_current_span()
        if "schema" not in parent_span.attributes:
            parent_span.set_attribute("schema", str(info.schema))
