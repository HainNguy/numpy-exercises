**Ziel:** NumPy-Grundlagen für Data Engineering durch die Analyse von ETL-Job-Metriken praktisch anwenden. Keine Musterlösung vor Abgabe.

**Schwierigkeit:** Grundlagen · **Dauer:** 35–50 Minuten · **Status:** In Bearbeitung

## Beruflicher Kontext

Als Junior Data Engineer überwachst du eine ETL-Pipeline. Für jeden Job werden Laufzeit in Millisekunden, gelesene Zeilen, geschriebene Zeilen und fehlerhafte Zeilen aufgezeichnet. Untersuche diese Kennzahlen mit NumPy.

## Lernziele

- `ndarray`, `shape`, `ndim`, `size`, `dtype` verstehen
- Indexing und Slicing bei zweidimensionalen Arrays anwenden
- Den Datentyp nach `float64` konvertieren, ohne das Original zu verändern
- Eine einfache Transformation ohne explizite Python-Schleifen durchführen
- Views und Shapes konzeptionell erklären

## Ausgangsdaten

```python
import numpy as np

# Spalten:
# 0: duration_ms
# 1: rows_read
# 2: rows_written
# 3: error_count

etl_jobs = np.array([
    [1200, 10000, 9950, 50],
    [1800, 15000, 14800, 200],
    [900,   8000, 8000, 0],
    [2500, 20000, 19500, 500],
    [1100, 12000, 11900, 100],
    [3000, 25000, 24500, 500]
])

print(etl_jobs)
```

## Teilaufgaben

- [ ]  **A – Array-Struktur:** `shape`, `ndim`, `size`, `dtype` ausgeben und die Zahl der ETL-Jobs programmatisch bestimmen.
- [ ]  **B – Indexing:** Laufzeit des dritten Jobs, alle Kennzahlen des vierten Jobs und `rows_read` aller Jobs extrahieren.
- [ ]  **C – Slicing:** Nur die ersten drei Jobs mit den Spalten `rows_read` und `rows_written` extrahieren. Erwartete Shape: `(3, 2)`.
- [ ]  **D – Datentypkonvertierung:** Neues Array mit Datentyp `float64` erzeugen, ohne `etl_jobs` zu verändern; den neuen Datentyp ausgeben.
- [ ]  **E – Vektorisierung:** Laufzeiten aller sechs Jobs von Millisekunden in Sekunden umrechnen, ohne explizite Python-Schleife. Ergebnis: 1D-Array mit sechs Elementen.

## Verständnis- und Interviewfragen

- [ ]  **1:** Was ist der Unterschied zwischen `shape`, `ndim` und `size`? Erkläre am Array `etl_jobs`.
- [ ]  **2:** Was ist der Unterschied zwischen `etl_jobs[0]` und `etl_jobs[0:1]`, insbesondere hinsichtlich der Shapes?
- [ ]  **3:** Wann ist die Konvertierung von `int64` nach `float64` in einer Datenpipeline sinnvoll? Welche Nachteile kann sie haben?
- [ ]  **4 – Interview:** Was sind die wichtigsten Unterschiede zwischen einer Python-Liste und einem NumPy-Array? Wann würdest du NumPy einsetzen? Formuliere eine kurze mündliche Antwort.

## Bewertung (maximal 10 Punkte)

| Kriterium | Punkte |
| --- | --- |
| Funktionale Korrektheit der Teile A–E | 5 |
| Richtiger NumPy-Einsatz | 1 |
| Lesbarkeit und Codequalität | 1 |
| Verständnisfragen 1–3 | 2 |
| Mündliche Interviewerklärung | 1 |

**Bestanden:** mindestens 8/10 Punkte und korrektes Verständnis der Kernkonzepte. Die Lösung wird erst nach deiner eigenen Abgabe erklärt.

## Abgabe

```python
# Teil A

# Teil B

# Teil C

# Teil D

# Teil E

# Verständnisfragen
# 1.
# 2.
# 3.
# 4.
```

## Lernnotizen und Feedback

**Bewertung:** noch offen
**Code-Review:** noch offen
**Nächster Schritt:** Aufgaben lösen und Code sowie Antworten im Chat einreichen.

**Quelle:** NumPy Mastery Challenge, ChatGPT-Gespräch vom 5. November 2026. Offizielle Dokumentation: https://numpy.org/doc/stable/