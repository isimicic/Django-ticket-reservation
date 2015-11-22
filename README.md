##HOW TO INSTALL:

````
virtualenv ticketReservation
cd ticketReservation/
. bin/activate

git clone https://isimicic@bitbucket.org/VsitePythonTeam/ticket-reservation.git

cd ticketReservation/
pip install -r requirements/requirements.txt
````

###Create super user

````
python manage.py createsuperuser
````

###Run server

````
python manage.py makemigration
python manage.py migrate    
python manage.py runserver
````