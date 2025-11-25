DevOps Medium Project (FastAPI + CI/CD + Kind + Terraform)

Small FastAPI app built to practice core DevOps concepts: testing, containerization, CI/CD, and Kubernetes infra-as-code.

Features:

- FastAPI app with simple CRUD-style endpoints

- Unit & integration tests using pytest

- Static analysis: flake8, black

- Security scan: bandit

- Containerization: Docker image built and pushed to GHCR

- CI: GitHub Actions runs lint, tests, security scan, build & push

- CD / Deployment: Kubernetes manifests (YAML) for app deployment

- Local cluster: Kind (Kubernetes in Docker) for local testing

- Infrastructure as Code: Terraform used for stable K8s resources (namespace, service, etc.)
