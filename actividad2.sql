-- Paso 1: Creación de la tabla Estudiantes
CREATE TABLE Estudiantes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    edad INT NOT NULL,
    ciudad VARCHAR(50) NOT NULL
);

-- Insertar datos básicos en la tabla
INSERT INTO Estudiantes (nombre, edad, ciudad) VALUES
('Ana López', 22, 'Bogotá'),
('Luis Pérez', 17, 'Medellín'),
('Carla Gómez', 25, 'Cali'),
('Pedro Sánchez', 18, 'Bogotá'),
('María Fernández', 21, 'Medellín'),
('Juan Rivera', 23, 'Cali'),
('Sofía Martínez', 20, 'Cartagena'),
('Diego Torres', 24, 'Bogotá'),
('Lucía Castro', 22, 'Cali'),
('Andrés Ramírez', 18, 'Medellín');

-- Filtrar estudiantes por ciudad
SELECT * FROM Estudiantes WHERE ciudad = 'Bogotá';

-- Consultar todos los registros de la tabla
SELECT * FROM Estudiantes;

-- Consultar estudiantes mayores de 20 años
SELECT * FROM Estudiantes WHERE edad > 20;
