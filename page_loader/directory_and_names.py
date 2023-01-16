import os
import re
from urllib.parse import urlparse


def make_directory(path):
    path = path.replace('.html', '_files')
    if not os.path.isdir(path):
        os.mkdir(path)
    else:
        pass


def get_file_name(url):
    parsed_url = urlparse(url)
    root, file_format = os.path.splitext(parsed_url.path)
    name = re.sub(r'(\W)', '-', parsed_url.netloc + root)
    if not file_format:
        file_format = '.html'
    return name + file_format


def get_directory_name(url):
    parsed_url = urlparse(url)
    root, file_format = os.path.splitext(parsed_url.path)
    name = re.sub(r'(\W)', '-', parsed_url.netloc + root)
    return name + '_files'
