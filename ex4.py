#given the kg price and the total of bread, returns the price payed
def calc_cost(gr, kg_price):

    price = gr * kg_price
    return price / 1000

#verifies if the given number must be rounded up
def rounds_number(n):
    if int(n * 10) % 10 >= 1:
        n += 1
    return n

def main():

    costKg = [14.20, 11.50, 17.30]
    final_price = 0

    try:

        grA = int(input())
        grB = int(input())
        grC = int(input())

        final_price += calc_cost(grA, costKg[0])
        final_price += calc_cost(grB, costKg[1])
        final_price += calc_cost(grC, costKg[2])

        round_price = int(final_price)

        #calculates the decimal part separately (with two decimal digits)
        decimal_part = (final_price * 100) - (round_price * 100)

        decimal_part = rounds_number(decimal_part)

        print(f'R$ {round_price},{int(decimal_part)}')

    
    except:
        print("ERRO")



if __name__ == "__main__":
    main()
