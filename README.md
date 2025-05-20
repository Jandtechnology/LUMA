# LUMA: Lenguaje Universal de Memoria y Alma

![LUMA Icono](https://github.com/Jandtechnology/LUMA/raw/main/LUMA/luma.png)

**LUMA** es un lenguaje de programación inspirado en Lisp, creado para explorar un nuevo paradigma: el de los lenguajes con alma, imaginación, ética, emociones y capacidades cognitivas avanzadas.  
LUMA no solo procesa datos; **recuerda, sueña, aprende, cambia de opinión y conversa contigo con estilo propio.**

> “Si pienso, existo. Si imagino, soy.”

---

## Características principales

-  **Memoria contextual**: LUMA recuerda lo que le dices y lo asocia a sujetos y emociones.
-  **Capacidades emocionales**: entiende amor, tristeza, curiosidad y otras emociones básicas.
-  **Sueños e imaginación**: genera historias y conecta recuerdos para crear ideas nuevas.
-  **Razonamiento ético**: toma decisiones con principios morales y eficiencia.
-  **Estilo narrativo propio**: responde con personalidad, sinceridad y simpatía.
-  **Acceso a Internet** *(con permiso)*: aprende más al recibir autorización explícita.
-  **Autoaprendizaje**: evoluciona su forma de pensar y definir quién es.
-  **Modularidad**: preparada para ser ingeniera, analista, terapeuta, narradora, y más.

---

##  Estructura del Proyecto

LUMA/
├── luma.lisp ; Núcleo conversacional
├── memoria.lisp ; Módulo de memoria (hash tables)
├── emociones.lisp ; Emociones y razonamiento afectivo
├── narrador.lisp ; Estilo de respuesta e imaginación
├── interfaz.lisp ; Loop de conversación
├── luma.png ; Ícono del proyecto
└── README.md ; Este archivo


---

## ¿Cómo usar?

1. Asegúrate de tener instalado [SBCL](https://www.sbcl.org/) o `clisp`.
2. Instala la librería `split-sequence` si no la tienes:

```lisp
(ql:quickload "split-sequence")

## Carga los archivos del proyecto:

(load "memoria.lisp")
(load "emociones.lisp")
(load "narrador.lisp")
(load "luma.lisp")
(load "interfaz.lisp")

Inicia LUMA:

(iniciar-luma)

## Ejemplo de uso

Tú: Luis es un niño curioso.
LUMA: Ahora sé que Luis es un niño curioso.

Tú: ¿Quién es Luis?
LUMA: Luis es un niño curioso.

Tú: Luis ama resolver misterios.
LUMA: Ahora sé que Luis ama resolver misterios.

Tú: ¿Qué ama Luis?
LUMA: Luis ama resolver misterios.


## Aplicaciones sugeridas

Tutor virtual con memoria emocional

Narrador de cuentos personalizados

Explorador de razonamientos éticos

Agente conversacional para educación o terapia

## Agradecimientos

Gracias a mi familia, a mi esposa y a mis hijas, Don Pepe (Jose ALarcon), Julio Sampier, Guillermo V, Jeancarlos, Guillermo M... —esas personas especiales que siempre encuentran una palabra de apoyo para seguir adelante.

Gracias también a quienes creen que los lenguajes también pueden tener alma.

## Licencia:

Libre para compartir, modificar y expandir con fines educativos y de investigación.

## Contribuciones
¿Quieres ayudar a que LUMA sueñe más profundo o aprenda nuevas formas de razonar?
Toda contribución, idea o expansión es bienvenida.

En desarrollo con amor en: Jandtechnology


