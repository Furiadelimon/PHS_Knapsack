# OptMochila: Optimizador del Problema de la Mochila Binaria

Una aplicación web interactiva desarrollada con Streamlit y Google OR-Tools para resolver problemas de mochila binaria con una interfaz gráfica moderna e intuitiva.

![Logo Mochila](https://img.icons8.com/color/96/000000/backpack.png)

## Descripción

Esta aplicación permite resolver el problema clásico de la mochila binaria de manera visual e interactiva. El usuario puede:

- Ingresar los coeficientes de beneficios para 5 ítems
- Ingresar los coeficientes de peso para esos mismos ítems
- Definir el valor del límite máximo de peso
- Ejecutar la optimización utilizando el solver CP-SAT de Google OR-Tools
- Visualizar los resultados mediante gráficos interactivos

## Características

- Interfaz de usuario moderna e intuitiva
- Visualización del modelo matemático usando LaTeX
- Gráficos interactivos con Plotly
- Optimización mediante el solver CP-SAT de Google OR-Tools
- Diseño responsive para usar en móvil o navegador

## Requisitos

- Python 3.8 o superior
- Las dependencias listadas en `requirements.txt`

## Instalación

1. Clona o descarga este repositorio
2. Navega hasta el directorio del proyecto
3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

## Uso

Para ejecutar la aplicación, desde el directorio del proyecto ejecuta:

```bash
streamlit run app.py
```

Se abrirá automáticamente una ventana en tu navegador web predeterminado. Si no se abre, navega a la URL indicada en la terminal (generalmente http://localhost:8501).

## Estructura del Proyecto

```
OptMochila/
├── app.py                  # Archivo principal de la aplicación
├── requirements.txt        # Dependencias del proyecto
├── README.md               # Documentación
├── components/             # Componentes de la interfaz de usuario
│   ├── __init__.py
│   ├── header.py           # Componentes del encabezado
│   ├── form.py             # Formulario de entrada de datos
│   └── results.py          # Visualización de resultados
├── logic/                  # Lógica de negocio
│   ├── __init__.py
│   └── knapsack_solver.py  # Solver para el problema de la mochila
└── static/                 # Recursos estáticos
    └── styles.py           # Estilos CSS
```

## Contribuciones

Las contribuciones son bienvenidas. Para cambios importantes, por favor abre primero un issue para discutir lo que te gustaría cambiar.

## Licencia

Este proyecto está licenciado bajo la licencia MIT.

## Autor

Desarrollado por: PHS

---

*Entregados a la causa*
