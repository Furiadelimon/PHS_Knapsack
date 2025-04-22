# PHS_Knapsack
Aplicación para aprendizaje y uso de algoritmos en el problema conocido de la mochila
Optimizador del Problema de la Mochila Binaria
Descripción general: OptMochila es una aplicación web interactiva desarrollada con Streamlit y Google OR-Tools para resolver el problema clásico de la mochila binaria. Permite a los usuarios definir y resolver instancias del problema de forma visual, intuitiva y profesional.

Funcionalidades principales:

Configuración flexible:
Permite seleccionar el número de ítems (de 2 a 50) y definir los beneficios y pesos de cada ítem mediante una tabla editable.

Definición de la capacidad:
El usuario puede establecer el peso máximo que la mochila puede soportar.

Selección de algoritmo:
Ofrece tres algoritmos para resolver el problema:

OR-Tools (Óptimo): Utiliza el solver CP-SAT de Google OR-Tools para encontrar la solución óptima de manera eficiente.
Greedy (Aproximado): Algoritmo voraz que selecciona ítems por mejor ratio beneficio/peso, rápido pero no siempre óptimo.
Fuerza Bruta (Óptimo, lento): Evalúa todas las combinaciones posibles, garantizando la solución óptima pero solo viable para pocos ítems.
Visualización de resultados:
Muestra los ítems seleccionados, el beneficio total, el peso utilizado, la eficiencia (beneficio/peso), y el tiempo de ejecución. Incluye tablas, gráficos de barras y gráficos circulares para una mejor comprensión.

Comparación de algoritmos:
Permite comparar los tres algoritmos con los mismos datos, mostrando una tabla comparativa y gráficos de rendimiento y eficiencia.

Análisis de complejidad:
Incluye una gráfica interactiva que muestra el crecimiento de la complejidad computacional de los algoritmos, especialmente la diferencia entre fuerza bruta (exponencial) y algoritmos eficientes (polinomial).

Exportación de resultados:
Permite exportar los resultados a PDF o Excel con un solo clic, generando informes profesionales.

Modelo matemático:
Muestra la formulación matemática del problema de la mochila usando LaTeX, accesible desde la barra lateral.

Interfaz moderna y responsive:
Diseño profesional, compacto y adaptable a dispositivos móviles o escritorio, con estilos personalizados y visualizaciones atractivas.

Soporte para múltiples ejecuciones:
El usuario puede resolver diferentes instancias del problema sin recargar la página.

Tecnologías utilizadas:

Python 3.8+
Streamlit
Google OR-Tools
Pandas, Numpy, Matplotlib, Seaborn
ReportLab y OpenPyXL (para exportación)
CSS personalizado para una mejor experiencia visual
