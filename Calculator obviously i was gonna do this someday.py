def add( n1 , n2 ):
    return n1 + n2
def sub( n1 , n2 ):
    return n1 - n2
def mult( n1 , n2 ):
    return n1 * n2
def divi( n1 , n2 ):
    return n1 / n2
operations = {
    "+" : add ,
    "-" : sub ,
    "*" : mult ,
    "/" : divi
}
def step2():
    for symbols in operations :
        print(symbols)
    action = input("Enter the function you want to perform : ")
    if action != "*" and action != "+" and action != "-" and action != "/":
        print("wrong parameter!!!")
        step2()
        return
    a = float(input("Enter first number : "))
    b = float(input("Enter second number : "))
    nana = operations[action](n1 = a,n2 = b)
    print(f" {a} {action} {b} = {nana}")
    again_ask()
def again_ask():
    ag = input("Do you want to perform another calculation (yes , no): ").lower()
    if ag =="yes" :
        print("\n" *20)
        step2()
    else:
        pass
step2()
