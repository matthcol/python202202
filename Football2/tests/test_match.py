# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 11:52:42 2022

@author: Matthias
"""
import pytest

import football as f

def test_constructor_simple():
    equipe1 = "Barcelona"
    equipe2 = "PSG"
    m = f.Match(equipe1, equipe2)
    assert m.equipe1 == equipe1
    assert m.equipe2 == equipe2
    assert m.score == (0,0)

def test_constructor_full():
    equipe1 = "Barcelona"
    equipe2 = "PSG"
    score = (6,1)
    m = f.Match(equipe1, equipe2, score)
    assert m.equipe1 == equipe1
    assert m.equipe2 == equipe2
    assert m.score == score

@pytest.fixture(params=[1,2], ids=["Team 1", "Team 2"])
def team(request):
    return request.param

def test_nombreBut_equipe1(team):
    # given
    equipe1 = "Barcelona"
    equipe2 = "PSG"
    score = (6,1)
    m = f.Match(equipe1, equipe2, score)
    # when
    nb = m.nombreBut(team)
    # then
    assert nb == score[team-1]
    
    
    
    
    