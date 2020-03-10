build_package:
	docker build -t telemetry-build:latest -f docker/Dockerfile.build .; docker run telemetry-build:latest /app/scripts/build.sh

upload_package: build_package
	docker build -t telemetry-build:latest -f docker/Dockerfile.build .; docker run -it telemetry-build:latest /app/scripts/upload.sh

setup:
	python3 -m pip install --upgrade setuptools wheel
