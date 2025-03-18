# -*- coding: utf-8 -*-
# lista con diccionario
contactos = [
    {
        'nombre': 'Victor',
        'email': 'victor@victor.com',
        'telefono': '1'
    },
    {
        'nombre': 'Luis',
        'email': 'Luis@Luis.com',
        'telefono': '2'
    },
    {
        'nombre': 'Salvador',
        'email': 'Salvador@salvador.com',
        'telefono': '3'
    }
]

print(contactos[0]['nombre'])
# Output: Victor

for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}")
    print(f"Email del contacto: {contacto['email']}")
    print(f"Telefono del contacto: {contacto['telefono']}")
    print("\n")
