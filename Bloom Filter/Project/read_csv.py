import csv
L = []
with open('articles.csv', 'r',encoding='utf8') as file:
    reader = csv.reader(file)
    for row in reader:
        L.append(row[4])
        
print(L)