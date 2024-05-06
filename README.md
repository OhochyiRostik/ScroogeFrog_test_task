## ScroogeFrog_test_task

### Running the code:
Clone the repository

`cp .env.example .env`

`docker-compose build`

`docker-compose up -d `

`docker-compose run --rm app sh -c "python manage.py makemigrations"`

`docker-compose run --rm app sh -c "python manage.py migrate"`

`docker-compose run --rm app sh -c "python manage.py createsuperuser"`

### A list of what was implemented:
Key Requirements:

• Design an Event model with fields such as title, description, date, location, and organizer.(Done)

• Create custom user model for registration with email and password.(Done)

• Implement CRUD (Create, Read, Update, Delete) operations for the Event model.(Done)

Url for CRUD operations, searching, filtering, ordering over events. An unauthorized user can only read.
#### http://127.0.0.1:8000/api/v1/event/

• Basic User Registration and Authentication.(Done)

Url for registration
#### http://127.0.0.1:8000/api/v1/users/

Login/Logout Session
#### http://127.0.0.1:8000/api/v1/auth/session/login/
#### http://127.0.0.1:8000/api/v1/auth/session/logout/

Login/Logout Token
#### http://127.0.0.1:8000/api/v1/auth/token/login/
#### http://127.0.0.1:8000/api/v1/auth/token/logout/

• Event Registration.(Done)

Event registration url (At the end of the link, you need to specify the event number)
#### http://127.0.0.1:8000/api/v1/register/1/


• Add unit tests.(Done)

They are in folder `drf_test_task_api/events/tests`

Command to run tests:
`docker-compose run --rm app sh -c "python manage.py test /drf_test_task_app/events/tests"`

Bonus Points:

• Containerize application with Docker, add Docker Compose.(Done)

• Implement an advanced feature like event search or filtering.(Done)


##### All available URLs can also be found in `drf_test_task_api/drf_test_task_api/urls.py`