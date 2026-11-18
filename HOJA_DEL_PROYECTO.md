# Hoja del proyecto EPTCD

## Identificación

| Campo | Información |
|---|---|
| Nombre | EPTCD |
| Tipo | Automatización meteorológica |
| Propósito | Consultar pronóstico, estructurar datos y preparar avisos |
| Ubicación principal | `EPTCD.ipynb` |
| Ejecución recomendada | Jupyter Notebook en Windows |

## Objetivo

Obtener el pronóstico de una ciudad, convertirlo en una tabla legible y enviar
un resumen por correo o por un servicio de mensajería.

## Alcance

### Incluido

- Consulta de pronóstico diario y horario.
- Extracción de datos relevantes.
- Conversión de datos JSON a `DataFrame`.
- Preparación de mensaje de lluvia.
- Integración configurable con Gmail SMTP y Twilio.

### Pendiente o por validar

- Ejecutar automáticamente el flujo desde `EPTCD.py`.
- Crear una interfaz gráfica o aplicación web.
- Guardar históricos en base de datos.
- Programar ejecuciones periódicas.
- Completar notificaciones por SMS o WhatsApp.

## Arquitectura funcional

```text
Usuario
  -> Jupyter Notebook
  -> WeatherAPI
  -> Respuesta JSON
  -> pandas DataFrame
  -> Mensaje de pronóstico
  -> Gmail SMTP / Twilio
```

## Tecnologías

| Tecnología | Categoría | Propósito |
|---|---|---|
| Python 3 | Lenguaje | Lógica del proyecto |
| Jupyter Notebook | Entorno interactivo | Ejecución y análisis |
| pandas | Procesamiento de datos | Tabla de pronóstico |
| Requests | Cliente HTTP | Peticiones a APIs |
| Beautiful Soup | Parsing | Procesamiento HTML futuro |
| tqdm | Interfaz de consola | Progreso de recorridos |
| WeatherAPI | API externa | Datos meteorológicos |
| SMTP de Gmail | Servicio de correo | Entrega de reportes |
| Twilio | Servicio de mensajería | SMS o WhatsApp futuro |

## Datos procesados

- Fecha
- Hora
- Condición meteorológica
- Temperatura
- Indicador de lluvia
- Probabilidad de lluvia

## Instalación rápida

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env
jupyter notebook
```

Después, configura las variables necesarias en `.env` y abre `EPTCD.ipynb`.

## Variables de entorno

| Variable | Servicio |
|---|---|
| `WEATHERAPI_KEY` | WeatherAPI |
| `GMAIL_ADDRESS` | Gmail remitente |
| `GMAIL_APP_PASSWORD` | Contraseña de aplicación de Gmail |
| `GMAIL_RECIPIENT` | Destinatario del correo |
| `TWILIO_ACCOUNT_SID` | Cuenta Twilio |
| `TWILIO_AUTH_TOKEN` | Autenticación Twilio |
| `TWILIO_PHONE_NUMBER` | Número remitente |

## Pruebas manuales mínimas

1. Ejecutar la consulta y comprobar que devuelve datos.
2. Verificar que el `DataFrame` contiene fecha, hora y condición.
3. Confirmar que el mensaje incluye ubicación y pronóstico.
4. Realizar una prueba de correo con una cuenta propia.
5. Realizar una prueba de Twilio después de configurar la cuenta.

## Riesgos

- Las API externas pueden cambiar sus respuestas o límites.
- Las credenciales deben mantenerse fuera del control de versiones.
- Los pronósticos pueden variar según la ubicación y el proveedor.
- El correo requiere acceso SMTP habilitado y contraseña de aplicación.
- `EPTCD.py` no está terminado y no debe considerarse una aplicación final.
