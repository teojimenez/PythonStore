class Usuario:
    def __init__(self, nombre, apellido, usuario, password):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__usuario = usuario
        self.__password = password

    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_apellido(self):
        return self.__apellido
    def set_apellido(self, apellido):
        self.__apellido = apellido

    def get_usuario(self):
        return self.__usuario
    def set_usuario(self, usuario):
        self.__usuario = usuario

    def get_password(self):
        return self.__password
    def set_password(self, password):
        self.__password = password

class Producto():
    def __init__(self, id, nombre, precio):
        self.__id = id
        self.__nombre = nombre
        self.__precio = precio

    def get_id(self):
        return self.__id
    def set_id(self, id):
        self.__id = id 

    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_precio(self):
        return self.__precio
    def set_precio(self, precio):
        self.__precio = precio 

usuario = Usuario('','','','')
producto = Producto('','','')

def añadirUsuario():
    InpNombre = input("Introduzca su nombre: ")
    InpApellido = input("Introduzca su apellido: ")
    InpUsuario = input("Introduzca su usuario: ")
    with open('usuario.txt', 'r+') as archivo:
        lineas = archivo.readlines()
        for indice,linea in enumerate(lineas):
            datosLinea = linea.strip().split(',')
            if datosLinea[2] == InpUsuario:
                print("Este usuario ya esta escogido, debe escoger uno diferente\n")
                añadirUsuario()
                break
        archivo.close()

    InpPassword = input("Introduzca su password: ")
    usuario = Usuario(InpNombre, InpApellido, InpUsuario, InpPassword)
    with open('usuario.txt' , 'a') as datos:
        datos.write(f"{usuario.get_nombre()},{usuario.get_apellido()},{usuario.get_usuario()},{usuario.get_password()}\n")
        datos.close()
    menuP()

def login():
    valido = False
    LogUsuario = input("\nIntroduzca su usuario: ")
    LogContraseña = input("Introduzca su contraseña: ")
    with open('usuario.txt', 'r') as datosUsuario:
        for linea in datosUsuario:
            partes = linea.strip().split(',')
            #if(partes[2] == LogUsuario and partes[3] == LogContraseña):
            if(LogUsuario == usuarioAdmin and LogContraseña == passwordAdmin):
                usuario.set_nombre(partes[0])
                usuario.set_apellido(partes[1])
                usuario.set_usuario(partes[2])
                usuario.set_password(partes[3])
                valido = True
                menuAdmin()
            elif len(partes) >= 4 and partes[2] == LogUsuario and partes[3] == LogContraseña:
                usuario.set_nombre(partes[0])
                usuario.set_apellido(partes[1])
                usuario.set_usuario(partes[2])
                usuario.set_password(partes[3])
                valido = True
                menuCliente()
        if not valido:
            option = input("El usuario no existe o los datos son incorrectos\n\nElija:\n1. Login\n2. Salir\n")
            if option == '1':login()
            elif option == '2':menuP()
            else:menuP()
    datosUsuario.close()

def verProductos():
    with open('producto.txt', 'r') as datosProductos:
        for linea in datosProductos:
            partes = linea.strip().split(',')
            print(f"| id:{partes[0]} || nombre:{partes[1]} || precio:{partes[2]}€ |")
            
        datosProductos.close()
        menuCliente()

def comprarProductos():
    encontrado2 = False
    option = input("Elija que producto quiere comprar: ")
    with open('producto.txt', 'r') as datos:
        for linea in datos:
            partes = linea.strip().split(',')
            if(option == partes[0]): #id
                producto.set_id(partes[0])
                producto.set_nombre(partes[1])
                producto.set_precio(partes[2])
                with open('factura.txt' , 'a') as datos:
                    datos.write(f"{usuario.get_usuario()},{producto.get_nombre()},{producto.get_precio()}\n")
                    datos.close()
                encontrado2 = True
                break
        datos.close()
    if encontrado2:
        print("Compra realizada con éxito.")
        menuCliente()
    else:
        print(f"El id {option} no pertenece ningun producto. Introduce un producto existente")
        comprarProductos()


def modificarDatos():
    print("\n1. nombre\n2. apellido\n3. usuario\n4. contraseña\n")
    option = input("Que dato quiere modificar?: ")
    controlPass = False
    if option == '1':
        new = input("Introduzca el nuevo: ")
        old = usuario.get_nombre()
        usuario.set_nombre(new)
        elemento = 0
    elif option == '2':
        new = input("Introduzca el nuevo: ")
        old = usuario.get_apellido()
        usuario.set_apellido(new)
        elemento = 1
    elif option == '3':
        new = input("Introduzca el nuevo: ")
        old = usuario.get_usuario()
        usuario.set_usuario(new)
        elemento = 2
        controlPass = True
    elif option == '4':
        new = input("Introduzca el nuevo: ")
        old = usuario.get_password()
        usuario.set_password(new)
        elemento = 3

    with open('usuario.txt', 'r+') as archivo:
        lineas = archivo.readlines()
        for indice,linea in enumerate(lineas):
            datosLinea = linea.strip().split(',')
            if datosLinea[elemento] == old and datosLinea[2] == usuario.get_usuario():
                datosLinea[elemento] = new
                lineas[indice] = ','.join(datosLinea)+ '\n'
                break
            elif datosLinea[elemento] == old and controlPass: #caso usuario
                datosLinea[elemento] = new
                lineas[indice] = ','.join(datosLinea)+ '\n'
                break
        archivo.seek(0)
        archivo.writelines(lineas)
        archivo.truncate()
        archivo.close()
        menuCliente()

def crearProductos():
    InpId = input("\nIntroduzca el ID: ")
    InpNombre = input("Introduzca el nombre: ")
    InpPrecio = input("Introduzca el precio: ")
    producto = Producto(InpId, InpNombre, InpPrecio)
    with open('producto.txt' , 'a') as datos:
        datos.write(f"{producto.get_id()},{producto.get_nombre()},{producto.get_precio()}\n")
        datos.close()
    menuAdmin()

def modificarProductos():
    with open('producto.txt', 'r') as datosProductos:
        for linea in datosProductos:
            partes = linea.strip().split(',')
            print(f"| id:{partes[0]} || nombre:{partes[1]} || precio:{partes[2]}€ |")
            
        datosProductos.close()
    option = input("\nSeleccione el id: ")
    optionAtrib = input("Que quiere modificar?\n1. Nombre\n2. Precio\n")
    if optionAtrib == '1':
        new = input("Introduzca el nuevo: ")
        producto.set_nombre(new)
        elemento = 1
    elif optionAtrib == '2':
        new = input("Introduzca el nuevo: ")
        producto.set_precio(new)
        elemento = 2
    else:
        print("Introduzca un id existente\n")
        modificarProductos()

    with open('producto.txt', 'r+') as archivo:
        lineas = archivo.readlines()
        for indice,linea in enumerate(lineas):
            datosLinea = linea.strip().split(',')

            if datosLinea[0] == option:
                datosLinea[elemento] = new
                lineas[indice] = ','.join(datosLinea)+ '\n'
                break
        archivo.seek(0)
        archivo.writelines(lineas)
        archivo.truncate()
        archivo.close()
        menuAdmin()

def verUsuarios():
    with open('usuario.txt', 'r') as datosUsuarios:
        for linea in datosUsuarios:
            partes = linea.strip().split(',')
            print(f"| usuario:{partes[2]} || contraseña:{partes[3]} |")
            
        datosUsuarios.close()

def eliminarUsuarios():
    eliminado = False
    verUsuarios()
    usuarioAEliminar = input("\nIntroduzca el usuario a eliminar: ")
    with open('usuario.txt', 'r') as datos:
        lineas = datos.readlines()
    with open('usuario.txt', 'w') as datos:
        for linea in lineas:
            partes = linea.strip().split(',')
            if partes[2] != usuarioAEliminar:
                datos.write(linea)
            elif partes[2] == usuarioAdmin:
                print("El usuario admin no se puede eliminar\n")
                break
            else:
                eliminado = True
        datos.close()
    if eliminado:
        print(f"El usuario {usuarioAEliminar} ha sido eliminado correctamente.\n")
        menuAdmin()
    elif partes[2] == usuarioAdmin:
        eliminarUsuarios()
    else:
        print(f"No se ha encontrado ningún usuario {usuarioAEliminar}.")

def facturacion():
    print("\n1. Facturacion total\n2. Facturacion de un usuario\n")
    option = input("Que facturacion desea ver?")
    facturacionT = 0
    if option == '1':
        with open('factura.txt', 'r') as datos:
            for linea in datos:
                partes = linea.strip().split(',')
                facturacionT += float(partes[2])
            datos.close()
            print(f"La facturacion total es de {facturacionT}€")
            menuAdmin()
    elif option == '2':
        verUsuarios()
        facturacionC = 0
        usuarioEleg = input("\nElige un usuario:\n")
        with open('factura.txt', 'r+') as archivo:
            lineas = archivo.readlines()
            for indice,linea in enumerate(lineas):
                datosLinea = linea.strip().split(',')
                if datosLinea[0] == usuarioEleg:
                    facturacionC += float(datosLinea[2])
            archivo.close()
            print(f"La facturacion de {usuarioEleg} es de {facturacionC}€")
            menuAdmin()
    else:
        print("Introduce un valor admitido")
        facturacion()

def menuP():
    print("\nMenu Principal\n--------------------")
    print("\033[31m1.\033[0m Registro Usuario\n\033[31m2.\033[0m Login\n\033[31m3.\033[0m Exit")
    option = input("Elija: ")
    if option == '1': añadirUsuario()
    elif option == '2': login()
    elif option == '3': exit()
    else:
        print("Introduzca una de las opciones anteriores\n")
        menuP()

def menuCliente():
    print("\nMenu Cliente\n--------------------")
    print("\033[31m1.\033[0m Ver productos\n\033[31m2.\033[0m Comprar productos\n\033[31m3.\033[0m Modificar sus datos\n\033[31m4.\033[0m Salir")    
    option = input("Elija: ")
    if option == '1': verProductos()
    elif option == '2': comprarProductos()
    elif option == '3': modificarDatos()
    elif option == '4': menuP()
    else:
        print("Introduzca una de las opciones anteriores\n")
        menuCliente()

def menuAdmin():
    print("\nMenu Admin\n--------------------")
    print("\033[31m1.\033[0m Crear productos\n\033[31m2.\033[0m Modificar productos\n\033[31m3.\033[0m Eliminar Usuarios\n\033[31m4.\033[0m Facturación\n\033[31m5.\033[0m Salir")
    option = input("Elija: ")
    if option == '1': crearProductos()
    elif option == '2': modificarProductos()
    elif option == '3': eliminarUsuarios()
    elif option == '4': facturacion() 
    elif option == '5': menuP()
    else: 
        print("Introduzca una de las opciones anteriores\n")
        menuAdmin()


archivo = open('usuario.txt', 'w+')
archivo.close()
archivo2 = open('producto.txt', 'w+')
archivo2.close()
archivo3 = open('factura.txt', 'w+')
archivo3.close()
#datos admin: -------------------------------------------------------------
usuarioAdmin = "root"
passwordAdmin =  "root12345"

encontrado = False
with open('usuario.txt', 'r') as datosUsuario:
    for linea in datosUsuario:
        partes = linea.strip().split(',')
        if (partes[2] == usuarioAdmin and partes[3] == passwordAdmin):
            encontrado = True
            datosUsuario.close()
            break
if not encontrado:
    with open('usuario.txt' , 'a') as datos:
        datos.write(f"admin,administrador,{usuarioAdmin},{passwordAdmin}\n")
        datos.close()
#--------------------------------------------------------------------------
menuP()