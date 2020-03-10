import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="graphene-telemetry",
    version="0.0.1",
    author="Amim Knabben",
    author_email="amim.knabben@gmail.com",
    description="OpenTelemetry + GraphQL",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/knabben/graphene-opentelemetry",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
