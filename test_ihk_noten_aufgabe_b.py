from tokenize import Double
from  ihk_noten import *
from pytest import raises

def test_aufgabe_b_100():
    #Arrange
    erreichte_prozentzahl = 100
    soll_ergebnis = "sehr gut";

    #Act
    ist_ergebnis = aufgabe_b(erreichte_prozentzahl)

    #Assert
    assert soll_ergebnis == ist_ergebnis

def test_aufgabe_b_92():
    #Arrange
    erreichte_prozentzahl = 92
    soll_ergebnis = "sehr gut";

    #Act
    ist_ergebnis = aufgabe_b(erreichte_prozentzahl)

    #Assert
    assert soll_ergebnis == ist_ergebnis

def test_aufgabe_b_91():
    #Arrange
    erreichte_prozentzahl = 91
    soll_ergebnis = "gut";

    #Act
    ist_ergebnis = aufgabe_b(erreichte_prozentzahl)

    #Assert
    assert soll_ergebnis == ist_ergebnis

def test_aufgabe_b_81():
    #Arrange
    erreichte_prozentzahl = 81
    soll_ergebnis = "gut";

    #Act
    ist_ergebnis = aufgabe_b(erreichte_prozentzahl)

    #Assert
    assert soll_ergebnis == ist_ergebnis

def test_aufgabe_b_80():
    #Arrange
    erreichte_prozentzahl = 80
    soll_ergebnis = "befriedigend";

    #Act
    ist_ergebnis = aufgabe_b(erreichte_prozentzahl)

    #Assert
    assert soll_ergebnis == ist_ergebnis

def test_aufgabe_b_67():
    #Arrange
    erreichte_prozentzahl = 67
    soll_ergebnis = "befriedigend";

    #Act
    ist_ergebnis = aufgabe_b(erreichte_prozentzahl)

    #Assert
    assert soll_ergebnis == ist_ergebnis

def test_aufgabe_b_66():
    #Arrange
    erreichte_prozentzahl = 66
    soll_ergebnis = "ausreichend";

    #Act
    ist_ergebnis = aufgabe_b(erreichte_prozentzahl)

    #Assert
    assert soll_ergebnis == ist_ergebnis

def test_aufgabe_b_50():
    #Arrange
    erreichte_prozentzahl = 50
    soll_ergebnis = "ausreichend";

    #Act
    ist_ergebnis = aufgabe_b(erreichte_prozentzahl)

    #Assert
    assert soll_ergebnis == ist_ergebnis

def test_aufgabe_b_49():
    #Arrange
    erreichte_prozentzahl = 49
    soll_ergebnis = "mangelhaft";

    #Act
    ist_ergebnis = aufgabe_b(erreichte_prozentzahl)

    #Assert
    assert soll_ergebnis == ist_ergebnis

def test_aufgabe_b_30():
    #Arrange
    erreichte_prozentzahl = 30
    soll_ergebnis = "mangelhaft";

    #Act
    ist_ergebnis = aufgabe_b(erreichte_prozentzahl)

    #Assert
    assert soll_ergebnis == ist_ergebnis

def test_aufgabe_b_29():
    #Arrange
    erreichte_prozentzahl = 29
    soll_ergebnis = "ungenügend";

    #Act
    ist_ergebnis = aufgabe_b(erreichte_prozentzahl)

    #Assert
    assert soll_ergebnis == ist_ergebnis

def test_aufgabe_b_0():
    #Arrange
    erreichte_prozentzahl = 0
    soll_ergebnis = "ungenügend";

    #Act
    ist_ergebnis = aufgabe_b(erreichte_prozentzahl)

    #Assert
    assert soll_ergebnis == ist_ergebnis

def test_aufgabe_b_raises_1():
    #Arrange
    erreichte_prozentzahl = -1

    # Assert
    with raises(ValueError):
        aufgabe_a(erreichte_prozentzahl)

def test_aufgabe_b_raises_1():
    #Arrange
    erreichte_prozentzahl = 100

    # Assert
    with raises(ValueError):
        aufgabe_a(erreichte_prozentzahl)

def test_aufgabe_b_raises_1():
    #Arrange
    erreichte_prozentzahl = "test"

    # Assert
    with raises(TypeError):
        aufgabe_a(erreichte_prozentzahl)

