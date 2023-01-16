import os
import requests
from page_loader.directory_and_names import get_file_name,\
    get_directory_name, make_directory
from page_loader.resources import replace_links, download_asset


def download(url, current_path):
    response = requests.get(url)
    page_name = get_file_name(url)
    page_path = os.path.join(current_path, page_name)

    assets_dir_name = get_directory_name(url)
    assets_path = os.path.join(current_path, assets_dir_name)
    make_directory(page_path)

    page, assets_links = replace_links(url, response.text, assets_dir_name)
    try:
        with open(page_path, 'w', encoding='utf-8') as f:
            f.write(page)
    except requests.exceptions.MissingSchema:
        pass

    if assets_links:
        for link in assets_links:
            download_asset(link, assets_path)

    return page_path
