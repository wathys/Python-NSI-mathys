import psutil
from time import sleep

while True:
    tempinfos = psutil.sensors_temperatures()
    t = tempinfos["coretemp"][0].current
    print("température du coeur: ", t)
    sleep(2)
    print(psutil.cpu_stats())
    print(psutil.disk_usage("c:"))
    print(psutil.disk_partitions())
    print(psutil.virtual_memory())
    print(psutil.sensors_battery())
    print(psutil.disk_usage("/"))
    print(psutil.sensors_fans())
    print(psutil.cpu_freq())
    sleep(2)
