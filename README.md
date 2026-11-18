# EPTCD

EPTCD es un proyecto en Python para consultar el pronóstico meteorológico por
ubicación, organizar la información por hora en un `DataFrame` de pandas y
preparar notificaciones por correo electrónico y Twilio.

## Estado del proyecto

La implementación principal se encuentra en `EPTCD.ipynb`. El archivo
`EPTCD.py` contiene una versión de arranque incompleta y todavía no es el
equivalente ejecutable del cuaderno.

## Tecnologías utilizadas

| Tecnología | Uso |
|---|---|
| Python | Lenguaje principal |
| Jupyter Notebook | Desarrollo y ejecución interactiva |
| pandas | Construcción y consulta del pronóstico horario |
| Requests | Consumo de la API meteorológica |
| Beautiful Soup | Procesamiento HTML disponible como dependencia |
| tqdm | Barra de progreso |
| WeatherAPI | Datos meteorológicos por ubicación |
| Twilio | Integración prevista para SMS o WhatsApp |
| Gmail SMTP | Envío de reportes por correo |

## Requisitos

- Windows 10 u 11
- Python 3.10 o superior
- Acceso a Internet
- Cuenta de [WeatherAPI](https://www.weatherapi.com/)
- Cuenta de Gmail con contraseña de aplicación para correo
- Cuenta Twilio y número habilitado para mensajería

## Instalación en Windows

1. Abre una terminal en la carpeta raíz del proyecto.

```powershell
cd C:\Users\<usuario>\Desktop\EPTCD
```

2. Crea y activa un entorno virtual.

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Si PowerShell bloquea la activación:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

3. Instala las dependencias.

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m ipykernel install --user --name eptcd
```

4. Configura las variables de entorno.

```powershell
Copy-Item .env.example .env
```

Completa `.env` y PowerShell con tus propias credenciales:

```powershell
$env:WEATHERAPI_KEY = "tu_clave"
$env:GMAIL_ADDRESS = "tu_correo@gmail.com"
$env:GMAIL_APP_PASSWORD = "tu_contrasena_de_aplicacion"
$env:GMAIL_RECIPIENT = "destinatario@gmail.com"
$env:TWILIO_ACCOUNT_SID = "tu_sid"
$env:TWILIO_AUTH_TOKEN = "tu_token"
$env:TWILIO_PHONE_NUMBER = "+525500000000"
```

Nunca publiques claves, tokens o contraseñas en el repositorio.

> Seguridad: las credenciales antiguas almacenadas en `twilio_conf.py` deben
> considerarse expuestas y rotarse en WeatherAPI, Twilio y Gmail.

## Ejecución

Inicia Jupyter desde el entorno virtual:

```powershell
jupyter notebook
```

Abre `EPTCD.ipynb`, selecciona el kernel `eptcd` y ejecuta las celdas en
orden. Cambia la variable `query` para consultar otra ciudad.

## Flujo general

1. Se configura la ubicación mediante `query`.
2. Se solicita el pronóstico a WeatherAPI.
3. Se extrae fecha, hora, condición, temperatura, lluvia y probabilidad.
4. Los registros se convierten en un `DataFrame`.
5. Se prepara un mensaje con el pronóstico de lluvia.
6. Opcionalmente se envía por correo o mediante Twilio.

## Archivos principales

| Archivo | Descripción |
|---|---|
| `EPTCD.ipynb` | Cuaderno principal |
| `EPTCD.py` | Borrador de implementación en script |
| `twilio_conf.py` | Lectura segura de variables de entorno |
| `twilio_conf-Template.py` | Plantilla de configuración |
| `requirements.txt` | Dependencias instalables |
| `.env.example` | Ejemplo de variables de entorno |
| `HOJA_DEL_PROYECTO.md` | Hoja técnica y resumen ejecutivo |

## Solución de problemas

- `ModuleNotFoundError`: activa `.venv` y reinstala `requirements.txt`.
- Error de Gmail: usa una contraseña de aplicación, no la contraseña normal.
- Respuesta vacía: confirma la clave de WeatherAPI y la ubicación.
- Error de Twilio: valida SID, token y que el destinatario esté habilitado.

## Seguridad

- `.env` y `.venv` están excluidos por `.gitignore`.
- No guardes claves en cuadernos ni archivos compartidos.