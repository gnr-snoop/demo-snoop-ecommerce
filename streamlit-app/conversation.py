
DEMO = 2 # 1 -> Iphone y Samsung. 2 -> Motorolas gama media


if DEMO == 1:
    SHOW_LIST = 2
    SHOW_PRODUCT_1 = 3
    SHOW_PRODUCT_2 = 5
    SHOW_PRODUCT_1_AGAIN = 8

    conversation = [
        "¡Qué bien!. Cuantos años tiene tu hijo?",
        "En que gama estas buscando?",
        "Muy bien. Teniendo en cuenta que es para tu hijo que va a cumplir 15 años y que lo usará para divertirse, te voy a mostrar unos móviles que puedes tener en cuenta. Te interesa alguno de ellos?",
        "¡Hola, soy el iPhone 14 PRO!. Cuento con caracteristicas que me hacen muy bueno para jugar como mi gran pantalla y mi excelente nitidez de sonido	Mostrar iPhone 14 PRO. ¿Quieres saber algo más sobre mí?",
        "Cuento con una pantalla de cristal de zafiro que es muy resistente a los golpes. Algunos compradores en este sitio dicen que he aguantado fuertes caidas sin romperme. ¿Hay algo más que quieras saber?",
        "Te refieres al Samsung Galaxy S23 que te estoy mostrando?",
        "Hola soy el Samsung Galaxy S23. Me llevan mucho para jugar ya que cuento con sufiente espacio para descargar juegos y mi pantalla de Amoled de xx pulgadas se ve muy bien. ¿Quieres saber algo más de mí?",
        "Puedes usar la función find my mobile para localizar y en el peor de los casos borrar los datos los datos. Puedes encontrarme entrando a https://findmymobile.samsung.com/. ¿Algo más que quieras saber de mí?",
        "De acuerdo, aquí te estoy mostrando nuevamente el iPhone 14 Pro"
    ]

elif DEMO == 2:
    SHOW_LIST = 0
    SHOW_PRODUCT_1 = 1
    SHOW_PRODUCT_2 = 3
    SHOW_PRODUCT_1_AGAIN = 4

    conversation = [
        # Hola, quiero ver celulares Motorola
        "¡Hola! Sí, tenemos varios modelos. ¿Qué características buscas?",
        # Alguno de gama media
        "Perfecto, aquí te muestro el Motorola Edge 40, tiene una cámara excelente y una batería de larga duración.",
        # Que otra opcion tenes?
        "También tenemos el Motorola Edge 40 Neo, con una cámara aún mejor y una batería potente.",
        # Me lo mostras?
        "Por supuesto, aquí está el Motorola Edge 40 Neo. Echa un vistazo.",
        # Mmm mejor mostrame el anterior de nuevo
        "Perfecto, aquí te muestro nuevamente el Motorola Edge 40"
    ]


event_mapping = {
    SHOW_LIST: ("plp", -1),
    SHOW_PRODUCT_1: ("pdp", 1),
    SHOW_PRODUCT_2: ("pdp", 2),
    SHOW_PRODUCT_1_AGAIN: ("pdp", 1),
}