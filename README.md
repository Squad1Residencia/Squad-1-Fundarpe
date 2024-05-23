<img alt="Python" src="https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white"/><img alt="Django" src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white"/><img alt="MySQL" src="https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=black"/><img alt="Visual Studio Code" src="https://img.shields.io/badge/VisualStudioCode-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white"/><img alt="Git" src="https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white"/>
# Sistema de Gerenciamento Fundarpe
Sistema de Gerenciamento de Processos desenvolvido por alunos da UNIT no desafio do Porto Digital de residência em software backend para a Fundarpe.

## 🛠Pré-requisitos
Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
- [Git](https://git-scm.com)
- [Python 3](https://www.python.org/downloads/)
- [MySQL](https://dev.mysql.com/downloads/installer/)
- [Visual Studio Code](https://code.visualstudio.com/Download)
> [!TIP]
> Ao instalar é recomendavel adicionar o caminho do python e o mysql ao ``PATH`` do sistema.
>
> Como Acessar: https://www.java.com/pt-BR/download/help/path_pt-br.html

## 🚀 Como executar o projeto
### 1. Clone este repositório
Acessando o terminal do VSCode, digite o comando a seguir. (De preferência, use a Interface (CLI) do Git Bash)
```git
git clone https://github.com/Squad1Residencia/Squad-1-Fundarpe.git
```
### 2. Acesse a pasta do projeto no terminal
Navegue até o diretório onde você clonou o repositório:
```
cd <caminho>/sg_fundarpe
```
- Substitua `<caminho>` pelo caminho real onde o projeto foi clonado.
- Caso já esteja no caminho certo, digite apenas `cd sg_fundarpe`.
### 3. Crie um ambiente virtual chamado "myenv"
Para isolar as dependências do projeto, crie um ambiente virtual com o seguinte comando:
```
python -m venv myenv
```
### 4. Ative o ambiente virtual
Ainda no terminal, execute:

**No Windows**
```
myenv\Scripts\activate
```
- Caso não consiga ativar com esse comando, tente também: `myenv/Scripts/activate`
  
**No Linux ou MacOS**
```
source myenv/bin/activate
```
### 5. Instale as dependências
Com o ambiente virtual ativado, instale as dependências do projeto, localizada na pasta do Squad-1-Fundarpe:
```
$ pip install -r requirements.txt
```
>[!note]
>Se ele não encontrar o ``requirementes.txt``, você provavelmente está no nível errado do projeto.
> Execute ``cd ..`` no terminal e/ou navegue para ``<caminho>\Squad-1-Fundarpe`` e tente novamente.
## 🎲Configurando o Banco de Dados
### 1. Acesse o MySQL 
```
mysql -u root -p
```
Após executar o comando digite a senha do usuário ``root``. (A mesma que acessa o MySQL)
>[!warning]
>Em caso de erro: ``'mysql' não é um termo reconhecido ...``, o MySQL provavelmente não está no ``PATH`` do Sistema.
> 
>A partir disso você pode adicioná-lo ao ``PATH`` nas váriaveis do sistema, saiba mais [aqui](https://www.java.com/pt-BR/download/help/path_pt-br.html). Ou você também pode Localizar o diretório de instalação do MySQL e executar lá. Geralmente o caminho é algo como:  ``C:\Program Files\MySQL\MySQL Server 8.0\bin``. Navegue para ```cd <caminho>\MySQL Server 8.0\bin``` e execute o comando acima.
> - Preste atenção a versão do seu MySQL Server, caso for executar este comando: `cd <caminho>\MySQL Server [aqui] \bin`

### 2. Crie um novo banco de dados
Após o `mysql>` digite o seguinte comando:
```sql
CREATE DATABASE gerenciamento_fundarpe;
```
Depois, saia do MySQL:
```sql
exit;
```
### 3. Conecte o projeto ao banco
Abra o arquivo `settings.py` do projeto no VS Code ou no editor de sua preferência. Localize a seção `DATABASES` que  é usada para configurar o banco de dados do seu projeto Django, 
e configure-a conforme abaixo:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'gerenciamento_fundarpe',
        'USER': 'root',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
>[!important]
>Lembre-se de substituir ``'sua_senha'`` pela senha real do usuário ``'root'``.
### 4. Execute as migrações
No terminal, com o ambiente virtual ativado, execute:
```
python manage.py makemigrations
```
```
python manage.py migrate
```
### 5. Execute o servidor de desenvolvimento do Django
Ainda no terminal, acesse a pasta do projeto novamente:
```
cd <caminho>/sg_fundarpe
``` 
Após isso, execute o servidor de desenvolvimento:
```
python manage.py runserver
```
Tendo feito tudo corretamente, é só acessar o projeto no seu navegador através do endereço proporcionado. 

Exemplo: `http://127.0.0.1:8000/`
## 🖥Desenvolvedores
- Hugo Oliveira Ramos
- João Gabriel Matos Santos Maia
- Isaac Castro Silva
- Adonai Santos Fernandes
- Marcos Vinicius de Brito Prado
- Igor Pedro Bezerra Bispo Santos
- Gabriel Carmo Oliveira Lima
- Jorge Célio do Prado Nascimento Júnior
- Pedro Henrique Marafelli Costa

