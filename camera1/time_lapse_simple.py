'''
Simple time lapse script obtained from
https://projects.raspberrypi.org/en/projects/raspberry-pi-zero-time-lapse-cam

Modified to create image files with name containing date (not just time).

To create Python venv in which to run use::

    python3 -m venv venv
    source venv/bin/activate
    pip install picamera

'''

from time import sleep
import picamera

WAIT_TIME = 30

def main() -> None:
    '''
    Entry function for ``time_lapse_simple``. Calls
    :meth:`picamera.PiCamera.capture_continuous` in loop with fixed delay.
    Captured images are stored in directory ``/home/pi/time-lapse``.
    '''
    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        for _ in camera.capture_continuous(
                '/home/pi/time-lapse/img{timestamp:%Y-%m-%dT%H-%M-%S}.jpg'):
            sleep(WAIT_TIME)

if __name__ == '__main__':
    main()
