Requirments:
    python 3.8 or later
    install required libraries using "pip install django django_restframework djangorestframework-simplejwt"
    

Steps:
    open cmd in project directory
    create virtual environment using command "python -m venv [virtual_environtment_name]"
    activate virtual environment using command "virtual_environment_name\Scripts\activate.bat" for windows
    run command "py manage.py createsuperuser" create admin by providing username and password
    run command "py manage.py runserver" now project is rendered on internal server

Functionalities
    Student Features:
        Students can register and log in.
        Students can view their results using their USN (University Seat Number / Roll Number).

    Teacher Features:
        Teachers can log in using superuser credentials.
        Teachers can enter and update students' marks for various semesters.

    Admin Features:
        Admins can add or update subjects for each semester.
        Admins can manage student and teacher accounts.

Additional Notes
    The project uses Django Rest Framework (DRF) for API development.
    JWT (JSON Web Token) authentication is used for secure access.
    The admin panel is accessible at: http://127.0.0.1:8000/admin/

