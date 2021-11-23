from imhere.delogger.delogger import Delogger


def example():
   Delogger.return_name()
   Delogger.return_name()
   Delogger.return_name()

def pippo():
   Delogger.return_name()

if __name__ == "__main__":
    example()
    pippo()