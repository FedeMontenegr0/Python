
import pandas as pd

def cm_a_pulgadas(cm):
    return cm / 2.54

# Leer el archivo de excel:
df = pd.read_excel("muebles_medidas.xlsx")

# Añadir una columna que sea de pulgadas y se rellene con el calculo de cm / 2.54
df["Pulgadas"] = df["Centimetros"].apply(cm_a_pulgadas)
df.to_excel("muebles_medidas_pulgadas.xlsx", index=False)
print("Conversion completada y guardada en el archivo 'muebles_medidas_pulgadas.xlsx'")
