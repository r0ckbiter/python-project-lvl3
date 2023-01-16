import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from page_loader.directory_and_names import get_file_name

ATTRIBUTES = {'img': 'src'}


def download_asset(link, assets_path):
    response = requests.get(link)

    file_name = get_file_name(link)
    file_path = os.path.join(assets_path, file_name)

    with open(file_path, 'wb') as file:
        file.write(response.content)


def replace_links(url, html_page, assets_dir_name):
    soup = BeautifulSoup(html_page, 'html.parser')
    assets_links = []

    for element in soup.find_all(ATTRIBUTES):
        attribute_name = ATTRIBUTES[element.name]
        asset_link = element.get(attribute_name)

        link = urljoin(url, asset_link)
        asset_name = get_file_name(link)
        asset_path = os.path.join(assets_dir_name, asset_name)
        element[attribute_name] = asset_path
        assets_links.append(link)

    return soup.prettify(), assets_links
