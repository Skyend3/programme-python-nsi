option = ()
option2 =()
def option():
    option = ()
    option2 =()
    while len(option) == 0 or option.upper() != "OUI" or option != "NON":
        option = input("Avez vous choisis une option ? (oui ou non)")
        
        if option.upper() == "OUI":
            option = input("Quel est l'option ? ")
            print("Vous avez choisis l'option : ",option)
            option = input("Quel est votre moyenne dans cette option : ")
            option2 = input("Avez vous choisis une autre option ? (oui ou non)")
            
            if option2.upper() == "OUI":
                option2 = input("Quel est l'option ? ")
                print("Vous avez choisis l'option : ",option2)
                option = input("Quel est votre moyenne dans cette option : ")
                break
            
            elif option2.upper() == "NON":
                print("Très bien ")
                break
            
            else:
                print("Veuillez réessayer")
                break
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
            notes = 99
            libelle = "Donner votre moyenne de controle continue en "+ notecontrolecontinu[matiere]+  " : "
            
            while  notes < 0.0 or notes > 20.0 :
                notes = float(input(libelle))
                if notes < 0.0 or notes > 20.0 :
                    print("La note doit être comprise entre 0 et 20. Veuillez resaisir.")
        
        matiere = 0
        while matiere < len (notecontrolecontinu) :
            notecontrolecontinu[matiere] = remplacenotecotrolcontinue()
            matiere = matiere + 1
        
        
        def remplacenotefinales():
            notes = 99
            libelle = "Donner votre moyenne de controle continue en "+ noteepreuvefinal[matiere]+  " : "
            
            while  notes < 0.0 or notes > 20.0 :
                notes = float(input(libelle))
                if notes < 0.0 or notes > 20.0 :
                    print("La note doit être comprise entre 0 et 20. Veuillez resaisir.")
        
        matiere = 0
        while matiere < len (noteepreuvefinal):
            noteepreuvefinal[matiere] = remplacenotefinales()
            matiere = matiere + 1
        
        #Note épreuves continue
        HG = notecontrolecontinu[0] * 3,33 + notecontrolecontinu[0] * 3
        LVA = notecontrolecontinu[1] * 3,33 + notecontrolecontinu[1] * 3
        LVB = notecontrolecontinu[2] * 3,33 + notecontrolecontinu[2] * 3
        Ens_scie = notecontrolecontinu[3]  *2.5 + notecontrolecontinu[3] * 2.5
        EPS = notecontrolecontinu[4] * 5
        EMC = notecontrolecontinu[5] * 1
        Moyenne_gen = notecontrolecontinu[6] * 5
        Spe_abandoné = notecontrolecontinu[7] * 5
        
        #Note épreuves final
        FR_ecrit = noteepreuvefinal[0] * 5
        FR_oral = noteepreuvefinal[1] * 5
        Philo = noteepreuvefinal[2] * 8
        Grand_oral = noteepreuvefinal[3] * 10
        spe1 = noteepreuvefinal[5] * 16
        spe2 = noteepreuvefinal[7] * 16
        if option.upper() == "oui":
            option1 = option * 2
            if option2.upper() == "oui":
                option2 = option2 * 2
        moyenne = HG+LVA+LVB + Ens_scie + EPS + EMC + Moyenne_gen + Spe_abandoné + FR_ecrit + FR_oral + Philo + Grand_oral + spe1 + spe2 / 100
        option = option1 + option2 / 4
        moyenne = moyenne + option
        
        print("Votre moyenne au bac est de : ", moyenne)
        if moyenne <10:
            print ("Désolé, vous êtes refusé.")
        elif moyenne >=12 and moyenne <14:
            print ("Vous avez obtenus la mention assez bien.")
        elif moyenne >=14 and moyenne <16:
            print ("Vous avez obtenus la mention bien.")
        elif moyenne >= 16:
            print ("Vous avez obtenus la mention très bien.")
                
        fin = True
        
#série technologique   
    elif serie.upper() == "TECHNOLOGIE" or serie.upper() == "TECHNOLOGIQUE" or serie.upper() == "TECHNO":
        
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
        notecontrolecontinu = ["Histoire Géographie","Langue vivante A : Anglais","Langue vivante B : Espagnol","Mathématique","Education physique et sportive","Enseignement moral et civique",specialiteabandonne]
        noteepreuvefinal = ["Français écrit","Français oral","Philosophie","Grand Oral","Spécialité ",specialiteune,"Spécialité ",specialitedeux]
    
        def remplacenotecotrolcontinue ():
            notes = 99
            libelle = "Donner votre moyenne de controle continue en "+ notecontrolecontinu[matiere]+  " : "
            
            while  notes < 0.0 or notes > 20.0 :
                notes = float(input(libelle))
                if notes < 0.0 or notes > 20.0 :
                    print("La note doit être comprise entre 0 et 20. Veuillez resaisir.")
        
        matiere = 0
        while matiere < len (notecontrolecontinu) :
            notecontrolecontinu[matiere] = remplacenotecotrolcontinue()
            matiere = matiere + 1
        
        
        def remplacenotefinales():
            notes = 99
            libelle = "Donner votre moyenne de controle continue en "+ noteepreuvefinal[matiere]+  " : "
            
            while  notes < 0.0 or notes > 20.0 :
                notes = float(input(libelle))
                if notes < 0.0 or notes > 20.0 :
                    print("La note doit être comprise entre 0 et 20. Veuillez resaisir.")
        
        matiere = 0
        while matiere < len (noteepreuvefinal):
            noteepreuvefinal[matiere] = remplacenotefinales()
            matiere = matiere + 1
            
           
        #Note épreuves continue
        HG = notecontrolecontinu[0] * 6.0
        LVA = notecontrolecontinu[1] * 6
        LVB = notecontrolecontinu[2] * 6
        Maths = notecontrolecontinu[3]  * 6
        EPS = notecontrolecontinu[4] * 6
        EMC = notecontrolecontinu[5] * 2
        Spe_abandoné = notecontrolecontinu[7] * 8
        if option.upper() == "oui":
            option1 = option * 2
            if option2.upper() == "oui":
                option2 = option2 * 2
        
        #Note épreuves final
        FR_ecrit = noteepreuvefinal[0] * 5
        FR_oral = noteepreuvefinal[1] * 5
        Philo = noteepreuvefinal[2] * 4
        Grand_oral = noteepreuvefinal[3] * 14
        spe1 = noteepreuvefinal[5] * 16
        spe2 = noteepreuvefinal[7] * 16
        
        #Calcule de la moyenne
        moyenne = HG+LVA+LVB + Maths() + EPS + EMC + Spe_abandoné + FR_ecrit + FR_oral + Philo + Grand_oral + spe1 + spe2 / 100
        option = option1 + option2 / 4
        moyenne = moyenne + option
        
        print("Votre moyenne au bac est de : ", moyenne)
        if moyenne <10:
            print ("Désolé, vous êtes refusé.")
        elif moyenne >=12 and moyenne <14:
            print ("Vous avez obtenus la mention assez bien.")
        elif moyenne >=14 and moyenne <16:
            print ("Vous avez obtenus la mention bien.")
        elif moyenne >= 16:
            print ("Vous avez obtenus la mention très bien.")
        
        fin = True
        
    else :
        print("Veuillez écrire soit : générale pour la voix général soit technologique pour la voix technologique.")
