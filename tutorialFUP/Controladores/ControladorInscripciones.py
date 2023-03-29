from tutorialFUP.Modelos.Inscripcion import Inscripcion
from tutorialFUP.Repositorios.RepositorioInscripcion import RepositorioInscripcion


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


   def index(self):
       print("Listar todos las Inscripciones")
       return self.repositorioInscripcion.findAll()

   def create(self, laInscripcion):
       print("Crear una inscripción")
       nuevaInscripcion = Inscripcion(laInscripcion)
       return self.repositorioInscripcion.save(nuevaInscripcion)


   def show(self, id):
       print("Mostrando una Inscripción con id ", id)
       laInscripcion = Inscripcion(self.repositorioInscripcion.findById(id))
       return laInscripcion.__dict__


   def update(self, id, laInscripcion):
       print("Actualizando Inscripción con id ", id)
       InscripcionActual = Inscripcion(self.repositorioInscripcion.findById(id))
       InscripcionActual.año = laInscripcion["año"]
       InscripcionActual.nota_final = laInscripcion["nota_final"]
       InscripcionActual.semestre = laInscripcion["semestre"]
       return self.repositorioInscripcion.save(InscripcionActual)


   def delete(self, id):
       print("Elimiando Inscripción con id ", id)
       return self.repositorioInscripcion.delete(id)