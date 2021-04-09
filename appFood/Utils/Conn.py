import sqlite3

class Conn(object):
    """docstring for Conn."""

    def __init__(self):
        super(Conn, self).__init__()
        self.__conn = sqlite3.connect('H:\\py3_completo\\appFood\\Utils\\db\\app_food.db')
        self.__cur = self.__conn.cursor()

    def _createTable(self, *args, **kwargs):
        table = kwargs["table"]

        fields = ""
        for i, field in enumerate(args):
            field+= ", " if i is not len(args)-1 else ""
            fields+=field
        try:
            self.__cur.execute(f"CREATE TABLE {table} ({fields})")
            self.__conn.close()
            return True
        except Exception as e:
            print(e)
            return False

    def _selectAll(self, *args, **kwargs):
        table = kwargs["table"]
        try:
            self.__cur.execute(f"SELECT * FROM {table}")
            response = self.__cur.fetchall()
            self.__conn.close()
            return True, response
        except Exception as e:
            print(e)
            return False, None

    def _selectEach(self, *args, **kwargs):
        table = kwargs["table"]
        try:
            self.__cur.execute(f"SELECT * FROM {table} WHERE {args[0]} = '{args[1]}'")
            response = self.__cur.fetchone()
            self.__conn.close()
            return True, response
        except Exception as e:
            print(e)
            return False, None

    def _insertItem(self, *args, **kwargs):
        table = kwargs["table"]
        try:
            self.__cur.execute(f"INSERT INTO {table}({args[0]}) VALUES({args[1]})");
            self.__conn.commit()
            self.__conn.close()
            return True
        except Exception as e:
            print(e)
            return False
