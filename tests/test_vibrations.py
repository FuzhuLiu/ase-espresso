
import numpy as np
from ase import Atoms
from ase.units import Rydberg, Bohr
from ase.vibrations import Vibrations
from espresso import Espresso, Vibespresso


def test_co_espresso_vibrations():

    co = Atoms('CO', positions=[[1.19382389081, 0.0, 0.0], [0.0, 0.0, 0.0]])
    co.set_cell(np.ones(3) * 12.0 * Bohr)

    calc = Espresso(pw=34.0 * Rydberg,
                    dw=144.0 * Rydberg,
                    kpts='gamma',
                    xc='PBE',
                    calculation='scf',
                    ion_dynamics='None',
                    spinpol=False,
                    outdir='vibs')

    co.set_calculator(calc)

    # calculate the vibrations
    vib = Vibrations(co, indices=range(len(co)), delta=0.01, nfree=2)
    vib.run()


def test_co_vibespresso_vibrations():

    co = Atoms('CO', positions=[[1.19382389081, 0.0, 0.0], [0.0, 0.0, 0.0]])
    co.set_cell(np.ones(3) * 12.0 * Bohr)

    calc = Vibespresso(pw=34.0 * Rydberg,
                       dw=144.0 * Rydberg,
                       kpts='gamma',
                       xc='PBE',
                       calculation='scf',
                       ion_dynamics='None',
                       spinpol=False,
                       outdir='vibs')

    co.set_calculator(calc)

    # calculate the vibrations
    vib = Vibrations(co, indices=range(len(co)), delta=0.01, nfree=2)
    vib.run()


test_co_espresso_vibrations()
test_co_vibespresso_vibrations()
