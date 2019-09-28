try:       
    from codelibrary import *
    
except Exception as e:        
    print(e)
    exit(-1)

class TechTerm:
    def __init__(self, term : str, definition : str):
        self.term = term
        self.definition = definition       
    def __str__(self):
        return self.term + '\n' + self.definition

def fromrow(rowdata:list):
    return TechTerm(rowdata[0],rowdata[1])

techterms = loadfromcsv('techterms.csv',fromrow)

print(pickrandom(techterms))


