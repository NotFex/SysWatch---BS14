"""
 !!! Python 3.10+ !!!

 ? Felix Burwitz, Davide Ruccia Arranz, Johann Felix Beinsen
 ? Berufliche Schule ITECH BS14, Hamburg, Lernfeld 8 IT-Systemelektroniker
 
 & << VSC extension: Colorful Comments optimiert >>
 & Der Code ist, bis auf explizit angegebene stellen, selbst geschrieben.
 & Kommentare wurden mit der hilfe von ChatGPT (@OpenAI) geschrieben.

* Der hier stehende Code ist eine Python-Implementierung eines Systemüberwachungs-Dashboards.
* Das Dashboard verwendet die Bibliotheken:
             tkinter, os, func, alarm, time, psutil und threading. 
* Es stellt eine GUI-Schnittstelle anhand TKinter zur Verfügung, die verschiedene Systeminformationen anzeigt, 
* einschließlich des Betriebssystems, der CPU, des RAMs, des Akkustands und weiterem.
"""


import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
import os
import func
import alarm
import time
import psutil
from threading import Thread

#* Der erste Teil des Codes erstellt die Klasse namens "App", die ein Objekt erstellt, welches ein GUI-Fenster darstellt.
class App:
    def __init__(self, root):
        root.title("SysWatch | LF8")
        width=400
        height=300
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
#* Im Konstruktor der "App"-Klasse wird das Fenster mit einem Titel versehen und die Breite, Höhe, Bildschirmbreite und Bildschirmhöhe des Fensters definiert.
#* Der Bildschirm wird auf die Mitte des Fensters ausgerichtet und das Fenster wird auf eine feste Größe festgelegt.

      
        #* Dann werden verschiedene Labels und Buttons erstellt und auf dem Fenster platziert, um Informationen über das Betriebssystem anzuzeigen. 
        #* Jedes Label und jeder Button wird mit bestimmten Texten versehen und an einer bestimmten Stelle im Fenster platziert.
        DEV_LABLE=tk.Label(root)
        DEV_LABLE["activebackground"] = "#cfcfcf"
        ft = tkFont.Font(family='Arial',size=10)
        DEV_LABLE["font"] = ft
        DEV_LABLE["fg"] = "#000000"
        DEV_LABLE["justify"] = "center"
        DEV_LABLE["text"] = "Felix Burwitz | Davide Ruccia Arranz | Johann Felix Beinsen"
        DEV_LABLE["relief"] = "flat"
        DEV_LABLE.place(x=0,y=270,width=400,height=30)

        NAME_LABEL=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        NAME_LABEL["font"] = ft
        NAME_LABEL["text"] = "SysWatch-Dashboard"
        NAME_LABEL.place(x=0,y=0,width=316,height=39)

        OS_LABEL=tk.Label(root, anchor="w")
        ft = tkFont.Font(family='Arial',size=10)
        OS_LABEL["font"] = ft
        OS_LABEL["text"] = "Betriebssystem: " + func.getSysInfo("os")
        OS_LABEL.place(x=20,y=40,width=300,height=30)

        NODE_LABEL=tk.Label(root, anchor="w")
        ft = tkFont.Font(family='Arial',size=10)
        NODE_LABEL["font"] = ft
        NODE_LABEL["text"] = "Node: " + func.getSysInfo("node")
        NODE_LABEL.place(x=20,y=70,width=119,height=30)

        ONLINE_LABEL=tk.Label(root, anchor="w")
        ft = tkFont.Font(family='Arial',size=10)
        ONLINE_LABEL["font"] = ft
        ONLINE_LABEL["text"] = "Online seit: " + func.getBootTime()
        ONLINE_LABEL.place(x=20,y=100,width=300,height=30)

        VERSION_LABEL=tk.Label(root, anchor="w")
        ft = tkFont.Font(family='Arial',size=10)
        VERSION_LABEL["font"] = ft
        VERSION_LABEL["text"] = "Version: " + func.getSysInfo("version")
        VERSION_LABEL.place(x=250,y=100,width=300,height=30)

        CPU_TYPE_LABEL=tk.Label(root, anchor="w")
        ft = tkFont.Font(family='Arial',size=10)
        CPU_TYPE_LABEL["font"] = ft
        CPU_TYPE_LABEL["text"] = "CPU-Typ: " + func.getSysInfo("cputype")
        CPU_TYPE_LABEL.place(x=250,y=40,width=300,height=30)

        CPU_LABEL=tk.Label(root, anchor="w")
        ft = tkFont.Font(family='Arial',size=10)
        CPU_LABEL["font"] = ft
        CPU_LABEL["text"] = "CPU: " + func.getSysInfo("cpu") 
        CPU_LABEL.place(x=250,y=70,width=145,height=30)

        RAM_LABEL=tk.Label(root, anchor="w")
        ft = tkFont.Font(family='Arial',size=10)
        RAM_LABEL["font"] = ft
        RAM_LABEL.place(x=20,y=180,width=184,height=30)
        
        #* Ein Thread wird gestartet, der in regelmäßigen Abständen die Auslastung des RAMs berechnet und auf dem dazugehörigen Label anzeigt. 
        def updateRam():    
            while(True):
                ram = psutil.virtual_memory()
                ram = f"{ram.percent:.0f}"

                RAM_LABEL["text"] = "RAM-Auslastung: " + ram + "%"
                time.sleep(1)
        
        thread_3 = Thread(target=updateRam)
        thread_3.start()

        OPEN_LOG_BUTTON=tk.Button(root)
        OPEN_LOG_BUTTON["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Arial',size=10)
        OPEN_LOG_BUTTON["font"] = ft
        OPEN_LOG_BUTTON["justify"] = "center"
        OPEN_LOG_BUTTON["text"] = "Log öffnen"
        OPEN_LOG_BUTTON.place(x=320,y=0,width=70,height=25)
        OPEN_LOG_BUTTON["command"] = self.OPEN_LOG_BUTTON_command

        BATTERY_LABEL=tk.Label(root, anchor="w")
        ft = tkFont.Font(family='Arial',size=10)
        BATTERY_LABEL["font"] = ft
        
        #* Ein weiterer Thread wird gestartet, der in regelmäßigen Abständen den Akkustand des Computers berechnet und auf dem dazugehörigen Label anzeigt.
        def updateBat():
            while(True):
                bat = psutil.sensors_battery()
                bat = bat.percent

                BATTERY_LABEL["text"] = "Akkustand: " + str(bat) + "%"
                time.sleep(10)
        
        thread_4 = Thread(target=updateBat)
        thread_4.start()
        BATTERY_LABEL.place(x=250,y=180,width=140,height=25)

        CHARGING_LABEL=tk.Label(root, anchor="w")
        ft = tkFont.Font(family='Arial',size=10)
        CHARGING_LABEL["font"] = ft
        CHARGING_LABEL["text"] = "Akku wird geladen"
        CHARGING_LABEL.place(x=20,y=210,width=154,height=30)

        LIVE_HEADER=tk.Label(root)
        LIVE_HEADER["bg"] = "#00babd"
        ft = tkFont.Font(family='Times',size=14)
        LIVE_HEADER["font"] = ft
        LIVE_HEADER["fg"] = "#333333"
        LIVE_HEADER["text"] = "Live-Informationen"
        LIVE_HEADER.place(x=0,y=140,width=400,height=30)

    #* Klickt der Nutzer auf obig definierten Button, so wird dieser Code ausgeführt.
    #* Hier wird die log.txt geöffnet um den Log anzeigen zu können.
    def OPEN_LOG_BUTTON_command(self):
        os.system("start " + "log.txt")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
