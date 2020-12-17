#Sistema para una escuela
#Este sistema permite registrar nuevos alumnos, profesores y cursos.
#Un alumno es asignado a un curso y un curso puede tener asociado más de un profesor. Los profesores tienen un horario que indica cuando están en cada curso.
#El horario asociará un curso y un profesor para un día de la semana (Lunes, Martes, Miércoles, Jueves, Viernes, Sábado, Domingo), una hora desde y una hora hasta.
#El sistema permitirá exportar los alumnos que pertenecen a un curso, el horario de cada profesor y el horario del curso.

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

engine=create_engine('sqlite:///:memory:')
Base=declarative_base(engine)

class Alumnos(Base):
    __tablename__='alumno'  
    id=Column(Integer,Sequence('seq_alumno'),primary_key=True)
    nombre=Column(String)
    apellido=Column(String)
    id_curso=Column(Integer,ForeignKey('curso.id'))
    
    cursos=relationship("Cursos",back_populates='alumnos')
    def __repr__(self):
        return'{}{}'.format(self.nombre, self.apellido)

class Cursos(Base):
    __tablename__='curso'
    id=Column(Integer, Sequence('seq_curso'),primary_key=True)
    nombre_curso=Column(String)
        
    alumnos=relationship("Alumnos",back_populates='cursos')
    horario_curso=relationship("Horarios",back_populates='curso_horario')
    def __repr__(self):
        return'{}'.format(self.nombre_curso)

class Horarios(Base):
    __tablename__='horario'
    id=Column(Integer, Sequence('seq_horario'),primary_key=True)
    dia=Column(String)
    hora_inicio=Column(String)
    hora_fin=Column(String)
    id_profesor=Column(Integer,ForeignKey('profesor.id'))
    id_curso=Column(Integer,ForeignKey('curso.id'))
    
    curso_horario=relationship("Cursos",back_populates='horario_curso')
    curso_profesor=relationship("Profesores",back_populates='profesor_curso')

    def __repr__(self):
        return'{}{}{}'.format(self.dia,self.hora_inicio, self.hora_fin)

class Profesores(Base):
    __tablename__='profesor'
    id=Column(Integer, Sequence('seq_profesor'),primary_key=True)
    nombre=Column(String)
    apellido=Column(String)
    
    profesor_curso=relationship("Horarios",back_populates='curso_profesor')
    def __repr__(self):
        return'{}{}'.format(self.nombre, self.apellido)


Base.metadata.create_all(engine)

Session=sessionmaker(bind=engine)
session=Session()


session.commit()