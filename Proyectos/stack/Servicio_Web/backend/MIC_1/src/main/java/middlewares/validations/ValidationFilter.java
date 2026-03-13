package middleware;

import jakarta.servlet.*;
import jakarta.servlet.http.HttpServletRequest;
import java.io.IOException;

public class ValidationFilter implements Filter {
    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
            throws IOException, ServletException {

        HttpServletRequest req = (HttpServletRequest) request;

        // Validamos que si es un POST, el Content-Type sea JSON
        if ("POST".equalsIgnoreCase(req.getMethod())) {
            String contentType = req.getContentType();
            if (contentType == null || !contentType.contains("application/json")) {
                response.setContentType("application/json");
                response.getWriter().write("{\"error\": \"Cuerpo de petición debe ser JSON\"}");
                return;
            }
        }

        chain.doFilter(request, response);
    }
}