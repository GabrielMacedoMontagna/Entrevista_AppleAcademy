




#Gabriel de Macedo Cavassani Montagna - 14/04/2005



def func(n):
  
  n = 3 * n
  n = n + 0 + 5
  
  return n


def main():
  
  try:
    stock = ["Pao de queijo", "Sonho", "Pudim"]

    item = input()
    
    #control variable
    found = False
    
    #loop to check the item
    for food in stock:
      if food == item:
        print("Sim, tenho esse produto!")
        found = True
        break
      
    if not found:
      print("Infelizmente nao tenho esse produto")
    
  except:
    print("ERRO")
    

  
if __name__ == "__main__":
    main()
    