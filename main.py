import revpimodio2
from setup import N_CHAMBERS, T_EXPAND, T_HOLD, T_RELAX
import tkinter as tk
import waves


def main():
    # Create the RevPiModIO object
    rpi = revpimodio2.RevPiModIO(autorefresh=True)

    # create waveform
    waveform = [[i, 0., T_EXPAND, T_HOLD, T_RELAX] for i in range(N_CHAMBERS)]

    # function to start the wavefront
    def start_wave():
        # retrieve set delay times
        for i in range(5):
            waveform[i][1] = splist[i].get()

        # start wave
        waves.create_wave(rpi, waveform)

        # close all valves
        waves.clean_up()
        
        return

    # create window
    window = tk.Tk()
    window.title("Waveform generator")
    window.resizable(width=300, height=400)

    fChambers = tk.Frame()
    fChambers.pack(side=tk.LEFT)

    lblChamHeading = tk.Label(fChambers, text="Time delay in seconds for wave chambers")
    lblChamHeading.pack()
    fChambersFields = tk.Frame(fChambers)
    fChambersFields.pack()

    splist = []
    lbllist = []
    for i in range(36):
        splist.append(tk.Spinbox(fChambersFields, from_=0.00, to=10.00, format="%.2f", increment=0.05, textvariable=tk.IntVar(value=0.00), wrap=True, width=4))
        splist[i].grid(row=i%9, column=(i//9)*2+1)

        lbllist.append(tk.Label(fChambersFields, text="Chamber {}".format(i)))
        lbllist[i].grid(row=i%9, column=(i//9)*2)

    fwaveform = tk.Frame(window)
    fwaveform.pack(side=tk.RIGHT)
    lblwaveform = tk.Label(fwaveform, text="Waveform")
    lblwaveform.pack()
    btnWave1 = tk.Button(fwaveform, text="Full")
    btnWave1.pack()
    btnWave1 = tk.Button(fwaveform, text="Right to left")
    btnWave1.pack()
    btnWave1 = tk.Button(fwaveform, text="Left to Right")
    btnWave1.pack()
    btnWave1 = tk.Button(fwaveform, text="Center-out")
    btnWave1.pack()
    btnWave1 = tk.Button(fwaveform, text="Outside-in")
    btnWave1.pack()

    btnstart = tk.Button(text="Start", command=start_wave)
    btnstart.pack(side=tk.BOTTOM)

    window.mainloop()


if __name__ == "__main__":
    main()