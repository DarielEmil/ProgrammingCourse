

def primerfuncion(f):
    def intervalo(): 
        print("Hola, la suma es de: ")
        return f
    return intervalo

@primerfuncion
def segundafuncion(a,b):
    return a+b

variable = primerfuncion(segundafuncion)

print(variable(5,5))
