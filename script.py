from selenium.webdriver import Firefox
import time
import os
import subprocess
import pyautogui

urlBase = "https://vsaludable.com/"
lista = ["AZMaPQ", "Vzc4r4", "Khrli1ga","cXvd","c5WH","1Ej17","vmcdCE","huPmAIU","TApyib1","aH6w","rLtB","AiV4uB","W13NV","sOC02","N0L9Oy","UNhef","WNhlREt","Dt40N","QP7klcR","dpz1wmrF","YW47L","kqU6","CJB6FFOT","pds4","GehV","YXjifA","ZwgbsPH","lDqpCd","U4nR","Ylf3k"]

# lista = ["cXvd"]
# ipInit = '10.0.2.3'
# counter = 0

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


def money():
    for oct4 in range(17,255):
        for i in range(len(lista)):
            # try:
            driver = Firefox()
            url = urlBase + lista[i]
            driver.get(url)
            time.sleep(11)
            print('10.0.2.'+str(oct4)+'  ----------'+lista[i])
            driver.quit()
            # except webbrowser.Error:
            #     driver.quit()
            #     print("Algo salio mal")
            # finally:
            #     driver.quit()
            #     print('10.0.2.'+str(oct4)+'  ----------'+lista[i]+"------Error----")

        addresses = "ip[11]="+"'      addresses: [10.0.2."+ str(oct4) +"/24]'"
        abrirConsola(addresses)
        print('10.0.2.'+str(oct4)+'  ----------'+lista[i]+' ------- Fin IP')
        
money()
