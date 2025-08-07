ARG PYTHON_VERSION=3.14
ARG UID
ARG GID

FROM astral/uv:python${PYTHON_VERSION}-rc-bookworm

RUN groupadd -g ${GID} user && \
useradd -m -s /bin/bash -u ${UID} -g ${GID} user

WORKDIR /app