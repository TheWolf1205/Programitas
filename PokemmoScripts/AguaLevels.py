import os
import time

veces = int(input("veces que se hace el ciclo: "))
vecesDA = int(input("Veces que se hace Dulce aroma: "))
for i in range(veces):
    ## Llevar del hospital hasta el lago
    print(str(int(i+1))+" Ciclo")
    os.system('xdotool key --delay 100 "super+1" + "Down" + "Down" + "Down" + "Down" + "Down" + "Down" + "Down" + "Down" + "Down" + "Down" + "Down" + "Down" + "Down" + "Down" + "Down" + "Down" + "Down" + "Down" + "Down" + "Down" + "Down" + "Down" + "Down"')
    time.sleep(3)
    os.system('xdotool key --delay 100 "7" + "Left" + "Left" + "Left" + "Left" + "Left" + "Left" + "Left" + "Left" + "Left" + "Left" + "Left" + "Left" + "Left" + "Left" + "Left" + "Left" + "Left" + "Left" + "Left" + "Left" + "Left" + "Left" + "Left" + "Left" + "Left" + "Left" + "Left" + "Left" + "Left" + "Left" + "Left" + "Left" + "Left" + "Left" + "Left" + "Left"')
    time.sleep(1)
    os.system('xdotool key --delay 100 "Up" + "Up"')

    ## Esperar 3 segundos
    time.sleep(3)

    ## Dulce aroma y atacar
    for j in range(vecesDA):
        print(str(int(j+1))+" Dulce Aroma")
        os.system('xdotool key --delay 100 "8"')
        time.sleep(15)
        os.system('xdotool key --delay 100 "Z" + "Z" + "Z" + "Z" + "Z" + "Z" + "Z" + "Z" + "Z" + "Z" + "Z"')
        time.sleep(23)


    ## Volver al hospital
    os.system('xdotool key --delay 100 "Down" + "Down"')
    time.sleep(1)
    os.system('xdotool key --delay 100 "Right" + "Right" + "Right" + "Right" + "Right" + "Right" + "Right" + "Right" + "Right" + "Right" + "Right" + "Right" + "Right" + "Right" + "Right" + "Right" + "Right" + "Right" + "Right" + "Right" + "Right" + "Right" + "Right" + "Right" + "Right" + "Right" + "Right" + "Right" + "Right" + "Right" + "Right" + "Right" + "Right" + "Right" + "Right" + "Right"')
    time.sleep(1)
    os.system('xdotool key --delay 100 "Up" + "Up" + "Up"')
    time.sleep(2)
    os.system('xdotool key --delay 100 "Up" + "Up" + "Up" + "Up" + "Up" + "Up" + "Up" + "Up" + "Up" + "Up" + "Up" + "Up" + "Up" + "Up" + "Up"')
    time.sleep(2)
    os.system('xdotool key --delay 100 "Z"')
    time.sleep(2)
    os.system('xdotool key --delay 100 "Z"')
    time.sleep(2)
    os.system('xdotool key --delay 100 "Z"')
    time.sleep(2)
    os.system('xdotool key --delay 100 "Z"')
    time.sleep(6)
    os.system('xdotool key --delay 100 "Z"')
    time.sleep(2)
    os.system('xdotool key --delay 100 "Z"')
    time.sleep(2)
    os.system('xdotool key --delay 100 "Z"')
    time.sleep(2)