'''
Wait an absolute amount of seconds between image captures.

To create Python venv in which to run use::

    python3 -m venv venv
    source venv/bin/activate
    pip install picamera

'''
# Standard imports
import textwrap
from argparse import ArgumentParser, RawDescriptionHelpFormatter
from pathlib import Path

# 3rd party imports
import picamera

# Local imports
from wait_funtions import caputure_continuous_wait_absolute

def time_lapse(wait_time: int, dir_name: str) -> None:
    '''
    Capture images by calling :meth:`wait_funtions.caputure_continuous_wait_absolute`.

    :param wait_time: Time in seconds to pass in call to ``caputure_continuous_wait_absolute``
    :type wait_time: int
    :param dir_name: Name of directory where captured images are to be stored,
        used to create ``capture_output`` param in call to ``caputure_continuous_wait_absolute``
    :type dir_name: str
    '''
    with picamera.PiCamera() as my_camera:
        my_camera.resolution = (1024, 768)
        caputure_continuous_wait_absolute(my_camera, wait_time,
            dir_name + '/img{timestamp:%Y-%m-%dT%H-%M-%S-%f}.jpg', True)

def main() -> None:
    '''
    Parse command line arguments and pass to :func:`time_lapse_wait_abs.time_lapse`.
    '''
    parser = ArgumentParser(formatter_class=RawDescriptionHelpFormatter,
                            description=textwrap.dedent(
                            '''
                            example: time_lapse_wait_abs.py -w 10 -d ~/time_lapse/raw
                            '''))
    parser.add_argument('-w', '--wait', type=int, action='store', default=30,
                        help="wait time between captures in seconds. " +
                             "Default: 30")
    parser.add_argument('-d', '--dir', type=str, action='store',
                        default='/home/pi/time-lapse/raw',
                        help="name of directory to store images. " +
                             "Default: /home/pi/time-lapse/raw")
    args = parser.parse_args()

    if args.wait <= 0:
        raise RuntimeError(f"Wait arg must be positive: {args.wait}")

    if not Path(args.dir).is_dir():
        raise RuntimeError(f"Directory arg does not exist: {args.dir}")

    time_lapse(args.wait, args.dir)

if __name__ == '__main__':
    main()
