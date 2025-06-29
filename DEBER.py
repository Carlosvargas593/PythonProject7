def calcular_imc(peso_kg, altura_metros):
    """
    Calcula el Índice de Masa Corporal (IMC) de una persona.

    Args:
        peso_kg (float): El peso de la persona en kilogramos.
        altura_metros (float): La altura de la persona en metros.

    Returns:
        float: El valor del IMC calculado.
    """
    if altura_metros <= 0:
        print("Error: La altura debe ser mayor que cero.")
        return None

    imc = peso_kg / (altura_metros ** 2)
    return imc


def clasificar_imc(imc):
    """
    Clasifica el IMC en diferentes categorías de peso.

    Args:
        imc (float): El valor del IMC.

    Returns:
        str: La clasificación del IMC.
    """
    if imc is None:
        return "No se pudo clasificar el IMC debido a un error."
    elif imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif imc >= 30:
        return "Obesidad"
    else:
        return "Clasificación no disponible"


# --- Datos de ejemplo para la ejecución ---

# Uso de diferentes tipos de datos e identificadores descriptivos
nombre_persona = "María Pérez"  # Tipo de dato: string
edad_persona = 30  # Tipo de dato: integer
peso_persona_kg = 65.5  # Tipo de dato: float (ejemplo 1)
altura_persona_metros = 1.68  # Tipo de dato: float (ejemplo 1)
es_mayor_de_edad = True  # Tipo de dato: boolean

peso_persona_2_kg = 80.0  # Tipo de dato: float (ejemplo 2)
altura_persona_2_metros = 1.75  # Tipo de dato: float (ejemplo 2)

# --- Ejecución del programa con datos reales ---

print(f"--- Cálculo de IMC para {nombre_persona} ---")
print(f"Edad: {edad_persona} años, Mayor de edad: {es_mayor_de_edad}")

# Cálculo del IMC usando la función
imc_calculado = calcular_imc(peso_persona_kg, altura_persona_metros)

if imc_calculado is not None:
    print(f"Peso: {peso_persona_kg} kg, Altura: {altura_persona_metros} m")
    print(f"Su Índice de Masa Corporal (IMC) es: {imc_calculado:.2f}")

    # Clasificación del IMC
    clasificacion = clasificar_imc(imc_calculado)
    print(f"Clasificación: {clasificacion}")
else:
    print("No se pudo calcular el IMC.")

print("\n--- Otro ejemplo de cálculo de IMC ---")
imc_ejemplo_2 = calcular_imc(peso_persona_2_kg, altura_persona_2_metros)

if imc_ejemplo_2 is not None:
    print(f"Peso: {peso_persona_2_kg} kg, Altura: {altura_persona_2_metros} m")
    print(f"El IMC para este ejemplo es: {imc_ejemplo_2:.2f}")
    print(f"Clasificación: {clasificar_imc(imc_ejemplo_2)}")
else:
    print("No se pudo calcular el IMC para el segundo ejemplo.")