# Usar una imagen base oficial de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar el archivo de requisitos e instalar las dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código fuente del proyecto al contenedor
COPY . .

# Establecer variables de entorno necesarias
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Exponer el puerto en el que se ejecutará la aplicación
EXPOSE 8000

# Ejecutar el servidor de Django al iniciar el contenedor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
