# DevOps Data Validation API & CI/CD Pipeline

![CI/CD Pipeline](https://github.com/KAppaiah04/devops-data-api/actions/workflows/ci-cd.yml/badge.svg)

A production-ready microservice built with **FastAPI** that enforces strict data validation rules before database ingestion. This project demonstrates enterprise DevOps practices, including automated testing with **Pytest**, static code linting with **Ruff**, and continuous integration via **GitHub Actions**.

---

## 🎯 Key Features

* **Data Quality API:** Validates incoming payloads using Pydantic models and rejects corrupted or negative metric values with standard HTTP status codes.
* **Automated CI/CD Pipeline:** Runs code quality checks (`ruff`) and unit tests (`pytest`) automatically on cloud runners (`ubuntu-latest`) on every commit or Pull Request.
* **Zero-Regression Gatekeeping:** Uses GitHub status checks and non-zero exit codes to block broken code from reaching the `main` branch.

---

## 🛠️ Tech Stack

* **Framework:** Python 3.11+, FastAPI, Uvicorn
* **Data Validation:** Pydantic
* **Testing & Linting:** Pytest, Ruff, HTTPX
* **DevOps & Automation:** GitHub Actions, Git

---

## 📂 Project Structure

```text
devops-data-api/
├── .github/
│   └── workflows/
│       └── ci-cd.yml    # GitHub Actions workflow configuration
├── .gitignore            # Version control exclusion rules
├── main.py               # FastAPI application & business validation logic
├── test_main.py          # Pytest unit test suite
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation


