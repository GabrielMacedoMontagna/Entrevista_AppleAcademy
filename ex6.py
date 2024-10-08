#recebe, como entrada, uma quantidade em gramas de algum produto.
#retorna  quantos grupos de 1000g, 450g e 100g (A, B ou C) precisam ser usados para chegar na quantidade total do produto.

def main():
                # A  B  C
    quantities = [0, 0, 0]

    try:

        order = int(input())

        while order > 0:
            #if order is bigger than or equal to 1kg
            if order >= 1000:
                quantities[2] += 1
                order -= 1000

            #else, if order is bigger than or equal to 450g
            elif order >= 450:
                quantities[1] += 1
                order -= 450
            
            else:
                quantities[0] += 1
                order -= 100

        print(f'A({quantities[0]}) B({quantities[1]}) C({quantities[2]})')

    except:
        print("ERRO")



if __name__ == "__main__":
    main()
