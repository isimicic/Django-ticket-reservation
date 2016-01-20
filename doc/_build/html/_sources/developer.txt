.. highlight:: bash

Developer guide
===============

Setup developer environment
---------------------------

Create environment
******************
::

   virtualenv ticketReservation
   cd ticketReservation/
   . bin/activate

Pull project from repo
**********************
::

   git clone git@bitbucket.org:VsitePythonTeam/ticket-reservation.git

Install requirements
********************
::

   cd ticketReservation/
   pip install -r requirements.txt

Create admin user
*****************
::

   python manage.py createsuperuser

Run server
**********
::

   python manage.py makemigration
   python manage.py migrate
   python manage.py runserver

Running Python tests
--------------------

Easy as::

    $ bin/nosetests

By default it will run against sqlite fixture, you can also tell nosetests to use mysql fixture (you need to import sql manually for now)::

    $ DATABASE="mysql" bin/nosetests

Or just specify sqlalchemy engine::

    $ ENGINE="sqlite:////var/lib/bacula/bacula.db" bin/nosetests

.. note::

    Installer will ask you few questions about SQL database and configuration for bconsole.

Running Javascript tests
------------------------

Install and configure phantomjs (webkit headless testing)::

    $ sudo apt-get install libqtwebkit-dev
    $ git clone git://github.com/ariya/phantomjs.git && cd phantomjs
    $ qmake-qt4 && make
    $ sudo cp bin/phantomjs /usr/local/bin/

Run tests::

    $ cd ../ticket-reservation
    $ ./.travis_qunit_tests.sh


Coding conventions
------------------

* `PEP8 <http://www.python.org/dev/peps/pep-0008/>`_ except for 80 char length rule
* add changelog, test and documentation with code in commits
* same applies to javascript
* jslinted javascript
