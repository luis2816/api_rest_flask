from tutorialFUP.Modelos.Materia import Materia
from tutorialFUP.Modelos.Departamento import Departamento
from tutorialFUP.Repositorios.RepositorioDepartamento import RepositorioDepartamento
from tutorialFUP.Repositorios.RepositorioMateria import RepositorioMateria

"""
Dentro de la clase se crean unos metodos, estos serán los encargados de manipular
a los modelos, en estos se programarán las tareas básicas tales como crear, listar,
visualizar, modificar y eliminar. (CRUD)
"""


class ControladorMateria():
    """
   constructor que permite llevar a cabo la creacion de instancias del controlador.
   """

    def __init__(self):
        self.repositorioMateria = RepositorioMateria();
        self.repositorioDepartamento = RepositorioDepartamento();
        print("Creando ControladorMateria")

    def index(self):
        print("Listar todas las Materias")
        return self.repositorioMateria.findAll()

    def create(self, laMateria):
        print("Crear una Materia")
        nuevaMateria = Materia(laMateria)
        return self.repositorioMateria.save(nuevaMateria)

    def show(self, id):
        print("Mostrando la Materia con id ", id)
        laMateria = Materia(self.repositorioMateria.findById(id))
        return laMateria.__dict__

    def update(self, id, laMateria):
        print("Actualizando materia con id ", id)
        materiaActual = Materia(self.repositorioMateria.findById(id))
        materiaActual.creditos = laMateria["creditos"]
        materiaActual.nombre = laMateria["nombre"]
        return self.repositorioMateria.save(materiaActual)

    def delete(self, id):
        print("Elimiando materia con id ", id)
        return self.repositorioMateria.delete(id)

    def asignarDepartamento(self, id, id_departamento):
        materiaActual = Materia(self.repositorioMateria.findById(id))
        departamentoActual = Departamento(self.repositorioDepartamento.findById(id_departamento))
        materiaActual.departamento = departamentoActual
        return self.repositorioMateria.save(materiaActual)
