# OJODEFURRO - Backend OCR para Extracción de Información de Dispositivos

## Descripción General
ODF es una aplicación backend basada en FastAPI diseñada para extraer información de dispositivos (como IMEIs y EIDs) a partir de capturas de pantalla de smartphones mediante Reconocimiento Óptico de Caracteres (OCR). Este proyecto utiliza librerías modernas de Python para procesar imágenes y proporcionar datos estructurados a través de una API RESTful.

## Características
- Extrae números IMEI y EID de capturas de pantalla de dispositivos Android.
- Utiliza EasyOCR para el reconocimiento de texto multilingüe (inglés y español).
- Incluye preprocesamiento de imágenes con OpenCV para mayor precisión.
- API simple y escalable construida con FastAPI.
- Soporte para almacenamiento local de modelos para evitar descargas en línea.

## Requisitos
- Python 3.10 o superior.
- pip y virtualenv para la gestión de dependencias.

## Instalación
1. Clona el repositorio:
   ```bash
   git clone https://github.com/yourusername/ODF.git
   cd ODF
   ```
2. Crea un entorno virtual y actívalo:
   - En Windows: `venv\Scripts\activate`
   - En macOS/Linux: `source venv/bin/activate`
3. Instala las dependencias requeridas:
   ```bash
   pip install fastapi uvicorn easyocr opencv-python python-multipart numpy<2
   ```

## Uso
1. Inicia el servidor:
   ```bash
   uvicorn main:app --reload
   ```
   - La API estará disponible en `http://127.0.0.1:8000`.
2. Prueba el endpoint usando una herramienta como Postman o curl:
   - Envía una solicitud POST a `http://127.0.0.1:8000/extract` con un archivo de captura de pantalla.
   - Ejemplo con curl:
     ```bash
     curl -X POST "http://127.0.0.1:8000/extract" -F "file=@captura.png"
     ```
   - Respuesta esperada: `{"imeis": ["358537796413234"], "eids": ["89033023423399010000021133062881"]}`.

## Configuración
- **Almacenamiento de Modelos**: Para evitar problemas de SSL durante la descarga de modelos, descarga manualmente los modelos de EasyOCR y configura el `model_storage_directory` en `main.py` (e.g., `reader = easyocr.Reader(['en', 'es'], model_storage_directory='./models')`).
- **Corrección de SSL**: Si encuentras errores de certificado, ejecuta `/Applications/Python\ 3.10/Install\ Certificates.command` en macOS o instala `certifi` con `pip install certifi --upgrade`.

## Endpoints de la API
- `POST /extract`: Sube una captura de pantalla para extraer información de IMEI y EID.
  - Solicitud: Datos de formulario multipart con un campo `file` que contiene la imagen.
  - Respuesta: Objeto JSON con arreglos `imeis` y `eids`.

## Agradecimientos
- Desarrollado con FastAPI, EasyOCR y OpenCV.
- Inspirado en la necesidad de automatizar la extracción de información de dispositivos.
