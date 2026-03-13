package logica.interfaces;

import data.entities.ModeloUsuario;
import java.sql.SQLException;
import java.util.List;

public interface IUsuarioRepositorio {
    void guardar(ModeloUsuario usuario) throws SQLException;
    List<ModeloUsuario> obtenerTodos() throws SQLException;
    // Aqui definimos toda las funciones abstractas que vamos a utilizar
}