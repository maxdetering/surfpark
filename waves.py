import chamber
from setup import N_CHAMBERS
import threading


def create_wave(rpi, waveform):
    threads = []
    # create thread for activation of each chamber
    for (nChamber, tDelay, tExpand, tHold, tRelax) in waveform:
        thread = threading.Thread(target=chamber.create_wave, args=(rpi, nChamber, tDelay, tExpand, tHold, tRelax))
        threads.append(thread)
        thread.start()
    
    # wait for end of threads
    for thread in threads:
        thread.join()
    
    return

def create_waveset(rpi, waveset):
    threads = []
    # create thread for activation of each chamber
    for nChamber, tWaveset in enumerate(waveset):
        thread = threading.Thread(target=chamber.create_waveset, args=(rpi, nChamber, tWaveset))
        threads.append(thread)
        thread.start()
    
    # wait for end of threads
    for thread in threads:
        thread.join()
    
    return

def clean_up(rpi):
    # close all valves
    for n in range(N_CHAMBERS):
        rpi.io["IntakeValve_{}".format(n)].value = False
        rpi.io["ExhaustValve_{}".format(n)].value = False
    
    return