
DROP TABLE IF EXISTS proyectos;
CREATE TABLE proyectos(
    id serial,
    nombre varchar(35), 
    rut_contratista varchar(10), 
    contratista varchar(70), 
    PRIMARY KEY(id)
);

DROP TABLE IF EXISTS grupos;
CREATE TABLE grupos(
    id serial,
    codigo_proyecto int, 
    nombre varchar(20), 
    PRIMARY KEY(id), 
    CONSTRAINT fk_proyecto 
        FOREIGN KEY(codigo_proyecto) 
            REFERENCES proyectos(id)
);

DROP TABLE IF EXISTS problemas;
CREATE TABLE problemas(
    id serial,
    titulo varchar(50),
    dificultad numeric(1), 
    enunciado text,
    grupo_id int, 
    PRIMARY KEY(id), 
    CONSTRAINT fk_grupo 
        FOREIGN KEY(grupo_id) 
            REFERENCES grupos(id) 
);


DROP TABLE IF EXISTS desarrolladores;
CREATE TABLE desarrolladores(
    id serial,
    nombres varchar(35), 
    apellidos varchar(35), 
    correo varchar(255), 
    contraseña varchar(255), 
    PRIMARY KEY(id)
);


DROP TABLE IF EXISTS miembros_grupo;
CREATE TABLE miembros_grupo(
    id serial,
    usuario_id int,
    grupo_id int, 
    PRIMARY KEY(id), 
    CONSTRAINT fk_grupo_member 
        FOREIGN KEY(grupo_id) 
            REFERENCES grupos(id) ,
    CONSTRAINT fk_dev_member 
    FOREIGN KEY(usuario_id) 
        REFERENCES desarrolladores(id) 
);

