#demande de série
serie = ()
while len(serie) == 0 or serie.upper()!="générale" or "generale" or "général" or "general":
    serie = str(input("De quel série faites vous parties générale ou technologique. "))

#série générale
    if serie.upper() == "générale" or "generale" or "général" or "general":
        print("Vous avez choisis la voie générale")
        break
#série technologique   
    elif serie.upper() == "technologique" :
        print("Vous êtes dans la série technologique.")

        break
    else :
        print("Veuillez écrire soit : générale pour la voix général soit technologique pour la voix technologique.")
