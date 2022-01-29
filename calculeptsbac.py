# demande de série

serie = ()
fin = False

while not fin:
    serie = str(input("De quel série faites vous parties générale ou technologique. ")).replace("é", "e")
    
    # série générale
    if serie.upper() == "GENERAL" or serie.upper() == "GENERALE":
        print("Vous êtes dans la série générale.")
        fin = True

    # série technologique
    elif serie.upper() == "TECHNOLOGIE" or serie.upper() == "TECHNOLOGIQUE" or serie.upper() == "TECHNO":
        print("Vous êtes dans la série technologique.")
        fin = True

    # si on se trompe
    else :
        print("Veuillez écrire soit : générale ou technologique.")
