"""
Módulo que contiene los componentes de formulario para la aplicación de
optimización de la mochila binaria.
"""

import streamlit as st
import numpy as np
import pandas as pd

def create_config_form():
    """
    Crea un formulario compacto para configurar el número de ítems del problema.
    
    Returns:
        int: Número de ítems para el problema de la mochila
    """
    # Inicializar session_state para el número de ítems si no existe
    if 'n_items' not in st.session_state:
        st.session_state.n_items = 5
    
    # Formulario de configuración minimalista
    st.markdown("""
    <div style="font-size: 0.9rem; color: #2c3e50; font-weight: 500; margin-bottom: 5px;">
        Configuración
    </div>
    """, unsafe_allow_html=True)
    
    # Configuración del número de ítems con slider más discreto
    n_items = st.slider(
        "Número de ítems:",
        min_value=2,
        max_value=50,
        value=st.session_state.n_items,
        step=1,
        help="Selecciona cuántos ítems tendrá tu problema"
    )
    
    # Actualizar el valor en session_state
    st.session_state.n_items = n_items
    
    # Separador sutil
    st.markdown("<hr style='margin: 10px 0; border-color: #ddd; opacity: 0.3;'>", unsafe_allow_html=True)
    
    return n_items

def create_input_form(n_items=5):
    """
    Crea y renderiza el formulario de entrada para ingresar los datos del problema.
    
    Args:
        n_items (int): Número de ítems para el problema de la mochila
        
    Returns:
        tuple: (benefits, weights, max_weight, submit_button) si el formulario fue enviado
    """
    # Valores predeterminados para los beneficios y pesos
    if 'default_benefits' not in st.session_state or len(st.session_state.default_benefits) < n_items:
        st.session_state.default_benefits = [60, 40, 50, 30, 20] + [random_value(10, 100) for _ in range(max(0, n_items-5))]
    
    if 'default_weights' not in st.session_state or len(st.session_state.default_weights) < n_items:
        st.session_state.default_weights = [20, 10, 30, 15, 25] + [random_value(5, 40) for _ in range(max(0, n_items-5))]
    
    # Recortar si hay más valores predeterminados que ítems
    st.session_state.default_benefits = st.session_state.default_benefits[:n_items]
    st.session_state.default_weights = st.session_state.default_weights[:n_items]
    
    with st.form(key='mochila_form'):
        # Crear columnas para mejor distribución espacial
        col1, col2 = st.columns([4, 1])
        
        with col1:
            # Crear un DataFrame para usar como tabla de entrada
            data = {
                'Ítem': [f'Ítem {i+1}' for i in range(n_items)],
                'Beneficio': st.session_state.default_benefits,
                'Peso': st.session_state.default_weights
            }
            df = pd.DataFrame(data)
            
            # Generar la tabla editable más compacta
            edited_df = st.data_editor(
                df,
                column_config={
                    "Ítem": st.column_config.TextColumn(
                        "Ítem",
                        help="Identificador del ítem",
                        disabled=True,
                    ),
                    "Beneficio": st.column_config.NumberColumn(
                        "Beneficio",
                        help="Valor o beneficio del ítem",
                        min_value=1,
                        max_value=100,
                        step=1,
                        format="%d",
                    ),
                    "Peso": st.column_config.NumberColumn(
                        "Peso",
                        help="Peso del ítem",
                        min_value=1,
                        max_value=50,
                        step=1,
                        format="%d",
                    )
                },
                hide_index=True,
                num_rows="fixed",
                use_container_width=True,
            )
            
            # Extraer los valores editados
            benefits = edited_df['Beneficio'].tolist()
            weights = edited_df['Peso'].tolist()
        
        # Columna para la capacidad y botón
        with col2:
            st.markdown("""
            <div style="background-color: #f5f5f5; 
                       padding: 6px; 
                       border-radius: 4px; 
                       margin-bottom: 8px;
                       border: 1px solid #ddd;
                       text-align: center;">
                <div style="margin: 0; color: #2c3e50; font-size: 0.85rem; font-weight: 600;">
                    🧳 Capacidad
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            max_weight = st.number_input(
                "Máximo peso:",
                min_value=10,
                max_value=200,
                value=80,
                step=5,
                help="Peso máximo que puede soportar la mochila"
            )
            
            # Espacio reducido
            st.write("")
            
            # Botón para ejecutar con estilo más sobrio
            submit_button = st.form_submit_button(
                label='✨ Optimizar',
                use_container_width=True
            )
    
    return benefits, weights, max_weight, submit_button

def random_value(min_val, max_val):
    """Genera un valor aleatorio entero entre min_val y max_val"""
    return np.random.randint(min_val, max_val + 1)