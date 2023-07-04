import numpy as np

class Edges:
    def __init__(self, vertices):
        self.v = vertices;

class Polygon( Edge ):
    def __init__(self, vertices):
        Edges.__init__(self, vertices);