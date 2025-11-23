# U1 S4 Tarea Asincronica: POO en Python con Herencia, Composición, Encapsulamiento y Métodos de Comportamiento

Este programa organiza el sistema de transporte separando cada clase en su propio archivo, lo cual es una buena práctica para proyectos escalables:

Jerarquía de Clases (Herencia): Vehiculo define la base común. Automovil y Motocicleta heredan de ella, reutilizando código (como marca y año) y añadiendo comportamientos únicos (como hacer_caballito).

Integración de Componentes (Composición): La clase Motor funciona como una pieza intercambiable. En main.py, creas motores primero y luego se los asignas a los vehículos, demostrando la relación "tiene un".

Orquestación: El archivo main.py importa todos los módulos, crea instancias específicas (como un Lexus Híbrido o una Ducati) e imprime sus estados usando el método __str__ sobreescrito en cada clase.

<img width="1920" height="1080" alt="Captura de pantalla 2025-11-14 164130" src="https://github.com/user-attachments/assets/cd8cd602-11c8-4a8a-9d1f-eb00bf36ac4e" />
