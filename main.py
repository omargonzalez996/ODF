from fastapi import FastAPI, UploadFile, File, HTTPException
import easyocr
import cv2
import numpy as np
import re

app = FastAPI()

# Inicializa el lector de EasyOCR con inglés y español
reader = easyocr.Reader(['en', 'es'])

@app.post("/extract")
async def extract_info(imagen: UploadFile = File(...)):
    try:
        # Lee el contenido del archivo subido
        contents = await imagen.read()
        
        # Decodifica la imagen usando OpenCV
        nparr = np.frombuffer(contents, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # Preprocesamiento con OpenCV para mejorar el OCR
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convierte a escala de grises
        _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)  # Umbralización

        # Extrae texto con EasyOCR
        result = reader.readtext(thresh)
        text = ' '.join([res[1] for res in result])  # Une todo el texto extraído

        # Usa regex para encontrar IMEIs (15 dígitos)
        imeis = re.findall(r'\b\d{15}\b', text)
        # Usa regex para encontrar EIDs (32 dígitos empezando con 89)
        eids = re.findall(r'\b89\d{30}\b', text)

        # Devuelve los resultados en JSON
        return {"imeis": imeis, "eids": eids}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error procesando la imagen: {str(e)}")
    