import pytest
import tempfile
import requests_mock
from page_loader.page_downloader import download, AppInternalError


def test_network_errors():
    for code in (400, 404, 500, 502):
        with requests_mock.Mocker() as mock, tempfile.TemporaryDirectory() as temp:
            mock.get('http://test.ru', text='data', status_code=code)
            with pytest.raises(AppInternalError):
                download('http://test.ru', temp)


def test_path_error():
    with pytest.raises(AppInternalError):
        download('http://test.ru', "doesn't exist")
