import os
import re
from requests import get
from urllib import parse
from bs4 import BeautifulSoup


def download(link_url, current_path):
    response = get(link_url)
    html_page = BeautifulSoup(response.text, 'html.parser')
    html_file_path = os.path.join(current_path, get_file_name(link_url))
    with open(html_file_path, 'w') as f:
        f.write(html_page.prettify())
    return html_file_path


def get_file_name(url):
    url_name = parse.urlparse(url)
    url_raw_name = '{0}{1}'.format(url_name.netloc, url_name.path)
    file_name = re.sub(r'(/|[.])', '-', url_raw_name)
    return '{0}{1}'.format(file_name, '.html')
