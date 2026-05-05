# 🚀 Pipeline ML Tabular - Detección de Malware Android

## Descripción

Pipeline completo en 2 notebooks para clasificación multiclase de aplicaciones Android en 5 categorías de malware usando características estáticas tabulares.

**Modalidad:** Análisis Estático Multimodal - Componente Tabular
**Dataset:** CIC-AndMal2020 (16,691 muestras × 400 características)
**Modelo:** Redes Neuronales Profundas (MLP) con regularización
**Métrica Principal:** Macro-F1 (balanceada para clases desiguales)

---

## 📋 Estructura

```
proyecto/
├── 01_eda_preprocessing.ipynb       # Exploración + Preprocesamiento (45 min)
├── 02_train_evaluate.ipynb          # Entrenamiento + Evaluación (45 min)
├── requirements.txt
├── README.md (este archivo)
│
├── data/
│   ├── raw/                         # Datos originales (no modificar)
│   │   └── Multimodal_CIC-MalDroid2020/Tabular/
│   └── processed/                   # Datos procesados (generado por notebook 1)
│
├── models/                          # Modelos entrenados y transformadores
│   ├── best_model_mlp.h5
│   ├── scaler.pkl
│   └── label_encoder.pkl
│
└── reports/                         # Salidas y visualizaciones
    ├── metrics_summary.csv
    ├── evaluation_report.txt
    ├── robustness_evaluation.csv
    └── *.png (gráficos)
```

---

## 🔧 Instalación

### Paso 1: Instalar dependencias

```bash
pip install -r requirements.txt
```

**Nota:** TensorFlow puede tomar tiempo en instalarse. Si tienes GPU CUDA, puedo optimizar la instalación.

### Paso 2: Crear carpetas necesarias

```bash
mkdir -p data/processed models reports
```

---

## 🏃 Ejecución

### **Notebook 1: 01_eda_preprocessing.ipynb**

**Duración:** ~45 minutos

**Qué hace:**
1. ✅ Carga datos train/test
2. ✅ EDA: Análisis univariado, correlaciones, sparsity
3. ✅ Visualiza separabilidad con PCA
4. ✅ Elimina features constantes y redundantes (400 → ~320)
5. ✅ Split estratificado: Train/Val/Test
6. ✅ Escalado con StandardScaler
7. ✅ Guarda datos procesados en `data/processed/`

**Output esperado:**
- `data/processed/X_train_scaled.npy`, `X_val_scaled.npy`, `X_test_scaled.npy`
- `data/processed/y_train_enc.npy`, `y_val_enc.npy`, `y_test_enc.npy`
- `data/processed/metadata.pkl`
- `models/scaler.pkl`, `models/label_encoder.pkl`
- Gráficos: `reports/01_correlation_matrix.png`, `reports/02_pca_analysis.png`

**Instrucciones:**
1. Abre el notebook en Jupyter
2. Ejecuta todas las celdas (Shift+Enter)
3. Espera a que termine

---

### **Notebook 2: 02_train_evaluate.ipynb**

**Duración:** ~45 minutos

**Qué hace:**
1. ✅ Carga datos procesados del notebook 1
2. ✅ Define 2 arquitecturas MLP
3. ✅ Entrena ambas con class_weight para balancear desbalance
4. ✅ Compara en validation set (selecciona mejor)
5. ✅ Evalúa en test con métricas detalladas
6. ✅ Calcula Feature Importance (Permutation)
7. ✅ Calcula SHAP values para interpretabilidad
8. ✅ Prueba robustez en datos adversarios y ofuscados
9. ✅ Genera reporte final

**Output esperado:**
- `models/best_model_mlp.h5` (modelo entrenado)
- `reports/metrics_summary.csv` (métricas principales)
- `reports/evaluation_report.txt` (reporte detallado)
- `reports/robustness_evaluation.csv` (robustez)
- Gráficos:
  - `reports/03_training_curves.png`
  - `reports/04_confusion_matrix.png`
  - `reports/05_feature_importance.png`
  - `reports/06_shap_importance.png`
  - `reports/07_robustness_comparison.png`

**Instrucciones:**
1. Asegúrate de que el Notebook 1 completó exitosamente
2. Abre este notebook
3. Ejecuta todas las celdas
4. Espera a que termine (incluye cálculo de SHAP que toma ~2-5 min)

---

## 📊 Resultados Esperados

### Métricas (Test Set)
- **Accuracy:** ~72-76%
- **Macro-F1:** ~72-78% ⭐ (métrica principal por desbalance)
- **Weighted-F1:** ~76-81%

### Distribución de Clases (Desbalance)
| Clase | Muestras | % | Ratio |
|-------|----------|---|-------|
| Adware | 450 | 9% | 1.0x |
| Banking | 720 | 14% | 1.6x |
| Benign | 1,209 | 24% | 2.7x |
| Riskware | 1,165 | 23% | 2.6x |
| SMS | 1,464 | 29% | 3.2x |

### Robustez
- **Test Original:** Macro-F1 = X.XXX
- **Data Adversario:** Macro-F1 = X.XXX (drop ~5-10%)
- **Data Ofuscado:** Macro-F1 = X.XXX (drop ~3-8%)

---

## 🎯 Claves del Diseño

### 1. Manejo del Desbalance
- **Class weights:** Balanceo automático en loss function
- **Estratificación:** En todos los splits
- **Métrica:** Macro-F1 (no accuracy)

### 2. Arquitectura MLP
```
V1: 400 → 256 → 128 → 64 → 5
V2: 400 → 512 → 256 → 128 → 5

Regularización: L2 + BatchNormalization + Dropout
Optimizador: Adam (lr=0.001 o 0.0008)
Loss: Sparse Categorical Crossentropy
```

### 3. Interpretabilidad
- **Permutation Importance:** Qué features impactan predicciones
- **SHAP:** Cómo cada feature contribuye a cada clase
- **Top 20 Features:** Identificadas para informe

### 4. Robustez
- Evaluación en datos adversarios (perturbaciones)
- Evaluación en datos ofuscados (código ofuscado)
- Comparativa de caída de performance

---

## 📝 Archivos Principales

| Archivo | Contenido |
|---------|-----------|
| `reports/metrics_summary.csv` | Accuracy, Macro-F1, Weighted-F1, Micro-F1 |
| `reports/evaluation_report.txt` | Reporte completo con métricas por clase |
| `reports/robustness_evaluation.csv` | Performance en adv/obfus |
| `models/best_model_mlp.h5` | Modelo serializado (cargable con Keras) |

---

## 🔍 Interpretación de Resultados

### Matriz de Confusión
- Diagonal principal: Clasificaciones correctas
- Fuera diagonal: Confusiones entre clases
- Vigilar especialmente **Adware** (clase minoritaria)

### Feature Importance
- Top features indican qué permisos/acciones son más discriminativos
- Útil para explicar al equipo de seguridad

### SHAP Values
- Cada gráfico muestra top features por clase
- Rojo = aumenta probabilidad, Azul = la disminuye
- Permite explicar decisiones individuales

---

## ⚡ Optimizaciones Disponibles

Si los notebooks son lentos:

1. **Reduce sample_size en SHAP** (línea ~200 notebook 2)
   - Cambiar `sample_size = min(300, len(X_test))` a `100`

2. **Reduce epochs**
   - Cambiar `epochs=100` a `epochs=50`

3. **Aumenta batch_size**
   - Cambiar `batch_size=32` a `batch_size=64`

4. **Usa GPU** (si disponible)
   ```bash
   pip install tensorflow[and-cuda]  # Con GPU
   ```

---

## 🐛 Troubleshooting

### Error: "No module named 'tensorflow'"
```bash
pip install tensorflow
```

### Error: "Shapes are incompatible"
- Verifica que el Notebook 1 completó exitosamente
- Verifica que `data/processed/` tiene todos los archivos .npy

### Error: "SHAP explainer failed"
- Esto puede ocurrir si hay valores infinitos o NaN
- Verifica `X_test_scaled` con `np.isfinite(X_test_scaled).all()`

### Notebook muy lento
- Usa los batch_size, epochs, sample_size recomendados arriba
- Reduce número de features manualmente (pero mantén top 200)

---

## 📚 Para el Informe Final

### Secciones Recomendadas

1. **Metodología**
   - Explicar preprocesamiento
   - Justificar arquitectura MLP vs otros modelos
   - Explicar manejo de desbalance

2. **Resultados**
   - Tabla: Métricas por clase
   - Figura: Matriz de confusión
   - Figura: Feature importance

3. **Análisis**
   - Top features por clase
   - Interpretación con SHAP
   - Robustez en adv/obfus

4. **Conclusiones**
   - Performance logrado
   - Limitaciones conocidas
   - Próximos pasos (fusión multimodal)

### Arquivos para Incluir
- `reports/04_confusion_matrix.png` (matriz)
- `reports/05_feature_importance.png` (importancia)
- `reports/06_shap_importance.png` (explicabilidad)
- `reports/evaluation_report.txt` (números exactos)

---

## 🎓 Notas Académicas

Este pipeline implementa:
- ✅ Manejo de desbalance con class weights
- ✅ Regularización L2 + Dropout + BatchNorm
- ✅ Validación estratificada
- ✅ Evaluación robusta (múltiples métricas)
- ✅ Interpretabilidad (Feature Importance + SHAP)
- ✅ Evaluación de robustez (adv/obfus)

Está diseñado para integrarse posteriormente con:
- Modalidad Visual (imágenes binarias)
- Modalidad Secuencial (grafos de APIs)
- Late Fusion para modelo multimodal final

---

## ✉️ Contacto / Dudas

Para preguntas sobre el pipeline:
1. Revisa los comentarios en los notebooks
2. Verifica los archivos de salida en `reports/`
3. Consulta el `evaluation_report.txt`

---

**Última actualización:** Mayo 2026  
**Versión:** 1.0
