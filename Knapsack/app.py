"""
Aplicación web con Streamlit para resolver el problema de la mochila binaria usando Google OR-Tools.
Esta aplicación permite ingresar datos de un problema de mochila binaria y resolverlo con el 
solucionador CP-SAT de OR-Tools, mostrando los resultados de forma visual e interactiva.
"""

import streamlit as st
import numpy as np
import time

# Importar módulos personalizados
from static.styles import load_css
from components.header import render_header, render_math_model, render_info_section, render_footer
from components.form import create_input_form, create_config_form
from components.results import display_results, display_comparison_table, display_complexity_growth
from logic.knapsack_solver import solve_knapsack

# Configuración de la página
st.set_page_config(
    page_title="PHS Knapsack - Optimizador de Mochila Binaria",
    page_icon="🎒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Aplicar estilos CSS (tema claro)
st.markdown(load_css(), unsafe_allow_html=True)

# Inicializar o recuperar el estado de la aplicación
if 'selected_algorithm' not in st.session_state:
    st.session_state.selected_algorithm = "ortools"
if 'results' not in st.session_state:
    st.session_state.results = None
if 'algorithm_used' not in st.session_state:
    st.session_state.algorithm_used = None

# Configuración de sidebar más profesional
with st.sidebar:
    # Elimino el logo y el título de la barra lateral, manteniendo directamente la sección de configuración
    
    # Título de configuración
    st.markdown("""
    <div style="font-size: 0.95rem; color: #2c3e50; font-weight: 600; margin-top: 0.5rem; margin-bottom: 0.8rem;">
        ⚙️ Configuración
    </div>
    """, unsafe_allow_html=True)
    
    # Formulario de configuración para el número de ítems
    n_items = create_config_form()
    
    # Mostrar el modelo matemático y la información en la barra lateral
    with st.expander("🧮 Modelo Matemático", expanded=False):
        render_math_model()
    
    with st.expander("ℹ️ Información del Problema", expanded=False):
        render_info_section()
    
    # Pie de página en la barra lateral con estilo más profesional
    st.markdown("""
    <div style="position: fixed; bottom: 0; left: 0; width: 100%; padding: 10px; background: #fafafa; border-top: 1px solid #eee; text-align: center; font-size: 0.7rem; color: #777;">
        <div>© 2025 - Todos los derechos reservados</div>
    </div>
    """, unsafe_allow_html=True)

# Área principal
render_header()

# Separador visual
st.markdown("<hr style='margin: 10px 0; border-color: #DEE2E6; opacity: 0.5;'>", unsafe_allow_html=True)

# Formulario para ingresar datos
benefits, weights, max_weight, submit_button = create_input_form(n_items)

# Contenedor para selección de algoritmo
st.markdown("""
<div style="background-color: #f9f9f9; border: 1px solid #ddd; border-radius: 5px; padding: 1rem; margin: 0.8rem 0;">
    <div style="font-size: 0.9rem; color: #2c3e50; font-weight: 600; margin-bottom: 0.7rem; display: flex; align-items: center;">
        <span style="margin-right: 6px;">🔄</span> Selección de Algoritmo
    </div>
""", unsafe_allow_html=True)

# Sustituir el selector normal por tarjetas de selección
col1, col2, col3 = st.columns(3)

with col1:
    ortools_selected = "background-color: #edf8ff; border-color: #2c3e50;" if st.session_state.selected_algorithm == "ortools" else ""
    st.markdown(f"""
    <div style="border: 1px solid #ddd; border-radius: 4px; padding: 0.7rem; cursor: pointer; {ortools_selected}" 
         onclick="document.getElementById('algo_ortools').click()">
        <div style="font-size: 0.85rem; font-weight: 600; color: #2c3e50; margin-bottom: 4px; display: flex; align-items: center;">
            <span style="margin-right: 5px;">⚙️</span> OR-Tools
        </div>
        <div style="font-size: 0.75rem; color: #7f8c8d; margin-bottom: 5px;">
            Algoritmo exacto basado en programación de restricciones.
        </div>
        <div>
            <span style="background-color: #edf7ed; color: #1e7e34; padding: 2px 6px; border-radius: 3px; font-size: 0.65rem; font-weight: 500;">Óptimo</span>
            <span style="background-color: #d1ecf1; color: #0c5460; padding: 2px 6px; border-radius: 3px; font-size: 0.65rem; font-weight: 500; margin-left: 4px;">Rápido</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    ortools_button = st.button("Seleccionar OR-Tools", key="algo_ortools")
    if ortools_button:
        st.session_state.selected_algorithm = "ortools"
        st.rerun()

with col2:
    greedy_selected = "background-color: #edf8ff; border-color: #2c3e50;" if st.session_state.selected_algorithm == "greedy" else ""
    st.markdown(f"""
    <div style="border: 1px solid #ddd; border-radius: 4px; padding: 0.7rem; cursor: pointer; {greedy_selected}"
         onclick="document.getElementById('algo_greedy').click()">
        <div style="font-size: 0.85rem; font-weight: 600; color: #2c3e50; margin-bottom: 4px; display: flex; align-items: center;">
            <span style="margin-right: 5px;">🚀</span> Greedy
        </div>
        <div style="font-size: 0.75rem; color: #7f8c8d; margin-bottom: 5px;">
            Algoritmo voraz que selecciona ítems por mejor ratio beneficio/peso.
        </div>
        <div>
            <span style="background-color: #fff3cd; color: #856404; padding: 2px 6px; border-radius: 3px; font-size: 0.65rem; font-weight: 500;">Aproximado</span>
            <span style="background-color: #d1ecf1; color: #0c5460; padding: 2px 6px; border-radius: 3px; font-size: 0.65rem; font-weight: 500; margin-left: 4px;">Muy rápido</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    greedy_button = st.button("Seleccionar Greedy", key="algo_greedy")
    if greedy_button:
        st.session_state.selected_algorithm = "greedy"
        st.rerun()

with col3:
    brute_selected = "background-color: #edf8ff; border-color: #2c3e50;" if st.session_state.selected_algorithm == "brute_force" else ""
    st.markdown(f"""
    <div style="border: 1px solid #ddd; border-radius: 4px; padding: 0.7rem; cursor: pointer; {brute_selected}"
         onclick="document.getElementById('algo_brute').click()">
        <div style="font-size: 0.85rem; font-weight: 600; color: #2c3e50; margin-bottom: 4px; display: flex; align-items: center;">
            <span style="margin-right: 5px;">🔍</span> Fuerza Bruta
        </div>
        <div style="font-size: 0.75rem; color: #7f8c8d; margin-bottom: 5px;">
            Evalúa todas las combinaciones posibles (2ⁿ).
        </div>
        <div>
            <span style="background-color: #edf7ed; color: #1e7e34; padding: 2px 6px; border-radius: 3px; font-size: 0.65rem; font-weight: 500;">Óptimo</span>
            <span style="background-color: #f8d7da; color: #721c24; padding: 2px 6px; border-radius: 3px; font-size: 0.65rem; font-weight: 500; margin-left: 4px;">Lento</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    brute_button = st.button("Seleccionar Fuerza Bruta", key="algo_brute")
    if brute_button:
        st.session_state.selected_algorithm = "brute_force"
        st.rerun()

# Botón de optimización con estilo mejorado
st.markdown("<div style='margin-top: 1rem;'></div>", unsafe_allow_html=True)
optimize_button = st.button(
    f"✨ Optimizar con {next((algo['nombre'] for algo_id, algo in {'ortools': {'nombre': 'OR-Tools'}, 'greedy': {'nombre': 'Greedy'}, 'brute_force': {'nombre': 'Fuerza Bruta'}}.items() if algo_id == st.session_state.selected_algorithm), 'OR-Tools')}",
    use_container_width=True,
    key="optimize_button"
)

st.markdown("</div>", unsafe_allow_html=True)

# Si se presiona el botón de optimización, ejecutar el algoritmo seleccionado
if optimize_button:
    with st.spinner(f'Resolviendo el problema de la mochila...'):
        algo = st.session_state.selected_algorithm
        start_time = time.perf_counter()
        if algo == "ortools":
            st.session_state.results = solve_knapsack(benefits, weights, max_weight)
            st.session_state.algorithm_used = "Óptima (OR-Tools)"
        elif algo == "greedy":
            from logic.knapsack_solver import solve_knapsack_greedy
            st.session_state.results = solve_knapsack_greedy(benefits, weights, max_weight)
            st.session_state.algorithm_used = "Aproximada (Greedy)"
        elif algo == "brute_force":
            from logic.knapsack_solver import solve_knapsack_brute_force
            st.session_state.results = solve_knapsack_brute_force(benefits, weights, max_weight)
            st.session_state.algorithm_used = "Óptima (Fuerza Bruta)"
        end_time = time.perf_counter()
        st.session_state.solve_time = end_time - start_time

# Mostrar resultados si están disponibles
if st.session_state.results is not None:
    st.markdown(f"<div style='margin-bottom:8px;'><span style='font-size:1rem; color:#388E3C; font-weight:500;'>Tipo de solución: {st.session_state.algorithm_used}</span></div>", unsafe_allow_html=True)
    display_results(st.session_state.results, max_weight, solve_time=st.session_state.get('solve_time', None))

# Zona de comparación de algoritmos
st.markdown("<hr style='margin: 18px 0; border-color: #DEE2E6; opacity: 0.5;'>", unsafe_allow_html=True)
st.markdown("<span style='font-size:1.05rem; color:#1976D2; font-weight:500;'>¿Quieres comparar los algoritmos?</span>", unsafe_allow_html=True)
if st.button("🔎 Comparar los 3 algoritmos con estos datos", use_container_width=True):
    from logic.knapsack_solver import solve_knapsack_greedy, solve_knapsack_brute_force
    import time
    # OR-Tools
    t0 = time.perf_counter()
    res_ortools = solve_knapsack(benefits, weights, max_weight)
    t1 = time.perf_counter()
    res_ortools['execution_time'] = (t1-t0)*1000
    # Greedy
    t0 = time.perf_counter()
    res_greedy = solve_knapsack_greedy(benefits, weights, max_weight)
    t1 = time.perf_counter()
    res_greedy['execution_time'] = (t1-t0)*1000
    # Brute Force
    t0 = time.perf_counter()
    res_brute = solve_knapsack_brute_force(benefits, weights, max_weight)
    t1 = time.perf_counter()
    res_brute['execution_time'] = (t1-t0)*1000
    # Mostrar tabla comparativa
    results_dict = {
        "OR-Tools (Óptimo)": res_ortools,
        "Greedy (Aproximado)": res_greedy,
        "Fuerza Bruta (Óptimo, lento)": res_brute
    }
    display_comparison_table(results_dict, max_weight)
    # Gráfica dinámica de complejidad
    st.markdown("<div style='margin-top:10px; margin-bottom:0;'></div>", unsafe_allow_html=True)
    st.markdown("<span style='font-size:0.98rem; color:#1976D2;'>Explora la complejidad de fuerza bruta:</span>", unsafe_allow_html=True)
    n_slider = st.slider("Selecciona n (número de ítems)", min_value=1, max_value=30, value=len(benefits), step=1, key="n_slider_complexity")
    from components.results import display_complexity_growth
    display_complexity_growth(max_n=30, brute_force_threshold=20, current_n=n_slider)