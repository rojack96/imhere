import inspect


class Delogger:

    def return_name():
        return print("[" + inspect.stack()[1][1] + "][" + inspect.stack()[1][3] + "][line " + str(inspect.stack()[1][2]) + "]")
