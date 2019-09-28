
def loadfromcsv(filename, row_method):
    import csv    
    data = []
    with open(filename,encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            data.append(row_method(row))    
    return data

def pickrandom(collection):    
    import secrets as random    
    return random.choice(collection)
