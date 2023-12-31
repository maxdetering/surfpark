# Steuerung Wellenerzeugung

Mit diesem Programm können beliebige Wellen auf dem Modell erzeugt werden.

## Umfang
- main.py
- waves.py
- chamber.py
- setup.py
- Ansteuerung-Wellenerzeugung.xlsx

## Vorraussetzungen
- Eine Python 3.x Installation auf dem Revolution Pi
- Die Python Modul erevpimodio2, pandas, threading, time, openpyxl (Installiere mit `pip install -r requirements.txt`)
- Eine Konfiguration des Revolution Pi Core mit angeschlossenen DIO/DO-Modulen wie folgt:
    - Der Output-Anschluss für das Einlassventil an der n-ten Wellenkammer wurde zu 'IntakeValve_n' umbenannt,
        wobei n hier durch die entsprechende Zahl ersetzt wurde.
    - Der Output-Anschluss für das Auslassventil an der n-ten Wellenkammer wurde zu 'ExhaustValve_n' umbenannt,
        wobei n hier durch die entsprechende Zahl ersetzt wurde.
    - Alle Startwerte für die Variablen sind auf 0/False gesetzt.

## Beschreibung
- setup.py
    Diese Datei enthält globale Variablen. Hier muss der Dateipfad zur .xlsx-Datei mit der Zeittabelle zur Wellenerzeugung angegeben werden, der Name der Tabelle in der .xlsx-Datei, und die Anzahl der Wellenkammern.
- chamber.py
    Diese Datei enthält die Funktion create_waveset, mit der ein ganzes Wellenset in einer Wellenkammer gesteuert wird.
- waves.py
    Diese Datei enthält die Funktion create_waveset, mit der ein beliebiges Wellenset mithilfe aller Wellenkammern erzeugt werden kann.
    Mit der enthaltenen Funktion clean_up können alle Ventile zum Programmenede geschlossen werden.
- main.py
    Die Hauptdatei enthält die main-Funktion, in der die Welleninformationen aus der .xlsx-Datei eingelesen werden und die Wellen erzeugt werden.





## Verwendung
In der Datei Ansteuerung-Wellenerzeugung.xlsx sind die Informationen zur Erzeugung eines Wellensets abzuspeichern. Jede Zeile enthaelt dabei die relevanten Zeitintervalle für eine Wellenkammer. Die Zeile enhält dabei Aneinanderreihungen von 4er-Gruppen von Zeitintervallen, die je eine Welle beschreiben. Eine Welle ist durch die 4 Wellenphasen "Totzeit/Delay", "Ausdehnung/Expansion", "Totzeit/Hold" und "Ablassen/Relaxation" gekennzeichnet. Die Zeitintervalle sind in Sekunden anzugeben.

Die Beispieldatei Ansteuerung-Wellenerzeugung.xlsx enthaelt Informationen zur Erzeugung einer einzelnen, gleichmaessigen Wellenfront.






© 2023 by Maximilian Detering
