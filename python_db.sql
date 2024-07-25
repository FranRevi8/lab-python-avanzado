drop database if exists python_db;
create database python_db;
use python_db;

create table videojuegos(
id INT auto_increment primary key,
titulo VARCHAR(100),
salida DATE,
descripcion VARCHAR(255)
);

INSERT INTO videojuegos (titulo, salida, descripcion) VALUES 
('The Legend of Zelda: Breath of the Wild', '2017-03-03', 'Un juego de aventura en un mundo abierto.'),
('Super Mario Odyssey', '2017-10-27', 'Un juego de plataformas en 3D con Mario explorando diferentes mundos.'),
('The Witcher 3: Wild Hunt', '2015-05-19', 'Un juego de rol de acción con una rica narrativa y un mundo abierto.'),
('Red Dead Redemption 2', '2018-10-26', 'Un juego de acción y aventura en un entorno de mundo abierto.'),
('Final Fantasy VII Remake', '2020-04-10', 'Una recreación moderna del clásico juego de rol con gráficos mejorados y nueva jugabilidad.');