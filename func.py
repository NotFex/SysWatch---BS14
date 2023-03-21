"""
 !!! Python 3.10+ !!!
 !! Dies ist NICHT die "Hauptdatei" !!

 ? Felix Burwitz
 
 & << VSC extension: Colorful Comments optimiert >>

* In dieser Datei werden drei Funktionen erstellt anhand Daten des Computers Abgefragt werden können
* Oder auch Bytes in ein anderes Format konvertiert werden.
"""

#* Zunächst importieren wir unsere Libarys.
import psutil
import platform
from datetime import datetime

#* Diese Funktion rechnet übermittelte Bytes in ein anderes Format um
def formatBytes(bytes, suffix="B"): # [Quelle: thepythoncode.com] 
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

"""
* Die Funktion getSysInfo fragt erst ab was angefordert wurde.
* Dann wird über die platform-libary jeh das geforderte wiedergegeben.
* bspw: getSysInfo("os") -> "Windows"
* Benötigt wird dies um später innerhalb unserer Programme einen übersichtlicheren Code zu haben.
"""
def getSysInfo(type="os, node, version, cputype, cpu"):
    s = platform.uname()
    match type:
        case "os":
            os = s.system
            return os 
        case "node":
            node = s.node
            return node
        case "version":
            version = s.version
            return version
        case "cputype":
            cputype = s.machine
            return cputype
        case "cpu":
            cpu = s.processor
            return cpu
        case _:
            err = "Überprüfe die Syntaxeingabe - Anforderung nicht gefunden."
            return err

#* Diese Funktion holt sich die Information wann der PC gestartet wurde, außerdem formatiert er das erhaltene Datum um.
def getBootTime():
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    res = f"{bt.day}.{bt.month}.{bt.year} {bt.hour}:{bt.minute}:{bt.second}"
    return res