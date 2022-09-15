# Generator für Kehrwochenplan

Erzeugt eine Vorlage, die im Querformat
auf zwei A4-Seiten (bzw. A4 mit zwei Seiten auf einer)
ausgedruckt werden kann.

## Pro Jahr ausfüllen
- months - Anpassen der Tage pro Monat
- restBio, papierGelb - Termin für Mülltonnen-Abholung (vom Landratsamt)
- dayOfWeek - Erster Wochentag des Jahres
- partei - Welche Partei beginnt mit der Kehrwoche


## Ausführung

python plan.py > out.html

HTML-Seite dann so drucken, dass beide Tabellen auf 
einer A4-Seite ausgedruckt werden können.

