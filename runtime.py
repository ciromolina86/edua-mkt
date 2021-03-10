import os
import time
import pyautogui
import json

def get_servers_json():
    servers = []

    with open('/home/cmolina/PycharmProjects/edua-mkt/ip vpn', 'r') as f:
        _servers = f.readlines()[1:]
        for svr in _servers:
            svr = ''.join(svr.split())
            servers.append(svr)

    # print(_servers)
    # print(servers)

    with open('/home/cmolina/PycharmProjects/edua-mkt/servers.json', 'w') as f:
        json.dump({'servers': servers}, f)

def get_servers():
    with open('/home/cmolina/PycharmProjects/edua-mkt/meta-data.json', 'r') as f:
        metaData = json.load(f)

    return metaData['servers']

def get_urls():
    with open('/home/cmolina/PycharmProjects/edua-mkt/meta-data.json', 'r') as f:
        metaData = json.load(f)

    urlBase = "https://vsaludable.com"
    urls = list(map(lambda x: '/'.join([urlBase, x]), metaData['surls']))

    return urls

if __name__ == '__main__':
    print(get_servers()[::-1])
    print(get_urls())
    print(len(get_urls()))