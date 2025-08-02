# *Agenda de Tareas - Sprint 0*

tareas = []

def agregar_tarea(titulo):
    if titulo.strip():
        tarea = {"titulo": titulo, "completada": False}
        tareas.append(tarea)
        return "Tarea agregada."
    return "Error: la tarea no puede estar vacía."

def mostrar_tareas():
    if not tareas:
        return "No hay tareas registradas."
    resultado = []
    for i, t in enumerate(tareas):
        estado = "✅" if t["completada"] else "❌"
        resultado.append(f"{i}. {t['titulo']} - {estado}")
    return "\n".join(resultado)

# Simulación
print("-----AGENDA - Sprint 0-----")
print(agregar_tarea("Estudiar para el examen"))
print(agregar_tarea("Comprar el pan"))
print(agregar_tarea("Limpiar la casa"))

print("\nLISTA DE TAREAS:")
print(mostrar_tareas())
