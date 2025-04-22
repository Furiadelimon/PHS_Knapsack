"""
Módulo que contiene la lógica para resolver el problema de la mochila binaria
utilizando el solver CP-SAT de Google OR-Tools.
"""

import time
import pandas as pd
import random
from ortools.sat.python import cp_model

def solve_knapsack(benefits, weights, max_weight, iteration=0, previous_solution=None):
    """
    Resuelve el problema de la mochila binaria con los beneficios y pesos dados.
    Además, imprime por la terminal todos los pasos y decisiones para depuración.
    
    Args:
        benefits (list): Lista de beneficios para cada ítem
        weights (list): Lista de pesos para cada ítem
        max_weight (int): Peso máximo permitido de la mochila
        iteration (int): Número de iteración actual
        previous_solution (dict): Solución previa para mejorar
        
    Returns:
        dict: Un diccionario con los resultados de la optimización
    """
    import sys
    print("\n--- INICIO DE OPTIMIZACIÓN DE MOCHILA ---", file=sys.stderr)
    print(f"Beneficios: {benefits}", file=sys.stderr)
    print(f"Pesos: {weights}", file=sys.stderr)
    print(f"Capacidad máxima: {max_weight}", file=sys.stderr)
    print(f"Iteración: {iteration}", file=sys.stderr)
    if previous_solution:
        print(f"Solución previa: {previous_solution}", file=sys.stderr)
    
    start_time = time.time()
    
    # Crear el modelo
    model = cp_model.CpModel()
    
    # Crear variables de decisión (binarias)
    x = {}
    for i in range(len(benefits)):
        x[i] = model.NewBoolVar(f'x_{i}')
    print(f"Variables de decisión creadas: {[f'x_{i}' for i in range(len(benefits))]}", file=sys.stderr)
    
    # Restricción de peso máximo
    print(f"Agregando restricción: suma de pesos <= {max_weight}", file=sys.stderr)
    model.Add(sum(weights[i] * x[i] for i in range(len(weights))) <= max_weight)
    
    # Si estamos en una iteración mayor que 0 y tenemos una solución previa,
    # añadimos restricciones para forzar algunas variaciones
    if iteration > 0 and previous_solution:
        prev_selected = [i for i, val in enumerate(previous_solution['selected_items_binary']) if val == 1]
        print(f"Ítems seleccionados en la solución previa: {prev_selected}", file=sys.stderr)
        
        # Estrategia de diversificación para explorar el espacio de soluciones
        if iteration % 3 == 1:  # Cada 3 iteraciones, forzar cambios
            # Forzar algunos cambios en la solución
            num_changes = min(max(1, len(prev_selected) // 3), len(benefits) // 4)
            items_to_change = random.sample(range(len(benefits)), num_changes)
            print(f"Forzando cambios en los ítems: {items_to_change}", file=sys.stderr)
            
            for i in items_to_change:
                if i in prev_selected:
                    # Si el ítem estaba seleccionado, forzar a NO seleccionarlo
                    print(f"Forzando que el ítem {i} NO se seleccione", file=sys.stderr)
                    model.Add(x[i] == 0)
                else:
                    # Intentar incluir algunos ítems nuevos con buen ratio beneficio/peso
                    if weights[i] <= max_weight / 4:  # Solo si no es muy pesado
                        print(f"Forzando que el ítem {i} SÍ se seleccione", file=sys.stderr)
                        model.Add(x[i] == 1)
        
        # En otras iteraciones, intentar mejorar incrementalmente
        else:
            # Asegurar que el beneficio sea al menos igual al anterior
            print(f"Forzando que el beneficio sea al menos igual al anterior", file=sys.stderr)
            model.Add(
                sum(benefits[i] * x[i] for i in range(len(benefits))) >= 
                previous_solution['total_benefit']
            )
    
    # Función objetivo: maximizar el beneficio
    print("Definiendo función objetivo: maximizar suma de beneficios", file=sys.stderr)
    model.Maximize(sum(benefits[i] * x[i] for i in range(len(benefits))))
    
    # Resolver el modelo
    solver = cp_model.CpSolver()
    print("Resolviendo el modelo...", file=sys.stderr)
    status = solver.Solve(model)
    print(f"Status del solver: {status}", file=sys.stderr)
    
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000  # en milisegundos
    
    # Verificar si se encontró una solución
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        # Recolectar resultados
        selected_items = []
        selected_items_binary = [0] * len(benefits)
        
        for i in range(len(benefits)):
            val = solver.Value(x[i])
            print(f"Ítem {i}: seleccionado={val} (beneficio={benefits[i]}, peso={weights[i]})", file=sys.stderr)
            if val == 1:
                selected_items.append(i)
                selected_items_binary[i] = 1
        
        total_benefit = sum(benefits[i] for i in selected_items)
        total_weight = sum(weights[i] for i in selected_items)
        print(f"Total beneficio: {total_benefit}", file=sys.stderr)
        print(f"Total peso: {total_weight}", file=sys.stderr)
        
        # Crear dataframe para visualización
        df = pd.DataFrame({
            'Ítem': [f'Ítem {i+1}' for i in range(len(benefits))],
            'Beneficio': benefits,
            'Peso': weights,
            'Seleccionado': [1 if i in selected_items else 0 for i in range(len(benefits))]
        })
        
        # Verificar si esta solución es mejor que la anterior
        is_improved = False
        improvement = 0
        
        if previous_solution and 'total_benefit' in previous_solution:
            if total_benefit > previous_solution['total_benefit']:
                is_improved = True
                improvement = total_benefit - previous_solution['total_benefit']
        
        return {
            'status': 'optimal' if status == cp_model.OPTIMAL else 'feasible',
            'selected_items': selected_items,
            'selected_items_binary': selected_items_binary,
            'total_benefit': total_benefit,
            'total_weight': total_weight,
            'execution_time': execution_time,
            'iteration': iteration,
            'is_improved': is_improved,
            'improvement': improvement,
            'dataframe': df,
            'weights': weights,
            'benefits': benefits
        }
    else:
        print("No se encontró solución factible.", file=sys.stderr)
        return {
            'status': 'infeasible',
            'execution_time': execution_time,
            'iteration': iteration
        }

def solve_knapsack_greedy(benefits, weights, max_weight):
    """
    Algoritmo voraz (greedy) para el problema de la mochila binaria.
    Retorna una solución aproximada.
    """
    n = len(benefits)
    ratio = [(benefits[i] / weights[i], i) for i in range(n)]
    ratio.sort(reverse=True)
    total_weight = 0
    total_benefit = 0
    selected_items = []
    selected_items_binary = [0] * n
    for r, i in ratio:
        if total_weight + weights[i] <= max_weight:
            total_weight += weights[i]
            total_benefit += benefits[i]
            selected_items.append(i)
            selected_items_binary[i] = 1
    return {
        'status': 'approximate',
        'selected_items': selected_items,
        'selected_items_binary': selected_items_binary,
        'total_benefit': total_benefit,
        'total_weight': total_weight,
        'execution_time': 0,
        'iteration': 0,
        'is_improved': False,
        'improvement': 0,
        'dataframe': None,
        'weights': weights,
        'benefits': benefits
    }

def solve_knapsack_brute_force(benefits, weights, max_weight):
    """
    Algoritmo de fuerza bruta para el problema de la mochila binaria.
    Retorna la solución óptima (solo para pocos ítems).
    """
    import itertools
    n = len(benefits)
    best_benefit = 0
    best_weight = 0
    best_comb = [0] * n
    best_items = []
    for comb in itertools.product([0, 1], repeat=n):
        w = sum(weights[i] for i in range(n) if comb[i])
        b = sum(benefits[i] for i in range(n) if comb[i])
        if w <= max_weight and b > best_benefit:
            best_benefit = b
            best_weight = w
            best_comb = list(comb)
            best_items = [i for i in range(n) if comb[i]]
    return {
        'status': 'optimal',
        'selected_items': best_items,
        'selected_items_binary': best_comb,
        'total_benefit': best_benefit,
        'total_weight': best_weight,
        'execution_time': 0,
        'iteration': 0,
        'is_improved': False,
        'improvement': 0,
        'dataframe': None,
        'weights': weights,
        'benefits': benefits
    }