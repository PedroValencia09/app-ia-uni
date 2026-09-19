import os
import webbrowser
import customtkinter as ctk
from PIL import Image

# Configuración inicial del tema
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class AppIA(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Plataforma Educativa de Inteligencia Artificial")
        self.geometry("1100x700")

        # Configuración de Grid Principal
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # ---------------------- MENÚ LATERAL (SIDEBAR) ----------------------
        self.sidebar_frame = ctk.CTkFrame(self, width=220, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(7, weight=1)

        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Menú Principal", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Botones del menú
        self.btn_1 = ctk.CTkButton(self.sidebar_frame, text="1. Concepto de IA", command=self.mostrar_concepto)
        self.btn_1.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        self.btn_2 = ctk.CTkButton(self.sidebar_frame, text="2. Antecedentes", command=self.mostrar_antecedentes)
        self.btn_2.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

        self.btn_3 = ctk.CTkButton(self.sidebar_frame, text="3. Clasificación", command=self.mostrar_clasificacion)
        self.btn_3.grid(row=3, column=0, padx=20, pady=10, sticky="ew")

        self.btn_4 = ctk.CTkButton(self.sidebar_frame, text="4. Herramientas", command=self.mostrar_herramientas)
        self.btn_4.grid(row=4, column=0, padx=20, pady=10, sticky="ew")

        self.btn_5 = ctk.CTkButton(self.sidebar_frame, text="5. Disciplinas", command=self.mostrar_disciplinas)
        self.btn_5.grid(row=5, column=0, padx=20, pady=10, sticky="ew")

        self.btn_6 = ctk.CTkButton(self.sidebar_frame, text="6. Glosario", command=self.mostrar_glosario)
        self.btn_6.grid(row=6, column=0, padx=20, pady=10, sticky="ew")

        # ---------------------- ÁREA DE CONTENIDO PRINCIPAL ----------------------
        self.main_frame = ctk.CTkScrollableFrame(self, label_text="Contenido")
        self.main_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        # Cargar primera pantalla por defecto
        self.mostrar_concepto()

    def limpiar_pantalla(self):
        """Elimina todos los widgets existentes en el panel principal."""
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def cargar_imagen(self, ruta_imagen, ancho_base=600):
        """Carga y escala una imagen manteniendo la relación de aspecto."""
        if os.path.exists(ruta_imagen):
            img_pil = Image.open(ruta_imagen)
            w, h = img_pil.size
            alto = int((ancho_base / float(w)) * float(h))
            img_ctk = ctk.CTkImage(light_image=img_pil, dark_image=img_pil, size=(ancho_base, alto))
            lbl_img = ctk.CTkLabel(self.main_frame, image=img_ctk, text="")
            lbl_img.pack(pady=15)
        else:
            lbl_err = ctk.CTkLabel(self.main_frame, text=f"[Imagen no encontrada: {ruta_imagen}]", text_color="red")
            lbl_err.pack(pady=10)

    # ---------------------- OPCIONES DEL MENÚ ----------------------

    def mostrar_concepto(self):
        self.limpiar_pantalla()
        self.main_frame.configure(label_text="1. Concepto de IA")

        texto_concepto = (
            "La Inteligencia Artificial es un campo interdisciplinario dedicado al diseño de "
            "sistemas capaces de realizar tareas asociadas con la inteligencia humana, como aprender, "
            "razonar, reconocer patrones, comprender lenguaje, resolver problemas y tomar decisiones."
        )

        lbl_texto = ctk.CTkLabel(self.main_frame, text=texto_concepto, font=ctk.CTkFont(size=16),
                                 wraplength=700, justify="left")
        lbl_texto.pack(padx=20, pady=20)

        self.cargar_imagen("generative-ai-and-tool-concept-illustration-png.png", ancho_base=450)

    def mostrar_antecedentes(self):
        self.limpiar_pantalla()
        self.main_frame.configure(label_text="2. Antecedentes de la IA - Línea del Tiempo")

        lbl_titulo = ctk.CTkLabel(self.main_frame, text="Antecedentes Históricos de la Inteligencia Artificial", 
                                  font=ctk.CTkFont(size=18, weight="bold"))
        lbl_titulo.pack(pady=10)

        imagenes_linea = [
            "Captura de pantalla 2026-09-19 163106.png",
            "Captura de pantalla 2026-09-19 163121.png",
            "Captura de pantalla 2026-09-19 163134.png"
        ]

        for img in imagenes_linea:
            self.cargar_imagen(img, ancho_base=750)

    def mostrar_clasificacion(self):
        self.limpiar_pantalla()
        self.main_frame.configure(label_text="3. Clasificación de la IA")

        # IA DÉBIL
        lbl_tit_debil = ctk.CTkLabel(self.main_frame, text="IA Débil o Estrecha (Narrow AI)", font=ctk.CTkFont(size=18, weight="bold"))
        lbl_tit_debil.pack(anchor="w", padx=20, pady=(15, 5))

        txt_debil = (
            "Está diseñada para resolver tareas específicas: traducción, recomendación, reconocimiento de imágenes, "
            "reconocimiento de voz, generación de texto, recomendaciones de productos. Impulsa la mayor parte de la IA "
            "que nos rodea hoy, no tiene nada de débil.\n\n"
            "Ejemplos habituales:\n"
            "• Asistente virtual\n• Motores de recomendación\n• Traductores automáticos\n"
            "• Sistemas antifraude\n• Chatbots de atención básica\n• Vehículos autónomos"
        )
        lbl_debil = ctk.CTkLabel(self.main_frame, text=txt_debil, font=ctk.CTkFont(size=14), wraplength=700, justify="left")
        lbl_debil.pack(anchor="w", padx=20, pady=5)
        self.cargar_imagen("IA débil_Waze_Valencia_Vazquez_Pedro_page-0001.jpg", ancho_base=600)

        ctk.CTkFrame(self.main_frame, height=2, fg_color="gray").pack(fill="x", padx=20, pady=20)

        # IA FUERTE
        lbl_tit_fuerte = ctk.CTkLabel(self.main_frame, text="IA Fuerte o General (AGI - General Artificial Intelligence)", font=ctk.CTkFont(size=18, weight="bold"))
        lbl_tit_fuerte.pack(anchor="w", padx=20, pady=(15, 5))

        txt_fuerte = (
            "Busca crear máquinas con inteligencia humana completa, capaces de realizar cualquier tarea intelectual "
            "que un humano pueda hacer. Es teórica y no existe de manera práctica. Es una categoría hipotética.\n\n"
            "• Hipotética: Se refiere a algo que se plantea como una posibilidad o supuesto para analizar qué podría ocurrir, "
            "sin afirmar que sea verdadero."
        )
        lbl_fuerte = ctk.CTkLabel(self.main_frame, text=txt_fuerte, font=ctk.CTkFont(size=14), wraplength=700, justify="left")
        lbl_fuerte.pack(anchor="w", padx=20, pady=5)
        self.cargar_imagen("IA fuerte_TestWosniak_Valencia_Vazquez_Pedro_page-0001.jpg", ancho_base=600)

        ctk.CTkFrame(self.main_frame, height=2, fg_color="gray").pack(fill="x", padx=20, pady=20)

        # IA SUPERINTELIGENTE
        lbl_tit_super = ctk.CTkLabel(self.main_frame, text="IA Superinteligente", font=ctk.CTkFont(size=18, weight="bold"))
        lbl_tit_super.pack(anchor="w", padx=20, pady=(15, 5))

        txt_super = (
            "Hace referencia a un sistema que superaría a los humanos en absolutamente todas las áreas cognitivas, "
            "sería autoconsciente y tendría la capacidad de resolver problemas, aprender y planificar para el futuro. "
            "Es una categoría especulativa.\n\n"
            "• Especulativa: Se refiere a algo basado principalmente en suposiciones, posibilidades o conjeturas, "
            "especialmente cuando existe poca evidencia para demostrarlo."
        )
        lbl_super = ctk.CTkLabel(self.main_frame, text=txt_super, font=ctk.CTkFont(size=14), wraplength=700, justify="left")
        lbl_super.pack(anchor="w", padx=20, pady=5)
        self.cargar_imagen("IA superinteligente_Terminator_Valencia_Vazquez_Pedro_page-0001.jpg", ancho_base=600)

    def mostrar_herramientas(self):
        self.limpiar_pantalla()
        self.main_frame.configure(label_text="4. Herramientas de IA")

        lbl_intro = ctk.CTkLabel(self.main_frame, text="Haz clic en los enlaces para abrir las herramientas de IA en tu navegador:", 
                                 font=ctk.CTkFont(size=16))
        lbl_intro.pack(anchor="w", padx=20, pady=20)

        # Gemini
        btn_gemini = ctk.CTkButton(self.main_frame, text="Abrir Google Gemini", 
                                   command=lambda: webbrowser.open("https://gemini.google.com/app?hl=es"),
                                   fg_color="#1a73e8", hover_color="#1557b0")
        btn_gemini.pack(anchor="w", padx=40, pady=10)

        lbl_url1 = ctk.CTkLabel(self.main_frame, text="URL: https://gemini.google.com/app?hl=es", font=ctk.CTkFont(size=12, slant="italic"))
        lbl_url1.pack(anchor="w", padx=40, pady=(0, 15))

        # ChatGPT
        btn_chatgpt = ctk.CTkButton(self.main_frame, text="Abrir ChatGPT", 
                                    command=lambda: webbrowser.open("https://chatgpt.com/"),
                                    fg_color="#10a37f", hover_color="#0e8568")
        btn_chatgpt.pack(anchor="w", padx=40, pady=10)

        lbl_url2 = ctk.CTkLabel(self.main_frame, text="URL: https://chatgpt.com/", font=ctk.CTkFont(size=12, slant="italic"))
        lbl_url2.pack(anchor="w", padx=40, pady=(0, 15))

    def mostrar_disciplinas(self):
        self.limpiar_pantalla()
        self.main_frame.configure(label_text="5. Disciplinas de la IA")

        lbl_intro = ctk.CTkLabel(self.main_frame, text="La Inteligencia Artificial se construyó en base a conocimientos y teorías existentes en otras áreas del conocimiento:",
                                 font=ctk.CTkFont(size=15, weight="bold"), wraplength=700, justify="left")
        lbl_intro.pack(anchor="w", padx=20, pady=(15, 10))

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
            lbl_item = ctk.CTkLabel(self.main_frame, text=f"• {nombre}: ", font=ctk.CTkFont(size=14, weight="bold"))
            lbl_item.pack(anchor="w", padx=20, pady=(5, 0))

            lbl_desc = ctk.CTkLabel(self.main_frame, text=desc, font=ctk.CTkFont(size=13), wraplength=670, justify="left")
            lbl_desc.pack(anchor="w", padx=40, pady=(0, 10))

    def mostrar_glosario(self):
        self.limpiar_pantalla()
        self.main_frame.configure(label_text="6. Glosario de IA")

        lbl_titulo = ctk.CTkLabel(self.main_frame, text="Glosario de Conceptos Fundamentales", font=ctk.CTkFont(size=18, weight="bold"))
        lbl_titulo.pack(anchor="w", padx=20, pady=15)

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

        # Desplegar los 20 conceptos con formato enriquecido
        for idx, (concepto, definicion) in enumerate(glosario_data, 1):
            frame_concepto = ctk.CTkFrame(self.main_frame, corner_radius=8)
            frame_concepto.pack(fill="x", padx=20, pady=6)

            lbl_num_nombre = ctk.CTkLabel(
                frame_concepto, 
                text=f"{idx}. {concepto}", 
                font=ctk.CTkFont(size=15, weight="bold"),
                text_color="#1f538d"
            )
            lbl_num_nombre.pack(anchor="w", padx=15, pady=(10, 2))

            lbl_def = ctk.CTkLabel(
                frame_concepto, 
                text=definicion, 
                font=ctk.CTkFont(size=13),
                wraplength=700, 
                justify="left"
            )
            lbl_def.pack(anchor="w", padx=25, pady=(0, 10))


if __name__ == "__main__":
    app = AppIA()
    app.mainloop()