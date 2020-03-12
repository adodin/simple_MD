# Ideal Gas Force Field

import numpy as np


class IdealGas:
    def __init__(self):
        pass

    def __call__(self, x, *args, **kwargs):
        return np.zeros_like(x)