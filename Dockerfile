FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY ./src/requirements.txt /app/requirements.txt

# ==== Install required system packages including ClamAV and libmagic ====
RUN apt-get update && apt-get install -y \
    libmagic1 \
    libmagic-dev \
    clamav \
    clamav-daemon \
    clamav-freshclam && \
    pip install --upgrade pip --root-user-action=ignore && \
    pip install setuptools && \
    pip install -r requirements.txt --no-input && \
    # ==== Clean up to reduce image size ====
    rm -rf /var/lib/apt/lists/* /root/.cache

COPY ./src /app

# Ensure ClamAV virus definitions are up to date
RUN freshclam


# Default command to run the Django app (or any custom command)
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


