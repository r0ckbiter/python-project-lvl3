import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from page_loader.logger import logger
from page_loader.directory_and_names import get_file_name

ATTRIBUTES = {'img': 'src', 'link': 'href', 'script': 'src'}


def replace_links(url, html_page, assets_dir_name):
    soup = BeautifulSoup(html_page, 'html.parser')
    assets_links = []

    logger.info('searching for links')
    for element in soup.find_all(ATTRIBUTES):
        attribute_name = ATTRIBUTES[element.name]
        asset_link = element.get(attribute_name)
        logger.info(f'received asset link {asset_link}')

        if is_local(url, asset_link):
            link = urljoin(url, asset_link)
            asset_name = get_file_name(link)
            asset_path = os.path.join(assets_dir_name, asset_name)
            element[attribute_name] = asset_path
            logger.info(f'asset link {asset_link} replaced with {asset_path}')
            assets_links.append(link)

    return soup.prettify(formatter='html5'), assets_links


def is_local(url, asset_link):
    base_domain = urlparse(url).netloc
    asset_domain = urlparse(asset_link).netloc
    if not asset_domain:
        return True
    return base_domain == asset_domain


def download_asset(link, assets_path):
    logger.info(f'trying to download {link} to {assets_path}')
    response = requests.get(link)
    logger.info(f"got {response}")

    file_name = get_file_name(link)
    logger.info(f'creating filename {file_name}')
    file_path = os.path.join(assets_path, file_name)
    logger.info(f'creating path to the page {file_path}')

    with open(file_path, 'wb') as file:
        file.write(response.content)
        logger.info(f'content has written to {file_path}')
