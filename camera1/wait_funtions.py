'''
Various wait functions to be used with time lapse scripts.
'''

from datetime import datetime, timedelta
from time import sleep
import picamera

def caputure_continuous_wait_absolute(camera: picamera.PiCamera, wait: int,
capture_output: str = '/home/pi/time-lapse/img{timestamp:%Y-%m-%dT%H-%M-%S-%f}.jpg',
do_print_file_name: bool = False) -> None:
    '''
    Capture image and delay so that total time to execute is given `wait` of
    seconds. I.e. delay is adjusted by how long it takes for image capture so
    that absolute time taken is the given wait time, **not** time taken to
    capture image **+** wait time.

    :param camera: The camera object on which ``capture_continuous`` is called.
    :type camera: picamera.PiCamera
    :param wait: Absolute time in seconds that this function is to take to
        execute
    :type wait: int
    :param capture_output: Value to pass as ``output`` parameter to
        :meth:`picamera.PiCamera.capture_continuous`. Default:
        ``/home/pi/time-lapse/img{timestamp:%Y-%m-%dT%H-%M-%S-%f}.jpg``
    :type capture_output: str
    :param do_print_file_name: When ``True`` print to stdout the name of capture
        output file when created. Default ``False``.
    :type do_print_file_name: bool
    '''
    # Calculate the time the 1st time lapse is to end
    next_exp = (datetime.now() + timedelta(seconds=wait)).replace(microsecond=0)

    for filename in camera.capture_continuous(capture_output):
        if do_print_file_name:
            print(filename)

        # Calculate the delay until the end of current time lapse
        delay = (next_exp - datetime.now()).total_seconds()
        sleep(delay)

        # Calculate the time next time lapse is to end
        next_exp = (datetime.now() + timedelta(seconds=wait)).replace(microsecond=0)

# end caputure_wait_absolute()
