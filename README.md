# SSYS Employee Manager - Documentação

## Introdução
O **SSYS Employee Manager** é uma API desenvolvida para gerenciar informações de funcionários e gerar relatórios. A API permite a criação, leitura, atualização e remoção (CRUD) de funcionários, além de fornecer relatórios baseados em idade e salário. Toda a aplicação é autenticada e pode ser integrada com outras ferramentas.

## Tecnologias Utilizadas
- **Python** (Linguagem principal)
- **FastAPI** (Framework para criação da API)
- **SQLite** (Banco de dados utilizado)
- **Docker** (Para containerização da aplicação)
- **AWS** (Hospedagem da API)

## Instalação e Configuração

### 1. Clonar o repositório
```bash
git clone https://github.com/seuusuario/ssys-employee-manager.git
cd ssys-employee-manager
```

### 2. Construir e rodar com Docker
```bash
docker-compose up --build
```
Isso iniciará a API e o banco de dados dentro de containers.

### 3. Acessar a API
A API estará disponível em:
```
http://localhost:8000/employees
```

A documentação automática do FastAPI pode ser acessada em:
```
http://localhost:8000/docs
```

## Uso da API

### 1. Autenticação
A API utiliza autenticação para acesso. Para realizar chamadas autenticadas, é necessário obter um token de acesso.

### 2. Endpoints Disponíveis

#### Funcionários (CRUD)
- **GET** `/employees/` - Lista todos os funcionários
- **POST** `/employees/` - Cria um novo funcionário
- **GET** `/employees/{id}/` - Retorna os detalhes de um funcionário específico
- **PUT** `/employees/{id}/` - Atualiza um funcionário
- **DELETE** `/employees/{id}/` - Remove um funcionário

#### Relatórios
- **GET** `/reports/employees/salary/` - Relatório de salários
- **GET** `/reports/employees/age/` - Relatório de idades

## Deploy na AWS
Para hospedar na AWS, foi utilizado um container Docker com a API rodando. Os passos para o deploy são:

1. Criar uma instância EC2 na AWS
2. Instalar o Docker na instância
3. Copiar o projeto para a instância
4. Rodar `docker-compose up --build`
5. Configurar regras de firewall para permitir conexões na porta 8000

Agora a API estará acessível publicamente pela URL gerada pela AWS.

## Conclusão
Este projeto fornece uma API robusta para gerenciamento de funcionários e relatórios. Ele pode ser expandido para novas funcionalidades e integrado a outros sistemas facilmente. Se houver alguma dúvida, consulte a documentação do FastAPI para mais detalhes sobre a estrutura da API.

