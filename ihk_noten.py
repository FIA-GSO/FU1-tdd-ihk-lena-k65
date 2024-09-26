def aufgabe_a(erreichte_punkte, Gesamtpunktzahl):

    if not isinstance(erreichte_punkte, (int)) or not isinstance(Gesamtpunktzahl, (int)):
        raise TypeError ("Erreichte Punktzahl und Gesamtpunktzahl müssen als natürliche Zahlen angegeben sein.")

    if erreichte_punkte < 0 or Gesamtpunktzahl < 0:
        raise ValueError ("Punktzahlen müssen positiv sein.")
    
    if erreichte_punkte > Gesamtpunktzahl:
        raise ValueError ("Erreichte Punktzahl ist größer als Gesamtpunktzahl")

    prozent = (erreichte_punkte / Gesamtpunktzahl) * 100
    return round(prozent, 2)


def aufgabe_b(erreichte_prozentzahl):

    if not isinstance(erreichte_prozentzahl, (int)):
        raise TypeError ("Erreichter Prozent muss als natürliche Zahl angegeben sein")
    
    if erreichte_prozentzahl < 0 or erreichte_prozentzahl > 100:
        raise ValueError ("Erreichter Prozent muss mind. 0 und darf max. 100 sein")

    if erreichte_prozentzahl > 91:
        return "sehr gut"
    elif erreichte_prozentzahl > 80:
        return "gut"
    elif erreichte_prozentzahl > 66:
        return "befriedigend"
    elif erreichte_prozentzahl > 49:
        return "ausreichend"
    elif erreichte_prozentzahl > 29:
        return "mangelhaft"
    else:
        return "ungenügend"
    
           

