import glob
import sys
from os.path import join


def get_input(directory, base=sys.argv[0].split(".")[0] + ".*"):
    """Return the input as read from the given directory.

    Arguments:
        directory {str} -- The directory that contains the given file

    Keyword Arguments:
        base {str} -- The base filename, without extension (default: {sys.argv[0][:-2]+"*"})

    Returns:
        str -- The contents of the file

    """
    path = join(directory, base)
    try:
        filename = glob.glob(path)[0]
    except IndexError:
        raise FileNotFoundError(path)
    with open(filename, "r") as f:
        return f.read()
