import os
import pandas as pd

# url del dataset
url = "https://huggingface.co/datasets/khepplewhite/SpotifyData/resolve/main/final.csv"

print("Descargando dataset...")
df = pd.read_csv(url)

os.makedirs("data/raw", exist_ok=True)
df.to_csv("data/raw/spotify_raw.csv", index=False)
print(f"Dataset guardado | Registros: {len(df)}")