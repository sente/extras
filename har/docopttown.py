"""
Usage: my_program <path> [options]

"""

from docopt import docopt



if __name__ == '__main__':
    arguments = docopt(__doc__)
    print(arguments)

