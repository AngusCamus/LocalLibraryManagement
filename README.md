# Biblioteca Local con Django
Biblioteca Local es un proyecto en Django Framework realizado por mi a modo de poner a prueba mi conocimiento, el mismo simula una web que informa los libros que dispone y ofrece un servicio de alquiler. La idea es con el paso del tiempo y adquirir nuevas habilidades ir mejorando la pagina.

El sitio se encuentra desplegado en Heroku y pueden visitarlo desde el siguiente [Link](https://dry-journey-94644.herokuapp.com/)

Utiliza como Base de Datos el addon postgresql de heroku

Cuenta con test unitarios usando TestCase de Django, los mismos se realizan tanto sobre modelos, vistas y formularios.

Conforme vaya realizando nuevas versiones notificare los cambios y su version en este readme.

## Versiones

1.0 - Version Base (10/7/2022)

## Permisos y/o grupos de usuarios

Biblioteca Local cuenta con permisos para sus usuarios dividiendolos en 3 grupos:

*-Bibliotecarios/Empleados*: Estos al logearse en el sitio tienen permisos para añadir nuevos libros a la Base de datos, nuevas copias de ellos y consultar/renovar/actualizar la fecha de devolucion de los libros que fueron prestados a los usuarios y tambien crear, actualizar o borrar autores de libros.

*-Usuarios*: Pueden logearse en el sitio y luego consultar una lista de los libros que tomo prestados, la fecha que debe devolverlos e informacion relativa a ello.

*-Visitante*: Puede navegar por la pagina, ver informacion sobre cantidad de libros disponibles y copias. Ver una lista de libros disponibles y acceder a detalles del mismo y su estado(ver mas en "Instancias de Libros"). Ver los autores que hay registrados y un listado de los libros de dicho autor.

Cada grupo en ese orden contiene los permisos del anterior. (En la seccion "URLs" se pueden ver en detalle, segun su permiso, los lugares que puede acceder cada uno)

## Libros

Los libros propiamente dichos contienen y muestran informacion sobre:
- Titulo
- Autor
- Resumen
- Generos

Cada libro tiene Instances o copias que son las que se pueden prestar, poner en mantenimiento, etc.

## Instancias de Libros

Las instancias o copias de libros se conforman de los mismos parametros que el Libro del cual son copia, con el agregado de:

- Lenguaje
- Editorial
- Un ID unico en formato UUIDv4

Y en caso de haber sido prestado: 
- Usuario que lo tiene en su haber
- Fecha de devolucion

Ademas tienen 4 estados para definir su situacion:
- "M" o "Maintenance"
- "O" o "On loan"
- "A" o "Available"
- "R" o "Reserved

## Autores

Los autores cuentan con:

- Nombre
- Apellido
- Fecha de nacimiento
- Fecha de fallecimiento ( en caso de haber fallecido )

## URLs

***-Permisos de Visitante:***

- Index- "/" o "/catalog"
- Books List- "/catalog/books"
- Author List- "/catalog/authors"

***-Permisos de Usuario:***

- My Borrowed Books- "/catalog/mybooks"

***-Permisos de Empleado/Bibliotecario:***

- All Borrowed Books- "/catalog/books_borrowed"
- Add new Book- "/catalog/book/create"
- Add new Author- "/catalog/author/create"



## Sobre mi

Ahora informacion sobre mi!

Mi nombre es Brian pero mayormente me conocen como "Pole", argentino de nacionalidad pero pertenezco a todo el mundo, creativo, innovador, curioso y ambicioso. Soy una persona apasionada en todo lo que hago, me gusta mucho resolver problemas y cuando me encuentro con uno, solo pienso en resolverlo. Me considero con gran capacidad de analisis, de rapido aprendizaje y trabajo en equipo sin que esto ultimo me impida llevar adelante tareas en solitario. Me gusta, ademas, liderar y organizar grupos y es lo que mayormente he hecho en el ambito laboral. Por ultimo, resaltar que prefiero hacer las cosas bien y (en lo posible) visualmente agradables.
