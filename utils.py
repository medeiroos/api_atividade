from models import Pessoas


# INSERE DADOS NA TABELA PESSOA
def insere_pessoas():
    pessoa= Pessoas(nome='João', idade=22)
    print(pessoa)
    pessoa.save()


# CONSULTA PESSOAS NA TABELA
def consulta_pessoas():
    pessoas= Pessoas.query.all()
    print(pessoas)
    pessoa= Pessoas.query.filter_by(nome='João').first()
    print(pessoa.idade)


# ALTERA PESSOAS NA TABELA
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='João').first()
    pessoa.idade = 22
    pessoa.save()

# EXCLUI PESSOAS
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome="João").first()
    pessoa.delete()


if __name__ == '__main__':
    insere_pessoas()
    altera_pessoa()
    exclui_pessoa()
    consulta_pessoas()
