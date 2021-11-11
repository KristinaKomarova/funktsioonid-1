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

def square(a:float):
    """P - ümbermõõd
    S - pindala
    d - diagonaal
    a - ruudu külg
    :param float a: ruudu külja pikkus
    :param float P: ruudu ümbermõõd
    :param float S: ruudu pindala
    :param float d: ruudu diagonaal
    :rtype float:
    """

    a=int(input("ruudu küle pikkus")
          if P==4*a: