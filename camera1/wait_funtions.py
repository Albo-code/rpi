'''
Various wait functions to be used with time lapse scripts.
'''

from datetime import datetime, timedelta
from time import sleep
import picamera

def caputure_continuous_wait_absolute(camera: picamera.PiCamera, wait: int,
capture_output: str = '/home/pi/time-lapse/img{timestamp:%Y-%m-%dT%H-%M-%S-%f}.jpg',
do_sync_with_period: bool = False, do_print_file_name: bool = False) -> None:
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
    :param do_sync_with_period: When ``True`` delay starting time lapse until the
        current time is a factor of the current wait period, e.g. if wait is
        5 seconds, the first image will not be taken until the current time is
        0, 5, 10, 15, ..., etc. seconds past the minute. Default ``False``
    :type do_sync_with_period: bool
    :param do_print_file_name: When ``True`` print to stdout the name of capture
        output file when created. Default ``False``.
    :type do_print_file_name: bool
    '''

    if do_sync_with_period:
        # Calculate the amount of time to delay before starting time lapse so
        # that each image is captured on a multiple of the wait period
        now = datetime.now()
        start_time = now + (datetime.min - now) % timedelta(seconds=wait)
        print(f"Time now = {now}")
        print(f"Sync on wait time gives start time = {start_time}")

        # Calculate time until start_time and delay unti this has arrived
        start_delay = (start_time - datetime.now()).total_seconds()
        print(f"Waiting {start_delay}s to start time lapse...")
        sleep(start_delay)

    for filename in camera.capture_continuous(capture_output):
        if do_print_file_name:
            print(filename)

        # Calculate the delay until the end of current time lapse
        next_exp = (datetime.now() + timedelta(seconds=wait)).replace(microsecond=0)
        delay = (next_exp - datetime.now()).total_seconds()
        sleep(delay)

# end caputure_wait_absolute()
