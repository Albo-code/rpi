camera1
=======

Modules using the `picamera`_ Python library to interface to the `Raspberry Pi`_
`camera`_.

Since release of Raspberry Pi OS image based on `Debian Bullseye`_ (8th Nov
2021) the Raspberry Pi OS **no longer supports** the *picamera* Python library
(or *raspicam* apps), see the `Bullseye camera system`_ news post for details.
Therefore the Python code described here **will not work** with this or later
releases of the Raspberry Pi OS.

.. _picamera: https://picamera.readthedocs.io/en/latest/
.. _Raspberry Pi: https://www.raspberrypi.org/
.. _camera: https://www.raspberrypi.org/learning/getting-started-with-picamera/
.. _Debian Bullseye: https://www.raspberrypi.com/news/raspberry-pi-os-debian-bullseye/
.. _Bullseye camera system: https://www.raspberrypi.com/news/bullseye-camera-system/

**camera1** contents:

.. toctree::
   :maxdepth: 4

   time_lapse
   time_lapse_simple
   time_lapse_wait_abs
   wait_funtions
