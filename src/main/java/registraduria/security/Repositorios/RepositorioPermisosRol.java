package registraduria.security.Repositorios;
import org.springframework.data.mongodb.repository.Query;
import registraduria.security.Modelos.PermisosRol;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface RepositorioPermisosRol extends MongoRepository<PermisosRol,String> {
    @Query("{'rol.$id': ObjectId(?0),'permiso.$id': ObjectId(?1)}")
    PermisosRol getPermisosRol(String id_rol,String id_permiso);
}