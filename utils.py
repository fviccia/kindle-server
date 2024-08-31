import glob
import os
from sys import platform

from config import *

"""
Return the filenames in the order selected in the config file
"""


def get_filenames():
    file_list = []
    for type in FILE_TYPES_ALLOWED:
        file_list.extend(glob.glob(SAVED_WEBPAGES_DIR + "*." + type))
        if platform == "linux" or platform == "linux2":
            file_list.extend(glob.glob(SAVED_WEBPAGES_DIR + "*." + type.upper()))
    if SORT_BY == "CREATION":
        file_list.sort(key=os.path.getctime, reverse=REVERSE_ORDER)
    elif SORT_BY == "MODIFIED":
        file_list.sort(key=os.path.getmtime, reverse=REVERSE_ORDER)
    else:
        file_list.sort(reverse=REVERSE_ORDER)
    return file_list


# It actually do not convert to html
# but adding <p> tags is enough to display text correctly  in the Kindle
def txt2html(text):
    paragraphs = text.split("\n")
    output = ""
    for para in paragraphs:
        output += "<p>" + para + "</p>"
    return output


def proccess_url(url):
    print(url)
