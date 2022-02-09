# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 09:05:00 2022

@author: Matthias
"""
from functools import total_ordering
from typing import Tuple

@total_ordering
class Match:
    
    # constructeur
    def __init__(self, equipe1: str, equipe2: str, score: Tuple[int,int] =(0,0)):
        self.equipe1 = equipe1
        self.equipe2 = equipe2
        self.score = score
        
    # override de __repr__ (et __str__ si __str__ non redefini)
    def __repr__(self):
        return f"<Match {self.equipe1} - {self.equipe2} {self.score}>"
    
    # override de __str__
    def __str__(self):
        return f"{self.equipe1} - {self.equipe2} {self.score}"
    
    # implementation de == et != par deduction
    def __eq__(self, other):
        if not isinstance(other, Match):
            return NotImplemented
        return (self.equipe1, self.equipe2, self.score) == (other.equipe1, other.equipe2, other.score) 
    
    # implementation du hashcode en coherence avec l'==
    def __hash__(self):
        return hash((self.equipe1, self.equipe2, self.score))
    
    # implementation de < (=> > puis <= et >= si @total_ordering)
    def __lt__(self, other):
        if not isinstance(other, Match):
            return NotImplemented
        return (self.score[0]+self.score[1], self.equipe1, self.equipe2) < (other.score[0]+other.score[1], other.equipe1, other.equipe2)
    
    def marque1(self):
        self.score = (self.score[0]+1, self.score[1])
        
    def marque2(self):
        self.score = (self.score[0], self.score[1]+1)
        
    def vainqueur(self):
        if self.score[0] == self.score[1]:
            return None
        return self.equipe1 if self.score[0] > self.score[1] else self.equipe2
    
    def nombreBut(self, numEquipe):
        return self.score[numEquipe-1]
    