Metodologgía:

Ante este escenario, el presente proyecto propone el desarrollo de un sistema de clasificación de aplicaciones  
Android basado en análisis estático multimodal. A diferencia del análisis dinámico, este enfoque permite inspeccionar las propiedades del software sin necesidad de ejecutarlo, eliminando el riesgo de infección durante el proceso.  
El objetivo principal es la categorización de las aplicaciones en cinco clases:  
• Adware: Material publicitario oculto en aplicaciones  
infectadas que ejecuta procesos persistentes de despliegue de anuncios y robo de información.  
• Banking: Troyanos que imitan interfaces bancarias  
para capturar credenciales y enviarlas a servidores de  
Comando y Control (C\&C).  
• SMS Malware: Explotación del servicio de mensajería  
para interceptar contenidos y coordinar ataques mediante servidores C\&C.  
• Riskware: Programas legítimos explotables que  
pueden escalar a otras formas de malware mediante  
la instalación de nuevos componentes infectados.  
• Benign: Aplicaciones validadas (vía VirusTotal) que  
no presentan comportamientos maliciosos.  
La motivación técnica del enfoque multimodal radica en  
que una sola fuente de información puede llegar a ser insuficiente para capturar la complejidad del malware actual.  
Por ello, el modelo integrará datos tabulares, imagenes  
provenientes del binario del archivos ejecutable de la aplicación y secuencias API

Estado del arte:

Multimodal Deep Learning for Android Malware Classification. Arrowsmith et al. \[2025\] El trabajo “Multimodal Deep Learning for Android Malware Classification” propone un enfoque multimodal que combina dos representaciones estáticas extraídas de los archivos DEX: imágenes binarias RGB generadas a partir del bytecode y grafos de llamadas a funciones (FCG), los cuales modelan las interacciones entre métodos. Para ello se utiliza una estrategia de late fusion, donde una Detección de Malware en Aplicaciones de Android CNN procesa las imágenes y una GNN analiza los grafos; posteriormente, las probabilidades de ambos modelos se combinan mediante un perceptrón multicapa (MLP) que actúa como clasificador final. Los resultados experimentales, obtenidos a partir de un dataset multimodal de 5000 aplicaciones derivado de MalNet y MalNet-Tiny, muestran que el modelo multimodal supera a los modelos unimodales. Por ejemplo, una CNN simple alcanza aproximadamente 83.1% de accuracy y una GNN basada en GCN alrededor de 80.6%, mientras que la combinación multimodal mediante late fusion logra hasta 90.6% de accuracy, precision, recall y F1-score en el modelo DenseNet121 \+ GIN con meta-clasificador optimizado. Estos resultados evidencian que la integración de representaciones heterogéneas (patrones visuales del bytecode y relaciones estructurales del código) mejora significativamente la capacidad de clasificación y la robustez del sistema, posicionando la late fusion como una estrategia eficiente para la detección multimodal de malware. 3.2 DMLDroid: Deep multimodal fusion framework for Android malware detection with resilience to code obfuscation and adversarial perturbations. Trung et al. \[2025\] Por la parte de la investigación realizada para el trabajo DMLDroid propone un sistema avanzado de detección de malware en Android basado en aprendizaje profundo multimodal, diseñado específicamente para mejorar la robustez frente a técnicas de evasión como la ofuscación de código y los ataques adversarios. El marco integra tres modalidades complementarias de información extraídas de aplicaciones Android: características tabulares derivadas del análisis del archivo AndroidManifest.xml, representaciones visuales RGB generadas a partir de los archivos DEX, que contienen el bytecode compilado de la aplicación, y secuencias derivadas de grafos de llamadas API, que modelan las dependencias estructurales entre métodos dentro del programa. Cada modalidad es procesada mediante arquitecturas especializadas de aprendizaje profundo: un MLP para las características tabulares, una CNN para las representaciones visuales derivadas de los archivos DEX y un modelo basado en DistilBERT para capturar dependencias semánticas en las secuencias de llamadas a APIs extraídas de grafos. Posteriormente, las representaciones latentes obtenidas de cada modalidad se integran mediante diferentes estrategias de fusión multimodal, entre las que se incluyen concatenación simple, self-attention, cross-attention, gated fusion y dynamic weighted fusion, lo que permite evaluar de manera sistemática el impacto de cada técnica en el desempeño del sistema. Los experimentos realizados sobre el dataset CICMalDroid 2020 muestran que el enfoque multimodal supera claramente a los modelos unimodales, alcanzando 97.98% de accuracy y 98.67% de F1-score, y manteniendo además una precisión superior al 98% incluso bajo escenarios de ofuscación de código y generación de ejemplos adversarios, lo que evidencia que la combinación de múltiples fuentes de información mejora la capacidad de generalización del modelo frente a variantes de malware. Este trabajo se relaciona directamente con el presente proyecto, ya que respalda la hipótesis de que la detección efectiva de malware requiere integrar representaciones heterogéneas del software para capturar tanto patrones estructurales como comportamentales; en particular, valida empíricamente el uso conjunto de características estáticas tabulares y representaciones visuales del bytecode, enfoque que también constituye la base metodológica de este estudio para clasificar aplicaciones Android en categorías como Adware, Banking, SMS malware y Riskware, mientras que la arquitectura de fusión multimodal propuesta en DMLDroid proporciona una referencia metodológica relevante para el diseño de sistemas de clasificación robustos frente a técnicas modernas de evasión. 3.3 Android Malware Detection Based on RGB Images and Multi-feature Fusion. Wang et al. \[2024\] El estudio Android Malware Detection Based on RGB Images and Multi-feature Fusion propone un enfoque de detección basado en la representación visual del software, donde múltiples componentes internos de una aplicación Android se transforman en imágenes para su posterior análisis mediante modelos de aprendizaje profundo. En particular, el método extrae tres fuentes principales de información de los archivos APK: el archivo DEX (que contiene el código ejecutable de la aplicación), el archivo AndroidManifest.xml (que define permisos, componentes y configuraciones de la aplicación) y las llamadas a APIs del sistema. Cada uno de estos elementos se convierte inicialmente en imágenes en escala de grises, interpretando directamente los bytes del archivo como valores de intensidad de píxel. Posteriormente, se aplican técnicas de mejoramiento de características visuales, como Canny edge detection, histogram equalization y adaptive thresholding, con el objetivo de resaltar patrones estructurales relevantes dentro de los datos binarios. Finalmente, las tres imágenes resultantes se combinan en una imagen RGB multicanal, donde cada canal representa una modalidad distinta de información del software analizado. Estas imágenes RGB son utilizadas como entrada para distintos modelos de clasificación de imágenes basados en redes neuronales profundas, incluyendo arquitecturas como AlexNet, ResNet, GoogleNet y MobileNetV2, permitiendo que la red neuronal aprenda automáticamente patrones espaciales asociados con diferentes familias de malware. Los resultados experimentales muestran que este enfoque alcanza una precisión de hasta 97.25% superando a métodos que utilizan únicamente representaciones derivadas del archivo DEX, lo que demuestra que la combinación de múltiples fuentes de información mejora significativamente la capacidad de discriminación del modelo. 

Exploracion de datos:

Datos Tabulares  
Se cuenta con un total de 16691 aplicaciones de Android,  
cada una descrita mediante 402 características estáticas.  
En este conjunto, la columna apk\_name cumple como identificador único de cada muestra, mientras que la columna  
Class define la categoría de malware asignada.  
En términos de la distribución de clases, se observa un notable desbalanceo de datos, como se ilustra en la Figura  
1\. La categoría Adware presenta un número de muestras  
significativamente menor en comparación con clases dominantes como Benign o SMS. Este desequilibrio es un factor  
crítico para el diseño del modelo, ya que implica que el  
clasificador podría presentar un sesgo hacia las clases mayoritarias si no se aplican técnicas de compensación durante  
el entrenamiento.  
adware banking benign riskware sms  
Clase  
0  
1000  
2000  
3000  
4000  
5000  
Cantidad de muestras  
Distribución de las etiquetas  
Figure 1: Distribución de etiquetas por tipo de Malware.  
permission.UPDATE\_APP\_OPS\_STATS  
permission.CHANGE\_WIFI\_STATE  
permission.GET\_TASKS  
action.ANY\_DATA\_STATE  
action.NOTIFICATION\_ADD  
action.NOTIFICATION\_REMOVE  
action.STATE\_CHANGED  
permission.WRITE\_SMS  
permission.ACCESS\_LOCATION\_EXTRA\_COMMANDS  
permission.VIBRATE  
permission.GET\_ACCOUNTS  
permission.ACCESS\_COARSE\_LOCATION  
permission.ACCESS\_FINE\_LOCATION  
permission.WRITE\_APN\_SETTINGS  
category.DEFAULT  
SmsService  
permission.READ\_INTERNAL\_STORAGE  
permission.READ\_EXTERNAL\_STORAGE  
permission.BROADCAST\_SMS  
permission.WRITE\_INTERNAL\_STORAGE  
permission.ACCESS\_WIFI\_STATE  
permission.RECEIVE\_BOOT\_COMPLETED  
permission.ACCESS\_MTK\_MMHW  
action.ACTION\_POWER\_CONNECTED  
permission.WRITE\_SYNC\_SETTINGS  
permission.UPDATE\_APP\_OPS\_STATS  
permission.CHANGE\_WIFI\_STATE  
permission.GET\_TASKS  
action.ANY\_DATA\_STATE  
action.NOTIFICATION\_ADD  
action.NOTIFICATION\_REMOVE  
action.STATE\_CHANGED  
permission.WRITE\_SMS  
permission.ACCESS\_LOCATION\_EXTRA\_COMMANDS  
permission.VIBRATE  
permission.GET\_ACCOUNTS  
permission.ACCESS\_COARSE\_LOCATION  
permission.ACCESS\_FINE\_LOCATION  
permission.WRITE\_APN\_SETTINGS  
category.DEFAULT  
SmsService  
permission.READ\_INTERNAL\_STORAGE  
permission.READ\_EXTERNAL\_STORAGE  
permission.BROADCAST\_SMS  
permission.WRITE\_INTERNAL\_STORAGE  
permission.ACCESS\_WIFI\_STATE  
permission.RECEIVE\_BOOT\_COMPLETED  
permission.ACCESS\_MTK\_MMHW  
action.ACTION\_POWER\_CONNECTED  
permission.WRITE\_SYNC\_SETTINGS  
Matriz de Correlación Reducida \- Top 25 Variables  
1.00  
0.75  
0.50  
0.25  
0.00  
0.25  
0.50  
0.75  
1.00  
Figure 2: Matriz de correlación de las variables con mayor  
coeficiente de interacción.  
Respecto al análisis de la matriz de correlación (Figura  
2), se identificaron grupos de variables con una dependencia lineal casi perfecta. Un ejemplo destacado es  
la correlación entre action.NOTIFICATION\_ADD y action.NOTIFICATION\_REMOVE. Estas características se  
refieren a las peticiones del sistema para gestionar el ciclo de vida de las notificaciones en el dispositivo. La alta  
correlación se debe a que las aplicaciones que implementan servicios de escucha de notificaciones suelen requerir  
ambas acciones de manera simétrica para añadir o eliminar alertas de la interfaz, lo que genera redundancia en  
el espacio de características. Esto indica que es importante hacer una selección de características o reducción de  
dimensionalidad.  
Para evaluar la separabilidad del dataset, se aplicó la técnica de reducción de dimensionalidad t-SNE (Figura 3). El  
resultado muestra que ciertas familias de malware, particularmente Adware, tienden a formar clusters o agrupamientos densos y definidos en el espacio reducido, lo que indica  
una firma conductual muy consistente. Por el contrario,  
la clase Benign aparece mucho más dispersa; esto se explica por la enorme heterogeneidad de las aplicaciones  
legítimas, las cuales no comparten un patrón funcional tan  
rígido como el software malicioso.  
3  
Detección de Malware en Aplicaciones de Android  
100 50 0 50 100  
Componente 1  
100  
50  
0  
50  
100  
150  
Componente 2  
Agrupamientos por tipo de Malware  
adware  
banking  
benign  
riskware  
sms  
Figure 3: Proyección de alta dimensionalidad mediante  
t-SNE.