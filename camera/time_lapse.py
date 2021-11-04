'''
Time lapse script accepting various arguments to determine how time lapse
images are to be captured and where they are to be stored.

To create Python venv in which to run use:

    python3 -m venv venv
    source venv/bin/activate
    pip install picamera
'''
# Standard imports
import argparse
import textwrap
from pathlib import Path
from time import sleep

# 3rd party imports
import picamera

def time_lapse(wait_time: int, dir_name: str) -> None:
    '''
    Capture images by calling the :func:`picamera.PiCamera.capture_continuous()
    function in loop with delay.

    :param wait_time: Time in seconds to delay between calls to
        `capture_continous()`
    :type wait_time: int
    :param dir_name: Name of directory where captured images are to be stored
    :type dir_name: str
    '''
    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        for filename in camera.capture_continuous(
                dir_name + '/img{timestamp:%Y-%m-%dT%H-%M-%S}.jpg'):
            print(filename)
            sleep(wait_time)

def main() -> None:
    '''
    Parse command line arguments and pass to :func:`time_lapse.time_lapse`.
    '''
    parser = argparse.ArgumentParser(
                formatter_class=argparse.RawDescriptionHelpFormatter,
                description=textwrap.dedent(
                    '''
                    example: time_lapse.py -w 10 -d ~/time_lapse/raw
                    '''))
    parser.add_argument('-w', '--wait', type=int, action='store', default=30,
                        help="wait time between captures in seconds. " + 
                             "Default: 30")
    parser.add_argument('-d', '--dir', type=str, action='store',
                        default='/home/pi/time-lapse/raw/',
                        help="name of directory to store images. " +
                             "Default: /home/pi/time-lapse/raw/")
    args = parser.parse_args()

    if args.wait <= 0:
        raise RuntimeError(f"Wait arg must be positive: {args.wait}")

    if not Path(args.dir).is_dir():
        raise RuntimeError(f"Directory arg does not exist: {args.dir}")

    time_lapse(args.wait, args.dir)

if __name__ == '__main__':
    main()
