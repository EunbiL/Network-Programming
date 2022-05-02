'''
Exercice 4 - Analyze CSV
1. Retrieve the file of the most loaned titles in libraries in Paris
2. Analyze the resulting CSV file to display, for all entris: title, author, and number of loans.
3. Display for each type of document (there can be several entries for the same type of document)
 the total number of loans for this type.
4. Display titles in order of profitability (in descending order of the number of loans per copy)
'''

from csv import *
with open('title.csv', newline='') as csvfile :
    r = reader(csvfile, delimiter=';', quotechar='|')
    document = []
    count = 0
    total1 = 0
    total2 = 0
    total3 = 0
    total4 = 0
    total5 = 0
    total6 = 0
    total7 = 0
    total8 = 0
    total9 = 0
    profit = 0
    l_profit = []
    dictionary = {}


    for row in r:
        try :
            count += 1
            document.append(row[1])
            profit = int(row[6])/int(row[8])
            print(row[1],',',row[6],',',row[3],',',row[8],',',profit)
            dictionary[row[3]] = profit
        except ValueError :
            print("hmm")


        if row[1] == 'Livre jeunesse' :
            total1 += int(row[6])
        if row[1] == 'Bande dessinée pour adulte':
            total2 += int(row[6])
        if row[1] == 'Jeux de société':
            total3 += int(row[6])
        if row[1] == 'Livre pour adulte':
            total4 += int(row[6])
        if row[1] == 'Bande dessinée jeunesse':
            total5 += int(row[6])
        if row[1] == 'Livre sonore jeunesse':
            total6 += int(row[6])
        if row[1] == 'Enregistrement musical pour la jeunesse':
            total7 += int(row[6])
        if row[1] == 'DVD jeunesse':
            total8 += int(row[6])
        if row[1] == 'Jeux Vidéos tous publics':
            total9 += int(row[6])

    print("=====================total====================")
    print("Livre jeunesse:",total1)
    print("Bande dessinée pour adulte:", total2)
    print("Jeux de société:", total3)
    print("Livre pour adulte:", total4)
    print("Bande dessinée jeunesse:", total5)
    print("Livre sonore jeunesse:", total6)
    print("Enregistrement musical pour la jeunesse:", total7)
    print("DVD jeunesse:", total8)
    print("Jeux Vidéos tous publics:", total9)
    print("===============================================")


    print("Type of document")
    doc = list(set(document))
    print(doc)

    print("===============================================")
    #print("dictionary:", dictionary)
    #print("values :", sorted(dictionary.values()))
    sorted_dictionary = sorted(dictionary, key=lambda x:dictionary[x])
    print("the titles in order of profitability")
    print(sorted_dictionary)