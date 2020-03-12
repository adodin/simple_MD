import numpy as np

from .context import PyRaMD

def test_ideal_gas():
    x = np.zeros((3, 100))
    p = np.ones_like(x)
    ff = PyRaMD.force.IdealGas()
    assert np.sum(ff(x, p) == np.zeros((3,100))) == 300
