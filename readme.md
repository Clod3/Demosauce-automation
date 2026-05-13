# Proyecto de Automatizacion QA - Milani Claudio

## Descripcion

Proyecto de automatizacion de pruebas realizado con Python, Selenium WebDriver y Pytest.

El objetivo del proyecto es automatizar distintas pruebas funcionales de una aplicacion web.

## Tecnologias usadas
- Python
- Selenium WebDriver
- Pytest
- Pytest HTML
- Git

## Instalacion

`git clone https://github.com/Clod3/Demosauce-automation`


## Instalacion dependencias

`pip install -r requirements.txt`

## Cómo ejecutar las pruebas

pytest pre-entrega-final/test_saucedemo.py

El reporte HTML se genera automáticamente (por el archivo pytest.ini) como `reporte.html`.

## Casos de prueba
- **Login:** valida redirección a `/inventory.html` y título "Swag Labs"
- **Catálogo:** verifica título, productos visibles, elementos de UI y datos del primer producto
- **Carrito:** agrega producto, verifica contador y que el ítem aparezca en el carrito