#imprime "bom dia", "boa tarde" ou "boa noite", a depender da hora do dia.

def main():
  
  try:
    msg = input()
    time = int(input())
    
    #checks time
    if time >= 19 or time <= 4:
      ans = "Boa noite"
    
    elif time <= 11:
      ans = "Bom dia"
    
    else:
      ans = "Boa tarde"
    
    print(ans + ", em que posso ajudar?")
    
  except:
    print("ERRO")


if __name__ == "__main__":
    main()
    
