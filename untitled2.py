# -*- coding: utf-8 -*-
"""Untitled2.ipynb
xadfsfdfdfsadfsadfsadfsadfsadfsaadfsdfadfsadfsadfsadfsadfs
Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13nCYTs6z7h4n7iw3Psy0oDkWdVFHGzJ5
"""

total = 0
while true:
  print("Bienvenido a PizzasDuoc")
  tipo_alumno = input("Ingrese el tipo de alumno (1-diurna/2-vespertina/3-administrativo o ingrese 0 para salir): ")
  if tipo_alumno = "0":
    break
  
  if 




while True:
    print("----- MENÚ RAPID -----")
    print("1. Pizza Tradicional - $12.000")
    print("2. Pizza Peperoni - $14.000")
    print("3. Pizza All carnes - $17.000")
    print("-----------------------")

    opcion = input("Seleccione una pizza (1-3) o ingrese '0' para anular el pedido: ")

    if opcion == "0":
        break

    if opcion in ["1", "2", "3"]:
        cantidad = int(input("Ingrese la cantidad de pizzas a pedir: "))
        if opcion == "1":
            total += 12000 * cantidad
        elif opcion == "2":
            total += 14000 * cantidad
        elif opcion == "3":
            total += 17000 * cantidad
    else:
        print("Opción inválida. Intente nuevamente.")
        continue

    continuar = input("¿Desea agregar más pizzas? (S/N): ")
    if continuar.upper() != "S":
        break

descuento = 0

if tipo_alumno == "diurna":
    descuento = total * 0.12
elif tipo_alumno == "vespertina":
    descuento = total * 0.10

total_pagar = total - descuento

print("----- Resumen del Pedido -----")
print("Subtotal: $", total)
print("Descuento: $", descuento)
print("Total a Pagar: $", total_pagar)

print("Formas de Pago:")
print("1. Efectivo")
print("2. Otro medio de pago")

opcion_pago = input("Seleccione una forma de pago: ")
if opcion_pago == "1":
    monto_pago = float(input("Ingrese el monto con el que paga: "))
    vuelto = monto_pago - total_pagar
    print("Vuelto:", vuelto)
else:
    monto_pago = total_pagar

print("Forma de Pago: Efectivo" if opcion_pago == "1" else "Forma de Pago: Otro medio de pago")
print("Monto de Pago: $", monto_pago)
print("Gracias por su preferencia!")

"""opcion 2 codigo"""

total = 0
continuar_pedido = True
print("Bienvenido a PizzasDuoc")

tipo_alumno = ""

while tipo_alumno not in ["1", "2", "3"]:
    tipo_alumno = input("elija de 1 al 3 el tipo de alumno (1 diurna/2 vespertina/3 administrativo): ")
    
    if tipo_alumno == "1":
        print("¡Hola alumno diurno! Disfruta de nuestra promoción especial.")
    elif tipo_alumno == "2":
        print("¡Hola alumno vespertino! Aprovecha nuestro descuento nocturno.")
    elif tipo_alumno == "3":
        print("¡Hola personal administrativo! Te ofrecemos un beneficio exclusivo.")
    else:
        print("Lo siento, el tipo de alumno ingresado no es válido.")

while continuar_pedido:
    print("----- MENÚ RAPID -----")
    print("1. Pizza Tradicional - $12.000")
    print("2. Pizza Peperoni - $14.000")
    print("3. Pizza All carnes - $17.000")
    print("-----------------------")

    opcion = input("Seleccione una pizza (1-3) o ingrese '0' para anular el pedido: ")

    if opcion == "0":
        continuar_pedido = False
    elif opcion in ["1", "2", "3"]:
        cantidad = int(input("Ingrese la cantidad de pizzas a pedir: "))
        if opcion == "1":
            total += 12000 * cantidad
        elif opcion == "2":
            total += 14000 * cantidad
        elif opcion == "3":
            total += 17000 * cantidad
    else:
        print("Opción inválida. Intente nuevamente.")
        continue

    continuar = input("¿Desea agregar más pizzas? (S/N): ")
    if continuar.upper() != "S":
        continuar_pedido = False

descuento = 0

if tipo_alumno == "1":
    descuento = total * 0.12
elif tipo_alumno == "2":
    descuento = total * 0.10

total_pagar = total - descuento

print("----- Resumen del Pedido -----")
print("Subtotal: $", total)
print("Descuento: $", descuento)
print("Total a Pagar: $", total_pagar)

print("Formas de Pago:")
print("1. Efectivo")
print("2. Otro medio de pago")
opcion_pago = ""

while opcion_pago not in {"1", "2"}:
   opcion_pago = input("Seleccione una forma de pago: ")

   if opcion_pago == "1":
       monto_pago = float(input("Ingrese el monto con el que paga: "))
       vuelto = monto_pago - total_pagar
       print("Vuelto:", vuelto)
    elif opcion_pago == "2":
       monto_pago = total_pagar
    else:
       print("opcion no valida")

print("Forma de Pago: Efectivo" if opcion_pago == "1" else "Forma de Pago: Otro medio de pago")
print("Monto de Pago: $", monto_pago)
print("Gracias por su preferencia!")

#CODIGO CASI FINAL
total = 0
continuar_pedido = True
print("Bienvenido a PizzasDuoc")

tipo_alumno = ""
while tipo_alumno not in ["1", "2", "3", "4"] and continuar_pedido:
    tipo_alumno = input("Elija del 1 al 3 el tipo de alumno y 4 para salir:\n1. Diurna\n2. Vespertina\n3. Administrativo : ")
    if tipo_alumno == "1":
        print("¡Hola alumno diurno! Disfruta de nuestra promoción especial.")
    elif tipo_alumno == "2":
        print("¡Hola alumno vespertino! Aprovecha nuestro descuento nocturno.")
    elif tipo_alumno == "3":
        print("¡Hola personal administrativo! Te ofrecemos un beneficio exclusivo.")
    elif tipo_alumno == "4":
        print("¡Muchas gracias, hasta pronto!")
        continuar_pedido = False
    else:
        print("Lo siento, el tipo de alumno ingresado no es válido.")

print("---------------------------------------------------------------------------------")
try:   
 if continuar_pedido:
    while continuar_pedido:
        print("----- MENÚ RÁPIDO -----")
        print("1. Pizza Tradicional - $12.000")
        print("2. Pizza Peperoni - $14.000")
        print("3. Pizza All Carnes - $17.000")
        print("-----------------------")

        opcion = input("Seleccione una pizza (1-3) o ingrese 4 para anular el pedido: ")

        if opcion == "4":
            total = 0
            continuar_pedido = False
            print("¡Hasta luego!")
            break
        elif opcion in ["1", "2", "3"]:
            cantidad = int(input("Ingrese la cantidad de pizzas a pedir: "))
            if opcion == "1":
                total += 12000 * cantidad
            elif opcion == "2":
                total += 14000 * cantidad
            elif opcion == "3":
                total += 17000 * cantidad
            else:
              print("Opción inválida. Intente nuevamente.")
              continuar = "s"
        continuar = input("¿Desea agregar más pizzas? (S/N): ")
        if continuar == "S":
            continuar_pedido = False
        else:
            print("Comando no válido.")         
except ValueError:
 print("NO SE A INGRESADO UN NUMERO")


print("---------------------------------------------------------------------------------")
descuento = 0
opcion_pago = ""
try:
 while opcion_pago not in ["1", "2", "4"]:
    opcion_pago = input("Seleccione una forma de pago:\n1. Efectivo\n2. Débito/Crédito\nOpción: ")

 while opcion_pago == "1":
    monto_pago = float(input("Ingrese el monto con el que paga: "))
    if monto_pago < total:
        print("El monto ingresado es insuficiente. Intente nuevamente.")
    else:
        vuelto = monto_pago - total
        print("Vuelto:", vuelto)
        break
 else:
    monto_pago = total

 if tipo_alumno == "1":
    descuento = total * 0.12
 elif tipo_alumno == "2":
    descuento = total * 0.10
except ValueError:
 print("no se a realizado el pedido")
try:
    print("----- Resumen del Pedido -----")
    print("Subtotal: $", total)
    print("Descuento: $", descuento)
    print("Total a Pagar: $", total - descuento)
    print("Forma de Pago: Efectivo" if opcion_pago == "1" else "Forma de Pago: Otro medio de pago")
    print("Monto de Pago: $", monto_pago)
    print("¡Gracias por su preferencia!")
except NameError:
    print("No se le ha cobrado.")

total = 0
continuar_pedido = True
print("Bienvenido a PizzasDuoc")

tipo_alumno = ""
while tipo_alumno not in ["1", "2", "3", "4"] and continuar_pedido:
  tipo_alumno = input("elija de 1 al 3 el tipo de alumno y 4 para salir \n 1 diurna \n2 vespertina \n3 administrativo \n- ")
  if tipo_alumno == "1":
        print("bienvenido alumno diurno.")
  elif tipo_alumno == "2":
        print("bienvenido alumno vespertino.")
  elif tipo_alumno == "3":
        print("bienvenido alumno vespertino.")
  elif tipo_alumno == "4":
        print("muchas gracias, hasta pronto ")
        continuar_pedido = False
  else:
   print("Lo siento, el tipo de alumno ingresado no es válido.")


print("---------------------------------------------------------------------------------")
try:
 if continuar_pedido:
  while continuar_pedido:
    print("----- MENÚ RAPIDO -----")
    print("1. Pizza Tradicional - $12.000")
    print("2. Pizza Peperoni - $14.000")
    print("3. Pizza All carnes - $17.000")
    print("-----------------------")

    opcion = input("Seleccione una pizza (1-3) o ingrese 4 para anular el pedido: ")

    if opcion == "4":
        total = 0
        continuar_pedido = False
        print("hasta luego")
        break
    elif opcion not in ["1", "2", "3"]:
        cantidad = int(input("Ingrese la cantidad de pizzas a pedir: "))
    if opcion == "1":
            total += 12000 * cantidad
    elif opcion == "2":
            total += 14000 * cantidad
    elif opcion == "3":
            total += 17000 * cantidad
    else:
          print("Opción inválida. Intente nuevamente.")
    continuar = input("¿Desea agregar más pizzas? (S/N): ")
    if continuar.upper() != "S":
          continuar_pedido = False
    else:
      print("commando no valido")
      
except ValueError:
 print("comando invalido")
 continuar_pedido = True

print("---------------------------------------------------------------------------------")
descuento = 0
opcion_pago = ""
try:
 while opcion_pago not in ["1", "2"]:
    opcion_pago = input("Seleccione una forma de pago:\n1. Efectivo\n2. Débito/Crédito\nOpción: ")

 while opcion_pago == "1":
    monto_pago = float(input("Ingrese el monto con el que paga: "))
    if monto_pago < total:
        print("El monto ingresado es insuficiente. Intente nuevamente.")
    else:
        vuelto = monto_pago - total
        print("Vuelto:", vuelto)
        break
 else:
    monto_pago = total

 if tipo_alumno == "1":
    descuento = total * 0.12
 elif tipo_alumno == "2":
    descuento = total * 0.10
except ValueError:
 print("no se a realizado el pedido")
try:
    print("----- Resumen del Pedido -----")
    print("Subtotal: $", total)
    print("Descuento: $", descuento)
    print("Total a Pagar: $", total - descuento)
    print("Forma de Pago: Efectivo" if opcion_pago == "1" else "Forma de Pago: Otro medio de pago")
    print("Monto de Pago: $", monto_pago)
    print("¡Gracias por su preferencia!")
except NameError:
    print("No se le ha cobrado.")

#corregido_con_chat_gpt
while True:
    total = 0
    continuar_pedido = True
    print("Bienvenido a PizzasDuoc")

    while True:
        tipo_alumno = input("Elija del 1 al 3 el tipo de alumno y 4 para salir:\n1. Diurna\n2. Vespertina\n3. Administrativo\nOpción: ")
        if tipo_alumno == "1":
            print("¡Hola alumno diurno! Disfruta de nuestra promoción especial.")
            break
        elif tipo_alumno == "2":
            print("¡Hola alumno vespertino! Aprovecha nuestro descuento nocturno.")
            break
        elif tipo_alumno == "3":
            print("¡Hola personal administrativo! Te ofrecemos un beneficio exclusivo.")
            break
        elif tipo_alumno == "4":
            print("¡Muchas gracias, hasta pronto!")
            continuar_pedido = False
            break
        else:
            print("Lo siento, el tipo de alumno ingresado no es válido.")

    if not continuar_pedido:
        break

    print("---------------------------------------------------------------------------------")

    while continuar_pedido:
        print("----- MENÚ RÁPIDO -----")
        print("1. Pizza Tradicional - $12.000")
        print("2. Pizza Peperoni - $14.000")
        print("3. Pizza All Carnes - $17.000")
        print("-----------------------")

        opcion = input("Seleccione una pizza (1-3) o ingrese 4 para anular el pedido: ")

        if opcion == "4":
            total = 0
            continuar_pedido = False
            print("¡Hasta luego!")
            break

        elif opcion in ["1", "2", "3"]:
            cantidad = int(input("Ingrese la cantidad de pizzas a pedir: "))
            if opcion == "1":
                total += 12000 * cantidad
            elif opcion == "2":
                total += 14000 * cantidad
            elif opcion == "3":
                total += 17000 * cantidad
        else:
            print("Opción inválida. Intente nuevamente.")
            continue

        continuar = input("¿Desea agregar más pizzas? (S/N): ")
        if continuar.upper() != "S":
            continuar_pedido = False
        else:
            print("Comando no válido.")

    descuento = 0

    print("---------------------------------------------------------------------------------")

    while True:
        opcion_pago = input("Seleccione una forma de pago:\n1. Efectivo\n2. Débito/Crédito\nOpción: ")
        if opcion_pago == "1":
            monto_pago = float(input("Ingrese el monto con el que paga: "))
            vuelto = monto_pago - total
            if vuelto < 0:
                print("El monto ingresado es insuficiente. Intente nuevamente.")
                continue
            else:
                print("Vuelto:", vuelto)
            break
        elif opcion_pago == "2":
            monto_pago = total
            continuar_pedido = True
            break
        else:
            print("Opción inválida. Intente nuevamente.")

    if tipo_alumno == "1":
        descuento = total * 0.12
    elif tipo_alumno == "2":
        descuento = total * 0.10

    try:
        print("----- Resumen del Pedido -----")
        print("Subtotal: $", total)
        print("Descuento: $", descuento)
        print("Total a Pagar: $", total - descuento)
        print("Forma de Pago: Efectivo" if opcion_pago == "1" else "Forma de Pago: Otro medio de pago")
        print("Monto de Pago: $", monto_pago)
        print("¡Gracias por su preferencia!")
    except NameError:
        print("No se le ha cobrado.")

    reiniciar = input("¿Desea realizar otro pedido? (S/N): ")
    if reiniciar.upper() != "S":
        break
