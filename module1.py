#1.Простейшие арифметические операции
def arithmetic(a: float,b:float,c:str):
    """lihtne kalkulaator
    + - liitmine
    - - lahutamine
    * - korrutamine
    / - jagamine
    :param float a: Esimene arv
    :param float b: Teine arv 
    :param str c: Aritmeetiline tehing
    :rtype float:
    """
    if c=="+":
        r=a+b
    elif c=="-":
        r=a-b
    elif c=="*":
        r=a*b
    elif c=="/":
        if b!=0:
            r=a/b
        else:
            print("Div0")
    else:
        print("viga")
    return r 

#2.Високосный год
def is_year_leap(aasta: int):
    """Liigaasta leidmine
    Tagastab true kui aasta on liigaasta False kui ei ole
    :param int aasta: Aasta number
    :rtype bool: Funktsioni vastus loogilises formaadis
    """
    if aasta%4==0:
        vastus=True
    else:
        vastus=False
    return vastus

#3.Квадрат
def ruud() 
result=square(int(input("lase ruudu pool: "))) 
print (result)

#4.Времена года
def season(kuu):
    """Kuu leidmine
    Tagastab aastaaeg
    """
    if kuu in (12, 1, 2): 
        return "talv" 
    elif kuu in (3, 4, 5): 
        return "kevad" 
    elif kuu in (6, 7, 8): 
        return "suvi" 
    elif kuu in (9, 10, 11): 
        return "sügis"
    
#5.Банковский вклад
def bank(a, years): 
    """tagastab summa
    mis on kontrol kasutaja
    """
    for year in range(years): 
        a *= 1.1 
    return a
#6.Простые числа
def is_prime(number): 

#7.Правильная дата
def date(p:int,k:int,a:int):
    """Kas see päev,kuu js aasta on olemas meie kalendris
    tagastab kui True kui on olemas ja False kui pole
    :param p: päev
    :param k: kuu
    :param a: aasta
    """

#8.XOR-шифрование
def xor_cipher(string: str, key:str)->str:
        """Tavaline sõna kodeeritakse
        """
        result=''
        temp=int()
        for i in range(len(string)):
            temp=ord(string[i]) #näitab sümboli kood
            for j in range(len(key)):
                temp ^= ord(key[j])
            result += chr(temp)
        return result

def xor_uncipher(string:str, key: str)-> str:
    """kodeeritud text dekodeeritakse
    """
    result=''
    temp=[]
    for i in range(len(string)):
        temp.apend(string[i])
        for j in reversed(range(len(key))):
            temp[i]=chr(ord(key[j]) ^ ord(temp[i]))
        result+=temp[i]
    return result


