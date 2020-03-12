import PyRaMD.force as force
import numpy as np

def test_ideal_gas():
    x = np.zeros((3, 100))
    p = np.ones_like(x)
    ff = force.IdealGas()
    assert np.sum(ff(x, p) == np.zeros((3,100))) == 300
