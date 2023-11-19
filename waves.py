from chamber import single_wave
from setup import N_CHAMBERS
import threading


def create_wave(rpi, waveform):
    threads = []
    # create thread for activation of each chamber
    for (nChamber, tDelay, tExpand, tHold, tRelax) in waveform:
        thread = threading.Thread(target=single_wave, args=(rpi, nChamber, tDelay, tExpand, tHold, tRelax))
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