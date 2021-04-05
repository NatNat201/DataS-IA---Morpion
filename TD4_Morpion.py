#TD 4 _ Morpion

import random

personne = -1
ordi = +1


def NouvellePartie():
    tab = []
    for i in range(3):
        tab.append([' ',' ',' '])
    return tab


def Afficher(jeu):
    affiche = '   0  1  2\n'
    affiche += '   _   _   _ \n\n'
    for i in range (len(jeu)):
        affiche+=str(i)
        affiche+='|'
        for j in range (len(jeu)):
            affiche+=str(jeu[i][j])+' | '
        affiche+='\n   _   _   _ \n\n'
    print(affiche)


def Actions_possibles(jeu):
    actions_possibles = []
    for i in range(3):
        for j in range (3):
            if (jeu[i][j] == ' '):
                actions_possibles.append([i,j])
    return actions_possibles


def Result(jeu,action,j):
    if j == ordi:
        jeu[action[0]][action[1]] = 'X'
        return jeu
    if j == personne:
        jeu[action[0]][action[1]] = 'O'
        return jeu


def Terminal_Test(jeu, joueur):
    #on reporte toutes les lignes, colonnes, diagonales gagnantes:
    set_gagnant = [[jeu[0][0],jeu[0][1],jeu[0][2]],[jeu[1][0],jeu[1][1],jeu[1][2]],[jeu[2][0],jeu[2][1],jeu[2][2]],[jeu[0][0],jeu[1][0],jeu[2][0]],[jeu[0][1],jeu[1][1],jeu[2][1]],[jeu[0][2],jeu[1][2],jeu[2][2]],[jeu[0][0],jeu[1][1],jeu[2][2]],[jeu[2][0],jeu[1][1],jeu[0][2]]]

    if [joueur,joueur,joueur] in set_gagnant : return True
    else : return False


def Gagnant(jeu):
    return Terminal_Test(jeu,'O') or Terminal_Test(jeu,'X')


def Action(jeu,i,j,joueur):
    if joueur==-1: jeu[i][j]='O'
    else : jeu [i][j]='X'


def Cases_vides(jeu):
    vide=[]
    for i in range(len(jeu)):
        for j in range (len(jeu)):
            if jeu[i][j]==' ':
                vide.append([i,j])
    return vide


def Heuristique(jeu):
    if Terminal_Test(jeu, 'X'):
        score = +1
    elif Terminal_Test(jeu,'O'):
        score = -1
    else :
        #en cas d'égalité
        score = 0
    return score


def minimax(jeu, profondeur, joueur):
    if joueur == ordi:
        best = [-1, -1, -1000]
    else:
        best = [-1, -1, +1000]

    if profondeur == 0 or Gagnant(jeu):
        score = Heuristique(jeu)
        return [-1, -1, score]


    for case in Cases_vides(jeu):
        i, j = case[0], case[1]
        if joueur==ordi:
            jeu[i][j]='X'
        else : jeu[i][j]='O'

        score = minimax(jeu, profondeur - 1, -joueur)
        jeu[i][j] = ' '
        score[0], score[1] = i, j

        if joueur == ordi:
            if score[2] > best[2]:
                best = score  # valeur max
        else:
            if score[2] < best[2]:
                best = score  # valeur min

    return best


def IA_joue(jeu):
    profondeur = len(Cases_vides(jeu))

    if profondeur == 9 :
        i = random.choice([0,1,2])
        j = random.choice([0,1,2])
    elif profondeur == 0 or Gagnant(jeu):
        return
    else :
        action=minimax(jeu,profondeur,ordi)
        i = action[0]
        j = action[1]

    Action(jeu,i,j,ordi)
    return jeu


def Personne_joue(jeu):
    profondeur = len(Cases_vides(jeu))

    if profondeur==0 or Gagnant(jeu):
        return

    print('Voici les actions possibles :\n')
    print(Actions_possibles(jeu))

    action=[-1,-1]
    while action not in Actions_possibles(jeu):
        print('Veuillez entrer la ligne sur laquelle vous souhaitez jouer :')
        i = eval(input('Ligne choisie :'))
        print('Veuillez entrer la colonne sur laquelle vous souhaitez jouer :')
        j = eval(input('Colonne choisie :'))
        action=[i,j]

    Action(jeu,action[0],action[1],personne)
    return jeu


def Jeu():
    print('\n\nVous avez commencé une nouvelle partie.')
    jeu = NouvellePartie()
    Afficher(jeu)

    print('Voulez-vous commencer à jouer ? (oui/non)')
    choice=(input('Votre choix : ')).upper()

    while len(Cases_vides(jeu))>0 and not Gagnant(jeu):
        if choice=='NON':
            IA_joue(jeu)
            Afficher(jeu)

        Personne_joue(jeu)
        Afficher(jeu)
        if Gagnant(jeu):
            if Terminal_Test(jeu,'X'):
                print('\nL ordinateur a gagné, dommage pour vous.')
            elif Terminal_Test(jeu,'O'):
                print('\nFélicitations, vous avez battu l ordinateur !')
            break

        if not Gagnant(jeu):
            #on vérifie si le jour a gagné avant que l'ordinateur ne joue, si non : alors on continue le jeu et c'est au tour de l'ordinateur
            IA_joue(jeu)
            Afficher(jeu)

        choice = ''

        if Gagnant(jeu):
            if Terminal_Test(jeu,'X'):
                print('\nL ordinateur a gagné, dommage pour vous.\nN hésitez pas à retenter votre chance.')
            elif Terminal_Test(jeu,'O'):
                print('\nFélicitations, vous avez battu l ordinateur !')



    #Si on sort de la boucle c'est que toutes les cases sont remplies
    #On regarde le résultat

    if not Gagnant(jeu) : print('Match nul ! Il ny a pas de gagnant.\nN hésitez pas à retenter votre chance.')


Jeu()

