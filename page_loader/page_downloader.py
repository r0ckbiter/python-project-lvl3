import os
import requests
from page_loader.directory_and_names import get_file_name,\
    get_directory_name, make_directory
from page_loader.resources import replace_links, download_asset
from page_loader.logger import logger


def download(url, current_path):
    logger.info(f'trying to download {url} to {current_path}')
    response = requests.get(url)
    logger.info(f'got a {response} from {url}')
    page_name = get_file_name(url)
    logger.info(f'page name {page_name}')
    page_path = os.path.join(current_path, page_name)
    logger.info(f'page path {page_path}')

    assets_dir_name = get_directory_name(url)
    assets_path = os.path.join(current_path, assets_dir_name)

    try:
        make_directory(page_path)
    except OSError as e:
        logger.error(e)

    page, assets_links = replace_links(url, response.text, assets_dir_name)

    logger.info('links have been replaced')

    try:
        with open(page_path, 'w', encoding='utf-8') as f:
            f.write(page)
            logger.info(f'page has been saved to {page_path}')
    except requests.exceptions.MissingSchema:
        pass

    if assets_links:
        for link in assets_links:
            download_asset(link, assets_path)

    logger.info('download function has been executed')
    return page_path
