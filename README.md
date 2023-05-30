```plaintext
██████╗  █████╗ ████████╗ █████╗     ██╗   ██╗██╗███████╗
██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗    ██║   ██║██║╚══███╔╝
██║  ██║███████║   ██║   ███████║    ██║   ██║██║  ███╔╝ 
██║  ██║██╔══██║   ██║   ██╔══██║    ╚██╗ ██╔╝██║ ███╔╝  
██████╔╝██║  ██║   ██║   ██║  ██║     ╚████╔╝ ██║███████╗
╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝      ╚═══╝  ╚═╝╚══════╝

[*] Story_telling in progress...
```

Proyecto individual de **Data Visualization** con datos provenientes de la fuente pública <a href="https://datosabiertos.enacom.gob.ar/dashboards/20000/acceso-a-internet/">ENACOM</a> del gobierno argentino, acerca del sector **telecomunicaciones**, principalmente el **acceso a internet**.

---

## Intro

La empresa Virgin desea evaluar el panorama del negocio de acceso a internet, por lo que nos encomienda la tarea de realizar la presentación y **data storytelling** en función a los datos extraídos de la fuente gubernamental.

## Desarrollo

+ Se realiza un análisis exploratorio a la información publicada, seleccionando los datasets con mayor información útil, el desarrollo se puede ver en **`EDA_pi.ipynb`**.

+ Mediante **`scriptPower.py`** como orígen de datos para **Power BI**, se extrae la información de los endpoint que pone a disposición el organismo y se empieza a trabajar sobre ello estableciendo las relaciones y transformaciones necesarias.

+ Para las visualizaciones tipo mapa, se genera de forma manual un dataset con las coordenadas de cada provincia de Argentina, objeto de estudio. Esto en **`provinciaData.py`**

## KPIs

Se ha establecido los siguientes indicadores clave para el estudio:

+ Incremento en 2% del acceso a internet por cada 100 hogares respecto al trimestre anterior, por provincia.
+ Incremento de la preferencia de tecnología wireless sobre el resto en 25%, por provincia.
+ Total ingreso último trimestre.
+ Incremento del ingreso en 10% respecto al trimestre anterior.

## Visualizaciones

<p align="center"><a href="https://lh3.googleusercontent.com/drive-viewer/AFGJ81qQkseLRDqL1LxLGJfxqJewWe0_ySEdA3MfDDguPmUkWP7h966JUaFO3rIRbAm-gMCawwYEe-0smsgZDpzL--Z5xxSiLw=s1600?source=screenshot.guru"> <img src="https://lh3.googleusercontent.com/drive-viewer/AFGJ81qQkseLRDqL1LxLGJfxqJewWe0_ySEdA3MfDDguPmUkWP7h966JUaFO3rIRbAm-gMCawwYEe-0smsgZDpzL--Z5xxSiLw=s1600" /></a></p>

<p align="center"><a href="https://lh3.googleusercontent.com/drive-viewer/AFGJ81ogWM0Cg1hpN_Dy3Hl4DGTB_PniLGTCSCGIotaq1Q7qLCAGUPm8789rhMi1mkyYIMOLTUHs_1ANs7UVBi_gWUfmiOqRwQ=s1600?source=screenshot.guru"> <img src="https://lh3.googleusercontent.com/drive-viewer/AFGJ81ogWM0Cg1hpN_Dy3Hl4DGTB_PniLGTCSCGIotaq1Q7qLCAGUPm8789rhMi1mkyYIMOLTUHs_1ANs7UVBi_gWUfmiOqRwQ=s1600" /></a></p>




