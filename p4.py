import csv
from datetime import datetime


# Primer módulo
class HistorialNavegacion:
    def __init__(self):
        self.historial = []  # Pila para el historial
        self.pila_atras = []  # Pila para navegar hacia atrás
        self.historial_csv = "historial.csv"

    def ir(self, url):
        # Agregar la URL al historial y limpiar la pila de atrás
        if self.historial:
            self.pila_atras.clear()  # Limpiar la pila de adelante si se visita una nueva URL
        self.historial.append(url)
        self.guardar_historial(url)
        print(f"Visitando: {url}")

    def atras(self):
        if self.historial:
            pagina_actual = self.historial.pop()
            self.pila_atras.append(pagina_actual)
            if self.historial:
                print(f"Volviendo a: {self.historial[-1]}")
            else:
                print("No hay más páginas en el historial.")
        else:
            print("No hay páginas visitadas.")

    def adelante(self):
        if self.pila_atras:
            pagina_siguiente = self.pila_atras.pop()
            self.historial.append(pagina_siguiente)
            print(f"Avanzando a: {pagina_siguiente}")
        else:
            print("No hay páginas para avanzar.")

    def mostrar_historial(self):
        print("Historial de navegación:")
        for url in self.historial:
            print(url)

    def guardar_historial(self, url):
        with open(self.historial_csv, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([url, datetime.now().strftime("%Y-%m-%d %H:%M:%S")])

    def cargar_historial(self):
        try:
            with open(self.historial_csv, mode="r") as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row)
        except FileNotFoundError:
            print("No hay historial guardado.")


# Segundo módulo
# Definición de la clase Nodo para representar una pestaña en la lista doblemente enlazada
class NodoPestana:
    def __init__(self, url):
        self.url = url  # Almacena la URL o IP de la pestaña
        self.prev = None  # Referencia al nodo anterior en la lista
        self.next = None  # Referencia al nodo siguiente en la lista


# Definición de la clase para manejar la lista doblemente enlazada de pestañas abiertas
class ListaPestanas:
    def __init__(self):
        self.head = None  # Primer nodo de la lista (primera pestaña)
        self.current = None  # Puntero a la pestaña actual

    # Método para abrir una nueva pestaña
    def nueva_pestana(self, url):
        nueva_pestana = NodoPestana(
            url
        )  # Crear un nuevo nodo de pestaña con la URL especificada
        if not self.head:  # Si la lista está vacía
            self.head = nueva_pestana  # Asigna la nueva pestaña como el primer nodo
            self.current = nueva_pestana  # Define esta pestaña como la actual
        else:  # Si hay pestañas en la lista
            self.current.next = nueva_pestana  # Conecta la pestaña actual con la nueva
            nueva_pestana.prev = (
                self.current
            )  # Conecta la nueva pestaña con la anterior
            self.current = nueva_pestana  # Establece la nueva pestaña como la actual
        print(f"Abriste una nueva pestaña con: {url}")  # Mensaje de confirmación

    # Método para cerrar la pestaña actual
    def cerrar_pestana(self):
        if not self.current:  # Si no hay pestañas abiertas
            print("No hay pestañas para cerrar.")
            return
        url = (
            self.current.url
        )  # Almacena la URL de la pestaña a cerrar para el mensaje de confirmación
        if self.current.prev:  # Si hay una pestaña anterior
            self.current.prev.next = (
                self.current.next
            )  # Salta la pestaña actual en la conexión
        if self.current.next:  # Si hay una pestaña siguiente
            self.current.next.prev = (
                self.current.prev
            )  # Conecta el nodo siguiente al anterior
            self.current = (
                self.current.next
            )  # Define la siguiente pestaña como la actual
        elif self.current.prev:  # Si no hay pestaña siguiente pero hay una anterior
            self.current = self.current.prev  # Define la anterior como la actual
        else:  # Si esta es la única pestaña
            self.head = None  # La lista queda vacía
            self.current = None  # No hay pestaña actual
        print(f"Cerraste la pestaña con: {url}")  # Mensaje de confirmación

    # Método para cambiar a una pestaña específica
    def cambiar_pestana(self, n):
        temp = self.head  # Empezamos en la primera pestaña
        index = 1  # Índice de la pestaña actual en el bucle
        while temp and index < n:  # Recorre hasta llegar a la pestaña deseada
            temp = temp.next  # Avanza al siguiente nodo
            index += 1
        if temp:  # Si existe una pestaña en el índice especificado
            self.current = temp  # Cambia la pestaña actual a la deseada
            print(
                f"Ahora estás en la pestaña con: {temp.url}"
            )  # Mensaje de confirmación
        else:  # Si el índice está fuera del rango
            print("Número de pestaña inválido.")

    # Método para mostrar todas las pestañas abiertas
    def mostrar_pestanas(self):
        temp = self.head  # Comienza desde la primera pestaña
        if not temp:  # Si no hay pestañas
            print("No hay pestañas abiertas.")
            return
        index = 1  # Índice para cada pestaña
        print("Pestañas abiertas:")
        while temp:  # Recorre cada nodo en la lista de pestañas
            # Muestra el índice y URL de cada pestaña
            print(f"{index}. {temp.url}")
            temp = temp.next  # Avanza al siguiente nodo
            index += 1


# Ejemplo de uso del historial de navegación
navegador = HistorialNavegacion()
navegador.ir("http://ejemplo.com")
navegador.ir("http://prueba.com")
navegador.atras()
navegador.adelante()
navegador.mostrar_historial()
navegador.cargar_historial()

# Ejemplo de uso de la lista de pestañas
pestanas = ListaPestanas()
pestanas.nueva_pestana("www.ejemplo.com")
pestanas.nueva_pestana("www.wikipedia.org")
pestanas.mostrar_pestanas()
pestanas.cambiar_pestana(2)
pestanas.cerrar_pestana()
pestanas.mostrar_pestanas()
