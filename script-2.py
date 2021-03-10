from selenium.webdriver import Firefox
import time
import os
import subprocess
import pyautogui
import json
import runtime
import random

def abrirConsola(addresses):
    pyautogui.PAUSE = 1.5
    pyautogui.hotkey('ctrl','alt','t')
    pyautogui.write('sudo su')
    pyautogui.press('enter')
    pyautogui.write(' ')
    pyautogui.press('enter')
    pyautogui.write('python3')
    pyautogui.press('enter')
    pyautogui.write('ip=[]')
    pyautogui.press('enter')
    pyautogui.write('with open("/etc/netplan/01-netcfg.yaml", "r+") as f:')
    pyautogui.press('enter')
    pyautogui.write('    ip = f.readlines()')
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.write( addresses )
    pyautogui.press('enter')
    pyautogui.write('with open("/etc/netplan/01-netcfg.yaml", "w") as f:')
    pyautogui.press('enter')
    pyautogui.write('    f.writelines(ip)')
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.hotkey('ctrl','d')
    pyautogui.write('netplan apply')
    pyautogui.press('enter')
    pyautogui.hotkey('alt','f4')
    pyautogui.press('enter')

def abrirPagina(url):
    print(url)

    try:
        driver = Firefox()
        driver.get(url)
    except Exception as e:
        print('fallo al cargar {}'.format(url))
        print(e)
        return

    pyautogui.moveTo(500, 500, duration=2)
    pyautogui.moveTo(600, 500, duration=2)
    time.sleep(random.randint(10, 30))
    driver.quit()



def crearVista(servers, urls):
    time.sleep(5)
    os.system('nordvpn disconnect')
    time.sleep(5)
    counter = 0

    for svr in servers[1000:3000]:
        # conectar al server
        response = os.system('nordvpn connect {}'.format(svr))
        time.sleep(5)

        if response == 0:
            url1 = urls[random.randint(0, len(urls)-1)]
            url2 = urls[random.randint(0, len(urls)-1)]

            for url in [url1, url2]:
                # print(url)
                abrirPagina(url)

            # desconectar del server
            os.system('nordvpn disconnect')
            time.sleep(5)
            counter += 1
            print('counter ', counter)

        else:
            continue


if __name__ == '__main__':
    # url variables
    urls = runtime.get_urls()

    # vpn servers
    servers = runtime.get_servers()

    # crear visitas
    crearVista(servers, urls)

