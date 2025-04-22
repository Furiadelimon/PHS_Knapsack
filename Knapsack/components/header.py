"""
Módulo que contiene el componente de encabezado de la aplicación.
"""

import streamlit as st
from static.styles import load_header_style, load_latex_model

def render_header():
    """
    Muestra un encabezado profesional con título centrado y diseño minimalista.
    """
    # Encabezado centrado y elegante
    st.markdown("""
    <div style="display: flex; flex-direction: column; align-items: center; margin-bottom: 1rem;">
        <div style="font-size: 1.1rem; font-weight: 600; color: #2c3e50; letter-spacing: 0.5px; display: flex; align-items: center; justify-content: center;">
            <span style="margin-right: 8px;">🎒</span>
            <span>PHS Knapsack</span>
        </div>
        <div style="font-size: 0.8rem; color: #7f8c8d; font-weight: 400; margin-top: 2px;">
            Optimizador de Mochila Binaria
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Descripción compacta
    with st.expander("ℹ️ Ver enunciado", expanded=False):
        st.markdown("""
        <div style="font-size: 0.85rem;">
        Selecciona ítems con beneficios y pesos para maximizar el beneficio total sin exceder la capacidad de la mochila.
        </div>
        """, unsafe_allow_html=True)

def render_math_model():
    """
    Renderiza el modelo matemático en formato LaTeX.
    """
    # En lugar de usar HTML para LaTeX, usamos la función de Streamlit
    # que renderiza LaTeX directamente
    st.markdown("### Modelo Matemático")
    
    st.markdown("#### Función Objetivo")
    st.latex(r"\max Z = \sum_{j=1}^{n} c_j x_j")
    
    st.markdown("#### Restricciones")
    st.latex(r"\sum_{j=1}^{n} w_j x_j \leq W")
    st.latex(r"x_j \in \{0,1\} \quad \forall j \in \{1,\ldots,n\}")
    
    st.markdown("#### Donde:")
    st.markdown("""
    - $c_j$ = beneficio del ítem $j$
    - $w_j$ = peso del ítem $j$
    - $W$ = capacidad máxima de la mochila
    - $x_j$ = variable de decisión (1 si el ítem $j$ es seleccionado, 0 en caso contrario)
    - $n$ = número de ítems disponibles
    """)
    
    # Para modo expander, mostramos un ejemplo
    st.markdown("#### Ejemplo simplificado")
    st.markdown("Si tenemos una mochila con capacidad $W = 10$ kg y 3 ítems disponibles:")
    st.markdown("""
    - Ítem 1: beneficio $c_1 = 6$, peso $w_1 = 4$ kg
    - Ítem 2: beneficio $c_2 = 5$, peso $w_2 = 3$ kg
    - Ítem 3: beneficio $c_3 = 8$, peso $w_3 = 5$ kg
    """)
    
    st.markdown("""
    La solución óptima sería seleccionar los ítems 1 y 2 ($x_1 = 1, x_2 = 1, x_3 = 0$), 
    dando un beneficio total de $6 + 5 = 11$ y un peso total de $4 + 3 = 7$ kg, 
    que está dentro de la capacidad de la mochila.
    """)

def render_info_section():
    """
    Renderiza la sección de información adicional sobre el problema de la mochila, con formato y ecuaciones matemáticas bien renderizadas.
    """
    import streamlit as st
    st.markdown("#### Problema de la Mochila Binaria")
    st.markdown("""
El **problema de la mochila binaria** es un problema clásico de optimización combinatoria donde se debe seleccionar un subconjunto de ítems, cada uno con un peso y un beneficio asociado, de modo que maximice el beneficio total sin exceder la capacidad de la mochila.
""")
    st.markdown("""
**Aplicaciones Prácticas:**
- Gestión de inversiones: Selección de proyectos con restricciones presupuestarias
- Logística: Optimización de carga en contenedores o camiones
- Fabricación: Selección de productos a fabricar con recursos limitados
- Finanzas: Asignación óptima de presupuesto entre diferentes activos
""")
    st.markdown("---")
    st.markdown("#### Formulación Matemática")
    st.markdown("Variables de decisión:")
    st.latex(r"x_i = \begin{cases} 1 & \text{si el ítem } i \text{ es seleccionado} \\ 0 & \text{si el ítem } i \text{ no es seleccionado} \end{cases}")
    st.markdown("Función objetivo (maximizar el beneficio total):")
    st.latex(r"\max Z = \sum_{i=1}^{n} c_i x_i")
    st.markdown("Sujeto a la restricción de capacidad:")
    st.latex(r"\sum_{i=1}^{n} w_i x_i \leq W")
    st.markdown("Restricciones de dominio:")
    st.latex(r"x_i \in \{0,1\} \quad \forall i \in \{1,2,\ldots,n\}")
    st.markdown("""
**Donde:**
- $n$ = número de ítems disponibles
- $c_i$ = beneficio asociado al ítem $i$
- $w_i$ = peso asociado al ítem $i$
- $W$ = capacidad máxima de la mochila
""")

def render_footer():
    """
    Renderiza el pie de página de la aplicación.
    """
    from static.styles import load_footer_style
    st.markdown(load_footer_style(), unsafe_allow_html=True)