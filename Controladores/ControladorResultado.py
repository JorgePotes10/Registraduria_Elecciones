from Repositorios.RepositorioResultado import RepositorioResultado
from Repositorios.RepositorioCandidato import RepositorioCandidato
from Repositorios.RepositorioMesa import RepositorioMesa

from Modelos.Resultado import Resultado
from Modelos.Candidato import Candidato
from Modelos.Mesa import Mesa

class ControladorResultado():
    def __init__(self):
        self.repositorioResultado = RepositorioResultado()
        self.repositorioCandidato = RepositorioCandidato()
        self.repositorioMesa = RepositorioMesa()
    def index(self):
        return self.repositorioResultado.findAll()
    def create(self,infoResultado,id_candidato,id_mesa):
        elResultado=Resultado(infoResultado)
        elCandidato=Candidato(self.repositorioCandidato.findById(id_candidato))
        laMesa=Mesa(self.repositorioMesa.findById(id_mesa))
        elResultado.candidato=elCandidato
        elResultado.mesa=laMesa
        return self.repositorioResultado.save(elResultado)
    def show(self,id):
        elResultado=Resultado(self.repositorioResultado.findById(id))
        return elResultado.__dict__
    def update(self,id,infoResultado,id_candidato,id_mesa):
        elResultado=Resultado(self.repositorioResultado.findById(id))
        elResultado.numero_mesa= infoResultado["numero_mesa"]
        elResultado.id_partido = infoResultado["id_partido"]
        elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        laMesa = Mesa(self.repositorioMesa.findById(id_mesa))
        elResultado.candidato = elCandidato
        elResultado.mesa = laMesa
        return self.repositorioResultado.save(elResultado)
    def delete(self,id):
        return self.repositorioResultado.delete(id)