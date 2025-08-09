ARG NODE_VERSION=18

FROM node:${NODE_VERSION}-bookworm

ARG UID
ARG GID

RUN groupmod -g ${UID} node  \
    && usermod -u ${UID} -g ${GID} node

USER ${UID}
WORKDIR /home/node
