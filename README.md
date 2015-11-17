##HOW TO INSTALL:

````
virtualenv ticketReservation
cd ticketReservation/
. bin/activate

git clone https://isimicic@bitbucket.org/isimicic/ticketreservation.git

cd ticketReservation/
pip install -r requirements.txt
````

###Run server

````
python manage.py migrate    
python manage.py runserver
````
