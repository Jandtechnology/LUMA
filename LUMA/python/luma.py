# LUMA - Lenguaje Universal de Memoria y Alma

# Selección de idioma
idioma = input("Selecciona idioma / Select language (español / english): ").strip().lower()

if idioma.startswith("e"):
    lang = "en"
    print("Hello! I'm LUMA. What would you like to program today?")
    goodbye = "Goodbye!"
    keywords_exit = ["exit", "quit"]
    prefix = "Interpreting:"
else:
    lang = "es"
    print("¡Hola! Soy LUMA. ¿Qué deseas programar hoy?")
    goodbye = "¡Hasta pronto!"
    keywords_exit = ["salir", "terminar"]
    prefix = "Interpretando:"

# Bucle principal
while True:
    entrada = input("> ")
    if entrada.lower() in keywords_exit:
        print(goodbye)
        break
    else:
        print(f"{prefix} {entrada}")
