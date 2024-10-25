 # CASE BACK-END

> API em django para cadastro, consulta, atualização e exclusão de usuários.

## Índice
- [Sobre o Projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Instalação](#instalação)
- [Uso](#uso)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Sobre o Projeto
    Essa API foi desenvolvida como parte de um projeto para uma empresa de tecnologia, com o objectivo de atender às necessidades de um cliente que busca uma apliicação web para o cadastro e gestão de informações básicas de seus funcionarios. A GenFocus, permite cadastrar, listar, atualizar e excluir registros de pessoas.
### Entidade Pessoa
Cada pessoa cadastrada na API possui os seguintes atributos:
- Nome Completo
- Data de nascimento
- Endereço
- CPF
- Estado Civil

## Funcionalidades

- **Cadastro de Pessoas**: Permite adicionar novas pessoas ao sistema.
- **Consulta de Pessoas**: Exibe as informações das pessoas cadastradas.
- **Atualização de Pessoas**: Permite atualizar dados de um cadastro existente.
- **Exclusão de Pessoas**: Permite remover registros de pessoas.

## Tecnologias Utilizadas

- **Linguagem**: Python
- **Framework**: Django
- **Banco de Dados**: SQLite

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/LuigiBMacario/caseBackEnd.git
2. Acesse o diretório do projeto:
   ```bash
   cd djangoBackEnd
3. Crie um ambiente virtual e ative-o:
    ```bash
    python3 -m venv venv
    source venv/bin/activate # Para sistemas Unix
    venv\Scripts\activate # Para Windows
4. Instale as dependências:
   ```bash 
   pip install -r requirements.txt
