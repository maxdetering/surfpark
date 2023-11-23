#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import chamber
from setup import N_CHAMBERS
import threading

def create_waveset(rpi, waveset):
    """Generate the entire waveset.

    Args:
        rpi (object): RevPiModIO instance to control the IO pins on the Revolution Pi and attached modules.
        waveset (array-ike): Array-like containing the times of the wave phases in seconds for each wave chamber. The size along the 0-axis has to be N_CHAMBERS (specified in setup.py), and a multiple of 4 along the 1-axis. Each row contains the wave time table for one chamber in increasing number. The columns contain the duration of a common wave phase.
    """

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
    """Close all valves at the end of the experiment.

    Args:
        rpi (object): RevPiModIO instance to control the IO pins on the Revolution Pi and attached modules.
    """
    
    # close all valves
    for n in range(N_CHAMBERS):
        rpi.io["IntakeValve_{}".format(n)].value = False
        rpi.io["ExhaustValve_{}".format(n)].value = False
    
    return