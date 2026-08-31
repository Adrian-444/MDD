# Minería de Datos

Repositorio para la entrega de las actividades.

Para el desarrollo de la materia se utiliza un [Dataset](https://huggingface.co/datasets/khepplewhite/SpotifyData) continuo de canciones de **Spotify** obtenido de HuggingFace.

El dataset crudo se omitió en el repo para evitar la duplicación de información, se puede descargar con el script **_dataset.py_**

---

## Estructura del proyecto

El proyecto está organizado con la siguiente estructura de carpetas y archivos:

```text
.
├── data/
│   ├── raw/
│   │   ├── dataset.py        # Script para descargar el dataset original desde HuggingFace
│   │   └── spotify_raw.csv   # Dataset original crudo
│   └── processed/
│       └── spotify_cleaned.csv  # Dataset limpio y estandarizado tras la Práctica 1
├── Practica 1/               # Carpeta correspondiente a la Práctica 1
├── Practica 2/               # Carpeta correspondiente a la Práctica 2
│   ├── outputs/              # Contiene graficas, el diagrama ER y un resumen .csv de la Practica 2
├── .gitignore
└── README.md
```
