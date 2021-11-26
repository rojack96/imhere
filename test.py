from imhere.imhere import ImHere, Separator
import time

imhere = ImHere(
   separator=Separator.ARROW, 
   timestamp=True, 
   time_format="%Y-%m-%d %H:%M:%S"
   )

class TestCase:
   def function_for_test():
      variabile_con_bel_nome = ["cinque",2]
      imhere.log()
      imhere.log(variabile_con_bel_nome)
      time.sleep(2)
      imhere.log(variabile_con_bel_nome)
      imhere.log(variabile_con_bel_nome)
      time.sleep(2)
      imhere.json_log(variabile_con_bel_nome)


   if __name__ == "__main__":
      function_for_test()