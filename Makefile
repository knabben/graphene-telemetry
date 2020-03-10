build_package:
	docker build -t telemetry-build:latest -f docker/Dockerfile.build .; docker run telemetry-build:latest

setup:
	python3 -m pip install --upgrade setuptools wheel
