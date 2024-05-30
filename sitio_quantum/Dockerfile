# Utiliza una imagen base oficial de Python
FROM python:3.10.12-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de requisitos y lo instala
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del proyecto Django en el contenedor
COPY . .

# Expone el puerto 8000
EXPOSE 8000

# Ejecuta el servidor de desarrollo de Django al iniciar el contenedor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
