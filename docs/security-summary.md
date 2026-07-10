# Security Summary

## Overview

This project follows basic cloud security and DevOps best practices while remaining within the AWS Free Tier. Security measures were implemented to protect the application, AWS resources, and deployment process.

---

## 1. IAM (Identity and Access Management)

* Created an IAM Role for the EC2 instance.
* Attached the IAM Role to the EC2 instance instead of storing AWS Access Keys on the server.
* Granted only the permissions required to access the Amazon S3 bucket (Least Privilege Principle).

**Benefits**

* No hardcoded AWS credentials.
* Reduced risk of credential leakage.
* Easier credential management.

---

## 2. EC2 Security Groups

The EC2 Security Group was configured with only the required inbound rules.

| Port | Protocol | Purpose          |
| ---- | -------- | ---------------- |
| 22   | TCP      | SSH access       |
| 80   | TCP      | HTTP access      |
| 443  | TCP      | HTTPS (optional) |

All other inbound ports remain blocked.

---

## 3. Application Security

The Flask application is **not exposed directly** to the internet.

Instead:

```
Internet
     │
 Port 80
     │
 Nginx
     │
127.0.0.1:8000
     │
 Gunicorn
     │
 Flask Application
```

Gunicorn listens only on:

```
127.0.0.1:8000
```

This prevents direct external access to the application server.

---

## 4. Reverse Proxy

Nginx is configured as a reverse proxy.

Benefits include:

* Hides the application server.
* Improves security.
* Handles client requests efficiently.
* Simplifies future HTTPS configuration.

---

## 5. GitHub Actions Security

The CI/CD pipeline uses **GitHub Secrets** to securely store sensitive information.

Secrets used:

* EC2 Host
* EC2 Username
* SSH Private Key

Sensitive credentials are **not stored** in the source code.

---

## 6. Amazon S3 Security

Amazon S3 is used to store application backups.

Security measures:

* Access through IAM Role.
* No public bucket access.
* Bucket used only for backup purposes.

---

## 7. SSH Security

SSH access is secured using **public/private key authentication**.

Password authentication is disabled in the deployment workflow.

Only authorized users with the correct private key can access the EC2 instance.

---

## 8. Python Virtual Environment

The application runs inside a Python virtual environment.

Benefits:

* Dependency isolation.
* Prevents conflicts with system packages.
* Easier dependency management.

---

## 9. Best Practices Followed

* Principle of Least Privilege (IAM)
* SSH Key Authentication
* Reverse Proxy using Nginx
* Gunicorn bound to localhost
* Virtual Environment for dependency isolation
* GitHub Secrets for CI/CD credentials
* Secure S3 access using IAM Role

---

## Future Improvements

The following improvements can further enhance security:

* Enable HTTPS using Let's Encrypt SSL certificates.
* Use AWS WAF to protect against common web attacks.
* Configure automatic security updates.
* Enable AWS CloudTrail for audit logging.
* Store secrets using AWS Secrets Manager or AWS Systems Manager Parameter Store.
* Implement regular vulnerability scanning.

---

## Conclusion

The application was deployed using secure DevOps practices on AWS Free Tier. IAM Roles, Security Groups, SSH key authentication, GitHub Secrets, and Nginx reverse proxy were used to improve the overall security of the deployment while following AWS and DevOps best practices.

---

