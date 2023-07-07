import numpy as np
import matplotlib.pyplot as plt

from Circle import *
from Polygon import *

class Robot( Circle ):
    def __init__(self, model, center, radius,
            color='#9C9C9C'):
        Circle.__init__(self, center, radius, color=color);
        self.F = model;