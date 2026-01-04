# Django Proyecto 1

Proyecto del módulo Django – Proyecto 1.

## Contexto del proyecto

Este proyecto corresponde al **CRM Básico** solicitado en el Proyecto 1 del módulo Django.

El desarrollo se ha realizado tomando como referencia un **caso real**, adaptándolo a **VitalTech Formación**, que es mi empresa dedicada a la formación sanitaria y técnica.

El objetivo del proyecto es gestionar de forma sencilla:
- Empresas
- Clientes
- Interacciones comerciales

utilizando Django y su panel de administración como núcleo del sistema.

## Tecnologías
- Python 3.12
- Django 6.0

## Instalación
1. Crear entorno virtual
2. Instalar dependencias
3. Ejecutar servidor

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

