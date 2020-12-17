from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///:memory:')
Base = declarative_base()

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

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

curso_a = Curso(name= 'Física')
curso_b = Curso(name= 'Programación')
profesor_miguel = Profesor(id=1, firstname= 'Miguel', lastname='Arizmendi')
profesora_gustavo = Profesor(id=2, firstname= 'Gustavo', lastname='Zabaleta')
curso_a.alumnos = [Alumno(firstname='Agustin',
                        lastname='Silva'),
                  Alumno(firstname='Manuel',
                        lastname='Casadei'),
                  Alumno(firstname='Juan',
                        lastname='Iruit'),
                  Alumno(firstname='Exequiel',
                        lastname='Gelosi')]
curso_b.alumnos = [Alumno(firstname='Jorge',
                        lastname='Diorio'),
                  Alumno(firstname='Emanuel',
                        lastname='Calcagno'),
                  Alumno(firstname='Nicolas',
                        lastname='Martin'),
                  Alumno(firstname='Alejandro',
                        lastname='Weschler')]
curso_a.horarios = [Horario(dia='Lunes',
                        hora_inicio='10:00',
                        hora_termino='12:00',
                        profesor_id =1),
                  Horario(dia='Lunes',
                        hora_inicio='14:00',
                        hora_termino='16:00',
                        profesor_id =1),
                  Horario(dia='Lunes',
                        hora_inicio ='16:00',
                        hora_termino ='18:00',
                        profesor_id =1)]
curso_b.horarios = [Horario(dia='Martes',
                        hora_inicio='10:00',
                        hora_termino='12:00',
                        profesor_id =2),
                  Horario(dia='Martes',
                        hora_inicio='14:00',
                        hora_termino='16:00',
                        profesor_id =2),
                  Horario(dia='Martes',
                        hora_inicio ='16:00',
                        hora_termino ='18:00',
                        profesor_id =2)]

session.add(curso_a)
session.add(curso_b)
session.add(profesor_miguel)
session.add(profesora_gustavo)
session.commit()

print('1: Exporta los alumnos de Física')
for curso, alumno in session.query(Curso, Alumno).\
            filter(Curso.id==Alumno.curso_id).\
            filter(Curso.name=='Física').\
            all():
    print(alumno,"\n")

print('2: Exporta los horarios del profesor Gustavo Zabaleta')
for profesor, horario in session.query(Profesor, Horario).\
            filter(Profesor.id==Horario.profesor_id).\
            filter(Profesor.firstname=='Miguel').\
            all():
    print(horario,"\n")

print('3: Exporta los horarios de Programación')
for curso, horario in session.query(Curso, Horario).\
            filter(Curso.id==Horario.curso_id).\
            filter(Curso.name=='Programación').\
            all():
    print(horario,"\n")