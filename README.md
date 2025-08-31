# Retry_Pattern
Implementación del patrón Retry con Backoff Exponencial en un escenario de microservicios desplegados en Azure App Service.   Incluye dos servicios construidos con Flask:   - HelloService: Responde con un mensaje simple.   - ClientService: Consume HelloService y aplica la lógica de reintentos con backoff exponencial para manejar fallos temporales. 
