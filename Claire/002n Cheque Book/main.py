NumberToNineteen = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fiveteen", "Sixteen", "Seventeen", "Egihteen", "Nighteen"]

WholeTen = ["Twenty", "Thirty", "Fourty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

Singles = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]

def toCheck(thenumber): 

    if thenumber < 20:
        result = NumberToNineteen[thenumber - 1]
       
    else: 
        firstOne = int(thenumber / 10)
        secondOne = thenumber % 10
        
        if secondOne == 0: 
            result = WholeTen[firstOne - 2]
        else:    
            result = "%s-%s"%(WholeTen[firstOne - 2], Singles[secondOne - 1] )

    return result 

numbersInt = int(input('Enter number: '))

print(toCheck(numbersInt))
