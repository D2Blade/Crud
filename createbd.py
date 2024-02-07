import peewee

#criando databse
db = peewee.SqliteDatabase("Clientes.db")

class BaseModel(peewee.Model):

    class Meta:

        database = db

class cliente(BaseModel):

    nome = peewee.CharField()
    nasc = peewee.DateField(formats=['%d-%b-%a'])
    cpf = peewee.IntegerField(unique = True)
    ativo = peewee.CharField()


if __name__ == '__main__':

    try:
        cliente.create_table()
        print('tabela criada com sucesos')
    except peewee.OperationalError:
        print('Tabela já existente')

    