ARG PYTHON_VERSION=3.14

FROM astral/uv:python${PYTHON_VERSION}-rc-bookworm

ARG UID
ARG GID

RUN groupadd -g ${GID} user && \
    useradd -m -s /bin/bash -u ${UID} -g ${GID} user

USER user
WORKDIR /user
