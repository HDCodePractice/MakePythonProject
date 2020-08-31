def translate(x:int):
    nbs0To19 = ["", " one", " two", " three", " four", " five", " six", " seven", " eight", " nine", " ten", " eleven", " twelve", " thirteen", " fourteen", " fifteen", " sixteen", " seventeen", " eighteen", " nineteen"]
    nbs0To19dash = ["", "-one", "-two", "-three", "-four", "-five", "-six", "-seven", "-eight", "-nine"]
    nbs20To99 = ["",""," twenty"," thirty"," forty"," fifty"," sixty"," seventy"," eighty"," ninety"]
    english = ""
    if x < 20:
        english = nbs0To19[x]
    elif x > 19 and x < 100:
        english = nbs20To99[int(x/10)] + nbs0To19dash[int(x%10)]
    elif x > 99:
        english = "THIS CALCULATOR BUSTED"
    if x == 1:
        english += " dollar"
    elif x > 1 and x < 100:
        english += " dollars"
    return english
print(translate(27))
