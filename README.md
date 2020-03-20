# BookMyShow - Python Microservices example


Overview
========

BookMyShow is an example project which demonstrates the use of microservices for a movie theater. 
The backend is powered by 4 microservices written in Python using Flask. 

 * Movie Service: Provides information like movie ratings, title, etc.
 * Show Times Service: Provides show times information.
 * Booking Service: Provides booking information. 
 * Users Service: Provides movie suggestions for users by communicating with other services.

Requirements
===========

* Python 3.5 or above
* Platform independent

Install
=======

The quick way is use the provided `setup` file.

<code>
$ python setup.py install
$ python setup.py develop
</code>

Starting and Stopping Services
==============================

To launch the services:

<code>
$ make launch
</code>

To stop the services: 

<code>
$ make shutdown
</code>
