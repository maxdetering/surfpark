import revpimodio2
from setup import N_CHAMBERS, PATH
import waves
import numpy as np

def main():
    # load wave information from csv file
    # transpose matrix (different chambers along 0-axis, timesteps for one chamber along 1-axis)
    wave_table = np.loadtxt(PATH, skiprows=2, dtype=float).T

    # check if file contains information for all wave chambers
    if np.size(wave_table, axis=0) != N_CHAMBERS:
         raise ValueError("Table does not contain information for all chambers or for too many chambers!")

    # get number of wave sets specified in file and perform sanity check
    if np.size(wave_table, axis=1) % 4 != 0:
           raise ValueError("Table contains incomplete wavesets! Length of columns must be multiple of 4.")
    
    # Create the RevPiModIO object
    rpi = revpimodio2.RevPiModIO(autorefresh=True)

    # cerate waveset
    waves.create_waveset(rpi, wave_table)

    # close all valves again
    waves.clean_up(rpi)



if __name__ == "__main__":
    main()