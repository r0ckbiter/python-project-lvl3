import os
import pytest
import tempfile
import requests_mock
from page_loader.page_downloader import download


@pytest.fixture
def original_page():
    with open('tests/fixtures/original_page.html', 'r') as f:
        return f.read()


@pytest.fixture
def expected_page():
    with open('tests/fixtures/expected_page.html', 'r') as f:
        return f.read()


@pytest.fixture
def downloaded_image():
    with open('tests/fixtures/img.png', 'rb') as f:
        return f.read()


def test_download(original_page, downloaded_image, expected_page):
    with requests_mock.Mocker() as mock, tempfile.TemporaryDirectory() as temp:
        mock.get('http://test.ru', text=original_page)
        mock.get('http://test.ru/files/img.png', content=downloaded_image)
        mock.get('http://test.ru/files/resource.html', text='data')
        mock.get('http://test.ru/script.js')
        path_to_file = download('http://test.ru', temp)
        assert os.path.isfile(path_to_file)
        assert read(path_to_file, 'r') == expected_page


def read(file_path, mode):
    with open(file_path, mode) as data:
        return data.read()

