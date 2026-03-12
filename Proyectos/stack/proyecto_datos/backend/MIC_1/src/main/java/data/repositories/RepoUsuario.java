package data.repositories;

import config.DatabaseConfig;
import data.entities.ModeloUsuario;
import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class RepoUsuario {

    // CREATE
    public void guardar_usuario(ModeloUsuario user) throws SQLException {
        String sql = "INSERT INTO users (name, email, password) VALUES (?, ?, ?)";
        try (Connection conn = DatabaseConfig.getConnection();
             PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setString(1, user.getName());
            stmt.setString(2, user.getEmail());
            stmt.setString(3, user.getPassword());
            stmt.executeUpdate();
        }
    }

    // READ (Obtener todos)
    public List<ModeloUsuario> obtener_todos() throws SQLException {
        List<ModeloUsuario> usuarios = new ArrayList<>();
        String sql = "SELECT * FROM users";
        try (Connection conn = DatabaseConfig.getConnection();
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {
            while (rs.next()) {
                usuarios.add(new ModeloUsuario(
                        rs.getLong("id"),
                        rs.getName("name"),
                        rs.getString("email"),
                        rs.getString("password")
                ));
            }
        }
        return usuarios;
    }

    // UPDATE
    public void actualizar_usuario(ModeloUsuario user) throws SQLException {
        String sql = "UPDATE users SET name = ?, email = ? WHERE id = ?";
        try (Connection conn = DatabaseConfig.getConnection();
             PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setString(1, user.getName());
            stmt.setString(2, user.getEmail());
            stmt.setLong(3, user.getId());
            stmt.executeUpdate();
        }
    }

    // DELETE
    public void eliminar_usuario(Long id) throws SQLException {
        String sql = "DELETE FROM users WHERE id = ?";
        try (Connection conn = DatabaseConfig.getConnection();
             PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setLong(1, id);
            stmt.executeUpdate();
        }
    }
}