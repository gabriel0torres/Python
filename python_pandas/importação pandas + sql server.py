# coding: utf-8
#autor: Gabriel Torres Santos

import pandas as pd
import pyodbc

#pega o arquivo com o pandas
arquivo = pd.read_csv('C:/diretorio', sep=';')
arquivo = arquivo.fillna(0)

# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = '' 
database = '' 
username = '' 
password = '' 
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

# Inserir o dataframe para o SQL Server:
cursor.execute("DELETE FROM tabela")
for index, row in arquivo.iterrows():
    cursor.execute("INSERT INTO tabela (campos) values(?)", row.campo_csv)
cnxn.commit()
cursor.close()