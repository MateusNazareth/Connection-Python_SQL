import pyodbc
import pandas as pd

# estabelecendo conexao:

dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-QIJHN40;"
    "Database=PythonSQL;"
    )

conexao = pyodbc.connect(dados_conexao)
print("conexao bem sucedida")

# Populando o Banco ou fazendo qualquer alteração:

#cursor = conexao.cursor()
# comando = """INSERT INTO Vendas(id_venda, cliente, produto, data_venda, preco, quantidade)
# VALUES
#     (4, 'Fra', 'PYTHON', '02/15/2021', 8000, 1)"""
#cursor.execute(comando)
#cursor.commit()        #Apenas se precisar editar o Banco de dados


#Lendo Tabelas

data = pd.read_sql('select * from exercise01', conexao)
print(data)




