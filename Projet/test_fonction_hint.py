# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 10:16:05 2022

@author: Matthias
"""

def f(x: int)->int:
    return x+1

print(f(3))

# erreur si un checker vérifie le programme
# mypy test_fonction_hint.py
# test_fonction_hint.py:12: error: Argument 1 to "f" has incompatible type "float"; expected "int"
# Found 1 error in 1 file (checked 1 source file)
print(f(3.4))