# Usa una imagen base oficial de Python
FROM python:3.9-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de requerimientos y luego instálalos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código fuente al contenedor
COPY ./src /app

# Exponer el puerto para la aplicación Flask
EXPOSE 8050

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
