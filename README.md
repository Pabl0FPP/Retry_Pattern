# Implementación del Patrón Retry con Backoff Exponencial

Este repositorio contiene una implementación práctica del **patrón Retry con Backoff Exponencial** aplicada en un entorno de **microservicios desplegados en Azure App Service**.  
El objetivo fue demostrar cómo este patrón ayuda a mejorar la resiliencia frente a errores temporales en la comunicación entre servicios.

---

## 📌 Contexto

Este trabajo corresponde a la asignatura **Ingeniería de Software 5**, donde se estudian **patrones de nube**.  
Para este caso, implementamos el patrón **Retry** con una lógica de **Backoff Exponencial**.

---

## 🏗️ Arquitectura de la Implementación

Se desarrollaron **dos microservicios con Flask**:

1. **HelloService**  
   - Servicio simple que responde con un mensaje `Hello, World!`.
   - Puede simular errores temporales devolviendo códigos `500` para pruebas.

2. **ClientService**  
   - Consume la API del HelloService mediante peticiones HTTP.
   - Implementa el patrón **Retry con Backoff Exponencial** para manejar fallos temporales.
   - Reintenta la petición varias veces incrementando el tiempo de espera entre intentos (exponencialmente).

---

## 🚀 Despliegue

Ambos servicios fueron **desplegados en Azure** usando **Azure App Service**:

- HelloService → App Service 1  
- ClientService → App Service 2  

Esto permite que ambos servicios se comuniquen sobre HTTP en la nube.

---

## ⚙️ ¿Cómo funciona el patrón Retry con Backoff Exponencial?

- El **ClientService** envía una solicitud al **HelloService**.
- Si ocurre un error temporal (por ejemplo, el servicio responde con `500`), el cliente:
  1. Espera un tiempo (por ejemplo, 1 segundo).
  2. Reintenta la petición.
  3. Si vuelve a fallar, **duplica** el tiempo de espera (2s, 4s, 8s...).
- El proceso se repite hasta:
  - Obtener una respuesta exitosa (`200 OK`), o
  - Alcanzar el número máximo de intentos.

---

## ✅ Flujo de Prueba Realizada

Para probar la resiliencia:

1. Se simularon **fallos temporales** en el HelloService (dos respuestas con `500`).
2. El ClientService hizo la solicitud:
   - Primer intento: falla (500)
   - Segundo intento: falla (500)
   - Tercer intento: **éxito (200)** después de un backoff exponencial.
3. En la consola:
   - HelloService: muestra dos errores `500` y luego un `200`.
   - ClientService: muestra solo el resultado exitoso (`200`), gracias a los reintentos.

En el video de demostración se ve cómo el ClientService gestiona los errores y finalmente obtiene una respuesta correcta.

https://www.youtube.com/watch?v=yxjcJZmN7Xk


---

## 🛠️ Tecnologías Utilizadas

- **Python**
- **Flask**
- **Azure App Service**

