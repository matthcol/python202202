# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 09:51:13 2022

@author: Matthias
"""

from . import Match

def run():
    m1 = Match("Barcelona", "PSG")
    for _ in range(6):
        m1.marque1()
    m1.marque2()
    print(m1)

if __name__ == '__main__':
    run()