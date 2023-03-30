from tutorialFUP.Modelos.Inscripcion import Inscripcion
from tutorialFUP.Modelos.Estudiante import Estudiante
from  tutorialFUP.Modelos.Materia import Materia

from tutorialFUP.Repositorios.RepositorioInscripcion import RepositorioInscripcion
from tutorialFUP.Repositorios.RepositorioEstudiante import RepositorioEstudiante
from tutorialFUP.Repositorios.RepositorioMateria import RepositorioMateria


"""
Dentro de la clase se crean unos metodos, estos serán los encargados de manipular
a los modelos, en estos se programarán las tareas básicas tales como crear, listar,
visualizar, modificar y eliminar. (CRUD)
"""

class ControladorInscripcion():
   """
   constructor que permite llevar a cabo la creacion de instancias del controlador.
   """
   def __init__(self):
       print("Creando ControladorInscripcion")
       self.repositorioInscripcion = RepositorioInscripcion();
       self.repositorioEstudiante = RepositorioEstudiante();
       self.repositorioMateria = RepositorioMateria();



   def index(self):
       print("Listar todos las Inscripciones")
       return self.repositorioInscripcion.findAll()

   def create(self, infoInscripcion, id_estudiante , id_materia):
       print("Crear una inscripción")

       nuevaInscripcion = Inscripcion(infoInscripcion)
       elEstudiante = Estudiante(self.repositorioEstudiante.findById(id_estudiante))
       laMateria = Materia(self.repositorioMateria.findById(id_materia))
       nuevaInscripcion.estudiante = elEstudiante
       nuevaInscripcion.materia= laMateria
       return self.repositorioInscripcion.save(nuevaInscripcion)


   def show(self, id):
       print("Mostrando una Inscripción con id ", id)
       laInscripcion = Inscripcion(self.repositorioInscripcion.findById(id))
       return laInscripcion.__dict__


   def update(self, id, infoInscripcion, id_estudiante , id_materia):
       print("Actualizando Inscripción con id ", id)
       InscripcionActual = Inscripcion(self.repositorioInscripcion.findById(id))
       InscripcionActual.anio = infoInscripcion["año"]
       InscripcionActual.nota_final = infoInscripcion["nota_final"]
       InscripcionActual.semestre = infoInscripcion["semestre"]
       elEstudiante= Estudiante(self.repositorioEstudiante.findById(id_estudiante))
       laMateria= Materia(self.repositorioMateria.findById(id_materia))
       InscripcionActual.estudiante= elEstudiante
       InscripcionActual.materia= laMateria
       return self.repositorioInscripcion.save(InscripcionActual)


   def delete(self, id):
       print("Elimiando Inscripción con id ", id)
       return self.repositorioInscripcion.delete(id)