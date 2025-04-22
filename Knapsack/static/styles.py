"""
Módulo que contiene los estilos CSS para la aplicación de optimización de la mochila.
"""

def load_css():
    """
    Retorna el CSS personalizado para una estética sobria, compacta y profesional.
    """
    # Nueva paleta de colores sobria
    primary_color = "#2c3e50"      # Azul oscuro sobrio
    secondary_color = "#34495e"    # Gris azulado
    accent_color = "#7f8c8d"       # Gris medio
    success_color = "#27ae60"      # Verde sobrio
    warning_color = "#f39c12"      # Ámbar sobrio
    light_bg = "#f5f5f5"           # Gris muy claro
    ultra_light_bg = "#fafafa"     # Fondo casi blanco
    text_color = "#333333"         # Gris oscuro
    subtle_text = "#7f8c8d"        # Gris medio
    border_color = "#ddd"          # Gris claro
    hover_color = "#3498db"        # Azul para hover

    return f"""
    <style>
        /* Fuentes y Tipografía Base */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
        body, .stApp {{ 
            font-family: 'Inter', sans-serif;
            color: {text_color};
            background-color: #ffffff;
            font-size: 0.92rem;
        }}
        h1, h2, h3, h4, h5, h6 {{
            color: {primary_color};
            font-weight: 600;
            margin-top: 0.6rem;
            margin-bottom: 0.4rem;
        }}
        h1 {{ font-size: 1.5rem; }}
        h2 {{ font-size: 1.3rem; }}
        h3 {{ font-size: 1.1rem; }}
        h4, h5, h6 {{ font-size: 1rem; }}
        
        /* Layout Principal y Sidebar - más compacto */
        .main .block-container {{
            padding: 0.8rem 1.2rem;
            max-width: 1100px;
        }}
        .stSidebar {{
            background-color: {ultra_light_bg};
            border-right: 1px solid {border_color};
        }}
        .stSidebar .block-container {{
            padding-top: 1rem;
        }}
        .stSidebar .stImage > img {{
            display: block;
            margin: 0 auto 0.6rem auto;
        }}
        .stSidebar h1, .stSidebar .stTitle {{
            font-size: 1.1rem;
            text-align: center;
            color: {primary_color};
            margin-bottom: 1rem;
            letter-spacing: 0.3px;
        }}
        
        /* Secciones y Contenedores - más compactos */
        .section-container {{
            background-color: #ffffff;
            border-radius: 6px;
            padding: 0.9rem;
            margin-bottom: 1rem;
            border: 1px solid {border_color};
            box-shadow: 0 1px 2px rgba(0,0,0,0.04);
        }}
        .section-header {{
            display: flex;
            align-items: center;
            margin-bottom: 0.7rem;
            padding-bottom: 0.4rem;
            border-bottom: 1px solid {border_color};
        }}
        .section-header-icon {{
            background-color: {ultra_light_bg};
            color: {primary_color};
            width: 26px;
            height: 26px;
            border-radius: 4px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-right: 0.5rem;
            font-size: 0.9rem;
        }}
        .section-title {{
            color: {primary_color};
            font-size: 0.95rem;
            font-weight: 600;
            margin: 0;
        }}
        
        /* Algoritmos Cards - más compactas */
        .algorithm-container {{
            display: flex;
            gap: 8px;
            margin: 0.7rem 0;
            overflow-x: auto;
            padding-bottom: 4px;
        }}
        .algorithm-card {{
            background-color: #ffffff;
            border: 1px solid {border_color};
            border-radius: 5px;
            padding: 0.7rem;
            min-width: 180px;
            flex: 1;
            cursor: pointer;
            transition: all 0.2s ease;
            position: relative;
        }}
        .algorithm-card:hover {{
            border-color: {accent_color};
            box-shadow: 0 2px 6px rgba(0,0,0,0.05);
        }}
        .algorithm-card.selected {{
            border-color: {primary_color};
            background-color: {ultra_light_bg};
        }}
        .algorithm-card-header {{
            display: flex;
            align-items: center;
            margin-bottom: 0.5rem;
        }}
        .algorithm-icon {{
            display: flex;
            align-items: center;
            justify-content: center;
            width: 24px;
            height: 24px;
            border-radius: 4px;
            margin-right: 8px;
            background-color: {ultra_light_bg};
            color: {primary_color};
            font-size: 0.85rem;
        }}
        .algorithm-title {{
            font-weight: 600;
            font-size: 0.85rem;
            color: {primary_color};
            margin: 0;
        }}
        .algorithm-desc {{
            font-size: 0.75rem;
            color: {subtle_text};
            margin-bottom: 0.5rem;
            line-height: 1.3;
        }}
        .algorithm-tag {{
            display: inline-block;
            padding: 2px 6px;
            border-radius: 4px;
            font-size: 0.65rem;
            font-weight: 500;
            margin-right: 4px;
        }}
        .algorithm-tag.optimal {{
            background-color: #edf7ed;
            color: #1e7e34;
        }}
        .algorithm-tag.approx {{
            background-color: #fff3cd;
            color: #856404;
        }}
        .algorithm-tag.slow {{
            background-color: #f8d7da;
            color: #721c24;
        }}
        .algorithm-tag.fast {{
            background-color: #d1ecf1;
            color: #0c5460;
        }}
        .selected-indicator {{
            position: absolute;
            top: -6px;
            right: -6px;
            background-color: {primary_color};
            color: white;
            width: 16px;
            height: 16px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.6rem;
            box-shadow: 0 1px 2px rgba(0,0,0,0.1);
            z-index: 1;
        }}
        
        /* Expanders - más compactos */
        .stExpander > div > details {{
            background-color: {ultra_light_bg};
            border-radius: 4px;
            border: 1px solid {border_color};
            box-shadow: none;
            margin-bottom: 0.5rem;
        }}
        .stExpander > div > details > summary {{
            padding: 0.5rem 0.7rem;
            font-size: 0.85rem;
            font-weight: 500;
            color: {primary_color};
        }}
        .stExpander > div > details > summary > span:first-child {{
            color: {primary_color};
        }}
        
        /* Botones - más compactos */
        .stButton>button {{
            background-color: {primary_color};
            color: white;
            border: none;
            border-radius: 4px;
            padding: 0.45rem 0.8rem;
            font-weight: 500;
            font-size: 0.85rem;
            letter-spacing: 0.2px;
            box-shadow: 0 1px 2px rgba(0,0,0,0.05);
            transition: all 0.2s ease;
        }}
        .stButton>button:hover {{
            background-color: {hover_color};
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            transform: translateY(-1px);
        }}
        .stButton>button:active {{
            transform: translateY(0);
        }}
        .success-button>button {{
            background-color: {success_color};
        }}
        .success-button>button:hover {{
            background-color: #219653;
        }}
        .warning-button>button {{
            background-color: {warning_color};
        }}
        .warning-button>button:hover {{
            background-color: #e67e22;
        }}
        
        /* Formularios e Inputs - más compactos */
        .stTextInput > div > div > input,
        .stNumberInput > div > div > input {{
            border-radius: 4px;
            border: 1px solid {border_color};
            padding: 0.45rem 0.6rem;
            font-size: 0.85rem;
            transition: all 0.2s ease;
        }}
        .stTextInput > div > div > input:focus,
        .stNumberInput > div > div > input:focus {{
            border-color: {accent_color};
            box-shadow: 0 0 0 1px rgba(52, 73, 94, 0.2);
        }}
        div[data-baseweb="select"] {{
            border-radius: 4px !important;
        }}
        div[data-baseweb="select"] > div {{
            background-color: #ffffff;
            border-radius: 4px !important;
            border: 1px solid {border_color};
            transition: all 0.2s ease;
        }}
        div[data-baseweb="select"] > div:focus-within {{
            border-color: {accent_color};
            box-shadow: 0 0 0 1px rgba(52, 73, 94, 0.2);
        }}
        div[data-baseweb="base-input"] {{
            font-family: 'Inter', sans-serif;
        }}
        
        /* Tablas - más compactas */
        .stDataFrame, .stDataEditor {{
            border-radius: 5px;
            overflow: hidden;
            border: 1px solid {border_color};
            box-shadow: 0 1px 2px rgba(0,0,0,0.03);
        }}
        .stDataFrame th, .stDataEditor th {{
            background-color: {ultra_light_bg};
            color: {primary_color};
            font-weight: 600;
            font-size: 0.8rem;
            padding: 0.5rem 0.7rem;
            border-bottom: 1px solid {border_color};
        }}
        .stDataFrame td, .stDataEditor td {{
            padding: 0.4rem 0.7rem;
            border-bottom: 1px solid {border_color};
            font-size: 0.8rem;
        }}
        .stDataFrame tr:last-child td, .stDataEditor tr:last-child td {{
            border-bottom: none;
        }}
        
        /* Tabs - más compactas */
        .stTabs [data-baseweb="tab-list"] {{
            gap: 0;
            border-bottom: 1px solid {border_color};
        }}
        .stTabs [data-baseweb="tab"] {{
            border-radius: 0;
            border-top: 2px solid transparent;
            border-bottom: none;
            border-left: none;
            border-right: none;
            padding: 0.5rem 0.8rem;
            font-size: 0.8rem;
            font-weight: 500;
            color: {subtle_text};
            background-color: transparent;
            transition: all 0.15s ease;
        }}
        .stTabs [aria-selected="true"] {{
            color: {primary_color};
            font-weight: 600;
            border-top-color: {primary_color};
        }}

        /* Métricas - más compactas */
        .metric-container {{
            background-color: {ultra_light_bg};
            border: 1px solid {border_color};
            border-radius: 5px;
            padding: 0.7rem;
            text-align: center;
            transition: all 0.2s ease;
        }}
        .metric-container:hover {{
            box-shadow: 0 2px 6px rgba(0,0,0,0.03);
        }}
        .metric-label {{
            font-size: 0.75rem;
            color: {subtle_text};
            margin-bottom: 0.3rem;
            font-weight: 500;
        }}
        .metric-value {{
            font-size: 1.5rem;
            font-weight: 700;
            color: {primary_color};
            line-height: 1.1;
        }}
        .metric-suffix {{
            font-size: 0.8rem;
            color: {subtle_text};
            margin-left: 0.2rem;
        }}

        /* Footer - más compacto */
        .footer {{
            margin-top: 1.5rem;
            padding-top: 0.7rem;
            text-align: center;
            border-top: 1px solid {border_color};
            font-size: 0.75rem;
            color: {subtle_text};
        }}
        .footer a {{
            color: {primary_color};
            text-decoration: none;
            font-weight: 500;
        }}
        
        /* Sliders y otros controles - más compactos */
        .stSlider [data-baseweb="slider"] {{
            margin-bottom: 0;
        }}
        .stSlider {{
            padding-top: 0.5rem;
            padding-bottom: 1rem;
        }}
    </style>
    """

def load_header_style():
    """
    Retorna los estilos CSS específicos para el encabezado.
    """
    return """
    <style>
        /* Estilos para la sección de header */
        .app-header {
            text-align: center;
            margin-bottom: 1.2rem;
        }
        .app-title {
            font-size: 1.8rem;
            font-weight: 700;
            background: linear-gradient(90deg, #1976D2 0%, #42A5F5 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.3rem;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
        }
        .app-subtitle {
            font-size: 1rem;
            color: #6C757D;
            margin-bottom: 0.8rem;
            font-weight: 400;
        }
    </style>
    """

def load_footer_style():
    """
    Retorna los estilos CSS específicos para el pie de página.
    """
    return """
    <div style="position: fixed; bottom: 0; right: 0; padding: 10px; font-size: 0.8rem; color: #6C757D; text-align: right;">
        <p style="margin: 0;">© 2025 - Optimizador de Mochila v1.0</p>
    </div>
    """

def load_latex_model():
    """
    Retorna HTML con las ecuaciones LaTeX del modelo matemático del problema de la mochila.
    """
    return """
    <div class="latex-box">
        <h4 style="margin-top: 0; color: #1976D2; margin-bottom: 10px;">Formulación Matemática:</h4>
        
        <p style="font-size: 0.95rem; margin-bottom: 10px; color: #212529;">Variables de decisión:</p>
        <div style="text-align: center;">
            $$x_i = \\begin{cases} 
            1 & \\text{si el ítem } i \\text{ es seleccionado} \\\\
            0 & \\text{si el ítem } i \\text{ no es seleccionado}
            \\end{cases}$$
        </div>
        
        <p style="font-size: 0.95rem; margin: 10px 0; color: #212529;">Función objetivo (maximizar el beneficio total):</p>
        <div style="text-align: center;">
            $$\\max Z = \\sum_{i=1}^{n} c_i x_i$$
        </div>
        
        <p style="font-size: 0.95rem; margin: 10px 0; color: #212529;">Sujeto a la restricción de capacidad:</p>
        <div style="text-align: center;">
            $$\\sum_{i=1}^{n} w_i x_i \\leq W$$
        </div>
        
        <p style="font-size: 0.95rem; margin: 10px 0; color: #212529;">Restricciones de dominio:</p>
        <div style="text-align: center;">
            $$x_i \\in \\{0,1\\} \\quad \\forall i \\in \\{1,2,\\ldots,n\\}$$
        </div>
        
        <p style="font-size: 0.95rem; margin: 10px 0; color: #212529;">Donde:</p>
        <ul style="font-size: 0.9rem; margin: 0; color: #212529;">
            <li>$n$ = número de ítems disponibles</li>
            <li>$c_i$ = beneficio asociado al ítem $i$</li>
            <li>$w_i$ = peso asociado al ítem $i$</li>
            <li>$W$ = capacidad máxima de la mochila</li>
        </ul>
    </div>
    """

def backpack_html(selected_count, total_count):
    """
    Crea una representación HTML de una mochila.
    
    Args:
        selected_count (int): Cantidad de ítems seleccionados
        total_count (int): Cantidad total de ítems disponibles
    
    Returns:
        str: Representación HTML
    """
    # Calcula el porcentaje de llenado para la animación
    fill_percentage = min(100, round(selected_count / total_count * 100))
    
    # Componente visual de la mochila
    return f"""
    <div style="text-align: center; margin: 1rem 0;">
        <div style="
            width: 120px;
            height: 150px;
            margin: 0 auto;
            position: relative;
            background-color: #EFF7FF;
            border-radius: 20px 20px 60px 60px;
            border: 4px solid #1976D2;
            overflow: hidden;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        ">
            <div style="
                position: absolute;
                bottom: 0;
                left: 0;
                width: 100%;
                height: {fill_percentage}%;
                background: linear-gradient(90deg, #1976D2 0%, #1565C0 100%);
                transition: height 1s ease;
                display: flex;
                justify-content: center;
                align-items: center;
                color: white;
                font-weight: bold;
            ">
                {selected_count}/{total_count}
            </div>
            <div style="
                position: absolute;
                top: -15px;
                left: 0;
                width: 100%;
                height: 30px;
                background-color: #E3F2FD;
                border-radius: 5px;
                border: 4px solid #1976D2;
                z-index: -1;
            "></div>
        </div>
        <div style="margin-top: 10px; font-size: 0.9rem; color: #666;">
            Mochila al <strong>{fill_percentage}%</strong> de capacidad
        </div>
    </div>
    """