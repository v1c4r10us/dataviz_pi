import pandas as pd
#Primer dataset
penetracion_internet=pd.read_csv('https://datosabiertos.enacom.gob.ar/rest/datastreams/275028/data.csv')
penetracion_internet['Accesos por cada 100 hogares']=penetracion_internet['Accesos por cada 100 hogares'].str.replace(',','.') #Normalizamos las cantidades numéricas
#Segundo dataset
penetracion_por_hogar_fijo=pd.read_csv('https://datosabiertos.enacom.gob.ar/rest/datastreams/281491/data.csv')
penetracion_por_hogar_fijo['Accesos por cada 100 hogares']=penetracion_por_hogar_fijo['Accesos por cada 100 hogares'].str.replace(',','.') #Normalización
penetracion_por_hogar_fijo['Accesos por cada 100 hab']=penetracion_por_hogar_fijo['Accesos por cada 100 hab'].str.replace(',','.') #Normalización
#Tercer dataset
tecnologia=pd.read_csv('https://datosabiertos.enacom.gob.ar/rest/datastreams/255796/data.csv')
tecnologia.dropna(inplace=True)
tecnologia['Año']=tecnologia['Año'].str.replace('*','')
tecnologia['Año']=tecnologia['Año'].str.strip()
tecnologia['Trimestre']=tecnologia['Trimestre'].str.replace('*','')
tecnologia['Trimestre']=tecnologia['Trimestre'].str.strip()
tecnologia['ADSL']=tecnologia['ADSL'].str.replace('.','')
tecnologia['Cablemodem']=tecnologia['Cablemodem'].str.replace('.','')
tecnologia['Fibra óptica']=tecnologia['Fibra óptica'].str.replace('.','')
tecnologia['Wireless']=tecnologia['Wireless'].astype(str)
tecnologia['Wireless']=tecnologia['Wireless'].str.replace('.','')
tecnologia['Otros']=tecnologia['Otros'].astype(str)
tecnologia['Otros']=tecnologia['Otros'].str.replace('.','')
tecnologia.drop(['Total'], axis=1, inplace=True)
#Cuarto dataset
ingresos=pd.read_csv('https://datosabiertos.enacom.gob.ar/rest/datastreams/275023/data.csv')
ingresos['Ingresos (miles de pesos)']=ingresos['Ingresos (miles de pesos)'].str.replace('.','')
#KPI_1: Incremento 2% para proximo trimestre
incremento_por_provincia=penetracion_internet[(penetracion_internet['Año']==2022)&(penetracion_internet['Trimestre']==3)]
incremento_por_provincia=incremento_por_provincia[['Provincia','Accesos por cada 100 hogares']]
incremento_por_provincia['Accesos por cada 100 hogares']=incremento_por_provincia['Accesos por cada 100 hogares'].astype(float)
incremento_por_provincia['Goal']=incremento_por_provincia['Accesos por cada 100 hogares'].apply(lambda x: round(x*1.02,2))
incremento_por_provincia=incremento_por_provincia[['Provincia','Goal']]
