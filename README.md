# 🧠 Proyecto Machine Learning - Alineación de Audio y Transcripción (Parte 1)

Este proyecto implementa un sistema de inteligencia artificial para alinear automáticamente la transcripción de audios en español con los segmentos de habla (IPUs), utilizando reconocimiento de voz, detección de voz y análisis fonético. Forma parte de la Fase 1 de un proyecto académico de la materia Machine Learning.

---

## 📌 Objetivos

### 🎯 Objetivo general
Evaluar y alinear automáticamente la transcripción de audios con los segmentos de habla y pausa, usando etiquetas del ASR (Automatic Speech Recognition) y VAD (Voice Activity Detection).

### 🧪 Fase 1a – Objetivos específicos
1. **Detectar IPUs (unidad prosódica intermedia)** mediante WebRTC VAD.
2. **Transcribir el texto por IPU** con Whisper (ASR).
3. **Comparar fonéticamente** las transcripciones usando `espeak-ng`.
4. **Visualizar resultados** en Praat mediante archivos `.TextGrid`.

---

## 🛠️ Tecnologías utilizadas

| Herramienta       | Descripción                              |
|-------------------|------------------------------------------|
| **Python 3.11**   | Lenguaje principal                       |
| **Whisper (OpenAI)** | Transcripción de voz a texto           |
| **WebRTC VAD**    | Detección de actividad vocal             |
| **espeak-ng**     | Conversión de texto a fonemas            |
| **praatio**       | Manipulación de archivos `.TextGrid`     |
| **Regex**         | Procesamiento de HTML                    |
| **FFmpeg**        | Conversión y recorte de audios           |
| **Praat**         | Visualización lingüística de TextGrid    |

---

## 🔧 Funcionalidades del Proyecto

✅ Conversión de audios `.mp3` a `.wav` (16kHz mono)  
✅ Transcripción automática usando Whisper  
✅ Detección de segmentos de habla con WebRTC VAD  
✅ Alineación de texto con segmentos de voz (IPUs)  
✅ Comparación fonética de segmentos con `espeak-ng`  
✅ Exportación a formatos `.TextGrid`, `.html`, y `.txt`  

---


## Verificación

✅ Visualización completa en Praat

