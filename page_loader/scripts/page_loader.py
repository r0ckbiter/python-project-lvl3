#!/usr/bin/env python3
import os
import sys
import argparse

import page_loader.page_downloader
from page_loader.page_downloader import download


def main():
    try:
        parser = argparse.ArgumentParser(description='Page-loader')
        parser.add_argument('url_address')
        parser.add_argument('-o', '--output', default=os.getcwd())
        args = parser.parse_args()
        page_path = download(args.url_address, args.output)
        print(f'Downloading complete. Path to file: {page_path}')
    except page_loader.page_downloader.AppInternalError as e:
        print(e)
        sys.exit(1)
    else:
        sys.exit(2)


if __name__ == '__main__':
    main()
