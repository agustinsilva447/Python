#importo todo lo necesario para crear la base
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey

engine=create_engine('sqlite:///:memory:')
Base=declarative_base(engine)

#defino los alumnos
class Educando(Base):
    __tablename__="alumno"

class Alumno(Base):
    __tablename__="alumno"   
    id=Column(Integer,Sequence('NÃºmero_de_InscripciÃ³n'),primary_key=True)
    nombrealumno=Column(String)
    apellidoalumno=Column(String)
    id_curso1=Column(Integer,ForeignKey('ID_curso_'))
    cursos=relationship("Materias",back_populates='escolares')

    asignatura=relationship("Materias",back_populates='escolares')
    def __repr__(self):
        return'{}'.format(self.nombrealumno)
        return'{}{}'.format(self.nombrealumno, self.apellidoalumno)

#defino los cursos
class Materias(Base):
    __tablename__='Los_Cursos'
    id=Column(Integer, Sequence('Curso_ID'),primary_key=True)
    nombredelcurso=Column(String)
    horadelcurso=Column(String)
    escolares=relationship("Educando",back_populates='cursos')

    escolares=relationship("Alumno",back_populates='asignatura')
    hora_del_curso=relationship("Horarios",back_populates='horacurso')
    def __repr__(self):
        return'{}'.format(self.nombredelcurso)

#defino los horarios
class Horarios(Base):
    __tablename__='horario'
    id=Column(Integer, Sequence('ID del Horario'),primary_key=True)
    dia=Column(String)
    horacomienza=Column(String)
    horatermina=Column(String)
    credencialprofesor=Column(Integer,ForeignKey('Credencial_Profesor'))
    IDcurso2=Column(Integer,ForeignKey('ID_curso'))

    maestros=relationship("Docente",back_populates='Materia_Asignada')
    horacurso=relationship("Materias",back_populates='hora_del_curso')
    curso_profesor=relationship("Docente",back_populates='Profesor_del_Curso')

    def __repr__(self):
        return'{}{}'.format(self.nombredelcurso,self.horario)
        return'{}{}{}'.format(self.dia,self.horacomienza, self.horatermina)

#defino los docentes
class Docente(Base):
    __tablename__='maestros'
    idpro=Column(Integer, Sequence('ID_del_Profesor'),primary_key=True)
    nombredelprofesor=Column(String)
    iddelcursoenprofesor=Column(Integer,ForeignKey('ID_del_Curso_Profesor'))
    apellidodelprofesor=Column(String)

    Materia_Asignada=relationship("Materias",back_populates='maestros')

    Profesor_del_Curso=relationship("Horarios",back_populates='curso_profesor')
    def __repr__(self):
        return'{}'.format(self.nombredelprofesor)
        return'{}{}'.format(self.nombredelprofesor, self.apellidodelprofesor)


Base.metadata.create_all(engine)

Session=sessionmaker(bind=engine)
session=Session()

#introduzco datos

alumno1=Educando(nombrealumno='Homero')
alumno1=Alumno(nombrealumno='Homero', apellidoalumno='Simpson')

session.add(alumno1)
alumno1.cursos=Materias(nombredelcurso='FÃ­sica Nuclear',horario='de 9 a 10')


profesor1=Docente(nombredelprofesor='Burns')
session.add(profesor1)
profesor1.Materia_Asignada=Materias(nombredelcurso='FÃ­sica Nuclear',horario='de 9 a 10')

alumno1.asignatura=Materias(nombredelcurso='Historia de la Cerveza')


horario1=Horario(dia='MiÃ©rcoles',horacomienza='9:00 am', horatermina='10:00 am')
session.add(horario1)
horario1.horacurso=Materias(nombredelcurso='FÃ­sica Nuclear')
horario1.curso_profesor=Docente(nombredelprofesor='Montgomery',apellidodelprofesor='Burns')


#imprimo para corroborar
print(alumno1)

print(alumno1.cursos)

print(profesor1.Materia_Asignada)
print(session.query(Materias).filter(Docente.Materia_Asignada.has()).all())
print(alumno1.asignatura)

print(horario1.curso_profesor)
print(session.query().filter(Docente.Profesor_del_Curso.any()).all())
print(session.query(Horarios).filter(Docente.Profesor_del_Curso.any()).all())

session.commit()

conn.close()
