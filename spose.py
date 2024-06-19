#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import argparse
import requests

class Spose:
    def __init__(self):
        parser = argparse.ArgumentParser(
            prog='Spose by Petruknisme',
            description='Squid Pivoting Open Port Scanner'
        )
        parser.add_argument("--proxy", help="Define proxy address url (http://xxx:3128)",
                            action="store", dest='proxy')
        parser.add_argument("--target", help="Define target IP behind proxy",
                            action="store", dest='target')
        results = parser.parse_args()

        if not results.target or not results.proxy:
            parser.print_help()
            sys.exit(1)

        target = results.target
        proxy = results.proxy
        common_ports = {21,22,23,25,53,69,80,109,110,123,137,138,139,143,156,389,443,546,547,995,993,2086,2087,2082,2083,3306,8080,8443,10000}

        print(f"Using proxy address {proxy}")

        for port in sorted(common_ports):
            try:
                url = f"http://{target}:{port}"
                response = requests.get(url, proxies={"http": proxy, "https": proxy}, timeout=5)
                code = response.status_code
                if code == 200 or code == 404 or code == 401:
                    print(f"{target} {port} seems OPEN")
            except requests.exceptions.RequestException as e:
                print(f"Exception occurred: {e}")

if __name__ == '__main__':
    Spose()
