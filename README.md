# Datenmodell Schulentwicklung

## 📋 Projektbeschreibung

Dieses Projekt dient der Entwicklung eines datenbasierten Modells zur Prognose von Schülerzahlen in Schulen. Es unterstützt Schulen und Bildungsbehörden bei der Planung von Klassen, Lehrerbedarf und Ressourcenverteilung.

## 🚀 Hauptziele

- **Prognose von Schülerzahlen** basierend auf historischen Daten und demografischen Trends.
- **Analyse von Schulbereichen** (Grundschule, Sekundarstufe I, Sekundarstufe II) und deren Entwicklungen.
- **Dashboard-ähnliche Visualisierung** der Ergebnisse für Entscheidungsträger.
- **Flexibles Daten-Input** für aktuelle Zahlen und Statistiken.

## 📂 Projektstruktur

```
.
├── data/
│   ├── raw/          # Hier werden die Rohdaten (Excel/CSV) abgelegt
│   └── processed/    # Bereinigte und aufbereitete Daten
├── notebooks/
│   └── schuelerzahlen_prognose.ipynb  # Haupt-Notebook für Entwicklung
├── requirements.txt   # Python-Abhängigkeiten
├── CONCEPT.md         # Konzept und technische Entscheidungen
└── README.md         # Diese Datei
```

## 📊 Technologien

- **Python 3.x** als Hauptprogrammiersprache
- **Pandas** für Datenmanipulation
- **NumPy** für numerische Berechnungen
- **Matplotlib/Seaborn** für Visualisierungen
- **Prophet** (Meta) für Zeitreihenprognosen
- **Jupyter Notebook** für interaktive Entwicklung
- **Streamlit** (optional) für interaktives Dashboard

## 🔧 Installation

1. **Repository klonen:**

   ```bash
   git clone https://github.com/dclausen01/datenmodell_schulentwicklung.git
   cd datenmodell_schulentwicklung
   ```

2. **Virtuelle Umgebung erstellen:**

   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # oder: source venv/bin/activate  # Linux/Mac
   ```

3. **Abhängigkeiten installieren:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Jupyter starten:**
   ```bash
   jupyter notebook
   ```

## 📄 Daten

### Erwartete Datenformate

- **Historische Schülerzahlen:** Excel/CSV mit Spalten wie `Jahr`, `Schulbereich`, `Schülerzahl`
- **Bevölkerungsstatistiken:** Excel/CSV mit demografischen Daten
- **Weitere relevante Statistiken:** Geburtenraten, Zuzug/Zugang, etc.

### Datenablage

- **Rohdaten:** `data/raw/`
- **Bereinigte Daten:** `data/processed/` (wird vom Notebook erstellt)

## 🧪 Verwendung

1. **Daten vorbereiten:**
   - Legen Sie Ihre Excel/CSV-Dateien im Ordner `data/raw/` ab.
   - Stellen Sie sicher, dass die Daten die erwarteten Spalten enthalten.

2. **Notebook starten:**
   - Öffnen Sie `notebooks/schuelerzahlen_prognose.ipynb` in Jupyter.
   - Führen Sie die Zellen nacheinander aus.

3. **Prognosen generieren:**
   - Das Notebook führt automatisch die Datenanalyse und Prognose durch.
   - Ergebnisse werden als Grafiken und Tabellen visualisiert.

## 📈 Prognose-Methodik

Das Modell verwendet **Prophet** (von Meta) für Zeitreihenprognosen. Prophet ist besonders geeignet für:

- Trends mit saisonalen Schwankungen
- Daten mit wöchentlichen oder jährlichen Mustern
- Robuste Prognosen auch bei fehlenden Daten

## 🔒 Datenschutz

- **Keine sensiblen Daten im Repository:** Die `.gitignore` schließt `data/raw/*` aus.
- **Lokale Verarbeitung:** Alle Berechnungen finden lokal auf Ihrem Rechner statt.
- **Keine externe Datenübertragung:** Es werden keine Daten an externe Dienste gesendet.

## 🤝 Mitwirken

Falls Sie Verbesserungsvorschläge oder Erweiterungen haben:

1. **Issue erstellen:** Beschreiben Sie Ihr Anliegen auf GitHub.
2. **Pull Request:** Falls Sie Code beitragen möchten, folgen Sie bitte den üblichen GitHub-Workflows.

## 📞 Kontakt

Bei Fragen oder Feedback können Sie gerne ein Issue im Repository erstellen.

---

**Hinweis:** Dieses Projekt befindet sich in der Entwicklungsphase. Die Prognosen dienen als Entscheidungshilfe und ersetzen keine professionelle Beratung.
