# ALIM-DEFENSE v0.1

**Motor Automatizado de Detección y Análisis de Tráfico**

---

## 🔹 Propósito

ALIM-DEFENSE es un **pipeline automatizado** para la detección y análisis de tráfico en aplicaciones defensivas.  
Genera datasets sintéticos, entrena modelos, exporta a ONNX y crea módulos C++ listos para integración en tu app.

Este proyecto está pensado para ser **privado** y seguro, con trazabilidad y reproducibilidad en mente.

---

## 🔹 Características MVP v0.1

- Generación de **dataset sintético** de tráfico (`ml/train_pipeline.py`).  
- **Feature extractor automatizado** (`generate_features.py`).  
- Entrenamiento de modelo **LightGBM** como baseline.  
- Exportación a **ONNX** para inferencia rápida en C++.  
- Guardado automático de **metadata y métricas** (`metadata.json`).  
- Pipeline reproducible con un solo comando:
  ```bash
  python ml/train_pipeline.py
