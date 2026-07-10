#funciones
#menu
def mostrar_menu():
    print("========== MENÚ PRINCIPAL =========")
    print("1. Cupos por género")
    print("2. Búsqueda de película por rango de precio")
    print("3. Actualizar precio de película")
    print("4. Agregar película")
    print("5. Eliminar película")
    print("6. Salir")
    
def leer_opcion():
    while True:
        try:
            opcion = int(input("ingrese la opcion del menu : "))
            if opcion >= 1 and opcion <= 6 :
                
                print(opcion)
                return opcion
            
            else:
                print("el valor ingresado debe estar entre las opciones (1 a 6)")
        except ValueError:
             
             
             print("el valor ingresado debe ser un valor numerico")
def Numero_entero_positivoigual(valor):
    
    return valor >= 0

def Numero_entero_positivo(texto_precio):
    try:
        nuevo_precio_correcto = int(texto_precio)
        return nuevo_precio_correcto > 0
    except ValueError:
        print("el valor ingresado no es numerico")
        return False

    
def cupos_genero(genero , peliculas , cartelera):
    totalpeliculas_genero = 0
    for codigo , datos in peliculas.items():
        if peliculas[codigo][1].lower() == genero.lower():
            totalpeliculas_genero += cartelera[codigo][1]
    if totalpeliculas_genero != 0:
        print(f"el cantidad de peliculas de ese genero es {totalpeliculas_genero}") 
    else:
        print("no se encuentran peliculas de ese genero en el listado")

        
def busqueda_precio(precio_min , precio_max , peliculas , cartelera):
    peliculas_enprecio = []
    for codigo , datos in peliculas.items():
        precio = cartelera[codigo][0]
        stock = cartelera[codigo][1]
        if precio_min <= precio <= precio_max:
            peliculas_enprecio.append(f"Titulo : {peliculas[codigo][0]} --- {precio}")
    if len(peliculas_enprecio) == 0:
        print("no hay peliculas en ese rango de precio ")
    else:
        print(peliculas_enprecio)

        
def buscar_codigo(codigo , peliculas , cartelera):
    return codigo in peliculas.keys()


def  actualizar_precio(codigo , nuevo_precio , peliculas , cartelera):
    if buscar_codigo(codigo,peliculas,cartelera):
        cartelera[1] = nuevo_precio
        
def Validar_texto_vacio(texto):
    return texto.strip()!= ""
def Validar_clasificacion(clasificacion):
    return clasificacion.upper() in ("A" , "B" , "C")

def Validar_respuesta(respuesta):
   return respuesta.lower() in ("s" , "n")
        
def Agregar_pelicula(codigo , titulo , genero , duracion , clasificacion , idioma , es_3d , precio , cupos , peliculas , cartelera):
    peliculas[codigo] = [titulo , genero , duracion , clasificacion , idioma , es_3d , precio , cupos]
    cartelera[codigo] = [precio , stock]
def Eliminar_pelicula(codigo , peliculas , catalogo):
    if codigo in peliculas:
        del peliculas[codigo]
        del catalogo[codigo]

    

#programa principal
#diccionarios
peliculas = {
    "P101" : ["Luz de Otoño" , "drama" , 110 , "b" , "español " , False],
    "P102" : ["Noche Neón" , "accion" , 125 , "c" , "ingles" , True] ,
    "P103" : ["Planeta Agua" , "documental" , 90 , "a" , "español ", False],
    "P104" : ["Risa Total" , "comedia" , 105 , "a" , "español" , True],
    "P105" : ["Código Zero" , "thriller" , 118 , "c" , "ingles" , True],
    "P106" : ["Viaje Lunar" , "ciencia ficcion" , 132 , "b" , "ingles" , False]
    }
cartelera = {
    "P101" : [5990 , 40],
    "P102" : [7990 , 0] ,
    "P103" : [4990 , 25],
    "P104" : [6990 , 12],
    "P105" : [8990 , 8],
    "P106" : [7490 , 3]
    }
opcion = 0
while opcion != 6 :
    
    mostrar_menu()
    opcion = leer_opcion()
    
    if opcion == 1 :
        genero = input("Ingrese el genero de peliculas a buscar :").lower()
        cupos_genero(genero, peliculas , cartelera )
    elif opcion == 2 :
        precio_min = None
        precio_max = None
        while precio_min == None and precio_max == None:
            try:
                precio_min = int(input("Ingrese el valor minimo a buscar :"))
                precio_max = int(input("Ingrese el valor maximo a buscar :"))
                

            except ValueError:
                print("Los valores ingresados deben ser numericos")
                precio_min = None
                precio_max = None
        busqueda_precio(precio_min , precio_max , peliculas , cartelera)        
    elif opcion == 3:
        respuesta = "s"
        while respuesta == "s":
        
            codigo = input("ingrese el codigo de la pelicula a buscar :").upper()
            
            if buscar_codigo(codigo , peliculas , cartelera):
                precio_nuevo = input("ingrese el nuevo valor de la pelicula :").lower()
                    
                if not Numero_entero_positivo(precio_nuevo):

                    print("El valor ingresado es incorrecto")
                    respuesta = input("¿Desea actualizar otro precio (s/n) ?")
                        
                else :
                    actualizar_precio(codigo ,precio_nuevo , peliculas , cartelera)
                    print("Precio actualizado")
                    
                  
            else:
                print("El codigo no existe")
                respuesta = input("¿Desea actualizar otro precio (s/n) ?")
                
    elif opcion == 4:
        dato_valido = True

        if dato_valido == True:
            
            codigo = input("Ingrese el codigo de la nueva pelicula a ingresar :")
            
            if buscar_codigo(codigo , peliculas , cartelera):
                
                print("el codigo ya existe")
                dato_valido = False
                
            if not Validar_texto_vacio(codigo):
                
                print("el codigo ingresado no es valido o no puede estar vacio ")
                
                dato_valido = False
                
        if dato_valido == True:
            titulo = input("ingrese titulo :")
            if not Validar_texto_vacio(titulo):
                print("el titulo no puede estar vacio")
                dato_valido = False
            
        if dato_valido == True:
            genero = input("ingrese genero :")
            if not Validar_texto_vacio(genero):
                print("el genero no puede estar vacio")
                dato_valido = False
            
                
        if dato_valido == True:
            
            duracion = int(input("ingrese duracion (minutos) :"))
                           
            if not Numero_entero_positivo(duracion):
                print("el valor ingresado debe ser un numero mayor a 0")
                dato_valido = False
                
        if dato_valido == True:
            clasificacion = input("Ingrese clasificacion :").upper()
            if not Validar_clasificacion(clasificacion):
                print("el valor debe ser entre (A/B/C)")
                dato_valido = False
        if dato_valido == True:
            idioma = input("ingrese idioma :")
            if not Validar_texto_vacio(idioma):
                print("el idioma no puede estar vacio")
                dato_valido = False
            
        if dato_valido == True:
                            
            es_3d = input("Es 3D (s/n) :").lower()
            if not Validar_respuesta(es_3d):
                print("el valor ingresado debe ser (s/n)")
                dato_valido == False
            
        if dato_valido == True:
            precio = int(input("Ingrese valor :"))
            if not Numero_entero_positivo(precio):
                print("el numero ingresado debe ser entero positivo")
                dato_valido == False
                
        if dato_valido == True:
            stock = int(input("Ingrese cupos :"))
            if not Numero_entero_positivoigual(stock):
                print("el numero ingresado debe ser mayor o igual a 0")
                
                        
        Agregar_pelicula(codigo , titulo , genero , duracion , clasificacion , idioma , es_3d , precio , stock , peliculas , cartelera)
        print("pelicula Agregada")
            
        
    elif opcion == 5:
        codigo = input("ingrese el codigo de la pelicula a eliminar ")
        if Buscar_codigo(codigo):
            Eliminar_codigo(codigo)
            print("pelicula eliminada")
        else:
            print("el codigo no existe")
            
            
                       
        
            
                         
    elif opcion == 6:
        print("Programa finalizado")
        
        
            
              
            
                                        
                               
                           
                        
                    
                        
                        
                    
                                         
        
        

        
        
                       
                       
        
