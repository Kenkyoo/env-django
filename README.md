📚 Documentación: Configuración de Entorno Virtual y Proyecto Django Base

Este repositorio contiene la documentación y el código base de un proyecto de inicio de Django, enfocado en las buenas prácticas de configuración de entornos virtuales de Python.

El objetivo es proporcionar un esqueleto limpio y funcional para nuevos proyectos web, demostrando cómo se inicializa un proyecto Django y cómo se realiza su despliegue inicial.

🚀 Despliegue en Producción

Este proyecto ha sido desplegado exitosamente en Render, lo que valida su configuración para entornos de producción.

URL del Proyecto Desplegado:
https://env-django-i3qf.onrender.com

📋 Funcionalidades

El proyecto incluye la estructura mínima y esencial de Django:

Estructura Base: Un proyecto (mi_portfolio) que contiene una aplicación principal (core).

Rutas Simples: Una vista de inicio (/) con contenido HTML básico.

Manejo de Estáticos: Configuración inicial para servir archivos CSS y JS.

🛠️ Configuración y Ejecución Local

Sigue estos pasos para levantar el proyecto en tu máquina.

1. Clonar el Repositorio

git clone [https://github.com/Kenkyoo/env-django.git](https://github.com/Kenkyoo/env-django.git)
cd env-django


2. Crear y Activar el Entorno Virtual

Es fundamental trabajar en un entorno virtual aislado para gestionar las dependencias del proyecto.

# Crear el entorno virtual (usando 'venv' en este ejemplo)
python -m venv .venv

# Activar el entorno virtual
# En Linux/macOS:
source .venv/bin/activate

# En Windows (CMD):
.venv\Scripts\activate.bat

# En Windows (PowerShell):
.venv\Scripts\Activate.ps1


3. Instalar Dependencias

Instala todas las bibliotecas necesarias listadas en requirements.txt.

pip install -r requirements.txt


4. Migraciones y Base de Datos

Aplica las migraciones iniciales para configurar la base de datos (SQLite por defecto).

python manage.py migrate


5. Ejecutar el Servidor de Desarrollo

Inicia el servidor local de Django.

python manage.py runserver


El proyecto estará disponible en tu navegador en: http://127.0.0.1:8000/

⚙️ Estructura del Proyecto

El proyecto sigue la convención de Django de separar la configuración del proyecto de la lógica de la aplicación.

.
├── mi_portfolio/         # Directorio de Configuración del Proyecto
│   ├── settings.py       # Configuración global
│   ├── urls.py           # Rutas URL principales
│   └── wsgi.py
├── core/                 # Aplicación principal
│   ├── views.py          # Lógica de las vistas
│   └── urls.py           # Rutas URL de la aplicación
├── requirements.txt      # Dependencias de Python
├── manage.py             # Herramienta de gestión de Django
├── Procfile              # Instrucción de despliegue para Render
└── README.md             # Este archivo

