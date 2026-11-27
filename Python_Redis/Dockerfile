#Stage 1
FROM python:3.12-slim AS builder

WORKDIR /build

COPY app/requirements.txt .

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

#Stage 2
FROM python:3.12-slim AS runtime

WORKDIR /app

RUN groupadd --system --gid 10001 appgroup \
    && useradd --system --uid 10001 --gid appgroup \
       --home-dir /app --no-create-home appuser

COPY --from=builder /install /usr/local

COPY --chown=10001:10001 app/ /app/

USER 10001:10001

EXPOSE 5000

CMD ["python","app.py"]
