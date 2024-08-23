import pandas as pd

# Dataframe es la informacion basica con el nombre de las piezas y centimetros para armar el excel
data = {
    "Piezas": ['Pata','Tablero','Puerta','Estante','Panel'],
    "Centimetros":[40,30,10,20,50]
}
df = pd.DataFrame(data)

# Guardar data frame en un archivo excel
df.to_excel("muebles_medidas.xlsx",index=False)




