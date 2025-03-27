# Project Setup Guide

This guide will help you clone and set up this Django project on your local machine.

## **1. Prerequisites**
Ensure you have the following installed on your system:
- **Python (3.10)
- **Git**
- **pip (Python package manager)**

## **2. Clone the Repository**
```sh
git clone https://github.com/abdul-yusuf/DroneDeliveryBackend.git
```
## **3. Create a Virtual Environment**
It's best to install dependencies in an isolated environment:
```sh
python -m venv venv
```
Activate the virtual environment:

Windows (Git Bash)
```sh
source venv/Scripts/activate
```

Mac/Linux
```sh
source venv/bin/activate
```

## **4. Install Dependencies**
```sh
pip install -r requirements.txt
```

## **6. Apply Migrations**
```sh
python manage.py migrate
```

## **7. Create a Superuser**
`For accessing admin panel:

```sh
python manage.py createsuperuser
```

## **8. Run the Server**
```sh
python manage.py runserver
```
