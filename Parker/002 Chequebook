NumbersBelow19  = ["One", "Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Ninteen"]

multiplesOf10 = ["Twenty" , "Thirty" , "Fourty" , "Fifty" , "Sixty" , "Seventy" ,"Eighty" , "Ninety"]

singleDigits = ["One", "Two","Three","Four","Five","Six","Seven","Eight","Nine"]

def doHigh(anumber):
   
    if anumber < 20: 
        result = NumbersBelow19[anumber-1]
    else: 
        aPart = int(anumber / 10)
        bPart = anumber % 10
        if bPart == 0:
            result = multiplesOf10[aPart - 2]
        else:    
            result = "%s-%s"%(multiplesOf10[aPart - 2], singleDigits[bPart - 1] )
    return result 

numberToBeConverted = int(input('Enter number: '))
print(doHigh(numberToBeConverted))
