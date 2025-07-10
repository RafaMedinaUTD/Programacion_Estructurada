
def borrarPantalla():
    import os
    os.system('cls')
    
def menu_principal():
    borrarPantalla()    
    print("📋..:: Sistema de Gestión de Agenda de Contactos ::..📋")
    print("\n\t 1️⃣ Agregar contacto")
    print("\t 2️⃣ Mostrar todos los contactos")
    print("\t 3️⃣ Buscar contacto por nombre")
    print("\t 4️⃣ Modificar contacto")
    print("\t 5️⃣ Eliminar contacto")
    print("\t 6️⃣ Salir")
    opc=input("\n\t 👉 Elige una opción (1-6): ")
    return opc

def esperarTecla():
    input("\n\n\tPresiona Enter para continuar...")

def agregar_contacto(agenda):
    borrarPantalla()
    print("📝..:: Agregar Contacto ::..📝")
    
    nombre = input("\n\tNombre del contacto: ").upper().strip()
    if nombre in agenda:
        print("❌ El contacto ya existe.")
    else:
        telefono = input("\tTeléfono del contacto: ").upper().strip()
        email = input("\tCorreo electrónico del contacto: ").lower().strip()
        agenda[nombre]=[telefono, email]
        print("\n\t✅ Contacto agregado exitosamente.")

def mostrar_contactos(agenda):
    borrarPantalla()
    print("📂..:: Lista de Contactos ::..📂")
    if not agenda:
        print("⚠️ No hay contactos en la agenda.")
    else:
        print(f"\n{'Nombre':<15} {'Teléfono':<15} {'Correo':<10}")
        print("-" * 60)
        for nombre,datos in agenda.items():
            print(f"{nombre:<15} {datos[0]:<15} {datos[1]:<10}")
        print("-" * 60)
    esperarTecla()
    
def buscar_contacto(agenda):
    borrarPantalla()
    print("🔎..:: Buscar Contacto ::..🔎")
    if not agenda:
        print("⚠️ No hay contactos en la agenda.")
        esperarTecla()
    else:
        nombre = input("\n\tNombre del contacto a buscar: ").upper().strip()
        if nombre in agenda:
            print("Usuario encontrado: \n")
            print("f{'Nombre':<15} {'# Telefono':<15} {'E-mail':<10}")
            print("-" * 60)
            print(f"{nombre:<15} {agenda[nombre][0]:<15} {agenda[nombre][1]:<10}")
            print("-" * 60)
            esperarTecla()
        else:
            print(f"❌ El contacto '{nombre}' no se encuentra en la agenda.")
            esperarTecla()

def modificar_contacto(agenda):
    borrarPantalla()
    print("➡️..:: Modificar Contacto ::..⬅️")
    if not agenda:
        print("⚠️ No hay contactos en la agenda.")
        esperarTecla()
    else:
        nombre = input("\n\tNombre del contacto a modificar: ").upper().strip()
        if nombre in agenda:
            print("Valores Actuales:\n")
            print(f"Nombre: {nombre}\nTelefono: {agenda[nombre][0]}\nCorreo: {agenda[nombre][1]}")
            resp=input("Deseas modificar este contacto? (Si/No): ").lower().strip()
            if resp == "si":
                telefono = input("\tNuevo teléfono del contacto: ").upper().strip()
                email = input("\tNuevo correo electrónico del contacto: ").lower().strip()
                agenda[nombre] = [telefono, email]
                print("\n\t✅ Contacto modificado exitosamente.")
            else:
                print("❌ Modificación cancelada.")
        else:
            print(f"❌ El contacto '{nombre}' no se encuentra en la agenda.")
            esperarTecla()

def borrar_contacto(agenda):
    borrarPantalla()
    print("🚮..:: Borrar Contacto ::..🚮")
    if not agenda:
        print("⚠️ No hay contactos en la agenda.")
        esperarTecla()
    else:
        nombre = input("\n\tNombre del contacto a eliminar: ").upper().strip()
        if nombre in agenda:
            print("Valores Actuales:\n")
            print(f"Nombre: {nombre}\nTelefono: {agenda[nombre][0]}\nCorreo: {agenda[nombre][1]}")
            resp=input("Deseas borrar este contacto? (Si/No): ").lower().strip()
            if resp == "si":
                agenda.pop(nombre)
                print("\n\t✅ Contacto borrado exitosamente.")
            else:
                print("❌ Borrar cancelado.")
        else:
            print(f"❌ El contacto '{nombre}' no se encuentra en la agenda.")