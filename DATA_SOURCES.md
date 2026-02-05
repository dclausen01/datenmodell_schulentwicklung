# Datenquellen für Schülerzahlen-Prognose

Dieser Leitfaden zeigt, wo Sie die relevanten externen Daten für präzisere Prognosen finden.

## 1. Bevölkerung nach Altersgruppen (15-20 Jahre)

**Quelle:** Statistikamt Nord
**URL:** https://www.statistik-nord.de/zahlen-fakten/bevoelkerung/oa

**Anleitung:**

1. Navigieren Sie zur Seite
2. Wählen Sie: "Bevölkerung nach Altersgruppen"
3. Filter: Schleswig-Holstein, Altersgruppe 15-19 Jahre (oder 15-24)
4. Zeitraum: Alle verfügbaren Jahre (mind. ab 2009)
5. Format: CSV oder Excel
6. **Speichern als:** `data/raw/bevoelkerung_altersgruppen_15_20.csv`

---

## 2. Schulabsolventen Schleswig-Holstein

**Quelle:** Statistikamt Nord / Bildungsstatistik
**URL:** https://www.statistik-nord.de/zahlen-fakten/bildung-kultur-rechtspflege/schulen

**Anleitung:**

1. Suchen Sie nach "Schulabgänger" oder "Abschlüsse"
2. Filter: Alle Schularten (Hauptschule, Realschule, Gymnasium)
3. Zeitraum: ab 2009
4. **Speichern als:** `data/raw/schulabsolventen_sh.csv`

**Alternative:** Kultusministerium SH
https://www.schleswig-holstein.de/DE/landesregierung/ministerien-behoerden/III/iii_node.html

---

## 3. Ausbildungsplatzzahlen (IHK/HWK)

**Quelle:** Bundesagentur für Arbeit - Statistik
**URL:** https://statistik.arbeitsagentur.de/

**Anleitung:**

1. Wählen Sie: "Ausbildungsmarkt" → "Berufsbildungsstatistik"
2. Region: Schleswig-Holstein oder Rendsburg-Eckernförde
3. Zeitraum: ab 2009
4. **Speichern als:** `data/raw/ausbildungsplaetze_regional.csv`

**Alternative IHK-Daten:**

- IHK Schleswig-Holstein: https://www.ihk-schleswig-holstein.de/
- Direkt anfragen oder Jahresberichte durchsuchen

---

## 4. Arbeitslosenquote Schleswig-Holstein

**Quelle:** Bundesagentur für Arbeit - Statistik
**URL:** https://statistik.arbeitsagentur.de/SiteGlobals/Forms/Suche/Einzelheftsuche_Formular.html

**Anleitung:**

1. Suchen Sie nach "Arbeitslosenquote Schleswig-Holstein"
2. Wählen Sie: Monatliche oder jährliche Zeitreihe
3. Zeitraum: ab 2009
4. **Speichern als:** `data/raw/arbeitslosenquote_sh.csv`

**Schnellere Alternative:**

- Destatis (Genesis-Online): https://www-genesis.destatis.de/
- Suche: "Arbeitslose Schleswig-Holstein"

---

## 5. Wirtschaftsindikatoren (BIP Schleswig-Holstein)

**Quelle:** Statistisches Bundesamt / Statistikamt Nord
**URL:** https://www.statistik-nord.de/zahlen-fakten/volkswirtschaftliche-gesamtrechnungen

**Anleitung:**

1. Wählen Sie: "Bruttoinlandsprodukt" → Schleswig-Holstein
2. Zeitraum: ab 2009
3. Optional: Nach Wirtschaftszweigen (Gesundheit, Handel, Industrie)
4. **Speichern als:** `data/raw/bip_sh.csv`

---

## Dateiformat-Hinweise

- **Bevorzugtes Format:** CSV (Semikolon-separiert oder Komma-separiert)
- **Alternative:** Excel (.xlsx) - wird automatisch erkannt
- **Wichtig:**
  - Achten Sie darauf, dass die Daten den **vollständigen Zeitraum ab 2009** abdecken
  - Bei Excel: Nur eine Tabelle pro Datei (keine Metadaten/Formatierungen)
  - Speichern Sie alle Dateien im Ordner `data/raw/`

---

## Schnellstart (falls Zeitmangel)

Falls Sie nicht alle Daten sofort beschaffen können, priorisieren Sie:

1. **Bevölkerung nach Altersgruppen (15-20 Jahre)** - höchste Relevanz
2. **Schulabsolventen** - zweitwichtigster Indikator
3. **Ausbildungsplatzzahlen** - falls verfügbar

Ich erstelle ein Skript, das automatisch alle vorhandenen Dateien einliest und in das Modell integriert.
