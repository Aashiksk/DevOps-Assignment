# Deployment Guide

## Prerequisites

- AWS Account
- Ubuntu EC2 Instance
- Python 3
- Git
- Nginx
- Gunicorn

---

## Clone Repository

git clone <repository-url>

---

## Create Virtual Environment

python3 -m venv venv

source venv/bin/activate

---

## Install Dependencies

pip install -r requirements.txt

---

## Configure Gunicorn

sudo nano /etc/systemd/system/gunicorn.service

Restart

sudo systemctl daemon-reload

sudo systemctl restart gunicorn

---

## Configure Nginx

sudo nano /etc/nginx/sites-available/default

Restart

sudo systemctl restart nginx

---

## Configure S3

- Create bucket
- Attach IAM Role
- Upload backup

---

## Configure GitHub Actions

- Add Secrets
- Push code
- Automatic deployment

---

## Verify

Open

http://<EC2-IP>