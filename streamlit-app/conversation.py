SHOW_LIST = 2
SHOW_IPHONE = 3
SHOW_SAMSUNG = 5
SHOW_IPHONE_AGAIN = 8

event_mapping = {
    SHOW_LIST: ("plp", -1),
    SHOW_SAMSUNG: ("pdp", 1),
    SHOW_IPHONE: ("pdp", 2),
    SHOW_IPHONE_AGAIN: ("pdp", 7),
}


conversation = [
    "Hola, soy el chatbot, en que te puedo ayudar?",
    "A la izquierda podes ver un listado de los mejores celulares",
    "Hola! Estas hablando con el Samsung s24+",
    "Hola! Soy el nuevo Iphone 15, preguntame lo que quieras saber sobre mí",
]

conversation_hector = [
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