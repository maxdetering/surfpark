# -*- coding: utf-8 -*-

import time

# create wave from single wave chamber
def create_waveset(rpi, nChamber, tSet):
    # loop over all waves in waveset
    for i, t in enumerate(tSet):
        if i%4 == 0:
            # delay by tDelay
            time.sleep(t)
            # open intake valve
            rpi.io["IntakeValve_{}".format(nChamber)].value = True
        if i%4 == 1:
            # expand for tExpand
            time.sleep(t)
            # close intake valve
            rpi.io["IntakeValve_{}".format(nChamber)].value = False
        if i%4 == 2:
            # pause for tHold
            time.sleep(t)
            # open exhaust valve
            rpi.io["ExhaustValve_{}".format(nChamber)].valve = True
        if i%4 == 3:
            # exhaust for tRelax
            time.sleep(t)
            # close exhaust valve
            rpi.io["ExhaustValve_{}".format(nChamber)].valve = False

    return