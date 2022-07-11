import pyodbc
import pandas as pd

dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-QIJHN40;"
    "Database=PythonSQL;"
    )
conexao = pyodbc.connect(dados_conexao)
print("conection estabilished")

cursor = conexao.cursor()

#Creating the table

comando ="""
CREATE TABLE exercise01(
produto varchar(50),
marca varchar(50),
valor decimal(9,2))"""

cursor.execute(comando)
cursor.commit()
print ('Table created in Data Base')

path = r"C:\\Users\\USUÁRIO\Documents\\Exercicio_python_sql_populandoDB.xlsx"
planilha = pd.read_excel(path)

for i in range(len(planilha)):
    
    produto = planilha.iloc[i,0]
    marca = planilha.iloc[i,1]
    valor = planilha.iloc[i,2]
    i+=1
    comando = f"""INSERT INTO exercise01 (Produto, Marca, Valor)
    VALUES ('{produto}', '{marca}',{valor})"""
    cursor.execute(comando)
    cursor.commit()

print(' tabela populada com sucesso!')