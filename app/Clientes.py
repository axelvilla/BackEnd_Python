class Cliente:
    def __init__(self,codigo, nombre, apellido, dni, telefono, email):
        self.codigo = codigo
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.telefono = telefono
        self.email = email

# función para agregar cliente a la bd
def  agregar_cliente(self,codigo, nombre, apellido, dni, telefono, email):
    if self.consultar_cliente(codigo):
        return False       
    
    nuevo_cliente = {
        "codigo": codigo,
        "nombre": nombre,
        "apellido": apellido,
        "dni": dni,
        "telefono": telefono,
        "email": email
    }
    
    self.clientes.append(nuevo_cliente)
    return True

def consultar_cliente(self, codigo):
    for cliente in self.clientes:
        if cliente["codigo"] == codigo:
            return True
    return False

def modificar_cliente(self, codigo, nombre=None, apellido=None, dni=None, telefono=None, email=None):
    for cliente in self.clientes:
        if cliente["codigo"] == codigo:
            if nombre:
                cliente["nombre"] = nombre
            if apellido:
                cliente["apellido"] = apellido
            if dni:
                cliente["dni"] = dni
            if telefono:
                cliente["telefono"] = telefono
            if email:
                cliente["email"] = email
            return True
    return False

def eliminar_cliente(self, codigo):
    for cliente in self.clientes:
        if cliente["codigo"] == codigo:
            self.clientes.remove(cliente)
            return True 
    return False

def listar_clientes(self):
    print("-"*50)
    print("LISTADO DE CLIENTES")
    for cliente in self.clientes:
        print(f"Código: {cliente['codigo']}")
        print(f"Nombre: {cliente['nombre']}")
        print(f"Apellido: {cliente['apellido']}")
        print(f"DNI: {cliente['dni']}")
        print(f"Teléfono: {cliente['telefono']}")
        print(f"Email: {cliente['email']}")
        print("-"*50)
    