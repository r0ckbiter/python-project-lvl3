import pytest
from page_loader import directory_and_names

URL = 'https://ru.35photo.pro'
NAME_PREFIX = 'ru-35photo-pro'


@pytest.mark.parametrize('url, expected_name', [
    (URL, f'{NAME_PREFIX}.html'),
    (f'{URL}/python.png', f'{NAME_PREFIX}-python.png'),
    (f'{URL}/python.jpg', f'{NAME_PREFIX}-python.jpg')])
def test_get_file_name(url, expected_name):
    assert directory_and_names.get_file_name(url) == expected_name


@pytest.mark.parametrize('url, expected_name_path', [
    (URL, f'{NAME_PREFIX}_files'),
    (f'{URL}/python', f'{NAME_PREFIX}-python_files'),
    (f'{URL}/python.html', f'{NAME_PREFIX}-python_files')])
def test_get_assets_path(url, expected_name_path):
    assert directory_and_names.get_directory_name(url) == expected_name_path
