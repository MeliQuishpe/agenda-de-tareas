# *Agenda de Tareas - Sprint 2*

tareas = []

def agregar_tarea(titulo):
    if titulo.strip():
        tarea = {"titulo": titulo, "completada": False}
        tareas.append(tarea)
        return "Tarea agregada."
    return "Error: la tarea no puede estar vacía."

def eliminar_tarea(indice):
    if 0 <= indice < len(tareas):
        tarea = tareas.pop(indice)
        return f"Tarea eliminada: {tarea['titulo']}"
    return "Índice inválido."

def mostrar_tareas():
    if not tareas:
        return "No hay tareas registradas."
    resultado = []
    for i, t in enumerate(tareas):
        estado = "✅" if t["completada"] else "❌"
        resultado.append(f"{i}. {t['titulo']} - {estado}")
    return "\n".join(resultado)

def marcar_completada(indice):
    if 0 <= indice < len(tareas):
        tareas[indice]["completada"] = True
        return f"Tarea '{tareas[indice]['titulo']}' marcada como completada."
    return "Índice inválido."

# Simulación
print("-----AGENDA - Sprint 2-----")
print(agregar_tarea("Estudiar para el examen"))
print(agregar_tarea("Comprar el pan"))
print(agregar_tarea("Limpiar la casa"))

print("\nLISTA DE TAREAS:")
print(mostrar_tareas())

print("\nMARCAR COMO COMPLETADAS:")
print(marcar_completada(0))
print(marcar_completada(2))

print("\nESTADO ACTUAL:")
print(mostrar_tareas())

print("\nELIMINAR UNA TAREA:")
print(eliminar_tarea(1))  # Elimina "Comprar el pan"

print("\nTAREAS FINALES:")
print(mostrar_tareas())

