print("April Arzaba Diaz")
print("3W")
print("1173")
#esta linea creara un diccionario vacio
persona = {}

#esta linea pedira al usuario que ingrese datos correspondientes y llenara el diccionario
nombre = input("ingrese su nombre: ")
persona['nombre'] = nombre
print(persona)

edad = input("ingrese su edad: ")
persona['edad'] = edad
print(persona)

sexo = input("ingrese su sexo (M/F): ")
persona['sexo'] = sexo
print(persona)

telefono = input("ingrese su telefono: ")
persona['telefono'] = telefono
print(persona)

correo = input("ingrese su correo electronico: ")
persona['correo'] = correo
print(persona)

#esta linea imprimira el diccionario final
print("informacion completa de la persona:")
print(persona)
