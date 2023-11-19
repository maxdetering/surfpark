import time

# create wave from single wave chamber
def single_wave(rpi, nChamber, tDelay=0, tExpand=0.3, tHold=0., tRelax=1):
    # delay by tDelay
    time.sleep(tDelay)

    # open intake valve
    rpi.io["IntakeValve_{}".format(nChamber)].value = True

    # expand for tExpand
    time.sleep(tExpand)

    # close intake valve
    rpi.io["IntakeValve_{}".format(nChamber)].value = False

    # pause for tHold
    time.sleep(tHold)

    # open exhaust valve
    rpi.io["ExhaustValve_{}".format(nChamber)].valve = True

    # exhaust for tRelax
    time.sleep(tRelax)

    # close exhaust valve
    rpi.io["ExhaustValve_{}".format(nChamber)].valve = False

    return