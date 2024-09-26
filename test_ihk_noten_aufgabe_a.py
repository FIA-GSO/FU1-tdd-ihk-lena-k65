import pytest
import ihk_noten

def test_aufgabe_a_0():
    #Arrange
    erreichte_punkte = 0
    Gesamtpunktzahl= 50
    soll_ergebnis = 0

    #Act
    ist_ergebnis = ihk_noten.aufgabe_a(erreichte_punkte,Gesamtpunktzahl)

    #Assert
    assert soll_ergebnis == ist_ergebnis

def test_aufgabe_a_10():
    #Arrange
    erreichte_punkte = 10
    Gesamtpunktzahl= 100
    soll_ergebnis = 10

    #Act
    ist_ergebnis = ihk_noten.aufgabe_a(erreichte_punkte,Gesamtpunktzahl)

    #Assert
    assert soll_ergebnis == ist_ergebnis

def test_aufgabe_a_100():
    #Arrange
    erreichte_punkte = 200
    Gesamtpunktzahl= 200
    soll_ergebnis = 100

    #Act
    ist_ergebnis = ihk_noten.aufgabe_a(erreichte_punkte,Gesamtpunktzahl)

    #Assert
    assert soll_ergebnis == ist_ergebnis

def test_aufgabe_a_raises():
    #Arrange
    erreichte_punkte = 10
    Gesamtpunktzahl= 100
    soll_ergebnis = 10

    #Act
    ist_ergebnis = ihk_noten.aufgabe_a(erreichte_punkte,Gesamtpunktzahl)

    #Assert
    assert soll_ergebnis == ist_ergebnis

def test_aufgabe_a_raises_1():
    #Arrange
    erreichte_punkte = "test"
    Gesamtpunktzahl= 100

    #Act
    with pytest.raises(TypeError): 
        ihk_noten.aufgabe_a(erreichte_punkte,Gesamtpunktzahl)

def test_aufgabe_a_raises_2():
    #Arrange
    erreichte_punkte = 10
    Gesamtpunktzahl= "test"
    
    #Act
    with pytest.raises(TypeError): 
        ihk_noten.aufgabe_a(erreichte_punkte,Gesamtpunktzahl)

def test_aufgabe_a_raises_3():
    erreichte_punkte = -10
    Gesamtpunktzahl = 100

    # Assert
    with pytest.raises(ValueError):
        ihk_noten.aufgabe_a(erreichte_punkte, Gesamtpunktzahl)

def test_aufgabe_a_raises_4():
    erreichte_punkte = 10
    Gesamtpunktzahl = -100

    # Assert
    with pytest.raises(ValueError):
        ihk_noten.aufgabe_a(erreichte_punkte, Gesamtpunktzahl)

def test_aufgabe_a_raises_5():
    erreichte_punkte = 10
    Gesamtpunktzahl = 5

    # Assert
    with pytest.raises(ValueError):
        ihk_noten.aufgabe_a(erreichte_punkte, Gesamtpunktzahl)