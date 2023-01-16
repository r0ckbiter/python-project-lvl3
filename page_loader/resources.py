import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from page_loader.directory_and_names import get_file_name

ATTRIBUTES = {'img': 'src', 'link': 'href', 'script': 'src'}


def replace_links(url, html_page, assets_dir_name):
    soup = BeautifulSoup(html_page, 'html.parser')
    assets_links = []

    for element in soup.find_all(ATTRIBUTES):
        attribute_name = ATTRIBUTES[element.name]
        asset_link = element.get(attribute_name)

        if is_local(url, asset_link):
            link = urljoin(url, asset_link)
            asset_name = get_file_name(link)
            asset_path = os.path.join(assets_dir_name, asset_name)
            element[attribute_name] = asset_path
            assets_links.append(link)

    return soup.prettify(formatter='html5'), assets_links


def is_local(url, asset_link):
    base_domain = urlparse(url).netloc
    asset_domain = urlparse(asset_link).netloc
    if not asset_domain:
        return True
    return base_domain == asset_domain


def download_asset(link, assets_path):
    response = requests.get(link)

    file_name = get_file_name(link)
    file_path = os.path.join(assets_path, file_name)

    with open(file_path, 'wb') as file:
        file.write(response.content)
