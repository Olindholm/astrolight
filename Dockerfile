FROM python:3.10.6-slim AS builder
WORKDIR /build

RUN pip install pip --upgrade
RUN pip install build

# Copying only neccesary files is a lot faster than e.g.: COPY . .
COPY setup.py pyproject.toml .
COPY src src

ARG PACKAGE_VERSION
ENV PACKAGE_VERSION $PACKAGE_VERSION
RUN python -m build --wheel .


FROM python:3.10.6-slim as image
WORKDIR /app

RUN pip install pip --upgrade
RUN --mount=from=builder,source=/build,target=/build pip install /build/dist/*.whl

ENTRYPOINT ["astrolight"]
