Graphene Telemetry
===

A graphene middleware to traces and metrics interception.

This software is Opentelementry-WSGI extension compatible.

Installation
---

Install this middleware via PyPI repository: 

```
pip install graphene-telemetry
```

Usage
---

First Span is provided by the OpenTelemetry WSGI, install it in your Django wsgi.py file.

```.python
import os

from django.core.wsgi import get_wsgi_application
from telemetry.wsgi import get_telemetry_app

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'microservice.settings')

application = get_wsgi_application()
application = get_telemetry_app(application)
```

The GraphQL attributes dump is provided in a child span, you need to enable it via a graphene middleware.

```
GRAPHENE = {
    "SCHEMA": "your_project.schema",
    "MIDDLEWARE": [
      "telemetry.middleware.TelemetryMiddleware"
    ],
}
```