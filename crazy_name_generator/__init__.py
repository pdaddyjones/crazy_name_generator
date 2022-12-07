""" A name generator """

__version__ = '0.1.0'
__author__ = 'Yo Mero <pdaddyjonesthethird@gmail.com>'
__all__ = []

from .dataset import dataset
from random import choice, shuffle

class NameGenerator:
    def __init__(self):
        part_name = [choice(dataset['animals']), choice(dataset['people']), choice(dataset['places'])]
        shuffle(part_name)
        self.name = '-'.join(part_name)
    
    def __str__(self):
        return self.name

    def __rpr__(self):
        return self.name
