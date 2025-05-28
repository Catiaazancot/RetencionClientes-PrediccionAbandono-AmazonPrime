# Amazon Prime: Detrás del abandono, lo que cuesta perder a un cliente

## Del dato a la acción: patrones y decisiones claves

A partir del análisis, se identificaron patrones clave que justifican las acciones de negocio propuestas a continuación:

**Patrones detectados:**

- Los clientes con contratos mensuales tienen mayor probabilidad de abandonar.

- A mayor número de llamadas al soporte, mayor es la probabilidad de abandono. Especialmente a partir de la tercera llamada.

- Los clientes con planes familiares tienen menor tasa de abandono. Compartir el servicio parece generar mayor compromiso.

- Los descuentos aplicados no parecen reducir significativamente el abandono. Se podría estar perdiendo dinero en descuentos que no influyen en la fidelización del cliente.

- Los clientes que contratan servicios adicionales como protección de dispositivos o backup en la nube tienden a abandonar menos.

- Los clientes nuevos (con menor tiempo en la plataforma) abandonan con más facilidad.

- Clientes menores de 30 años presentan una mayor fidelidad al servicio.

- Clientes mayores de 65 años tienen una tasa de abandono significativamente más alta.

**Acciones de negocio propuestas a partir del análisis realizado:**

- Diseñar campañas promocionales que ofrezcan beneficios exclusivos (descuentos, servicios gratuitos, puntos de fidelidad) para quienes contraten planes anuales o bianuales.

- Implementar un sistema de seguimiento para identificar clientes que han llamado más de dos veces y asignarles soporte especializado para evitar la pérdida.

- Lanzar campañas dirigidas con descuentos grupales, posibilidad de añadir miembros fácilmente o beneficios compartidos (como almacenamiento extra o atención prioritaria).

- Redirigir los recursos de descuentos hacia acciones más eficaces, como recompensas por lealtad o mejoras en el servicio.

- Ofrecer paquetes combinados con descuentos si se contratan servicios adicionales, destacando su valor añadido.

- Diseñar una experiencia de bienvenida con tutoriales, beneficios iniciales y seguimiento personalizado durante los primeros meses.

- Desarrollar campañas enfocadas a jóvenes con ventajas tecnológicas, precios especiales para estudiantes o contenido personalizado.

- Crear una interfaz simplificada, soporte asistido o formación personalizada para mayores, y adaptar el contenido a sus preferencias.

### Resultados de negocio potenciales de las acciones propuestas

La implementación de estas acciones podría evitar la pérdida de más de 1.700 clientes, reduciendo el abandono de manera significativa. Esto se traduce en un potencial de recuperación de más de 65.000 € al mes en ingresos, según el valor medio mensual por cliente.

Además, estas acciones no solo tienen impacto económico inmediato, sino que también contribuyen a una mejor experiencia del cliente, fomentan una mayor fidelidad y aumentan el valor de vida del usuario (CLV).

### Habilidades demostradas en este proyecto

Conciencia del impacto en negocio: foco constante en la mejora de la eficiencia operativa y aumento de la retención de clientes

Conocimiento profundo del negocio y enfoque estratégico: formulación de preguntas clave alineadas con los objetivos empresariales para transformar datos en decisiones

Buenas prácticas en calidad, validación y gobernanza del dato: validación de consistencia, tratamiento de nulos y outliers, normalización y limpieza con enfoque en la integridad de la información

Automatización con inteligencia artificial: uso de IA para documentar procesos, asistir en tareas repetitivas y generar código, lo que permite centrar el esfuerzo en el análisis de valor

Mentalidad orientada a la optimización y al rendimiento: uso de funciones en python (optimización del tiempo), buenas prácticas en PowerBI y SQL (mejora del rendimiento).

Análisis exploratorio de datos (EDA)

Aplicación de un modelo de regresión logística en R con el objetivo de identificar los factores que más influyen en la pérdida de clientes, utilizando las librerías dplyr, broom, janitor y ggplot2.

Diseño e implementación de una base de datos relacional en PostgreSQL

Consultas SQL orientadas al negocio

Visualización y storytelling con Power BI

ETL básico y modelado de datos

## Historia del proyecto Amazon Prime: Detrás del abandono, lo que cuesta perder a un cliente

#### **Contexto**

Amazon Prime es uno de los servicios de suscripción más utilizados a nivel mundial. Sin embargo, como en cualquier modelo basado en suscripción, la retención de clientes es un factor crítico para su rentabilidad y sostenibilidad. A medida que el mercado se vuelve más competitivo, entender por qué los clientes deciden cancelar su suscripción se ha vuelto más importante que nunca.

#### **¿Cuál era el verdadero problema?**

Un análisis inicial de los datos reveló un problema alarmante: una parte significativa de los clientes de Amazon Prime está abandonando el servicio, especialmente durante los primeros meses de contratación. Además, existen ciertos patrones que se repiten en los clientes que se marchan, lo que sugiere que el abandono no es aleatorio, sino que responde a causas específicas que pueden ser abordadas.

#### **¿Dónde estaba el origen del problema?**

Mediante el análisis exploratorio, visualizaciones interactivas y un modelo de regresión logística realizado en R, se detectaron los factores con mayor influencia en el abandono:

- Los **clientes con contrato mensual** tienen una tasa de abandono mucho mayor que aquellos con contratos de mayor duración.
- A partir de la **tercera llamada al servicio de atención al cliente**, el abandono es casi inevitable.
- Los **clientes sin plan familiar** presentan mayor propensión a cancelar el servicio.
- Los **descuentos aplicados** no están funcionando para reducir el abandono.

#### **Soluciones propuestas**

Basado en los datos y en los patrones detectados, se propusieron acciones específicas orientadas a reducir el abandono como, entre otras:

1. **Fomentar contratos de largo plazo**, con beneficios como descuentos o servicios exclusivos.
2. **Mejorar la eficiencia del soporte**, resolviendo los problemas en las primeras llamadas.
3. **Incentivar planes familiares**, que han demostrado una tasa de retención mucho mayor.
4. **Rediseñar la estrategia de descuentos**, redirigiendo el esfuerzo a acciones que generen verdadero compromiso.
5. **Reforzar la experiencia inicial del cliente**, con onboarding personalizado, tutoriales y seguimiento proactivo.

La acción más recomendable es reforzar la experiencia inicial del cliente con un onboarding proactivo. Esto significa acompañar al usuario desde el primer día, anticipándose a sus dudas y guiándole para que entienda el valor del servicio desde el inicio. Los datos muestran que la mayoría de cancelaciones ocurren en los primeros tres meses, por lo que actuar en esa fase es clave para reducir el abandono.

Dentro del onboarding, una de las acciones más efectivas es invitar a activar el plan familiar, ya que los clientes que lo utilizan presentan una tasa de abandono muy baja. Por ello, se considera también la segunda acción más recomendada.

#### **Consecuencias de no actuar**

Si no se aplican estas soluciones, el servicio seguirá perdiendo cientos de clientes al mes, lo que implica pérdidas considerables en ingresos recurrentes y un impacto negativo en la imagen de marca. El modelo predictivo mostró que solo en tres segmentos críticos (contrato mensual, sin plan familiar y 3+ llamadas al soporte) se podrían estar perdiendo más de **1.700 clientes al año** que serían recuperables con las acciones adecuadas.

#### **Beneficios de implementar las soluciones**

- **+1.700 clientes retenidos** con acciones dirigidas
- **Más de 65.000 € al mes en ingresos recuperables**, según el valor medio mensual por cliente
- Mejor experiencia del cliente, mayor fidelidad y valor de vida del usuario
- Uso más eficiente de recursos de soporte y marketing
- Imagen de marca reforzada gracias a la personalización y la atención a las necesidades reales del usuario

#### **Conclusión**

Este proyecto demuestra que, con los datos adecuados y un análisis enfocado, es posible convertir patrones invisibles en acciones concretas de negocio.
El análisis de datos no solo ha permitido identificar los factores de abandono, sino también proyectar el impacto de actuar sobre ellos.

Implementar estas soluciones es una decisión estratégica con beneficios medibles y sostenibles a corto y largo plazo.

## Desarrollo técnico del análisis

### Tecnologías utilizadas

- Python (Pandas, Numpy, psycopg2, matplotlib, seaborn)

- R (dplyr, janitor, broom, ggplot2)

- SQL (PostgreSQL)

- Power BI (Storytelling, Power Query, modelado, DAX)

- Inteligencia artificial (ChatGPT, algoritmos de aprendizaje)

- GitHub (mantenimiento en la nube)

- Jupyter Notebook

### Fases del análisis

1. Comprensión del negocio y definición del objetivo

Antes de comenzar el análisis, dediqué un tiempo a estudiar el contexto de la empresa, comprender sus necesidades reales, identificar claramente el problema y formular múltiples preguntas de negocio orientadas a posibles soluciones.

También analicé los datos disponibles para asegurarme de que respondían a esos objetivos y ofrecían el potencial necesario para extraer valor.

Esta fase me permitió conectar los datos con los objetivos estratégicos de la empresa, y plantear el análisis desde una perspectiva orientada a impacto real.

2. Preparación, limpieza y validazción de datos (Python)

Comencé trabajando con Python para cargar y explorar los datos, asegurando su calidad desde el inicio. Normalicé formatos, detecté y traté outliers según el contexto del negocio, y gestioné los valores nulos de forma estratégica.

También verifiqué la consistencia entre tablas y apliqué principios de validación cruzada para mantener la integridad del dataset tanto a nivel técnico como operativo.

Además, para optimizar el desarrollo, modularicé el código en funciones dentro de un archivo src, que importé en los notebooks correspondientes. Esta estructura permitió evitar duplicaciones, facilitar el mantenimiento y fomentar la reutilización eficiente del código.

3. Análisis exploratorio y generación de insights

Realicé un análisis exploratorio detallado, tanto univariado como multivariado, centrándome en relaciones clave entre variables para detectar patrones relevantes y descubrir oportunidades de mejora. Para ello, utilicé gráficos de dispersión, matrices de correlación y gráficos de barras, con el fin de entender cómo ciertos factores influían en métricas clave, por ejemplo, la tasa de cancelación.

4. Modelo de regresión logística en R (dplyr, broom, janitor, ggplot2)

Desarrollé un modelo predictivo en R con el objetivo de identificar los factores que más influían en la pérdida de clientes. Incluí todas las variables relevantes como predictoras, tras una limpieza de datos y transformación de variables categóricas. Los coeficientes estadísticamente significativos fueron visualizados mediante un gráfico de barras para facilitar la interpretación del modelo.

Resultado: El modelo permitió detectar que variables como el tipo de contrato, el número de llamadas al soporte y la pertenencia a un plan familiar tienen un impacto claro sobre la probabilidad de abandono. Esta información fue clave para proponer acciones de retención concretas y orientar decisiones estratégicas.

5. Modelado relacional y consultas en SQL (PostgreSQL)

Diseñé un modelo relacional en PostgreSQL que reflejase con precisión la estructura lógica del dataset. Para ello, trabajé con relaciones uno a varios, definiendo correctamente claves primarias y foráneas para garantizar la integridad referencial y facilitar futuras consultas.

Una vez cargados los datos desde Python, elaboré consultas SQL específicas orientadas a responder preguntas clave del negocio, como: “¿Qué impacto tiene el número de llamadas al soporte sobre el abandono?” o “¿Los clientes con plan familiar abandonan menos que los individuales?”.

Estas consultas no solo reproducen los principales hallazgos del análisis exploratorio, sino que también permiten obtener respuestas reproducibles, escalables y directamente accionables desde la base de datos.

6. Visualización y storytelling en Power BI

Integré los datos desde PostgreSQL directamente en Power BI, manteniendo la estructura relacional optimizada. En Power Query validé los datos, establecí relaciones en el modelado y desarrollé medidas DAX personalizadas, así como una tabla calendario para análisis temporal detallado.

Se desarrollaron tres dashboards principales:

Página 1 y página 2: Análisis de segmentos y factores

Página 3: Resumen ejecutivo

- Modelo predictivo (R): Los factores más determinantes en el abandono.
- Tabla resumen de patrones detectados, conclusiones y acciones de negocio recomendadas.

Se aplicó storytelling visual en los títulos de cada gráfico para guiar al lector, y se utilizó la paleta de colores corporativa.

Construí los dashboards con foco en:

- Responder directamente a preguntas clave del negocio
- Mostrar insights claros, rápidos y accionables
- Aplicar principios de visualización, jerarquía visual y atributos preatentivos para destacar los puntos más críticos.

Incorporé marcadores, tooltips personalizados y visuales de alerta para destacar indicadores críticos. Previamente, diseñé las plantillas en Figma, garantizando un mejor rendimiento y una experiencia más optimizada.

7. Cuantificación del impacto

En esta sección hemos cuantificado el impacto que tendrían las acciones de negocio recomendadas sobre tres grupos críticos de clientes:

- Clientes con contrato mensual

- Clientes sin plan familiar

- Clientes con 3 o más llamadas al soporte

Para cada uno de estos segmentos, hemos calculado:

- El número de clientes afectados actualmente

- La tasa de abandono real

- Una tasa de abandono mejorada si se aplica la acción recomendada

- La cantidad de clientes que podríamos retener

- El gasto mensual que se podría recuperar al evitar esas cancelaciones

Todo ello se ha hecho usando medidas DAX en Power BI, basadas en tus datos reales. Esta simulación permite cuantificar con datos concretos el beneficio que tendría para la empresa actuar sobre los factores que más impulsan el abandono.

La implementación de estas acciones podría evitar la pérdida de más de 1.700 clientes, reduciendo el abandono de manera significativa. Esto se traduce en un potencial de recuperación de más de 65.000 € al mes en ingresos, según el valor medio mensual por cliente.

Además, estas acciones no solo tienen impacto económico inmediato, sino que también contribuyen a una mejor experiencia del cliente, fomentan una mayor fidelidad y aumentan el valor de vida del usuario (CLV).
El resultado es un dashboard pensado tanto para perfiles técnicos como de negocio, que facilita la toma de decisiones desde el primer vistazo.​

8. Automatización e inteligencia artificial

Durante el proceso, integré automatizaciones para tareas repetitivas, desde la generación asistida de funciones en Python hasta el uso de inteligencia artificial (GPT)  para documentar, generar código y explicar errores.
Esto permitió optimizar el tiempo y enfocar los esfuerzos en obtener insights relevantes y aplicables al negocio.

9. Documentación del proyecto y datos

Todo el desarrollo técnico del proyecto está documentado con más detalle en mi repositorio de GitHub, donde puede consultarse el código completo.
🔗 (Repositorio vinculado a empresa ficticia)

Los datos utilizados provienen de un dataset público de Kaggle, centrado en la predicción de abandono de clientes en servicios de suscripción.

## Reflexiones finales y evolución futura

Este proyecto no solo permitió identificar con precisión los factores que impulsan la pérdida de clientes, sino también demostrar cómo un enfoque basado en datos puede traducirse en decisiones estratégicas con impacto directo en la retención y rentabilidad del negocio.

Entre las acciones propuestas, destacan tres con impacto inmediato:

- Fomentar contratos de larga duración, como medida preventiva frente al abandono.

- Mejorar la eficiencia del soporte al cliente en las primeras interacciones, evitando frustraciones acumuladas.

- Potenciar planes familiares y servicios complementarios, que se asocian a mayor fidelidad y compromiso.

Estas medidas forman parte de un conjunto más amplio de estrategias derivadas del análisis, todas ellas orientadas a reducir el abandono y aumentar el valor del cliente.

Además de ofrecer resultados tangibles, este análisis sienta las bases para futuras líneas de acción como:

- Integrar modelos de predicción de churn en tiempo real.

- Automatizar alertas para detectar clientes en riesgo.

- Diseñar campañas personalizadas basadas en segmentaciones avanzadas (RFM, CLV).

Este proyecto demuestra cómo el análisis de datos puede anticipar comportamientos críticos y ayudar a construir una relación más sólida, rentable y sostenible entre empresa y cliente.

### Contacto

Portfolio:
Teléfono: 672175240
Email: catiaazancotc@gmail.com
Linkedin:
