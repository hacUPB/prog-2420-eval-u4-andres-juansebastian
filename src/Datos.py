import csv
import matplotlib.pyplot as plt

def main():
    while True:
        print("Menu principal")
        print("1. Listar archivos presentes en la ruta actual o ingresar una ruta donde buscar los archivos")
        print("2. Procesar archivo de texto (.txt)")
        print("3. Procesar archivo separado por comas (.csv)")
        print("4. salir")


        opcion = input(f"Seleccione una opcion: ")
        if opcion == '1':
            ListarArchivos()
        elif opcion == '2':
            ProcesarArchivos_txt()
        elif opcion == '3':
            ProcesarArchivos_csv()
        elif opcion == '4':
            print("Saliendo del programa")
            break
        else:
            print("opcion no valida, es del 1 al 4")

def ListarArchivos():
    print("Archivos simulados en la ruta actual")
    print("Archivos1.txt")
    print("ejemplo.csv")
    print("datos.csv")
    
def ProcesarArchivos_txt():
    archivo = input("ingrese el nombre del archivo de texto: ")
    try:
        f = open(archivo, 'r')
        texto = f.read()
        f.close()
    except FileNotFoundError:
        print("El archivo no existe ")
        return
    
    while True:
        print("Submenu")
        print("1. contar numero de palabras")
        print("2. Remplazar una plabra")
        print("3. contar el numero de caracteres")
        print("4. volver al menu")

      
  
        opcion = input("Seleccione una opcion: ")
        if opcion == '1':
            ContarPalabras(texto)
        elif opcion == '2':
            RemplazarPalabras(archivo, texto)
        elif opcion == '3':
            ContarCaracteres(texto)
        elif opcion == '4':
            break
        else:
            print("opcion no valida, es del 1 al 4")

def ContarPalabras(texto):
    Numpalabras = len(texto.split())
    print(f"El numero de palabras en el archivo es: {Numpalabras}")

def RemplazarPalabras(archivo, texto):
    PalabraRemplazar = input("Ingrese la palbra a remplazaar: ")
    NuevaPalabra = input("Ingrese la nueva palabra: ")

    textoModificado = texto.replace(PalabraRemplazar, NuevaPalabra)
    
    f = open(archivo, 'w')
    f.write(textoModificado)
    f.close()
    print(f"La palabra {PalabraRemplazar} ha sido remplazada por {NuevaPalabra}")
    return textoModificado


def ContarCaracteres(texto):
    Totaltexto = len(texto)
    CarateresSinEspacio = len(texto.replace(" ", ""))
    print(f"numero total de caracteres (contando espacios) {Totaltexto}")
    print(f"Numero de caracteres (sin espacios): {CarateresSinEspacio}")
  
def ProcesarArchivos_csv():
    archivo = input("Ingrese el nombre del archivo CSV: ")
    try:
        f = open(archivo, newline='')
        lector_csv = csv.reader(f)
        encabezado = next(lector_csv)
    except FileNotFoundError:
        print("El archivo no existe ")
        return
    finally:
        f.close

    while True:
        
        print(f"Submenu csv")
        print(f"1. Mostrar las 15 primera lineas")
        print(f"2. calcular estadisticas de una columna")
        print(f"3. Graficar una columna completa")
        print(f"4. volver al menu")

        opcion = input(f"Seleccione una opcion: ")
        if opcion == '1':
            mostrar_15_lineas(archivo)
        elif opcion == '2':
            CalcularEstadistica(archivo)
        elif opcion == '3':
            GraficarColumna(archivo)
        elif opcion == '4':
            print("Saliendo del programa")
            break
        else:
            print("opcion no valida, es del 1 al 4")

def mostrar_15_lineas(archivo):
    with open(archivo, newline='') as f:
        lector_csv = csv.DictReader(f)
        for i, fila in enumerate(lector_csv):
            if i >= 15:
                break
            print(fila)

def CalcularEstadistica(archivo):
    columna = input("Ingrese el nombre de la columna: ")
    with open(archivo, newline='') as f:
        lector_csv = csv.DictReader(f)
        datos = [] 
        for fila in lector_csv: 
            if fila[columna].replace('.', '', 1).isdigit(): 
                datos.append(float(fila[columna]))
    if not datos:
        print("No se encontró la columna seleccionada")
        return

    #uso de ia
    num_datos = len(datos)
    promedio = sum(datos) / num_datos
    datos_ordenados=sorted(datos)
    if num_datos % 2 != 0: 
        mediana = datos_ordenados[num_datos // 2] 
    else: 
        mediana = (datos_ordenados[num_datos // 2 - 1] + datos_ordenados[num_datos // 2]) / 2
    valor_max = max(datos)
    valor_min = min(datos)

    print(f"Número de datos: {num_datos}")
    print(f"Promedio: {promedio:.2f}")
    print(f"Mediana: {mediana:.2f}")
    print(f"Valor máximo: {valor_max}")
    print(f"Valor mínimo: {valor_min}")

def GraficarColumna(archivo):
    columna = input("Ingrese el nombre de la columna: ")
    with open(archivo, newline='') as f:
        lector_csv = csv.DictReader(f)
        datos = [] 
        for fila in lector_csv: 
            if fila[columna].replace('.', '', 1).isdigit(): 
                datos.append(float(fila[columna]))
        
    if not datos:
        print("No se encontraron datos")
        return

    plt.plot(datos)
    plt.title(f'Gráfica de la columna {columna}')
    plt.xlabel('Índice')
    plt.ylabel('Valor')
    plt.show()

if __name__ == "__main__":
    main()



