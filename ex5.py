#recebe como entrada a data do dia de hoje.
#retorna os nomes de todos os produtos que já venceram até essa data.

from datetime import date

#recieves an argument (type str) and converts it to a date
def processInput(str):

    expirationDate = date(int(str[6]) * 10**3 + int(str[7]) * 10**2 + int(str[8]) * 10 + int(str[9]),
                          int(str[3]) * 10 + int(str[4]),
                          int(str[0]) * 10 + int(str[1]))
    
    return expirationDate

def main():
    expiration = [date(2024, 9, 23),
                date(2023, 11, 9),
                date(2025, 6, 18),
                date(2024, 2, 4),
                date(2024, 7, 13)]
    
    products = ['A', 'B', 'C', 'D', 'E']
    expired = ''
            
    try:
    
        expirationDate = processInput(input())

        i = -1
        while i < 4:
            i += 1

            #not expired, for sure
            if expirationDate.year < expiration[i].year:
                pass

            #expired, for sure
            elif expirationDate.year > expiration[i].year:
                expired += products[i] + ", "

            #else, verify month

            #not expired, for sure
            elif expirationDate.month < expiration[i].month:
                pass

            #expired, for sure
            elif expirationDate.month > expiration[i].month:
                expired += products[i] + ", "

            #else, verify day

            #not expired, for sure
            elif expirationDate.day < expiration[i].day:
                pass

            #expired, for sure
            elif expirationDate.day >= expiration[i].day:
                expired += products[i] + ", "
        

        if expired == '':
            print('NENHUM')

        else:
            expired = expired[:-2]
            print(expired)


    except:
        print("ERRO")



if __name__ == "__main__":
    main()
