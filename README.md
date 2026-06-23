# CelFar Automation Testing

## Descripción

Este proyecto corresponde al Trabajo Práctico Final de la materia Taller de Testing Automation.
El objetivo es automatizar la validación funcional de la aplicación CelFar, la cual permite convertir temperaturas de grados Celsius a Fahrenheit, incluyendo validaciones sobre los datos ingresados.

La automatización fue desarrollada en Python utilizando Selenium WebDriver.

---

## Objetivo

Implementar pruebas automatizadas que validen el correcto funcionamiento de la aplicación CelFar en distintos escenarios:

* Conversión válida de temperatura
* Ingreso de valores fuera de rango
* Ingreso de caracteres no válidos

---

## Tecnologías utilizadas

* Python
* Selenium WebDriver
* unittest
* ChromeDriver

---

## Casos de prueba automatizados

### Caso 1 – Conversión válida

Verifica que, al ingresar un valor numérico válido, la aplicación realice correctamente la conversión de Celsius a Fahrenheit.

Ejemplo:

* Entrada: 10
* Resultado esperado: 50

---

### Caso 2 – Número fuera de rango

Verifica el comportamiento de la aplicación al ingresar un número de siete cifras.

Se valida que el mensaje mostrado coincida con lo especificado funcionalmente.

---

### Caso 3 – Carácter no válido

Verifica el comportamiento de la aplicación al ingresar caracteres especiales.

Se valida que la aplicación muestre el mensaje de error correspondiente.

---

## Estructura del proyecto

```
celfar-test-automation/
│
├── casos-de-prueba-codigo/
│   ├── caso1.py
│   ├── caso2.py
│   └── caso3.py
│
├── capturas/
│   ├── casoPrueba1/
│   │   ├── pruebaA/
│   │   │   ├── captura_1.png
│   │   │   ├── captura_2.png
│   │   │   └── captura_3.png
│   │   │
│   │   ├── pruebaB/
│   │   │   ├── captura_1.png
│   │   │   ├── captura_2.png
│   │   │   └── captura_3.png
│   │   │
│   │   └── pruebaC/
│   │       ├── captura_1.png
│   │       ├── captura_2.png
│   │       └── captura_3.png
│   │
│   ├── casoPrueba2/
│   │   ├── captura_1.png
│   │   └── captura_2.png
|   |   └── captura_3.png
│   │
│   └── casoPrueba3/
│       ├── captura_1.png
│       └── captura_2.png
|       └── captura_3.png
│
└── README.md
```

---

## Ejecución

1. Instalar dependencias:

```
pip install selenium
```

2. Descargar ChromeDriver y asegurarse de que esté en el PATH.

3. Ejecutar el script:

```
python celfar_test.py
```

---

## Consideraciones

* Se utilizan esperas explícitas para asegurar la correcta interacción con la interfaz.
* Los tests están implementados utilizando el framework unittest.
* Cada caso de prueba valida tanto el comportamiento funcional como los mensajes devueltos por la aplicación.

---

## Posibles mejoras

* Implementación de Page Object Model (POM)
* Integración con herramientas de visual testing
* Ejecución en múltiples navegadores
* Integración con pipelines de CI/CD

---

## Autor

David Acosta
