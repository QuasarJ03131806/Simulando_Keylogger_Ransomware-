#!/bin/bash

# Cria o ambiente virtual
python3 -m venv venv

# Ativa o ambiente virtual
source venv/bin/activate

# Instala as dependências
pip install -r requirements.txt

echo "Ambiente configurado com sucesso!"
echo "Para ativar o ambiente no futuro, use: source venv/bin/activate"
