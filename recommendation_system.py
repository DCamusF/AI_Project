# Crear un sistema simple de recomendación de productos en Python.
# Debe tener productos con nombre, categoría y precio.
# El usuario debe ingresar una categoría.
# Mostrar los productos recomendados que pertenezcan a esa categoría.

productos = [
    {"nombre": "Laptop", "categoria": "tecnologia", "precio": 899.99},
    {"nombre": "Auriculares inalámbricos", "categoria": "tecnologia", "precio": 79.99},
    {"nombre": "Camiseta", "categoria": "ropa", "precio": 24.99},
    {"nombre": "Zapatillas deportivas", "categoria": "ropa", "precio": 59.99},
    {"nombre": "Cafetera", "categoria": "hogar", "precio": 49.99},
]

categoria_buscada = input("Ingresa una categoría: ").strip().lower()

recomendaciones = [
    producto
    for producto in productos
    if producto["categoria"].lower() == categoria_buscada
]

if recomendaciones:
    print(f"\nProductos recomendados de la categoría '{categoria_buscada}':")

    for producto in recomendaciones:
        print(f"- {producto['nombre']}: ${producto['precio']:.2f}")
else:
    print(
        f"\nNo se encontraron productos en la categoría "
        f"'{categoria_buscada}'."
    )