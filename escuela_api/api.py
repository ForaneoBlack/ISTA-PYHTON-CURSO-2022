from flask import Flask, jsonify
import json
import csv


app = Flask(__name__)
#Para ordenar los datos
def ordenar(key):
    return key["primer_nombre"] + key["primer_apellido"] 


@app.route('/lista_estudiantes', methods=['GET'])
def obtener_estudiantes():
    #Se lee y abre el archivo csv
    with open("../datos/estudiante.csv", "r") as archivo:
        archivo = csv.reader(archivo)
        next(archivo, None)
       # Declaramos un arreglo vacio
        estudiante = []
        # Comenzamos a recorrer nuestro archivo csv
        for fila in archivo:
           # Aqui colocamos como van a ir los datos      
            archiv = {'cedula': fila[0], 'primer_apellido': fila[1], 'segundo_apellido': fila[2],'primer_nombre': fila[3],'segundo_nombre': fila[4]}
            # Agregamos los datos a nuestro arreglo
            estudiante.append(archiv)
            #Ordenamos por orden la informacion
        estudiante.sort(key = ordenar)
        # Imprimimos todo nuestro arreglo ordenado, con diferentes mensajes de exito.
        return jsonify({'Estudiantes': estudiante, 'mensaje': "Estudiantes listados.", 'exito': True})


@app.route('/registro_asistencia', methods = ['POST'])
def registro_asistencia():
    # Leemos el archivo csv
    with open("../datos/asistencia.csv", "r") as file:
        archivo = csv.reader(file)
        next(archivo, None)
        #Declaramos un array vacio
        estudiante = []
        #Recorremos el array
        for fila in archivo:
            # Poenmos como van a salir los datos
            archiv = [fila[0], fila[1], fila[2], fila[3], fila[4]]
            #Agregamos los datos al array
            estudiante.append(archiv)
        
        # Colocamos los datos que vamos a ingresar como nuevos a nuestro archivo csv
        estudiante.append(["12131123423", "Lenguaje" , "2022", "07", "14"])
        #Abrimos el archivo para escribir en el
        with open("../datos/asistencia.csv", "w") as filer:
            # Agregamos y escribimos en una nueva fila los datos a nuestro archivo
            writer = csv.writer(filer)
            next(archivo, None)
            writer.writerows(estudiante)
    

if __name__ == '__main__':
    app.run(debug=True)
