# Olympic History
Esta API foi densenvolvida com o intuito armazenar os dados históricos sobre jogos olímpicos modernos contidos em um arquivo csv na raiz deste projeto.

## Como desenvolver?

1. Clone do repositório
2. Crie um ambiente virtual
3. Ative o ambiente
4. Instale as dependências
5. Faça uma cópia do ENV_SAMPLE na raiz do projeto nomeado como .env e configure as variáveis sensiveis
6. Execute as migrations
7. Execute os testes
8. Crie um super usuário
9. Adicione o dataset ao banco de dados
10. Execute a aplicação

```console
git clone https://github.com/gomaaygo/vough.git
pipenv --three
pipenv shell
pivenv install -r requirements.txt
cp ENV_SAMPLE .env
python manage.py migrate
python manage.py test
python manage.py createsuperuser
python manage.py runscript load
python manage.py runserver
```

## Disponível em:

https://olympic-history.herokuapp.com/
