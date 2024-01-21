#!/usr/bin/env python3

import asyncio, argparse, textwrap, validators
from colorama import Fore, Style
from helpers.utils import *
from helpers.interactive import connection

parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    prog='cef-interactive',
    description=textwrap.dedent('''
        Script to interact with Node inspector/CEF debug
    '''),
    epilog=textwrap.dedent('''
        Examples:

        ./cef-interactive.py -i 127.0.0.1
        ./cef-interactive.py -i 127.0.0.1 -p 1337
        ./cef-interactive.py -u http://localhost/node-inspector-path
        ./cef-interactive.py -s -i 127.0.0.1 -p 1337
    ''')
)

parser.add_argument('-i', '--ip', type=str, help='Specify node inspector ip address')
parser.add_argument('-p', '--port', type=str, help='Specify node inspector port. Default: 9229', default="9229")
parser.add_argument('-u', '--url', type=str, help='Specify node inspector URL')
parser.add_argument('-s', '--shell', action='store_true', help='Enable interactive shell')

args = parser.parse_args()
host = args.ip
port = args.port
url = args.url

if not host and not url or host and url:
    parser.print_help()
    exit(1)

if url:
    url = url[:-1] if url[-1] == '/' else url
    
    if not validators.url(url):
        print(Fore.RED + 'Invalid URL' + Style.RESET_ALL)
        exit(1)

    cef_ws_url = get_cef_ws_url_from_url(url)
else:
    if not validate_ip(host):
        print(Fore.RED + 'Invalid ip address' + Style.RESET_ALL)
        exit(1)

    if not validate_port(port):
        print(Fore.RED + 'Invalid port' + Style.RESET_ALL)
        exit(1)

    cef_ws_url = get_cef_ws_url_from_host(host, port)

if __name__ == '__main__':
    try:
        asyncio.get_event_loop().run_until_complete(connection(cef_ws_url, args.shell))
    except KeyboardInterrupt:
        exit(0)