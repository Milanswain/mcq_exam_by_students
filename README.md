# MCQ EXAM OF STUDENTS BY API


## step - 1
clone the project <br >
` git clone https://github.com/Milanswain/mcq_exam_by_students.git`                                         


## step - 2
create a virtual environment with name venv and activate <br >
`virtualenv venv` <br >
`source venv/bib/activate`


## step - 3
install depedancies <br >
`pip install -r requirements.txt`


## step - 4
create databasse <br >
`make migrate` <br >
or <br >

`python manage.py makemigrations`
`python manage.py migrate`

## step - 5
initial set up <br >
`make intial-setup` <br >
or <br >
`python manage.py initial_setup`

## step - 6
create admin <br >
`make admin` <br >
or <br >
`python manage.py createsuperuser`

## step - 7
runserver <br >
`make runserver` <br >
or <br >
`python manage.py runserver`

## step - 8
swagger documentaion <br >
`http://127.0.0.1:8000/swagger/` <br >
redoc documentaion <br>
`http://127.0.0.1:8000/redoc/`


