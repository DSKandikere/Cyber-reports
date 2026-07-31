FROM python:3.11-slim@sha256:db3ff2e1800a8581e2c48a27c3995339d47bdf046da21c7627accd3d51053a93

ARG APP_USER=app
ARG APP_UID=10001
ARG APP_GID=10001

RUN groupadd --gid "${APP_GID}" "${APP_USER}" \
 && useradd --uid "${APP_UID}" --gid "${APP_GID}" --create-home --shell /usr/sbin/nologin "${APP_USER}" \
 && mkdir -p /app \
 && chown -R "${APP_UID}:${APP_GID}" /app

WORKDIR /app

COPY --chown=${APP_UID}:${APP_GID} app.py /app/

USER ${APP_UID}:${APP_GID}

EXPOSE 1337

CMD ["python3", "app.py"]
