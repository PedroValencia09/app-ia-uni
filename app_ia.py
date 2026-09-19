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
        "3. Clasificación",
        "4. Herramientas",
        "5. Disciplinas",
        "6. Glosario"
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
    
    glosario_data = [
        ("Deep learning", "Subcampo del Machine Learning basado en redes neuronales profundas con múltiples capas que aprenden representaciones complejas de datos."),
        ("Predicción de comportamiento", "Técnica analítica que utiliza algoritmos e información histórica para anticipar acciones, tendencias o decisiones futuras de un sistema o usuario."),
        ("Red neuronal", "Modelo computacional inspirado en la estructura y funcionamiento del cerebro humano, compuesto por nodos (neuronas artificiales) interconectados."),
        ("LLM multimodales", "Grandes Modelos de Lenguaje capaces de procesar, comprender y generar múltiples tipos de datos de forma simultánea (texto, imágenes, audio, video)."),
        ("Asistente virtual", "Software basado en IA diseñado para interactuar con usuarios, comprender comandos de voz o texto y ejecutar tareas específicas de manera autónoma."),
        ("Visión Artificial", "Campo de la IA que permite a las computadoras procesar, analizar y comprender imágenes o videos del mundo real para extraer información útil."),
        ("Agentico", "Propiedad o enfoque de un sistema de IA que tiene autonomía para tomar decisiones, planificar pasos y ejecutar acciones dirigidas a lograr un objetivo."),
        ("Machine Learning", "Rama de la IA que permite a los sistemas aprender y mejorar automáticamente a partir de datos sin ser programados explícitamente para cada tarea."),
        ("Datos de entrenamiento", "Conjunto de información recolectada y procesada que se utiliza para entrenar un modelo de IA y enseñarle a identificar patrones o hacer predicciones."),
        ("Ingeniería inversa", "Proceso de descomponer o analizar un sistema informático o modelo para comprender su funcionamiento interno, arquitectura o algoritmos."),
        ("Agente", "Entidad de software o hardware que percibe su entorno a través de sensores, toma decisiones y ejecuta acciones mediante actuadores para lograr un fin."),
        ("Sesgo algorítmico", "Error sistemático e injusto en los resultados de un modelo de IA derivado de prejuicios presentes en los datos de entrenamiento o el diseño."),
        ("Equidad algorítmica", "Principio o práctica de diseñar algoritmos para garantizar que sus resultados no discriminen ni beneficien desproporcionadamente a ningún grupo."),
        ("Integridad de datos", "Exactitud, consistencia, precisión y confiabilidad de los datos a lo largo de todo su ciclo de vida y procesamiento."),
        ("Análisis de datos", "Proceso de examinar, limpiar, transformar y modelar datos para descubrir información útil, patrones relevantes y respaldar la toma de decisiones."),
        ("Detección de objetos", "Tecnología de visión por computadora que identifica y localiza objetos específicos dentro de una imagen o secuencia de video en tiempo real."),
        ("Chatbot", "Programa informático diseñado para simular conversaciones con usuarios humanos a través de texto o voz mediante reglas o modelos de IA."),
        ("Sistema experto", "Sistema informático que emula la capacidad de toma de decisiones de un experto humano en un dominio o área específica del conocimiento."),
        ("Automatización", "Uso de tecnología, software e IA para realizar procesos y tareas con mínima o nula intervención humana directa."),
        ("Big data", "Conjuntos de datos de gran volumen, alta velocidad y gran variedad que requieren tecnologías avanzadas para su procesamiento y análisis.")
    ]

    for idx, (concepto, definicion) in enumerate(glosario_data, 1):
        with st.expander(f"{idx}. {concepto}"):
            st.write(definicion)
