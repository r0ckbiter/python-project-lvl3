#!/usr/bin/env python3

import argparse
import os

from page_loader.page_downloader import download


def main():
    parser = argparse.ArgumentParser(description='Page-loader')
    parser.add_argument('url_address')
    parser.add_argument('-o', '--output', default=os.getcwd())
    args = parser.parse_args()
    file_path = download(args.url_address, args.output)
    print(f'Downloading complete. Path to file: {file_path}')


if __name__ == '__main__':
    main()
