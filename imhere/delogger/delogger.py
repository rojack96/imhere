import inspect


class Delogger:

    def return_name(counter=[0]):
        counter[0]+=1 # mutable variable get evaluated ONCE
        return print(inspect.stack()[-1][1] + "_" + inspect.stack()[1][3] + "_" + str(counter[0]))
