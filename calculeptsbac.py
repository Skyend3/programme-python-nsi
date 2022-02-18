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

        #demande d'option (qron c'est question reponse de oui ou non)
        qron = "nul"
        qron2 = "nul"
        while qron.upper() != "OUI" or qron.upper() != "NON":
            qron = input("Avez vous choisis une option ? (oui ou non)")
            
            if qron.upper() == "OUI":
                option = input("Quel est l'option ? ")
                print("Vous avez choisis l'option : ",option)
                option = input("Quel est votre moyenne dans cette option : ")
                qron2 = input("Avez vous choisis une autre option ? (oui ou non)")
                
                if qron2.upper() == "OUI":
                    option2 = input("Quel est l'option ? ")
                    print("Vous avez choisis l'option : ",option2)
                    option2 = input("Quel est votre moyenne dans cette option : ")
                    break
                
                elif qron2.upper() == "NON":
                    print("Très bien ")
                    break
                
                else:
                    print("Veuillez réessayer")
                break    
            elif qron.upper() == "NON":
                print("Très bien ")
                break
            
            else:
                print("Veuillez réessayer")
        
    
        #demande des notes de première
        notecontrolecontinu = ["Histoire Géographie en premiere ","Histoire Géographie en terminal ","Espagnol en premiere ","Espagnol en terminal","Anglais en premiere","Anglais en terminal","Enseignement scientifique en premiere ","Enseignement scientifique en terminal ","Education physique et sportive en terminal ","Enseignement moral et civique en terminal","Moyenne générale Bulletin 1re", " spécialité abandonné en premiere "]
        noteepreuvefinal = ["Français écrit","Français oral","Philosophie","Grand Oral"," spécialité une gardé en terminale ", " spécialité deux gardé en terminale "]
            
        def remplacenotecotrolcontinue ():
            notes = 99
            libelle = "Donner votre moyenne de controle continue en "+ notecontrolecontinu[matiere]+  " : "
            
            while  notes < 0.0 or notes > 20.0 :
                notes = float(input(libelle))
                if notes < 0.0 or notes > 20.0 :
                    print("La note doit être comprise entre 0 et 20. Veuillez resaisir.")
            return notes
        
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
            return notes
        
        matiere = 0
        while matiere < len (noteepreuvefinal):
            noteepreuvefinal[matiere] = remplacenotefinales()
            matiere = matiere + 1
        
        notestoutesepreuves = ["Histoire Géographie en premiere ","Histoire Géographie en terminal ","Espagnol en premiere ","Espagnol en terminal","Anglais en premiere","Anglais en terminal","Enseignement scientifique en premiere ","Enseignement scientifique en terminal ","Education physique et sportive en terminal ","Enseignement moral et civique en terminal","Moyenne générale Bulletin 1re", " spécialité abandonné en premiere ","Français écrit","Français oral","Philosophie","Grand Oral"," spécialité une gardé en terminale ", " spécialité deux gardé en terminale "]
        
        #Note épreuves continue
        notestoutesepreuves[0] = notecontrolecontinu[0] * 3.33
        notestoutesepreuves[1] = notecontrolecontinu[1] * 3
        notestoutesepreuves[2] = notecontrolecontinu[2] * 3.33
        notestoutesepreuves[3] = notecontrolecontinu[3]  * 3
        notestoutesepreuves[4] = notecontrolecontinu[4] * 3.33
        notestoutesepreuves[5] = notecontrolecontinu[5] * 3
        notestoutesepreuves[6] = notecontrolecontinu[6] * 2.5
        notestoutesepreuves[7] = notecontrolecontinu[7] * 2.5
        notestoutesepreuves[8] = notecontrolecontinu[8] * 5
        notestoutesepreuves[9] = notecontrolecontinu[9] * 1
        notestoutesepreuves[10] = notecontrolecontinu[10] * 5
        notestoutesepreuves[11] = notecontrolecontinu[11] * 5
        
        
        #Note épreuves final
        notestoutesepreuves[12] = noteepreuvefinal[0] * 5
        notestoutesepreuves[13] = noteepreuvefinal[1] * 5
        notestoutesepreuves[14] = noteepreuvefinal[2] * 8
        notestoutesepreuves[15] = noteepreuvefinal[3] * 10
        notestoutesepreuves[16] = noteepreuvefinal[4] * 16
        notestoutesepreuves[17] = noteepreuvefinal[5] * 16

        
        
        #calcule de la moyenne
        conteur = 1
        while conteur < len (notestoutesepreuves):
            moyenne = notestoutesepreuves[0] + notestoutesepreuves[conteur]
            notestoutesepreuves[0] = moyenne
            conteur = conteur + 1
        
        if qron.upper() == "OUI" :
            addoption1 = option * 2
            moyenne = moyenne + addoption1
            if qron2.upper() == "OUI" :
                addoption2 = option2 * 2
                moyenne = moyenne + addoption2
        
        print("Vous avez un total de : ", moyenne," points au bac.")
        moyenne = moyenne / 100.0
        print("Ce qui vous fait ", moyenne," sur 20.")
        
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

        #demande d'option (qron c'est question reponse de oui ou non)
        qron = "nul"
        qron2 = "nul"
        while qron.upper() != "OUI" or qron.upper() != "NON":
            qron = input("Avez vous choisis une option ? (oui ou non)")
            
            if qron.upper() == "OUI":
                option = input("Quel est l'option ? ")
                print("Vous avez choisis l'option : ",option)
                option = input("Quel est votre moyenne dans cette option : ")
                break    
            elif qron.upper() == "NON":
                print("Très bien ")
                break
            
            else:
                print("Veuillez réessayer")
        
    
        #demande des notes de première
        notecontrolecontinu = ["Histoire Géographie ","Espagnol ","Anglais ","Education physique et sportive ","Enseignement moral et civique ", specialiteabandonne,"mathématiques "]
        noteepreuvefinal = ["Français écrit","Français oral","Philosophie","Grand Oral",specialiteune, specialitedeux]
            
        def remplacenotecotrolcontinue ():
            notes = 99
            libelle = "Donner votre moyenne de controle continue en "+ notecontrolecontinu[matiere]+  " : "
            
            while  notes < 0.0 or notes > 20.0 :
                notes = float(input(libelle))
                if notes < 0.0 or notes > 20.0 :
                    print("La note doit être comprise entre 0 et 20. Veuillez resaisir.")
            return notes
        
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
            return notes
        
        matiere = 0
        while matiere < len (noteepreuvefinal):
            noteepreuvefinal[matiere] = remplacenotefinales()
            matiere = matiere + 1
        
        notestoutesepreuves = ["Histoire Géographie ","Espagnol ","Anglais ","Education physique et sportive ","Enseignement moral et civique ", specialiteabandonne,"mathématiques ","Français écrit","Français oral","Philosophie","Grand Oral",specialiteune, specialitedeux]
        
        #Note épreuves continue
        notestoutesepreuves[0] = notecontrolecontinu[0] * 6
        notestoutesepreuves[1] = notecontrolecontinu[1] * 6
        notestoutesepreuves[2] = notecontrolecontinu[2] * 6
        notestoutesepreuves[3] = notecontrolecontinu[3]  * 6
        notestoutesepreuves[4] = notecontrolecontinu[4] * 2
        notestoutesepreuves[5] = notecontrolecontinu[5] * 8
        notestoutesepreuves[6] = notecontrolecontinu[6] * 6        
        
        #Note épreuves final
        notestoutesepreuves[7] = noteepreuvefinal[0] * 5
        notestoutesepreuves[8] = noteepreuvefinal[1] * 5
        notestoutesepreuves[9] = noteepreuvefinal[2] * 4
        notestoutesepreuves[10] = noteepreuvefinal[3] * 14
        notestoutesepreuves[11] = noteepreuvefinal[4] * 16
        notestoutesepreuves[12] = noteepreuvefinal[5] * 16
        
        
        #calcule de la moyenne
        conteur = 1
        while conteur < len (notestoutesepreuves):
            moyenne = notestoutesepreuves[0] + notestoutesepreuves[conteur]
            notestoutesepreuves[0] = moyenne
            conteur = conteur + 1
        
        if qron.upper() == "OUI":
            option1 = option * 4
            moyenne = moyenne + option1
        
        print("Vous avez un total de : ", moyenne," points au bac.")
        moyenne = moyenne / 100.0
        print("Ce qui vous fait ", moyenne," sur 20.")
        
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
