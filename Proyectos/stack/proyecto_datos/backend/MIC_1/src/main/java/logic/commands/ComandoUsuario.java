package logica.comandos;

import data.entities.ModeloUsuario;
import data.repositories.RepoUsuario;
import transfer.dtos.UsuarioDTO;
import transfer.mappers.UsuarioMapper;
import logica.interfaces.IComando;
import java.sql.SQLException;

public class ComandoUsuario {
    private final RepoUsuario repoUsuario = new RepoUsuario();

    // Lógica para crear un usuario
    public void crearUsuario(ModeloUsuario usuario) throws Exception {
        // Aquí podrías validar si el email ya existe antes de guardar
        repoUsuario.guardar_usuario(usuario);
    }

    // Lógica para obtener un DTO (Transformación)
    public UsuarioDTO obtenerUsuarioParaVista(ModeloUsuario entidad) {
        // Siguiendo tu diagrama: Transformar entidad en DTO [cite: 20]
        return UsuarioMapper.toDTO(entidad);
    }
}