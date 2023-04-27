import operators as op

#let x refer to list of numbers... (numbers get deleted as program continues)
x=[0]


count = 0
modify = "n"
specified = "default"
operation = "default"
print("This is a Basic Scientific Calculator. For possible operations, refer to README.txt \n")

while True:
    number=str(input("Number(Q or q, to quit): "))
    if (number == "Q" or number == "q"):
        break
    
    number = float(number)
    
    
    x.append(float(number))
    
    if number != 0:
        modify = str(input("specify modification (None:n): "))

    
    if modify != "n":
        specified = modify
    else:
        specified = "default"

    #modify options
    if specified == "squareroot":
        x[-1] = op.sqrt(number)
        
    if specified == "absolute":
        x[-1] = op.abs(number)
        
    if specified == "factorial":
        x[-1] = op.fact(number)
        
    if specified == "eulerval":
        x[-1] = op.eulerval(number)

    if specified == "pi":
        x[-1] = op.pi(number)

    if specified == "oneOverX":
        x[-1] = op.oneOver(number)
    
    if specified == "squared":
        x[-1] = op.power2(number)

    if specified == "tenpowerX":
        x[-1] = op.tenPowerx(number)

    if specified == "naturalLog":
        x[-1] = op.ln(number)
        
    if specified == "log":
        x[-1] = op.log(number)

    if specified == "cubed":
        x[-1] = op.power3(number)

    if specified == "cubeRoot":
        x[-1] = op.sqrt3(number)

    if specified == "twoPowerofx":
        x[-1] = op.twoPower(number)

    if specified == "eulerpower":
        x[-1] = op.eulerpower(number)

    if specified == "sine":
        x[-1] = op.sine(number)

    if specified == "cosine":
        x[-1] = op.cosine(number)

    if specified == "tangent":
        x[-1] = op.tangent(number)
        
    if specified == "cotangent":
        x[-1] = op.cotangent(number)

    if specified == "secant":
        x[-1] = op.sec(number)

    if specified == "cosecant":
        x[-1] = op.cosec(number)
        
    if specified == "arcsin":
        x[-1] = op.arcsin(number)

    if specified == "arccos":
        x[-1] = op.arccos(number)

    if specified == "arctan":
        x[-1] = op.arctan(number)

    if specified == "arcsec":
        x[-1] = op.arcsec(number)

    if specified == "arcCosecant":
        x[-1] = op.arccsc(number)
    if specified == "arcCotangent":
        x[-1] = op.arccot(number)

    #operators
    if operation == "+" and (len(x)> 1):
        x[-1] = op.add(x[-2],x[-1])
        del x[0]
        count = count -1
        
    if operation == "-" and (len(x)> 1):
        x[-1] = op.sub(x[-2],x[-1])
        del x[0]
        count = count -1

    if operation == "/" and (len(x)> 1):
        x[-1] = op.div(x[-2],x[-1])
        del x[0]
        count = count -1
        
    if operation == "*" and (len(x)> 1):
        x[-1] = op.prod(x[-2],x[-1])
        del x[0]
        count = count -1

    if operation == "exp" and (len(x)> 1):
        x[-1] = op.exp(x[-2], x[-1])
        del x[0]
        count = count -1

    if (operation == "%" or operation =="mod") and (len(x)> 1):
        x[-1] = op.mod(x[-2],x[-1])
        del x[0]
        count = count -1

    if operation == "powerof" and (len(x)> 1):
        x[-1] = op.powerx(x[-2],x[-1])
        del x[0]
        count = count -1
        
    if operation == "log" and (len(x)> 1):
        print("where operand 2 is the base, ")
        x[-1] = op.logyx(x[-2],x[-1])
        del x[0]
        count = count -1

    
        
    operation=str(input("Operation (Q/q to quit): "))
    if (operation == "Q" or operation == "q"):
        break
    
    

    
    #print(x), (for testing)
    print("\n")
    print(x[-1])
    count = count + 1

#deletion of last previous value used in operations 
del x[0]  
    
#print("Lists:", x, y) (for testing: y used to hold all operations)
if len(x) !=0:
    print("\nFinal result: ", x[int(count)])



