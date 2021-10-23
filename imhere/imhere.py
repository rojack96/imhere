import inspect


class ImHere:

    def returnName(counter=[0]):
        counter[0]+=1 # mutable variable get evaluated ONCE
        return inspect.stack()[-1][1] + "_" + inspect.stack()[1][3] + "_" + str(counter[0])


