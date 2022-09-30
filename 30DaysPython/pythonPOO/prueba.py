
#TODO: 1er Ejercicio

def porcentage(num,porcentage=18):
    final = num * (porcentage/100)
    return final

# class Alumno:
    # def __init__(self,nombre,edad,direccion,asigAlumno,calificacionFinal):
        # self.nombre = nombre
        # self.edad = int(edad)
        # self.direccion = direccion
        # self.asigAlumno = asigAlumno
        # self.calificacionFinal = calificacionFinal
    # def imprimirDatos(self):
        # print(f"""
# Su nombre es: {self.nombre},
# su edad es: {self.edad},
# su direccion es: {self.direccion},
# su asignatura es: {self.asigAlumno},
# su calificacionFinal es: {self.calificacionFinal} 
                # """)
    # def mayorEdad(self):
        # if self.edad >= 18:
            # print("Usted es mayor edad")
        # else:
            # print("No es mayor de edad")

# miAlunmo = Alumno(
        # input("Ingrese su nombre: "),
        # input("Ingrese su edad: "),
        # input("Ingrese su direccion: "),
        # input("Ingrese su asignatura: "),
        # input("Ingrese su calificacionFinal: ")
        # )

# miAlunmo.imprimirDatos()
# miAlunmo.mayorEdad()

#TODO: 2do Ejercicio

# class cliente:
    # def __init__(self): 
        # self.precioProductos = []
        # while not len(self.precioProductos) == 4:
            # valores = int(input("Ingrese su valor del precio: "))
            # if valores > 0:
                # self.precioProductos.append(valores)
            # else:
                # continue
        # self.precioTotal= sum(self.precioProductos)
    # def formaDePago(self, formaDePago):
        # if formaDePago.lower() == 'tarjeta':
            # numCuenta = int(input("Ingrese su numero de cuenta: ")) 
            # precioFinal = self.precioTotal + porcentage(self.precioTotal)
            # print(f"Su numero de cuenta es {numCuenta}\nsu precio a pagar es de {precioFinal}\nGRACIAS POR SU COMPRA!!\n ")
        # else:
            # print(f"Su precio a pagar es de {self.precioTotal}\n ")

# miCliente = cliente()
# miCliente.formaDePago(input("Eliga su metodo de pago (Efectivo, Tarjeta): "))
            
#TODO: 3er Ejercicio

