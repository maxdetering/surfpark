Mit diesem Programm können beliebige Wellen auf dem Modell erzeugt werden.

### Umfang
- main.py
- waves.py
- chamber.py
- setup.py

### Vorraussetzungen
- Eine Python 3.x Installation auf dem Revolution Pi
- Das Python Modul revpimodio2
- Eine Konfiguration des Revolution Pi Core mit angeschlossenen DIO/DO-Modulen wie folgt:
    Der Output-Anschluss für das Einlassventil an der n-ten Wellenkammer wurde zu IntakeValve_n umbenannt,
        wobei n hier durch die entsprechende Zahl ersetzt wurde.
    Der Output-Anschluss für das Auslassventil an der n-ten Wellenkammer wurde zu ExhaustValve_m umbenannt,
        wobei n hier durhc die entsprechende Zahl ersetzt wurde.
    Alle Startwerte für die Variablen sind auf 0/False gesetzt.

### Beschreibung
- setup.py
    Diese Datei enthält globale Variablen.
- chamber.py
    Diese Datei enthält die Funktion single_wave, mit der eine einzige Wellenkammer ausgelöst wird.
- waves.py
    Diese Datei enthält die Funktion create_wave, mit der eine beliebige Welle mithilfe aller Wellenkammern
    erzeugt werden kann. Mit der enthaltenen Funktion clean_up können alle Ventile zum Programmenede
    geschlossen werden.
- main.py
    Die Hauptdatei enthält die grafische Benutzeroberfläche, mit der eine einzelne Wellenfront erzeugt werden kann.












© 2023 by Maximilian Detering