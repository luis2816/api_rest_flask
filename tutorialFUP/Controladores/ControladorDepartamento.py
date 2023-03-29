from tutorialFUP.Modelos.Departamento import Departamento
from tutorialFUP.Repositorios.RepositorioDepartamento import RepositorioDepartamento

"""
Dentro de la clase se crean unos metodos, estos serán los encargados de manipular
a los modelos, en estos se programarán las tareas básicas tales como crear, listar,
visualizar, modificar y eliminar. (CRUD)
"""


class ControladorDepartamento():
   """
   constructor que permite llevar a cabo la creacion de instancias del controlador.
   """
   def __init__(self):
       self.repositorioDepartamento = RepositorioDepartamento()
       print("Creando ControladorDepartamento")


   def index(self):
       print("Listar todos los Departamentos")
       return self.repositorioDepartamento.findAll()

   def create(self, elDepartamento):
       print("Crear un Departamento")
       nuevoDepartamento = Departamento(elDepartamento)
       return self.repositorioDepartamento.save(nuevoDepartamento)

   def show(self, id):
       elDepartamento = Departamento(self.repositorioDepartamento.findById(id))
       return elDepartamento.__dict__

   def update(self, id, elDepartamento):
       departamentoActual = Departamento(self.repositorioDepartamento.findById(id))
       departamentoActual.nombre = elDepartamento["nombre"]
       return self.repositorioDepartamento.save(departamentoActual)

   def delete(self, id):
       print("Elimiando departamento con id ", id)
       return self.repositorioDepartamento.delete(id)

