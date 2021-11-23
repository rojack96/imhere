import inspect


class Delogger:

    def return_name():
        return print(inspect.stack()[1][1] + "_" + inspect.stack()[1][3] + "_line " + str(inspect.stack()[1][2]))
