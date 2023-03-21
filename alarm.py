"""
 !!! Python 3.10+ !!!
 !! Dies ist NICHT die "Hauptdatei" !!
 
 ? Felix Burwitz,
 
 & << VSC extension: Colorful Comments optimiert >>
"""

#* Auch hier werden zunächst die Libarys importiert.
import psutil
import time     
from threading import Thread
from datetime import datetime


#* Definieren der Funktion: ram_watch
def ram_watch():
    print("="*10, "Arbeitsspeicherüberwachung gestartet" ,"="*10) 

    #* Alle 5 Sekunden (siehe time.sleep) wird dieser Loop ausgeführt.
    #* Innerhalb des Loops wird geprüft wie die Ramauslastung ist, hat diese einen Wert überschritten wird dies in die Log.txt geschrieben.
    while(True):
        mem = psutil.virtual_memory()
        per = f"{mem.percent:.0f}"
        # Alarm
        if per < "80":
            log = open('log.txt', 'a')
            print("Ramauslastung über 80%")
            timestamp = datetime.now()
            alarmmsg = timestamp.strftime("%c") + " | RAM: Auslastung von mehr als 80%, Auslastung bei: " + per + "%\n" 
            log.write(alarmmsg)
            log.close()
        time.sleep(5)

def battery_watch():
    print("="*10, "Batterieüberwachung gestartet" ,"="*10) 

    #* Alle 5 Sekunden (siehe time.sleep) wird dieser Loop ausgeführt.
    #* Innerhalb des Loops wird geprüft wie die Akku-Kapazität ist, hat diese einen Wert unterschritten wird dies in die Log.txt geschrieben.
    while(True):
        bat = psutil.sensors_battery()

        if bat.percent > 50:
            log = open('log.txt', 'a')
            print("Akkustand unter 50%!")
            timestamp = datetime.now()
            alarmmsg = timestamp.strftime("%c") + " | Batterie: Akkustand unter 50%, Aktuell: " + str(bat.percent) + "%\n" 
            log.write(alarmmsg)
            log.close()
        time.sleep(5)

#* Um gleichzeitig mehrere loops effizient auszuführen benötigen wir "threads"
#* Es sind quasi: "Unteranwendungen" unseres Programmes.
thread_1 = Thread(target=battery_watch)
thread_2 = Thread(target=ram_watch)

thread_1.start()
thread_2.start()








