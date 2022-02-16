def option():
    option = ()
    while len(option) == 0 or option.upper() != "OUI" or option != "NON":
        option = input("Avez vous choisis une option ? (oui ou non)")
        
        if option.upper() == "OUI":
            option = input("Quel est l'option ? ")
            print("Vous avez choisis l'option : ",option)
            option = input("Avez vous choisis une autre option ? (oui ou non)")
            if option.upper() == "OUI":
                option = input("Quel est l'option ? ")
                print("Vous avez choisis l'option : ",option)
                option = input("Avez vous choisis une autre option ? (oui ou non)")
                break
            
            elif option.upper() == "NON":
                print("Très bien ")
                break
            
            else:
                print("Veuillez réessayer")
            break
        elif option.upper() == "NON":
            print("Très bien ")
            break
        
        else:
            print("Veuillez réessayer")

#demande de série
serie = ()
fin = False
while not fin:
    serie = input("De quel série faites vous parties générale ou technologique. ").replace("é", "e")

#série générale
    if serie.upper() == "GENERAL" or serie.upper() == "GENERALE":
 
    #demande des spécialités abandonné et gardé
    
        specialiteabandonne = input("Quelle spécialité avez vous choisis d'abandonner : ")
        print("Vous avez abandonné(e) la spécialité : ",specialiteabandonne," en fin de première.")
    
        specialiteune = input("Choisissez la spécialité gardé en fin de première : ")
        print("Vous avez choisis de garder ",specialiteune," en fin de première.")
        
        specialitedeux = input("Choisissez l'autre spécialité gardé en fin de première : ")
        print("Vous avez choisis de garder ",specialitedeux," en fin de première.")

        #demande d'option
        option()
        
    
        #demande des notes de première
        notecontrolecontinu = ["Histoire Géographie","Langue vivante A : Espagnol","Langue vivante B : Anglais","Enseignement scietifique","Education physique et sportive","Enseignement moral et civique","Moyenne générale Bulletin 1re",specialiteabandonne]
        noteepreuvefinal = ["Français écrit","Français oral","Philosophie","Grand Oral","Spécialité ",specialiteune,"Spécialité ",specialitedeux]
    
        def remplacenotecotrolcontinue ():
            notes = "Donner votre moyenne de controle continue en "+ notecontrolecontinu[matiere]+  " : "
            return float(input(notes))
        
        matiere = 0
        while matiere < len (notecontrolecontinu) :
            notecontrolecontinu[matiere] = remplacenotecotrolcontinue()
            matiere = matiere + 1
        print(notecontrolecontinu)
        
        
        def remplacenotefinales():
            notes = "Donner votre moyenne de controle continue en "+ noteepreuvefinal[matiere]+  " : "
            return float(input(notes))
        
        matiere = 0
        while matiere < len (noteepreuvefinal):
            noteepreuvefinal[matiere] = remplacenotefinales()
            matiere = matiere + 1
        print(noteepreuvefinal)
                
        fin = True
        
#série technologique   
    elif serie.upper() == "TECHNOLOGIE" or serie.upper() == "TECHNOLOGIQUE" or serie.upper() == "TECHNO":
        print("Vous êtes dans la série technologique.")

        fin = True
    else :
        print("Veuillez écrire soit : générale pour la voix général soit technologique pour la voix technologique.")
