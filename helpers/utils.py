import requests
from colorama import Fore, Style

def get_cef_ws_url_from_url(url):
    try:
        request_to_get_uid = requests.get(f"{url}/json/list").json()
        ws_url = request_to_get_uid[0]['webSocketDebuggerUrl']
        
        cef_protocol = ws_url.split('://')[0]
        cef_id = ws_url.split('/')[-1]
        
        cef_ws_url = f"{cef_protocol}://{url.split('://')[1]}"
        cef_ws_url += f"/{cef_id}"

        return cef_ws_url
    except Exception:
        print(Fore.RED + "Error to get websocket URL" + Style.RESET_ALL)
        exit()

def get_cef_ws_url_from_host(host, port = 9229):
    try:
        request_to_get_uid = requests.get(f"http://{host}:{port}/json/list").json()
        return request_to_get_uid[0]['webSocketDebuggerUrl']
    except Exception:
        print(Fore.RED + "Error to get websocket URL" + Style.RESET_ALL)
        exit()

def validate_ip(ip):
    ip = ip.split('.')

    if(len(ip) != 4):
        return False
    
    for octal in ip:
        if(len(octal) < 1 or len(octal) > 3):
            return False

    return True

def validate_port(port):
    if(int(port) < 1 or int(port) > 65535):
        return False
    return True