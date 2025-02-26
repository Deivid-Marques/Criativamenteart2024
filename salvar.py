from flask import Flask, request, jsonify
import pandas as pd
import os

app = Flask(__name__)

# Nome do arquivo Excel
arquivo_excel = "usuarios.xlsx"

@app.route('/salvar', methods=['POST'])
def salvar_dados():
    dados = request.json  # Recebe os dados enviados pelo JavaScript

    # Verifica se o arquivo Excel já existe
    if os.path.exists(arquivo_excel):
        df = pd.read_excel(arquivo_excel)  # Abre o arquivo existente
    else:
        df = pd.DataFrame(columns=["Nome", "E-mail", "Senha"])  # Cria um novo DataFrame

    # Adiciona os novos dados
    novo_dado = pd.DataFrame([[dados["nome"], dados["email"], dados["senha"]]], columns=["Nome", "E-mail", "Senha"])
    df = pd.concat([df, novo_dado], ignore_index=True)

    # Salva no arquivo Excel
    df.to_excel(arquivo_excel, index=False)

    return jsonify({"mensagem": "Cadastro realizado com sucesso!"})

if __name__ == '__main__':
    app.run(debug=True)