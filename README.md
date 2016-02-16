##HOW TO INSTALL:

````
virtualenv ticketReservation
cd ticketReservation/
. bin/activate

git clone https://github.com/isimicic/Django-ticket-reservation.git

cd ticketReservation/
pip install -r requirements.txt
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