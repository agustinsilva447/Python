# Sistema de escuelas por DawffyddRiv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine ( 'sqlite3:///:memory:' )
Base = declarative_base ( engine )


class Estudiante ( Base ):
    __tablename__ = "alumno"
    id = Column ( Integer, Sequence ( 'alumno_seq_id' ), primary_key=True )
    nombre1 = Column ( String )
    apellido1 = Column ( String )
    curso_id1 = Column ( Integer, ForeignKey ( 'curso.id' ) )

    cursos = relationship ( "Course", back_populates='estudiantes' )

    def __repr__(self):
        return '{}{}'.format ( self.nombrea, self.apellidoa )


class Course ( Base ):
    __tablename__ = 'curso'
    id = Column ( Integer, Sequence ( 'curso_seq_id' ), primary_key=True )
    nombre3 = Column ( String )

    estudiantes = relationship ( "Estudiante", back_populates='cursos' )
    hora_curso = relationship ( "Crono", back_populates='curso_hora' )

    def __repr__(self):
        return '{}'.format ( self.nombrec )


class Crono ( Base ):
    __tablename__ = 'horario'
    id = Column ( Integer, Sequence ( 'horario_seq_id' ), primary_key=True )
    dia = Column ( String )
    hora_inicio = Column ( String )
    hora_fin = Column ( String )
    profesor_id = Column ( Integer, ForeignKey ( 'profesor.id' ) )
    curso_id = Column ( Integer, ForeignKey ( 'curso.id' ) )

    curso_hora = relationship ( "Course", back_populates='hora_curso' )
    curso_profe = relationship ( "Maestro", back_populates='profe_curso' )

    def __repr__(self):
        return '{}{}{}'.format ( self.dia, self.hora_inicio, self.hora_fin )


class Maestro ( Base ):
    __tablename__ = 'profesor'
    id = Column ( Integer, Sequence ( 'profesor_seq_id' ), primary_key=True )
    nombrep = Column ( String )
    apellidop = Column ( String )

    profe_curso = relationship ( "Crono", back_populates='curso_profe' )

    def __repr__(self):
        return '{}{}'.format ( self.nombrep, self.apellidop )


Base.metadata.create_all ( engine )

Session = sessionmaker ( bind=engine )
session = Session ()

alumno1 = Estudiante ( nombrea='Panchito', apellidoa='  Gonzalez' )
print ( alumno1 )
session.add ( alumno1 )
alumno1.cursos = Course ( nombrec='Fisica' )
print ( alumno1.cursos )

horario1 = Crono ( dia='lunes', hora_inicio="7:00 am", hora_fin='8:00' )
session.add ( horario1 )
horario1.curso_hora = Course ( nombrec='Quimica' )
horario1.curso_profe = Maestro ( nombrep='Vicente', apellidop='  Huidobro' )

print ( horario1.curso_profe )
print ( session.query ( Course ).filter ( Maestro.profe_curso.any () ).all () )
print ( session.query ( Crono ).filter ( Maestro.profe_curso.any () ).all () )

session.commit ()
