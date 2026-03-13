package transfer.mappers;

import data.entities.ModeloUsuario;
import transfer.dtos.UsuarioDTO;

public class UsuarioMapper {
    // Mapea entidades a DTO para ocultar el password
    public static UsuarioDTO toDTO(ModeloUsuario entity) {
        if (entity == null) return null;
        UsuarioDTO dto = new UsuarioDTO();
        dto.setName(entity.getName());
        dto.setEmail(entity.getEmail());
        return dto;
    }
}