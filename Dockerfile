FROM python:3.12-slim AS runtime
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py readme.txt ./
ENV PORT=8505
EXPOSE 8505
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD python -c "import urllib.request, sys; sys.exit(0 if urllib.request.urlopen('http://127.0.0.1:8505/health').status==200 else 1)" || exit 1
CMD ["gunicorn", "--bind", "0.0.0.0:8505", "--workers", "2", "--access-logfile", "-", "app:app"]
