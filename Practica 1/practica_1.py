# practica 1: limpieza de datos
# dataset: spotify data

import pandas as pd
import numpy as np
import os

def cargar_datos(path_input):
    df = pd.read_csv(path_input)
    print(f"Dimensiones iniciales: {df.shape[0]} filas y {df.shape[1]} columnas.\n")
    return df

def diagnostico_inicial(df):
    print("Información del Dataset:/n")
    print(df.info())
    
    print("\nValores nulos por Columna:")
    nulos = df.isnull().sum()
    print(nulos[nulos > 0] if nulos.sum() > 0 else "No se encontraron valores nulos.")
    
    duplicados = df.duplicated().sum()
    print(f"\nFilas duplicadas: {duplicados}\n")

def limpiar_datos(df):
    df_clean = df.copy()
    
    # eliminacion de duplicados exactos
    filas_antes = len(df_clean)
    df_clean = df_clean.drop_duplicates()
    print(f"-> Se eliminaron {filas_antes - len(df_clean)} filas duplicadas.")
    
    # manejo de valores nulos
    # si existen columnas categoricas nulas se llenan con 'unknown'
    cols_texto = df_clean.select_dtypes(include=['object', 'string', 'str']).columns
    for col in cols_texto:
        if df_clean[col].isnull().sum() > 0:
            df_clean[col] = df_clean[col].fillna("Unknown")
            print(f"-> Imputados valores nulos en columna categórica: '{col}' con 'Unknown'.")
            
    # si existen columnas numericas nulas se llenan con la mediana
    cols_num = df_clean.select_dtypes(include=['number']).columns
    for col in cols_num:
        if df_clean[col].isnull().sum() > 0:
            mediana = df_clean[col].median()
            df_clean[col] = df_clean[col].fillna(mediana)
            print(f"-> Imputados valores nulos en columna numérica: '{col}' con la mediana ({mediana}).")
            
    # formatear nombres de columnas
    df_clean.columns = (
        df_clean.columns
        .str.strip()
        .str.lower()
        .str.replace(' ', '_')
        .str.replace('[^a-zA-Z0-2_]', '', regex=True)
    )
    print("-> Nombres de columnas estandarizados (snake_case).")
    
    # conversion de tipos de datos (si aplica)
    # por ejemplo, asegurar que la duracion o tempo sean flotantes/enteros positivos
    if 'duration' in df_clean.columns:
        df_clean = df_clean[df_clean['duration'] > 0]
        
    print(f"\nDimensiones finales tras limpieza: {df_clean.shape[0]} filas y {df_clean.shape[1]} columnas.")
    return df_clean

def guardar_datos_limpios(df, path_output):
    os.makedirs(os.path.dirname(path_output), exist_ok=True)
    df.to_csv("data/processed/spotify_cleaned.csv", index=False, encoding="utf-8")
    print(f"Dataset limpio guardado exitosamente en: '{path_output}'")

if __name__ == "__main__":
    PATH_RAW = "data/raw/spotify_raw.csv"
    PATH_PROCESSED = "data/processed/spotify_cleaned.csv"
    
    df_raw = cargar_datos(PATH_RAW)
    diagnostico_inicial(df_raw)
    df_clean = limpiar_datos(df_raw)
    guardar_datos_limpios(df_clean, PATH_PROCESSED)