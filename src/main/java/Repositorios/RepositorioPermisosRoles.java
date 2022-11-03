package Repositorios;

import org.springframework.data.mongodb.repository.MongoRepository;
import Modelos.PermisosRoles;


public interface RepositorioPermisosRoles extends MongoRepository<PermisosRoles,String> {
}