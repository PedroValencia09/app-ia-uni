import streamlit as st
import os

# Configuración de la página web
st.set_page_config(page_title="Plataforma Educativa de IA", page_icon="🤖", layout="wide")

# Menú Lateral
st.sidebar.title("Menú Principal")
opcion = st.sidebar.radio(
    "Selecciona una opción:",
    [
        "1. Concepto de IA",
        "2. Antecedentes",
        "3. Clasificación de la IA",
        "4. Herramientas",
        "5. Disciplinas",
        "6. Glosario",
        "7. Ensayo de IA",
        "8. Clasificación de Algoritmos de Búsqueda",
        "9. Elementos de Búsqueda",
        "10. Ejemplo Práctico de Búsqueda",
        "11. Infografía de Búsqueda"
    ]
)

# ---------------- 1. CONCEPTO ----------------
if opcion == "1. Concepto de IA":
    st.header("1. Concepto de IA")
    st.write(
        "La Inteligencia Artificial es un campo interdisciplinario dedicado al diseño de "
        "sistemas capaces de realizar tareas asociadas con la inteligencia humana, como aprender, "
        "razonar, reconocer patrones, comprender lenguaje, resolver problemas y tomar decisiones."
    )
    if os.path.exists("generative-ai-and-tool-concept-illustration-png.png"):
        st.image("generative-ai-and-tool-concept-illustration-png.png", width=450)

# ---------------- 2. ANTECEDENTES ----------------
elif opcion == "2. Antecedentes":
    st.header("2. Antecedentes de la IA - Línea del Tiempo")
    imgs = [
        "Captura de pantalla 2026-09-19 163106.png",
        "Captura de pantalla 2026-09-19 163121.png",
        "Captura de pantalla 2026-09-19 163134.png"
    ]
    for img in imgs:
        if os.path.exists(img):
            st.image(img, use_container_width=True)

# ---------------- 3. CLASIFICACIÓN ----------------
elif opcion == "3. Clasificación":
    st.header("3. Clasificación de la IA")
    
    st.subheader("IA Débil o Estrecha (Narrow AI)")
    st.write(
        "Está diseñada para resolver tareas específicas: traducción, recomendación, reconocimiento de imágenes, "
        "reconocimiento de voz, generación de texto, recomendaciones de productos. Impulsa la mayor parte de la IA "
        "que nos rodea hoy, no tiene nada de débil."
    )
    st.markdown("**Ejemplos habituales:** Asistente virtual, Motores de recomendación, Traductores automáticos, Sistemas antifraude, Chatbots de atención básica, Vehículos autónomos.")
    if os.path.exists("IA débil_Waze_Valencia_Vazquez_Pedro_page-0001.jpg"):
        st.image("IA débil_Waze_Valencia_Vazquez_Pedro_page-0001.jpg", width=600)

    st.divider()

    st.subheader("IA Fuerte o General (AGI - General Artificial Intelligence)")
    st.write(
        "Busca crear máquinas con inteligencia humana completa, capaces de realizar cualquier tarea intelectual "
        "que un humano pueda hacer. Es teórica y no existe de manera práctica. Es una categoría hipotética."
    )
    st.info("**Hipotética:** Se refiere a algo que se plantea como una posibilidad o supuesto para analizar qué podría ocurrir, sin afirmar que sea verdadero.")
    if os.path.exists("IA fuerte_TestWosniak_Valencia_Vazquez_Pedro_page-0001.jpg"):
        st.image("IA fuerte_TestWosniak_Valencia_Vazquez_Pedro_page-0001.jpg", width=600)

    st.divider()

    st.subheader("IA Superinteligente")
    st.write(
        "Hace referencia a un sistema que superaría a los humanos en absolutamente todas las áreas cognitivas, "
        "sería autoconsciente y tendría la capacidad de resolver problemas, aprender y planificar para el futuro. "
        "Es una categoría especulativa."
    )
    st.info("**Especulativa:** Se refiere a algo basado principalmente en suposiciones, posibilidades o conjeturas, especialmente cuando existe poca evidencia para demostrarlo.")
    if os.path.exists("IA superinteligente_Terminator_Valencia_Vazquez_Pedro_page-0001.jpg"):
        st.image("IA superinteligente_Terminator_Valencia_Vazquez_Pedro_page-0001.jpg", width=600)

# ---------------- 4. HERRAMIENTAS ----------------
elif opcion == "4. Herramientas":
    st.header("4. Herramientas de IA")
    st.write("Haz clic en los enlaces para abrir las herramientas de IA en tu navegador:")
    st.link_button("🌐 Abrir Google Gemini", "https://gemini.google.com/app?hl=es")
    st.link_button("🌐 Abrir ChatGPT", "https://chatgpt.com/")

# ---------------- 5. DISCIPLINAS ----------------
elif opcion == "5. Disciplinas":
    st.header("5. Disciplinas de la IA")
    st.write("La Inteligencia Artificial se construyó en base a conocimientos y teorías existentes en otras áreas del conocimiento:")
    
    disciplinas = [
        ("Filosofía", "Aristóteles (300 AC) Describe de forma estructurada la forma como el ser humano produce conclusiones racionales a partir de un grupo de premisas. (Silogismos)"),
        ("Matemáticas", "Razonamiento con algoritmos. Cálculo: brindó las herramientas que nos permiten la modelación de diferentes tipos de fenómenos."),
        ("Psicología", "Refuerza la idea de que los humanos y otros animales pueden ser considerados como máquinas para el procesamiento de información, psicólogos como Piaget y Craik definieron teorías como el conductismo – psicología cognitiva."),
        ("Computación", "Las teorías de la IA encuentran un medio para su implementación de artefactos y modelado cognitivo a través de las computadoras."),
        ("Lingüística", "Aporta un área híbrida conocida como lingüística computacional o procesamiento del lenguaje natural."),
        ("Economía", "Área experta en la toma de decisiones, debido que éstas implican la pérdida o ganancia del rendimiento. (Teoría de la decisión –que combina la Teoría de la Probabilidad y la Teoría de la utilidad; Teoría de juegos – para pequeñas economías; Procesos de decisión de Markov – para procesos secuenciales; entre otras)."),
        ("Neurociencia", "Ha contribuido a la IA con los conocimientos recabados hasta la fecha sobre la forma como el cerebro procesa la información.")
    ]
    for nombre, desc in disciplinas:
        st.markdown(f"**• {nombre}:** {desc}")

# ---------------- 6. GLOSARIO ----------------
elif opcion == "6. Glosario":
    st.header("6. Glosario de IA")
    st.subheader("Glosario de Conceptos Fundamentales")

    # Nombre exacto de la imagen en GitHub
    imagen_sistema_experto = "366dcdbb-ab63-4bb8-8114-9018ca9aea19.jpg"

    glosario_data = [
        ("Algoritmo de búsqueda", "Conjunto de reglas y procesos que los motores de búsqueda u otros sistemas computacionales utilizan para analizar, clasificar y mostrar los resultados más relevantes para una consulta o tarea determinada.", None),
        ("Deep learning", "Subcampo del Machine Learning basado en redes neuronales profundas con múltiples capas que aprenden representaciones complejas de datos.", None),
        ("Predicción de comportamiento", "Técnica analítica que utiliza algoritmos e información histórica para anticipar acciones, tendencias o decisiones futuras de un sistema o usuario.", None),
        ("Red neuronal", "Modelo computacional inspirado en la estructura y funcionamiento del cerebro humano, compuesto por nodos (neuronas artificiales) interconectados.", None),
        ("LLM multimodales", "Grandes Modelos de Lenguaje capaces de procesar, comprender y generar múltiples tipos de datos de forma simultánea (texto, imágenes, audio, video).", None),
        ("Asistente virtual", "Software basado en IA diseñado para interactuar con usuarios, comprender comandos de voz o texto y ejecutar tareas específicas de manera autónoma.", None),
        ("Visión Artificial", "Campo de la IA que permite a las computadoras procesar, analizar y comprender imágenes o videos del mundo real para extraer información útil.", None),
        ("Agentico", "Propiedad o enfoque de un sistema de IA que tiene autonomía para tomar decisiones, planificar pasos y ejecutar acciones dirigidas a lograr un objetivo.", None),
        (
            "Machine Learning", 
            "Rama de la IA que permite a los sistemas aprender y mejorar automáticamente a partir de datos sin ser programados explícitamente para cada tarea.\n\n"
            "**Ejemplo de uso en TikTok:**\n"
            "Las plataformas de video corto necesitan atraer y retener usuarios mostrándoles videos que se adapten a sus intereses en un flujo infinito de contenido. Para lograrlo, implementan modelos de Machine Learning entrenados con patrones de interacción y características del video.\n\n"
            "• **Datos de Entrada:**\n"
            "  - *Características del video:* La estructura visual y sonora del contenido (objetos detectados en imagen, movimientos, transcripciones de audio, texto en pantalla, hashtags y género).\n"
            "  - *Historial de comportamiento del usuario:* El registro de secuencias de visualización (si el usuario vio un video antes o después de una recomendación, tiempo de retención, videos omitidos con scroll rápido, loops, likes y guardados).\n\n"
            "• **Procesamiento:** Algoritmos de recomendación y visión artificial analizan la relación entre la estructura del video y los patrones de interacción guardados de millones de usuarios para predecir la afinidad del espectador con videos no vistos.\n\n"
            "• **Datos de Salida:**\n"
            "  - *Sugerencia personalizada de videos:* Una secuencia de clips seleccionada explícitamente para el usuario (presentada en la sección 'Para Ti' o bajo el criterio 'porque interactuaste con...').",
            None
        ),
        ("Datos de entrenamiento", "Conjunto de información recolectada y procesada que se utiliza para entrenar un modelo de IA y enseñarle a identificar patrones o hacer predicciones.", None),
        ("Ingeniería inversa", "Proceso de descomponer o analizar un sistema informático o modelo para comprender su funcionamiento interno, arquitectura o algoritmos.", None),
        ("Agente", "Entidad de software o hardware que percibe su entorno a través de sensores, toma decisiones y ejecuta acciones mediante actuadores para lograr un fin.", None),
        ("Sesgo algorítmico", "Error sistemático e injusto en los resultados de un modelo de IA derivado de prejuicios presentes en los datos de entrenamiento o el diseño.", None),
        ("Equidad algorítmica", "Principio o práctica de diseñar algoritmos para garantizar que sus resultados no discriminen ni beneficien desproporcionadamente a ningún grupo.", None),
        ("Integridad de datos", "Exactitud, consistencia, precisión y confiabilidad de los datos a lo largo de todo su ciclo de vida y procesamiento.", None),
        ("Análisis de datos", "Proceso de examinar, limpiar, transformar y modelar datos para descubrir información útil, patrones relevantes y respaldar la toma de decisiones.", None),
        ("Detección de objetos", "Tecnología de visión por computadora que identifica y localiza objetos específicos dentro de una imagen o secuencia de video en tiempo real.", None),
        ("Chatbot", "Programa informático diseñado para simular conversaciones con usuarios humanos a través de texto o voz mediante reglas o modelos de IA.", None),
        ("Sistema experto", "Sistema informático que emula la capacidad de toma de decisiones de un experto humano en un dominio o área específica del conocimiento.", imagen_sistema_experto),
        ("Automatización", "Uso de tecnología, software e IA para realizar procesos y tareas con mínima o nula intervención humana directa.", None),
        ("Big data", "Conjuntos de datos de gran volumen, alta velocidad y gran variedad que requieren tecnologías avanzadas para su procesamiento y análisis.", None)
    ]

    for idx, (concepto, definicion, imagen) in enumerate(glosario_data, 1):
        with st.expander(f"{idx}. {concepto}"):
            st.markdown(definicion)
            if imagen:
                if os.path.exists(imagen):
                    st.image(imagen, caption="Esquema del Sistema Experto / Inteligente", use_container_width=True)
                else:
                    st.warning(f"No se encontró la imagen '{imagen}' en el repositorio.")

# ---------------- 7. ENSAYO DE IA ----------------
elif opcion == "7. Ensayo de IA":
    st.header("7. Ensayo de IA")
    st.subheader("Inteligencia Artificial: ¿Una herramienta para avanzar o un riesgo sin control?")
    st.write(
        "En este ensayo elaborado por **Pedro Valencia Vazquez** se analizan los principales dilemas éticos y sociales "
        "relacionados con la Inteligencia Artificial, abordando temas como prejuicios algorítmicos, impacto laboral, "
        "privacidad y el uso responsable de la tecnología."
    )
    
    pdf_filename = "Ensayo_IA_Valencia.pdf"
    
    if os.path.exists(pdf_filename):
        with open(pdf_filename, "rb") as pdf_file:
            st.download_button(
                label="📄 Descargar / Leer Ensayo (PDF)",
                data=pdf_file,
                file_name=pdf_filename,
                mime="application/pdf",
                use_container_width=False
            )
    else:
        st.warning(f"El archivo '{pdf_filename}' no se encuentra en el directorio actual. Por favor, súbelo a tu repositorio de GitHub.")

# ---------------- 8. ELEMENTOS DE BÚSQUEDA ----------------
elif opcion == "8. Elementos de Búsqueda":
    st.header("8. Elementos que Intervienen en un Algoritmo de Búsqueda")
    st.write(
        "Para que un algoritmo de búsqueda pueda ejecutarse de manera correcta dentro de un sistema o estructura de datos, "
        "intervienen seis elementos fundamentales:"
    )
    
    elementos = [
        ("📍 Espacio de búsqueda", "El lugar donde buscas (una lista, tabla, arreglo o archivo) o la colección completa de datos."),
        ("🔑 Dato objetivo (Clave)", "Lo que estás buscando exactamente (un número, nombre, ID o valor específico)."),
        ("👉 Puntero o Posición", "El indicador o índice que señala qué elemento o nodo estás revisando en ese preciso momento."),
        ("⚖️ Regla de comparación", "La condición de evaluación básica: ¿El elemento actual es igual, mayor o menor al valor que busco?"),
        ("🛑 Condición de fin", "El mecanismo que detiene el algoritmo, ya sea porque se halló el elemento deseado o porque se agotaron todas las opciones sin éxito."),
        ("🎯 Resultado", "La respuesta final devuelta por el sistema (por ejemplo, la posición/índice del dato o un mensaje de 'no encontrado').")
    ]
    
    # Renderizado interactivo con expanders y columnas
    for titulo, descripcion in elementos:
        with st.expander(titulo):
            st.write(descripcion)
            
    st.divider()
    st.info(
        "💡** Recuerda que estos 6 elementos aplican tanto para algoritmos simples en estructuras de datos "
        "(como la Búsqueda Lineal o Binaria) como para algoritmos avanzados en Inteligencia Artificial (como BFS, DFS o A*)."
    )
# ---------------- 9. EJEMPLO PRÁCTICO DE BÚSQUEDA ----------------
elif opcion == "9. Ejemplo Práctico de Búsqueda":
    st.header("9. Ejemplo Práctico: Identificación de Elementos en un Algoritmo")
    
    st.subheader("Caso de Estudio: Búsqueda de la Palabra Más Larga (Búsqueda por Condición)")
    st.write(
        "Imagina que tienes un párrafo y deseas encontrar cuál es la palabra con mayor cantidad de letras. "
        "A continuación se detalla el paso a paso del proceso:"
    )
    
    # Secuencia paso a paso del algoritmo
    st.markdown("""
    1. **Paso 1:** Lees la primera palabra: *"El"* (2 letras). Es la palabra más larga hasta el momento.
    2. **Paso 2:** Lees la segunda palabra: *"algoritmo"* (9 letras). Es más larga que *"El"*, así que la guardas como tu nuevo récord.
    3. **Paso 3:** Lees la tercera palabra: *"busca"* (5 letras). No supera a *"algoritmo"*, por lo que la ignoras.
    4. **Paso 4:** Sigues revisando de manera secuencial hasta llegar a la última palabra del texto.
    """)
    
    st.divider()
    
    st.subheader("📌 Identificación de los 6 Elementos Fundamentales")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("**1. Espacio de búsqueda:**\nEl párrafo completo dividido en una lista de palabras.")
        st.info("**2. Dato objetivo:**\nNo es un valor fijo, sino la condición de cumplir con la **máxima longitud de caracteres**.")
        st.info("**3. Puntero o Posición:**\nEl indicador que recorre el texto palabra por palabra, desde la primera hasta la última.")
        
    with col2:
        st.success("**4. Regla de comparación:**\n¿La longitud de la palabra actual es mayor que la longitud de la palabra récord guardada?")
        st.success("**5. Condición de fin:**\nLlegar al final del párrafo tras haber revisado la última palabra.")
        st.success("**6. Resultado:**\nLa palabra *'algoritmo'* y su tamaño (9 letras).")

    st.divider()
    st.caption("💡**Este ejemplo demuestra que un algoritmo de búsqueda no solo sirve para encontrar un número fijo, sino también para evaluar condiciones o propiedades específicas en un conjunto de datos.")

# ---------------- 10. CLASIFICACIÓN DE ALGORITMOS ----------------
elif opcion == "10. Clasificación de Algoritmos":
    st.header("10. Clasificación de Algoritmos de Búsqueda")
    st.write(
        "A continuación se presenta la clasificación completa de los algoritmos de búsqueda "
        "utilizados en Ciencias de la Computación e Inteligencia Artificial:"
    )

    categorias = [
        (
            "1. Algoritmos No Informados (Ciegos)",
            "Métodos que solo conocen el estado inicial, las acciones posibles y cómo verificar si alcanzaron la meta. No tienen una estimación de qué tan lejos o cerca están del objetivo.",
            "Exploración ordenada y exhaustiva según reglas fijas de la estructura del árbol o grafo.",
            [
                ("BFS (Búsqueda en Anchura)", "Explora nivel por nivel todos los nodos de una misma profundidad.", "Redes sociales (LinkedIn/Facebook) para encontrar contactos de 1.er, 2.º o 3.er grado."),
                ("DFS (Búsqueda en Profundidad)", "Avanza lo más profundo posible en cada rama antes de retroceder (backtracking).", "Resolución de laberintos por un robot al chocar con pared ciega."),
                ("UCS (Búsqueda de Costo Uniforme)", "Evalúa caminos acumulando el costo de cada paso y expande la ruta con menor costo total g(n).", "Seleccionar ruta de auto con menor costo de casetas de cobro.")
            ]
        ),
        (
            "2. Algoritmos Informados (Heurísticos)",
            "Métodos que emplean conocimiento adicional específico del dominio (función heurística h(n)) para guiarse hacia la meta.",
            "Evalúan y priorizan los caminos que parecen más prometedores para ahorrar tiempo y cómputo.",
            [
                ("Búsqueda Voraz (Greedy Best-First)", "Elige en cada paso la opción que parece estar más cerca de la meta según h(n), ignorando el costo recorrido.", "Fantasmas en Pac-Man moviéndose directamente hacia el jugador."),
                ("Algoritmo A* (A-Estrella)", "Navegación óptima que combina el costo recorrido g(n) con la estimación restante h(n).", "Sistemas de GPS (Google Maps / Waze) calculando la ruta más rápida.")
            ]
        ),
        (
            "3. Algoritmos de Búsqueda Local",
            "Métodos que operan sobre un único estado actual en lugar de guardar todo el mapa o árbol de rutas.",
            "Evalúan los vecinos inmediatos del estado actual y avanzan hacia el que mejore la función de calidad o costo.",
            [
                ("Escalada de Colinas (Hill-Climbing)", "Evalúa a los vecinos inmediatos y avanza hacia el que mejore la solución, deteniéndose en máximos locales.", "Enfoque automático de la cámara de un smartphone (Autofocus)."),
                ("Templado Simulado (Simulated Annealing)", "Inspirado en el enfriamiento de metales; acepta soluciones peores al inicio para escapar de máximos locales.", "Diseño e interconexión de componentes en microchips."),
                ("Búsqueda Tabú (Tabu Search)", "Guarda una memoria a corto plazo ('Lista Tabú') con las últimas soluciones para no caer en ciclos.", "Asignación de horarios universitarios y aulas sin traslapes.")
            ]
        ),
        (
            "4. Algoritmos Evolutivos y Metaheurísticos",
            "Métodos de optimización basados en poblaciones, inspirados en la biología (selección natural y genética).",
            "Mantienen un grupo de soluciones candidatas que se seleccionan, combinan (cruce) y mutan a lo largo de generaciones.",
            [
                ("Algoritmos Genéticos (GA)", "Evoluciona una población de soluciones candidatas mediante aptitud, cruce de parámetros y mutación.", "Diseño aerodinámico virtual de carrocerías de autos de carrera."),
                ("Estrategias Evolutivas (ES)", "Diseñado para optimizar parámetros numéricos continuos (con decimales) aplicando variaciones gaussianas.", "Calibración automática de suspensión y amortiguadores en vehículos."),
                ("Programación Genética (GP)", "Variante donde las soluciones candidatas son programas de computadora o código ejecutable.", "Bots de trading financiero automático que evolucionan reglas de compra/venta.")
            ]
        ),
        (
            "5. Algoritmos de Búsqueda Adversarial (Juegos)",
            "Métodos diseñados para entornos competitivos donde las decisiones del oponente afectan directamente el resultado.",
            "Exploran un árbol de estados futuros calculando las mejores jugadas propias asumiendo que el rival elegirá lo peor para nosotros.",
            [
                ("Minimax", "Maximiza la ganancia propia asumiendo que el adversario jugará de forma perfecta para minimizarla.", "Motores de juego para Tres en Raya (Gato) o Damas."),
                ("Poda Alfa-Beta (Alpha-Beta Pruning)", "Optimización para Minimax que descarta ramas del árbol de decisión que no afectarán la elección final.", "Motores de Ajedrez que descartan ramas con pérdidas inmediatas de piezas clave."),
                ("MCTS (Búsqueda Monte Carlo)", "Algoritmo probabilístico que evalúa movimientos realizando miles de partidas simuladas aleatoriamente.", "Bots para juegos complejos como Go (AlphaGo) o videojuegos de estrategia.")
            ]
        ),
        (
            "6. Búsqueda en Estructuras de Datos (Clásica)",
            "Métodos diseñados para localizar la posición de un valor específico dentro de un conjunto de datos en memoria.",
            "Recorren o dividen arreglos y listas comparando los datos almacenados con el valor buscado.",
            [
                ("Búsqueda Lineal (Secuencial)", "Revisa elemento por elemento, de principio a fin, hasta encontrar la coincidencia.", "Buscar un nombre en una lista impresas no ordenada alfabéticamente."),
                ("Búsqueda Binaria", "Divide repetidamente a la mitad el rango de búsqueda en datos estrictamente ordenados.", "Buscar una palabra en un diccionario impreso abriendo siempre por el centro."),
                ("Búsqueda por Interpolación", "Calcula una posición probable en datos ordenados uniformemente en lugar de ir al centro exacto.", "Buscar un nombre con la letra 'A' abriendo directo las primeras páginas de la guía.")
            ]
        )
    ]

    for titulo, defn, estr, casos in categorias:
        with st.expander(titulo):
            st.markdown(f"**Definición:** {defn}")
            st.markdown(f"**Estrategia:** {estr}")
            st.markdown("---")
            st.subheader("Casos típicos:")
            for nombre_alg, desc_alg, ej_alg in casos:
                st.markdown(f"🔹 **{nombre_alg}:** {desc_alg}")
                st.caption(f"💡 *Ejemplo práctico:* {ej_alg}")

# ---------------- 11. INFOGRAFÍA DE BÚSQUEDA ----------------
elif opcion == "11. Infografía de Búsqueda":
    st.header("11. Infografía: Clasificación de Algoritmos de Búsqueda")
    st.write(
        "A continuación se presenta la guía visual y rápida con las 6 familias principales "
        "de algoritmos de búsqueda:"
    )
    
    infografias = [
        "Infografias_Algoritmos_de_Busqueda_v2_page-0001.jpg",
        "Infografias_Algoritmos_de_Busqueda_v2_page-0002.jpg",
        "Infografias_Algoritmos_de_Busqueda_v2_page-0003.jpg",
        "Infografias_Algoritmos_de_Busqueda_v2_page-0004.jpg",
        "Infografias_Algoritmos_de_Busqueda_v2_page-0005.jpg",
        "Infografias_Algoritmos_de_Busqueda_v2_page-0006.jpg",
        "Infografias_Algoritmos_de_Busqueda_v2_page-0007.jpg"
    ]
    
    for i, img_path in enumerate(infografias, 1):
        if os.path.exists(img_path):
            st.image(img_path, caption=f"Página {i} - Infografía de Algoritmos de Búsqueda", use_container_width=True)
            st.divider()
        else:

