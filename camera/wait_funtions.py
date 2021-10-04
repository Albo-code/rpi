'''
Various wait functions to be used with time lapse scripts.
'''

from datetime import datetime, timedelta
from time import sleep
import picamera

def caputure_continuous_wait_absolute(camera: picamera.PiCamera, wait: int,
capture_output: str = '/home/pi/time-lapse/img{timestamp:%Y-%m-%dT%H-%M-%S-%f}.jpg'
) -> None:
    '''
    Capture image and delay so that total time to execute is given `wait` of
    seconds. I.e. delay is adjusted by how long it takes for image capture so
    that absolute time taken is the given wait time, **not** time taken to
    capture image **+** wait time.
    :param camera: The camera object on which `capture_continuous` is called.
    :type camera: picamera.PiCamera
    :param wait: Absolute time in seconds that this function is to take to
                execute
    :type wait: int
    :param capture_output: Value to pass as `output` parameter to
                `picamera.PiCamera.capture_continuous`. Default:
                `/home/pi/time-lapse/img{timestamp:%Y-%m-%dT%H-%M-%S-%f}.jpg`
    :type capture_output: str
    :return: None
    '''
    # Calculate the delay to the start of the next exposure
    next_exp = (datetime.now() + timedelta(seconds=wait)).replace(microsecond=0)
    camera.capture_continuous(capture_output)
    delay = (next_exp - datetime.now()).seconds
    sleep(delay)
# end caputure_wait_absolute()
