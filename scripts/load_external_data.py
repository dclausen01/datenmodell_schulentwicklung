"""
Automatisches Laden und Vorbereiten von externen Datenquellen
für die Schülerzahlen-Prognose.

Dieses Skript durchsucht den data/raw Ordner nach bekannten Datenquellen
und bereitet sie für die Integration ins Prognose-Modell vor.
"""

import pandas as pd
import numpy as np
import os
from pathlib import Path

class ExternalDataLoader:
    def __init__(self, raw_data_path='../data/raw'):
        self.raw_data_path = Path(raw_data_path)
        self.data = {}
        
    def load_population_by_age(self, filename='bevoelkerung_altersgruppen_15_20.csv'):
        """Lädt Bevölkerungsdaten nach Altersgruppe (15-20 Jahre)."""
        filepath = self.raw_data_path / filename
        if not filepath.exists():
            print(f"Datei {filename} nicht gefunden.")
            return None
        
        try:
            df = pd.read_csv(filepath, sep=';', encoding='latin-1')
            # Anpassung je nach tatsächlichem Format
            # Annahme: Spalten ['Jahr', 'Alter_15_20']
            df_clean = df[['Jahr', 'Anzahl']].copy()
            df_clean.columns = ['jahr', 'bevoelkerung_15_20']
            self.data['bevoelkerung_15_20'] = df_clean
            print(f"✓ {filename} geladen ({len(df_clean)} Jahre)")
            return df_clean
        except Exception as e:
            print(f"Fehler beim Laden von {filename}: {e}")
            return None
    
    def load_school_graduates(self, filename='schulabsolventen_sh.csv'):
        """Lädt Schulabsolventen-Daten."""
        filepath = self.raw_data_path / filename
        if not filepath.exists():
            print(f"Datei {filename} nicht gefunden.")
            return None
        
        try:
            df = pd.read_csv(filepath, sep=';', encoding='latin-1')
            df_clean = df[['Jahr', 'Absolventen_Gesamt']].copy()
            df_clean.columns = ['jahr', 'absolventen']
            self.data['absolventen'] = df_clean
            print(f"✓ {filename} geladen ({len(df_clean)} Jahre)")
            return df_clean
        except Exception as e:
            print(f"Fehler beim Laden von {filename}: {e}")
            return None
    
    def load_apprenticeship_positions(self, filename='ausbildungsplaetze_regional.csv'):
        """Lädt Ausbildungsplatzzahlen."""
        filepath = self.raw_data_path / filename
        if not filepath.exists():
            print(f"Datei {filename} nicht gefunden.")
            return None
        
        try:
            df = pd.read_csv(filepath, sep=';', encoding='latin-1')
            df_clean = df[['Jahr', 'Ausbildungsplaetze']].copy()
            df_clean.columns = ['jahr', 'ausbildungsplaetze']
            self.data['ausbildungsplaetze'] = df_clean
            print(f"✓ {filename} geladen ({len(df_clean)} Jahre)")
            return df_clean
        except Exception as e:
            print(f"Fehler beim Laden von {filename}: {e}")
            return None
    
    def load_unemployment_rate(self, filename='arbeitslosenquote_sh.csv'):
        """Lädt Arbeitslosenquote SH."""
        filepath = self.raw_data_path / filename
        if not filepath.exists():
            print(f"Datei {filename} nicht gefunden.")
            return None
        
        try:
            df = pd.read_csv(filepath, sep=';', encoding='latin-1')
            df_clean = df[['Jahr', 'Arbeitslosenquote']].copy()
            df_clean.columns = ['jahr', 'arbeitslosenquote']
            self.data['arbeitslosenquote'] = df_clean
            print(f"✓ {filename} geladen ({len(df_clean)} Jahre)")
            return df_clean
        except Exception as e:
            print(f"Fehler beim Laden von {filename}: {e}")
            return None
    
    def load_gdp(self, filename='bip_sh.csv'):
        """Lädt BIP Schleswig-Holstein."""
        filepath = self.raw_data_path / filename
        if not filepath.exists():
            print(f"Datei {filename} nicht gefunden.")
            return None
        
        try:
            df = pd.read_csv(filepath, sep=';', encoding='latin-1')
            df_clean = df[['Jahr', 'BIP']].copy()
            df_clean.columns = ['jahr', 'bip']
            self.data['bip'] = df_clean
            print(f"✓ {filename} geladen ({len(df_clean)} Jahre)")
            return df_clean
        except Exception as e:
            print(f"Fehler beim Laden von {filename}: {e}")
            return None
    
    def load_all(self):
        """Lädt alle verfügbaren Datenquellen."""
        print("Suche nach externen Datenquellen...")
        print("-" * 50)
        
        self.load_population_by_age()
        self.load_school_graduates()
        self.load_apprenticeship_positions()
        self.load_unemployment_rate()
        self.load_gdp()
        
        print("-" * 50)
        print(f"Gefundene Datenquellen: {len(self.data)}")
        return self.data
    
    def merge_with_student_data(self, df_students):
        """Merged alle geladenen Datenquellen mit den Schülerdaten."""
        df_merged = df_students.copy()
        
        for name, df_ext in self.data.items():
            df_merged = pd.merge(df_merged, df_ext, on='jahr', how='left')
            print(f"✓ {name} gemerged")
        
        # Fehlende Werte interpolieren (falls Daten nicht komplett sind)
        for col in df_merged.columns:
            if col not in ['jahr', 'ds', 'y', 'schuelerzahl', 'anmerkung']:
                df_merged[col] = df_merged[col].interpolate(method='linear')
        
        return df_merged


if __name__ == "__main__":
    # Test
    loader = ExternalDataLoader()
    data = loader.load_all()
    
    # Beispiel: Merge mit Schülerdaten
    df_students = pd.read_csv('../data/processed/schuelerzahlen_aggregated.csv')
    df_final = loader.merge_with_student_data(df_students)
    
    print("\nFinaler Datensatz:")
    print(df_final.head())
    print(f"\nSpalten: {list(df_final.columns)}")