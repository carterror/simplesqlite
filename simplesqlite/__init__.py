import sqlite3


class Field:

    def __init__(self, field):
        self.__type = field
        self.__key = False
        self.__nul = False

    def primary(self):
        self.__key = True
        return self

    def integer(self):
        self.__type += f' INTEGER'
        return self

    def null(self):
        self.__nul = True
        return self

    def boolean(self):
        self.__type += f' BOOLEAN'
        return self

    def text(self):
        self.__type += f' TEXT'
        return self

    def real(self):
        self.__type += f' REAL'
        return self

    def __str__(self) -> str:
        return f'''{self.__type} {('NULL' if self.__nul else 'NOT NULL')} {('PRIMARY KEY' if self.__key else '')}'''


class SSQLite:

    def __init__(self, src='sqlite.db'):
        self.src = src
        self.cn = sqlite3.connect(src)
        self.db = self.cn.cursor()

    def __str__(self) -> str:
        return f'''Conexion created with {self.src}'''

    def create(self, name: str, *types: Field):
        sentence = ''
        for index, typ in enumerate(types):
            sentence = f'''{sentence}{'' if (index == 0) else ', '}{typ}'''

        # print(sentence)
        self.db.execute(f'''CREATE TABLE {name}(
{sentence}
)''')

    def insert(self, name, fields):
        sentence = ''
        values = ''
        tag = True

        for key, value in fields.items():

            if not tag:
                sentence += ', '
                values += ', '

            sentence += f'{key}'

            values += f'{type.__str__(value)}'

            tag = False
        # print(values)
        # print(sentence)
        try:
            self.db.execute(f'''INSERT INTO {name}({sentence}) VALUES ( {values} )''')
            self.cn.commit()
        except Exception as e:
            print(e)