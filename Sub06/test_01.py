# import pytest
from musculoskeletal_system import Musculoskeletal_System

# Starting tests...
def test_01():
    a = Musculoskeletal_System("muscles")
    """ Check that move() == True """
    assert a.move() == True

def test_02():
    a = Musculoskeletal_System("bones")
    """ Check that move() == True """
    assert a.move() == True

def test_03():
    a = Musculoskeletal_System("nerves")
    """ Check that move() == False """
    assert a.move() == False
