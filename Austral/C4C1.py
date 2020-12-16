# -*- coding: utf-8 -*-

# Importación de librerias
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///:memory:')
Base = declarative_base()

# Contrucción de las Clases
class Curso(Base):
    __tablename__ = 'curso'

    id = Column(Integer, Sequence('curso_id_seq'), primary_key=True)
    name = Column(String)
    alumnos = relationship("Alumno", order_by="Alumno.id", back_populates="curso")
    horarios = relationship("Horario", order_by="Horario.id", back_populates="curso")

    def __repr__(self):
        return "{}".format(self.name)


class Alumno(Base):
    __tablename__ = 'alumno'

    id = Column(Integer, Sequence('book_id_seq'), primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    curso_id = Column(Integer, ForeignKey('curso.id'))
    curso = relationship("Curso", back_populates="alumnos")

    def __repr__(self):
        return "{} {}".format(self.firstname, self.lastname)


class Horario(Base):
    __tablename__ = 'horario'

    id = Column(Integer, Sequence('horario_id_seq'), primary_key=True)
    dia = Column(String)
    hora_inicio = Column(String)
    hora_termino = Column(String)
    curso_id = Column(Integer, ForeignKey('curso.id'))
    curso = relationship("Curso", back_populates="horarios")
    profesor_id = Column(Integer, ForeignKey('profesor.id'))
    profesor = relationship("Profesor", back_populates="horarios")

    def __repr__(self):
        return "{} de {} a {}".format(self.dia, self.hora_inicio, self.hora_termino)


class Profesor(Base):
    __tablename__ = 'profesor'

    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    horarios = relationship("Horario", back_populates="profesor")

    def __repr__(self):
        return "{} {}".format(self.firstname, self.lastname)

# Creando una Sesión
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


# Agregando los datos para los ejemplos de la aplicación
# Agregando los datos los Cursos
curso_a = Curso(name= 'Curso A')
curso_b = Curso(name= 'Curso B')

# Agregando los Profesores
profesor_javier = Profesor(id=1, firstname= 'Javier', lastname='Insotroza')
profesora_daniela = Profesor(id=2, firstname= 'Daniela', lastname='Toledo')

# Agregando los Alumnos
curso_a.alumnos = [Alumno(firstname='Juan',
                        lastname='Donoso'),
                  Alumno(firstname='Pedro',
                        lastname='Paramo'),
                  Alumno(firstname='Gabriel',
                        lastname='Soto'),
                  Alumno(firstname='Manuel',
                        lastname='Rodriguez')]

curso_b.alumnos = [Alumno(firstname='Ingrid',
                        lastname='Duarte'),
                  Alumno(firstname='Pedro',
                        lastname='Martinez'),
                  Alumno(firstname='Fernanda',
                        lastname='Rossetti'),
                  Alumno(firstname='Ismael',
                        lastname='Perez')]

# Agregando los Horarios
curso_a.horarios = [Horario(dia='Lunes',
                        hora_inicio='8:00',
                        hora_termino='10:00',
                        profesor_id =1),
                  Horario(dia='Lunes',
                        hora_inicio='10:30',
                        hora_termino='12:00',
                        profesor_id =2),
                  Horario(dia='Lunes',
                        hora_inicio ='14:00',
                        hora_termino ='17:30',
                        profesor_id =1)]

curso_b.horarios = [Horario(dia='Martes',
                        hora_inicio='8:00',
                        hora_termino='12:00',
                        profesor_id =1),
                  Horario(dia='Martes',
                        hora_inicio='14:00',
                        hora_termino='16:00',
                        profesor_id =2),
                  Horario(dia='Martes',
                        hora_inicio ='16:30',
                        hora_termino ='18:00',
                        profesor_id =1)]


session.add(curso_a)
session.add(curso_b)
session.add(profesor_javier)
session.add(profesora_daniela)
session.commit()


# Ejemplos de las exportaciones requeridas en el Proyecto
print('\nQuery #1 - Exporta los alumnos del Curso A')
for curso, alumno in session.query(Curso, Alumno).\
            filter(Curso.id==Alumno.curso_id).\
            filter(Curso.name=='Curso A').\
            all():
    print(alumno)


print('\nQuery #2 - Exporta los horarios del profesor Javier Inostroza')
for profesor, horario in session.query(Profesor, Horario).\
            filter(Profesor.id==Horario.profesor_id).\
            filter(Profesor.firstname=='Javier' and Profesor.firstname=='Insotroza').\
            all():
    print(horario)


print('\nQuery #3 - Exporta los horarios del Curso B')
for curso, horario in session.query(Curso, Horario).\
            filter(Curso.id==Horario.curso_id).\
            filter(Curso.name=='Curso B').\
            all():
    print(horario)
