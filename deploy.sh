#!/bin/bash

# Activar el entorno virtual
source env/Scripts/activate

# Instalar los requerimientos
pip install -r requirements.txt

# Actualizar pip (opcional)
pip install --upgrade pip

# Navegar a la carpeta del frontend si es necesario (por ejemplo, npm)
cd src/static/lib
npm install  # Si utilizas npm para el frontend

# Correr el programa
python src/manage.py runserver
