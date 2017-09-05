from django.db import connections, transaction


class Connection(object):

    __targets = list
    __save_points = dict()

    def __init__(self, targets: list):
        self.__targets = targets

    def get_targets(self):
        return self.__targets

    def exec_query(self, sql: str, create=False):
        if create is False:
            self.start_transaction()
        rollback = False

        for target in self.__targets:
            cursor = connections[target].cursor()
            try:
                cursor.execute(sql)
            except BaseException as e:
                rollback = True
                result = str(e)
                if create is False:
                    self.rollback()
                if create is True:
                    raise RuntimeError("Spitzer could not install: {0}".format(e))

            result = cursor.fetchall()

        if rollback is False and create is False:
            self.commit()

        return result

    def start_transaction(self):
        for target in self.__targets:
            transaction.savepoint(using=target)
            transaction.atomic(using=target)
            self.__save_points[target] = ''
        return self

    def commit(self):
        for target in self.__targets:
            self.__save_points[target]
            transaction.commit(using=target)
        return self

    def rollback(self):
        for target in self.__targets:
            self.__save_points[target]
            transaction.rollback(using=target)
        return self
