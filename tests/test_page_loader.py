import os
import requests
import tempfile
from page_loader.page_downloader import download

URL = 'https://ya.ru/'
WEB_PAGE = 'tests/fixtures/web_page.html'


def test_download(requests_mock):
    with tempfile.TemporaryDirectory() as temp:
        with open(WEB_PAGE, 'rb') as fixture_file:
            mocking_content = fixture_file.read()
        requests_mock.get(URL, content=mocking_content)
        path_load_page = download(URL, temp)

        with open(os.path.join(temp, path_load_page)) as test_page:
            with open(WEB_PAGE) as fixture_page:
                assert test_page.read() == fixture_page.read()
