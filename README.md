# Installation Guide

1. Clone the repository:
   ```bash
   git clone https://github.com/RuslanShitik/adamanta-test-task.git
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables.
    ```dotenv
   # App
    SECRET_KEY=
    DEBUG=
    
    # Database
    DB_NAME=
    DB_USER=
    DB_PASSWORD=
    DB_HOST=
    DB_PORT=
    
    # IBANAPI
    IBANAPI_API_KEY=
   ```

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

7. Start the development server:
   ```bash
   python manage.py runserver
   ```