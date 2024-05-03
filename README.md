<img alt="Python" src="https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white"/><img alt="Django" src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white"/><img alt="MySQL" src="https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=black"/><img alt="Visual Studio Code" src="https://img.shields.io/badge/VisualStudioCode-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white"/><img alt="Git" src="https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white"/>
# Sistema de gerenciamento fundarpe
Sistema de gerenciamento de processos desenvolvido por alunos da UNIT no desafio do porto digital de residência em software backend para a fundarpe.

## 🛠Pré-requisitos
Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
- [Git](https://git-scm.com)
- [Python 3](https://www.python.org/downloads/)
- [MySQL](https://dev.mysql.com/downloads/installer/)
- [Visual Studio Code](https://code.visualstudio.com/Download)

## 🚀 Como executar o projeto
### Clone este repositório
```git
git clone https://github.com/Squad1Residencia/Squad-1-Fundarpe.git
```
### Acesse a pasta do projeto no terminal
```
cd sg_fundarpe
```
### Crie um ambiente virtual chamado "myenv"
```
virtualenv myenv
```
### Ative o ambiente virtual
```
myenv\Scripts\activate
```
### Instale as dependências
```
$ pip install -r requirements.txt
```
## 🎲Configurando o Banco de Dados
### Acesse o MySQL
```
mysql -u root -p
```
### Crie um novo banco de dados
```sql
mysql> CREATE DATABASE gerenciamento_fundarpe;
```
```sql
mysql> exit;
```
### Conecte o projeto ao banco
No arquivo ``settings.py``, você encontrará uma seção chamada ``DATABASES``. Esta seção é usada para configurar o banco de dados do seu projeto Django
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
### Execute as migrações
```
python manage.py makemigrations
```
```
python manage.py migrate
```
### Execute o servidor de desenvolvimento do Django
```
python manage.py runserver
```
## 🖥Desenvolvedores
-
-
-
-
-
-
-
-
-
