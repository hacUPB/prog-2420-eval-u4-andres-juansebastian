import csv
import matplotlib.pyplot as plt
import os

def main():
    while True:
        print("Menu principal")
        print("1. Listar archivos presentes en la ruta actual o ingresar una ruta donde buscar los archivos")
        print("2. Procesar archivo de texto (.txt)")
        print("3. Procesar archivo separado por comas (.csv)")
        print("4. salir")


        opcion = input(f"Seleccione una opcion: ")
        if opcion == '1':
            listar_archivos()
        elif opcion == '2':
            ProcesarArchivos_txt()
        elif opcion == '3':
            ProcesarArchivos_csv()
        elif opcion == '4':
            print("Saliendo del programa")
            break
        else:
            print("opcion no valida, es del 1 al 4")

def listar_archivos():
    directorio = input("Ingrese la ruta del directorio: ") 
    if not os.path.isdir(directorio):
        print("La ruta ingresada no es válida o no es un directorio.")
        return
    with os.scandir(directorio) as archivos:
        for archivo in archivos:
            print(archivo.name)
    
def ProcesarArchivos_txt():    
    ruta_archivo = input("Ingrese la ruta completa del archivo de texto: ")
    try:
        with open(ruta_archivo, 'r') as f:
            texto = f.read()
        print("Contenido del archivo:")
        print(texto)
    except FileNotFoundError:
        print("El archivo no existe en la ruta especificada.")
    except IsADirectoryError:
        print("La ruta especificada es un directorio, no un archivo.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

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
            RemplazarPalabras(ruta_archivo, texto)
        elif opcion == '3':
            ContarCaracteres(texto)
        elif opcion == '4':
            break
        else:
            print("opcion no valida, es del 1 al 4")

def ContarPalabras(texto):
    Numpalabras = len(texto.split())
    print(f"El numero de palabras en el archivo es: {Numpalabras}")

def RemplazarPalabras(ruta_archivo, texto):
    PalabraRemplazar = input("Ingrese la palbra a remplazaar: ")
    NuevaPalabra = input("Ingrese la nueva palabra: ")

    textoModificado = texto.replace(PalabraRemplazar, NuevaPalabra)
    
    f = open(ruta_archivo, 'w')
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
    ruta_archivo = input("Ingrese la ruta completa del archivo CSV: ")
    try:
        with open(ruta_archivo, newline='') as f:
            lector_csv = csv.reader(f)
            encabezado = next(lector_csv)
            datos = []
            for fila in lector_csv:
                datos.append(fila)
    except FileNotFoundError:
        print("El archivo no existe en la ruta especificada.")
        return
    except IsADirectoryError:
        print("La ruta especificada es un directorio, no un archivo.")
        return
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return

    while True:
        
        print(f"Submenu csv")
        print(f"1. Mostrar las 15 primera lineas")
        print(f"2. calcular estadisticas de una columna")
        print(f"3. Graficar una columna completa")
        print(f"4. volver al menu")

        opcion = input(f"Seleccione una opcion: ")
        if opcion == '1':
            mostrar_15_lineas(ruta_archivo)
        elif opcion == '2':
            CalcularEstadistica(ruta_archivo)
        elif opcion == '3':
            GraficarColumna(ruta_archivo)
        elif opcion == '4':
            print("Saliendo del programa")
            break
        else:
            print("opcion no valida, es del 1 al 4")

def mostrar_15_lineas(ruta_archivo):
    with open( ruta_archivo, newline='') as f:
        lector_csv = csv.DictReader(f)
        for i, fila in enumerate(lector_csv):
            if i >= 15:
                break
            print(fila)

def CalcularEstadistica( ruta_archivo):
    columna = input("Ingrese el nombre de la columna: ")
    with open( ruta_archivo, newline='') as f:
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

def GraficarColumna( ruta_archivo):
    columna = input("Ingrese el nombre de la columna: ")
    with open( ruta_archivo, newline='') as f:
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