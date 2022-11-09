package registraduria.security.Controladores;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;
import registraduria.security.Modelos.Permiso;
import registraduria.security.Modelos.PermisosRol;
import registraduria.security.Modelos.Rol;
import registraduria.security.Repositorios.RepositorioPermiso;
import registraduria.security.Repositorios.RepositorioPermisosRol;
import registraduria.security.Repositorios.RepositorioRol;
import java.util.List;

@CrossOrigin
@RestController
@RequestMapping("/permisos-rol")
public class ControladorPermisosRol{
    @Autowired
    private RepositorioPermisosRol miRepositorioPermisoRol;
    @Autowired
    private RepositorioPermiso miRepositorioPermiso;
    @Autowired
    private RepositorioRol miRepositorioRol;
    @GetMapping("")
    public List<PermisosRol> index(){
        return this.miRepositorioPermisoRol.findAll();
    }
    /**

     * Asignación rol y permiso
     * @param id_rol
     * @param id_permiso
     * @return
     */
    @ResponseStatus(HttpStatus.CREATED)
    @PostMapping("rol/{id_rol}/permiso/{id_permiso}")
    public PermisosRol create(@PathVariable String id_rol,@PathVariable
    String id_permiso){
        PermisosRol nuevo=new PermisosRol();
        Rol elRol=this.miRepositorioRol.findById(id_rol).get();
        Permiso
                elPermiso=this.miRepositorioPermiso.findById(id_permiso).get();
        if (elRol!=null && elPermiso!=null){
            nuevo.setPermiso(elPermiso);
            nuevo.setRol(elRol);
            return this.miRepositorioPermisoRol.save(nuevo);
        }else{
            return null;
        }
    }
    @GetMapping("{id}")
    public PermisosRol show(@PathVariable String id){
        PermisosRol permisosRolActual=this.miRepositorioPermisoRol
                .findById(id)
                .orElse(null);
        return permisosRolActual;
    }
    /**
     * Modificación Rol y Permiso
     * @param id
     * @param id_rol
     * @param id_permiso
     * @return
     */
    @PutMapping("{id}/rol/{id_rol}/permiso/{id_permiso}")
    public PermisosRol update(@PathVariable String id,@PathVariable
    String id_rol,@PathVariable String id_permiso){
        PermisosRol permisosRolActual=this.miRepositorioPermisoRol
                .findById(id)
                .orElse(null);
        Rol elRol=this.miRepositorioRol.findById(id_rol).get();
        Permiso
                elPermiso=this.miRepositorioPermiso.findById(id_permiso).get();
        if(permisosRolActual!=null && elPermiso!=null && elRol!=null){
            permisosRolActual.setPermiso(elPermiso);
            permisosRolActual.setRol(elRol);
            return
                    this.miRepositorioPermisoRol.save(permisosRolActual);
        }else{
            return null;
        }
    }
    @ResponseStatus(HttpStatus.NO_CONTENT)
    @DeleteMapping("{id}")
    public void delete(@PathVariable String id){
        PermisosRol permisosRolActual=this.miRepositorioPermisoRol
                .findById(id)
                .orElse(null);
        if (permisosRolActual!=null){
            this.miRepositorioPermisoRol.delete(permisosRolActual);
        }
    }

    @GetMapping("validar-permiso/rol/{id_rol}")
    public PermisosRol getPermisos(@PathVariable String id_rol,@RequestBody Permiso infoPermiso){
        Permiso elPermiso=this.miRepositorioPermiso
                .getPermiso(infoPermiso.getUrl(),
                        infoPermiso.getMetodo());
        Rol elRol=this.miRepositorioRol.findById(id_rol).get();
        if (elPermiso!=null && elRol!=null){
            return this.miRepositorioPermisoRol.getPermisosRol(elRol.get_id(),elPermiso.get_id());
        }else{
            return null;
        }
    }
}