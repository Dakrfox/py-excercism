def convert(number):
    str1 =""
    flag=True
    if number%3==0:
        str1 = str1 + "Pling"
        flag=False
    if number%5==0:
        str1 = str1 + "Plang"
        flag=False
    if number%7==0:
        str1 = str1 + "Plong"
        flag=False
    if flag:
        str1 = f"{number}"
    return str1
