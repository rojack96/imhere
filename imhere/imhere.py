import inspect


class ImHere:

    def log(var):
        variabile:str = inspect.stack()[1][4][0]
        print("ciao", variabile.split("log(")[1].replace(")", ""))
            
        return print("[" + inspect.stack()[1][1] + "][" + inspect.stack()[1][3] + "][line " + str(inspect.stack()[1][2]) + "]")
