#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

# create wave from single wave chamber
def create_waveset(rpi, nChamber, tSet):
    """Generate the entire waveset in a specific wave chamber.

    Args:
        rpi (object): RevPiModIO instance to control the IO pins on the Revolution Pi and attached modules.
        nChamber (int): Number of the chamber.
        tSet (array-like): Array-like of floats describing the times of each wave phase in seconds.
    """
    # loop over all waves in waveset
    for i, t in enumerate(tSet):
        if i%4 == 0:
            # delay
            time.sleep(t)
            # open intake valve
            rpi.io["IntakeValve_{}".format(nChamber)].value = True
        elif i%4 == 1:
            # expand
            time.sleep(t)
            # close intake valve
            rpi.io["IntakeValve_{}".format(nChamber)].value = False
        elif i%4 == 2:
            # pause
            time.sleep(t)
            # open exhaust valve
            rpi.io["ExhaustValve_{}".format(nChamber)].valve = True
        elif i%4 == 3:
            # exhaust
            time.sleep(t)
            # close exhaust valve
            rpi.io["ExhaustValve_{}".format(nChamber)].valve = False

    return