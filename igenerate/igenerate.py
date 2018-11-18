#!/usr/bin/python
import os
import sys
from enum import Enum

from PIL import Image


class Formats(Enum):
    iwatch = [48, 55, 58, 80, 87, 88, 100, 172, 196, 216, 1024]
    ios = [40, 60, 58, 87, 80, 120, 180, 20, 29, 76, 152, 167, 1024]


def generate(file, size, out_path):
    postfix = "-%d-%d.jpg" % (size, size)
    img_size = size, size
    file_name = os.path.splitext(file)[0]
    outfile = "%s/%s%s" % (out_path, file_name, postfix)
    try:
        print("generating '%s%s'" % (file_name, postfix))
        im = Image.open(file)
        im.thumbnail(img_size, Image.ANTIALIAS)
        im.save(outfile, "JPEG")
    except IOError:
        print("cannot create %dx%d for '%s'" % (size, size, file))


def valid(argv):
    if len(argv) < 1:
        return False
    if argv[0] not in Formats.__members__:
        return False

    return True


def main(argv):
    if not valid(argv):
        print("usage: igenerate [%s] [icon_path]" % '|'.join(Formats.__members__))
        exit(0)

    type = argv[0]
    file = argv[1]

    for size in Formats[type].value:
        generate(file, size, os.getcwd())

    print("all icons generated for %s" % type)


if __name__ == "__main__":
    main(sys.argv[1:])
