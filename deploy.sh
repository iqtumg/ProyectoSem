!/bin/bash

# Activar el entorno virtual
source env/Scripts/activate

# Instalar los requerimientos
pip install -r requirements.txt

# Actualizar pip (opcional)
pip install --upgrade pip

# Navegar a la carpeta del frontend 
cd src/static/lib
npm install  

# Correr el programa
python src/manage.py runserver
