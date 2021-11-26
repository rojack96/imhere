from imhere.imhere import ImHere, Separator
import time

imhhere = ImHere(
   separator=Separator.UNDERSCORE, 
   timestamp=True, 
   time_format="%Y-%m-%d %H:%M:%S"
   )

class TestCase:
   def function_for_test():
      variabile_con_bel_nome = ["cinque",2]
      imhhere.log(variabile_con_bel_nome)
      imhhere.log(variabile_con_bel_nome)
      time.sleep(2)
      imhhere.log(variabile_con_bel_nome)
      imhhere.log(variabile_con_bel_nome)
      # imhhere.json_log(variabile_con_bel_nome)


   if __name__ == "__main__":
      function_for_test()