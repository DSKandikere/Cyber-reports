FROM python:3.9-slim@sha256:2d97f6910b16bd338d3060f261f53f144965f755599aab1acda1e13cf1731b1b

RUN apt-get update \
    && apt-get install -y --no-install-recommends socat=1.8.0.3-1 \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir ecdsa==0.19.2 pycryptodome==3.23.0

RUN useradd -m -u 10001 ctf

WORKDIR /app
COPY --chown=ctf:ctf chal.py serve.sh /app/
RUN chmod +x /app/chal.py /app/serve.sh

USER ctf
EXPOSE 1337

CMD ["/app/serve.sh"]