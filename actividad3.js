
use escuela;


db.Estudiantes.drop();


db.Estudiantes.insertMany([
    { nombre: "Juan", edad: 20, ciudad: "Bogotá" },
    { nombre: "Ana", edad: 22, ciudad: "Medellín" },
    { nombre: "Luis", edad: 19, ciudad: "Cali" },
    { nombre: "María", edad: 23, ciudad: "Bogotá" },
    { nombre: "Carlos", edad: 21, ciudad: "Cartagena" },
    { nombre: "Sofía", edad: 24, ciudad: "Medellín" },
    { nombre: "Pedro", edad: 18, ciudad: "Cali" },
    { nombre: "Lucía", edad: 20, ciudad: "Cartagena" },
    { nombre: "Andrés", edad: 22, ciudad: "Bogotá" },
    { nombre: "Camila", edad: 25, ciudad: "Medellín" }
]);

// Consultar todos los documentos de la colección
print("Todos los estudiantes:");
printjson(db.Estudiantes.find().toArray());

// Filtrar estudiantes por ciudad
const ciudad = "Medellín";
print(`\nEstudiantes de la ciudad ${ciudad}:`);
printjson(db.Estudiantes.find({ ciudad: ciudad }).toArray());

// Consultar estudiantes mayores de 20 años
print("\nEstudiantes mayores de 20 años:");
printjson(db.Estudiantes.find({ edad: { $gt: 20 } }).toArray());

