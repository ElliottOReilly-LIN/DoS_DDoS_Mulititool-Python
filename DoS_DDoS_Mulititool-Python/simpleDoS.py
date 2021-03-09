# Author: Elliott O'Reilly - 09 March 2021
# Cyber Security CMP3750 ASS1 Item-1
# Graphical front-end for the DoS / DDoS Multi-tool program
from tkinter import *
from dosAttack import runSingleDoS
from multiIPAttack import runMultiDoS
from DDoS_attack import dosDetect
from tcpdumpLocal import runTCPDump

window = Tk()
window.configure(background="#0892d0")
window.geometry("720x720")


def runSDoS():  # Subprogram 1. Fires dosAttack.py to emulate a sing IP Spoof
    runSingleDoS()


def runMDoS():  # Subprogram 2. Fires multiIPAttack.py to emulate a Multi IP Spoof
    runMultiDoS()

def runSocketGrab():  # Subprogram 3. Fires DDoS_attack.py to emulate a DDoS Random IP Spoof


def runTCP():  # Verbose Detection 4. Fires the tcpdumpLocal.py generate .cap files
    runTCPDump()


logo = PhotoImage(file='ddos.png')
Label(window, text=" This is the DoS / DDoS \n Attack Inspector Tool! ",
      pady=10, font=('Arial', 20, 'bold')).pack()
window.title("Elliott O'Reilly Cyber Security DoS Tool")
Label(window, image=logo).pack()
Label(window, text="     Choose your Attack Vectors:     ", bd=4, pady=10, fg='#00ff66',
      font=('Arial', 14, 'bold')).pack()
Button(window, text="  Begin Single IP DoS  ", bd=4, command=runSDoS).pack()
Button(window, text="  Stop Single IP DoS   ", bd=4, command=window.destroy).pack()
Button(window, text="   Begin Multi IP DoS  ", bd=4, command=runMDoS).pack()
Button(window, text="   Stop Multi IP DoS   ", bd=4, command=window.destroy).pack()
Button(window, text="  Begin DDoS IP Scan ", bd=4, command=runSocketGrab).pack()
Button(window, text="  Stop DDoS IP Scan  ", bd=4, command=window.destroy).pack()
Label(window, text="  Start the Defence\n Detection Subsystem: ", bd=4, pady=10,
      fg='#00ff66', font=('Arial', 14, 'bold')).pack()
Button(window, text="    Begin tcpDump analytics  ", bd=6, pady=10,
       command=runTCP).pack()
Button(window, text="    Stop tcpDump analytics   ", bd=6, pady=10,
       command=window.destroy).pack()
window.mainloop()
