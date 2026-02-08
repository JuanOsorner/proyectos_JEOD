# Django Practice Environment

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-4.2-092E20?style=for-the-badge&logo=django&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)

## 📋 Overview

**Practica Ej2** is a robust boilerplate designed for Django development and practice. It serves as a foundational environment pre-configured with essential dependencies for building scalable web applications using Python and MySQL.

This project is intended for:
-   **Skill Development**: A sandbox for testing Django features, ORM queries, and view logic.
-   **Rapid Prototyping**: A clean starting point for new ideas without repetitive setup.
-   **Backend Architecture**: Demonstrating best practices in project structure and database integration.

## ✨ Key Features

-   **Django 4.2 LTS**: Built on the latest Long-Term Support version of Django for stability and security.
-   **Database Ready**: Pre-configured with `mysqlclient` for seamless integration with MySQL databases.
-   **Development Tools**: Includes utilities like `django-browser-reload` for an enhanced developer experience.
-   **Clean Architecture**: Follows standard Django project layout for maintainability.

## 🚀 Getting Started

Follow these steps to set up the environment locally.

### 1. Prerequisites

Ensure you have Python 3.10+ installed on your system.

### 2. Installation

Clone the repository and navigate to the project directory:

```bash
git clone <repository_url>
cd practica_ej2
```

### 3. Environment Setup

It is recommended to use a virtual environment to manage dependencies.

**Create and activate the environment:**

```bash
# Windows
python -m venv entorno
.\entorno\Scripts\activate

# Linux/macOS
python3 -m venv entorno
source entorno/bin/activate
```

**Install dependencies:**

```bash
pip install -r requirements.txt
```

### 4. Database Configuration

Ensure your MySQL server is running. configure your database credentials in `settings.py` (or `.env` if applicable) before running migrations.

```bash
python manage.py migrate
```

### 5. Run the Server

Start the development server:

```bash
python manage.py runserver
```

Access the application at `http://127.0.0.1:8000/`.

## 📚 Documentation & Commands

For a detailed reference on common commands for virtual environments, package management, and Django operations, please refer to the [Commands Guide](comandos.md).

---
*Developed for educational purposes and professional development.*
