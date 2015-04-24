__authors__ = 'Ajoutez les noms des membres de votre équipe!'
__date__ = "Ajoutez la date de remise"

"""Ce fichier permet de...(complétez la description de ce que
ce fichier est supposé faire ! """

from tkinter import Tk, Canvas, Label, Frame, GROOVE, Entry, Radiobutton, IntVar, Button
from tkinter.ttk import Combobox
from tictactoe.partie import Partie
from tictactoe.joueur import Joueur


class CanvasPlateau(Canvas):
    """
    Classe représentant le Widget d'un plateau de tic-tac-toe
    """
    def __init__(self, parent, plateau, taille_case=60):

        # Une instance d'un des 9 plateaux du jeu ultimate Tic-Tac-Toe.
        self.plateau = plateau

        # Nombre de pixels par case.
        self.taille_case = taille_case

        #Actif ou non
        self.est_Active = True
        self.est_gagne = False
        self.est_plein = False
        self.est_gagne_par = ""

        # Appel du constructeur de la classe de base (Canvas).
        super().__init__(parent, width=self.plateau.n_lignes * taille_case,
                         height=self.plateau.n_colonnes * self.taille_case)

        # Dessiner le plateau du jeu ultimate Tic-Tac-Toe.
        self.dessiner_plateau()



    def dessiner_plateau(self):
        """
        Méthode permettant de dessiner les différent rectangles composant le Widget de plateau.
        :return: Rien
        """
        for i in range(self.plateau.n_lignes):
            for j in range(self.plateau.n_colonnes):
                debut_ligne = i * self.taille_case
                fin_ligne = debut_ligne + self.taille_case
                debut_colonne = j * self.taille_case
                fin_colonne = debut_colonne + self.taille_case
                # On dessine le rectangle représentant une case!

                self.create_rectangle(debut_colonne, debut_ligne, fin_colonne, fin_ligne,
                                      fill='#e1e1e1', width = 2, outline = "red")
class ParametrePartie():
    def __init__(self):
        self.ChoixAdversaire = 0
        self.PremierJoueur = Joueur("Personne")
        self.DeuxiemeJoueur = Joueur()


class choisir_types(Tk):
    def __init__(self):
        self.title="type d'adversaire"
        super().__init__()


        self.type_label = Label(text="Contre qui désirez-vous jouer?")
        self.type_label.grid(row=2)
        self.v= IntVar()
        #on pose la question du type avec des radioboutons!
        self.type_1 = Radiobutton(text="Un Ordinateur", variable=self.v, value=1, command = self.retourval)
        self.type_1.grid(row =2,column=2)
        self.type_2 = Radiobutton(text="Un Autre Joueur", variable=self.v, value=2, command=self.retourval)
        self.type_2.grid(row =3,column=2)
        self.choix = 0
        #pour obtenir la réponse

        self.Bouton1=Button(text="Entrer", command=self.ClicBouton)
        self.Bouton1.grid(row=4, column=2)

    def retourval(self):
        self.choix = self.v.get()

    def ClicBouton(self):
        self.destroy()




class info_joueur(Tk):
    def __init__(self, type_choisi):
        super().__init__()

        if type_choisi == 1:
            #titre de la fenêtre
            self.title("Informations sur les joueurs?")
            #on pose la première question
            self.nom_1_q = Label (text="Quel est le nom du premier joueur?")
            self.nom_1_q.grid(padx=10, column = 0,row=0)
            #on obtient la première réponse!
            self.nom_1_r = Entry()
            self.nom_1_r.grid(column=1,row=0)
            self.NomJoueur1 = self.nom_1_r.get()

            #on demande pour le pion!
            self.pion_label = Label(text="Quel Pion Désirez-Vous?")
            self.pion_label.grid(row=2)
            self.v= IntVar()
            #on pose la question du pion avec des radioboutons!
            self.pion_1 = Radiobutton(text="X", variable=self.v, value=1, command = self.retourval)
            self.pion_1.grid(row =2,column=1)
            self.pion_2 = Radiobutton(text="O", variable=self.v, value=2, command = self.retourval)
            self.pion_2.grid(row =2,column=2)
            #x est le choix par défaut
            self.choix = "X"
            #pour obtenir la réponse

            self.Bouton2=Button(text="Entrer", command=self.ClicBouton)
            self.Bouton2.grid(row=3, column=1)

        else:
            #titre de la fenêtre
            self.title("Informations sur les joueurs?")
            #on pose la première question
            self.nom_1_q = Label (text="Quel est le nom du premier joueur?")
            self.nom_1_q.grid(padx=10, column = 0,row=0)
            self.nom_2_q = Label (text="Quel est le nom du deuxieme joueur?")
            self.nom_2_q.grid(padx=10, column = 0,row=1)
            #on obtient la première réponse!
            self.nom_1_r = Entry()
            self.nom_1_r.grid(column=1,row=0)
            self.nom_2_r = Entry()
            self.nom_2_r.grid(column=1,row=1)

            #on demande pour le pion!
            self.pion_label = Label(text="Quel Pion le Joueur 1 Désire-T'Il?")
            self.pion_label.grid(row=3)
            self.v= IntVar()
            #x est le choix par défaut
            self.choix = "X"
            #on pose la question du pion avec des radioboutons!
            self.pion_1 = Radiobutton(text="X", variable=self.v, value=1, command = self.retourval())
            self.pion_1.grid(row =3,column=1)
            self.pion_2 = Radiobutton(text="O", variable=self.v, value=2, command = self.retourval)
            self.pion_2.grid(row =3,column=2)
            #pour obtenir la réponse



            premier_nom = self.nom_1_r.get()
            self.Bouton2=Button(text="Entrer", command=self.ClicBouton)
            self.Bouton2.grid(row=4, column=1)

    def retourval(self):
        if self.v.get() == 1:
            self.choix = "X"
        else:
            self.choix = "O"


    def ClicBouton(self):
        self.NomJoueur1 = self.nom_1_r.get()
        self.NomJoueur2 = "Colosse"
        self.destroy()



class FenetreJeu(Tk):
    """

    """
    def __init__(self, parametres):

        """
            À completer !.
        """
        super().__init__()

        # Nom de la fenêtre.
        self.title("Ultimate Tic-Tac-Toe")


        # La partie de ultimate Tic-Tac-Toe
        self.partie = Partie()

        # Un ditionnaire contenant les 9 canvas des 9 plateaux du jeu
        self.canvas_uplateau = {}

        # Création des frames et des canvas du jeu
        for i in range(0, 3):
            for j in range(0, 3):
                cadre = Frame(self, borderwidth=5, relief=GROOVE, bg="blue")
                cadre.grid(row=i, column=j, padx=25, pady=25)
                self.canvas_uplateau[i,j] = CanvasPlateau(cadre, self.partie.uplateau[i,j])
                self.canvas_uplateau[i,j].grid()
                # On lie les événements sur le Canvas à une méthode.
                self.canvas_uplateau[i,j].bind('<Button-1>', self.selectionner)
                self.canvas_uplateau[i,j].bind('<Motion>', self.SurbrillanceProchainPlateau)
                self.canvas_uplateau[i,j].bind('<Leave>', self.LeaveCanvas)



        # Ajout d'une étiquette d'information.
        self.messages = Label(self)
        self.messages.grid(columnspan=3)

        # Création de deux joueurs. Ce code doit être bien sûr modifié,
        # car il faut chercher ces infos dans les widgets de la fenêtre.
        # Vous pouvez également déplacer ce code dans une autre méthode selon votre propre solution.


        p1 = parametres.PremierJoueur
        p2 = parametres.DeuxiemeJoueur
        self.partie.joueurs = [p1,p2]
        self.partie.joueur_courant = p1

        self.UpdateBordureCouleur()

    def ai_ordinateur(self,pion):
        for ligne in [0,2]:
            for colonne in [0,2]:
                self.partie.uplateau[ligne,colonne].selectionner_case(ligne,colonne,self.partie.joueur_courant.pion)
                if self.partie.est_gagne(self.partie.joueur_courant.pion):
                    self.selectionner()


    def selectionner(self, event):
        """
            À completer !.
        """
        # On trouve le numéro de ligne/colonne en divisant par le nombre de pixels par case.
        # event.widget représente ici un des 9 canvas !
        if (event.widget.est_Active and event.widget.est_gagne == False):
            ligne = event.y // event.widget.taille_case
            colonne = event.x // event.widget.taille_case

            if ligne <= 2 and colonne <= 2:
                self.afficher_message("Case sélectionnée à la position (({},{}),({},{}))."
                                      .format(event.widget.plateau.cordonnees_parent[0],
                                              event.widget.plateau.cordonnees_parent[1],
                                              ligne, colonne))

                if(event.widget.plateau.cases[ligne, colonne].est_vide()):
                    #Si la sélection est valide on exécute le code suivant:

                    #On dessine le pion dans le rectangle du canvas plateau
                    self.dessiner_pion(ligne, colonne, event)

                    #On mets à jour la case sélectionnée
                    self.partie.uplateau[event.widget.plateau.cordonnees_parent]\
                        .selectionner_case(ligne, colonne, self.partie.joueur_courant.pion)

                    #On regarde si le plateau et la partie sont gagnants
                    self.DeterminerGagnant(event)

                    #On met à joueur le status des plateaux
                    self.UpdatePlateauStatus(ligne, colonne)

                    #On Update la couleur des bordures des plateaux
                    self.UpdateBordureCouleur()

                    # On Changer le joueur courant.
                    self.ChangerJoueurCourant()

                else:
                    #Si la sélection est non valide
                    self.bell()
                    self.afficher_message("Cette case est déjà sélectionnée, veuillez en choisir une autre.", 'red')

        # Effacer le contenu du widget (canvas) et du plateau (dictionnaire) quand ce dernier devient plein.
        # Vous pouvez modifier ou déplacer ce code dans une autre méthode selon votre propre solution.
        #if not event.widget.plateau.non_plein():
        #    event.widget.delete('pion')
        #    event.widget.plateau.initialiser()



    def UpdateBordureCouleur(self):
        """
        Cette méthode met à jour la couleur de la bordure de chaque plateau en fonction de son état
        :return: Rien
        """
        for coordinate in self.canvas_uplateau:
            if self.canvas_uplateau[coordinate].est_gagne:
                    if self.canvas_uplateau[coordinate].est_gagne_par == "X":
                        self.canvas_uplateau[coordinate].master["bg"] = "blue"
                    else:
                        self.canvas_uplateau[coordinate].master["bg"] = "cyan"
            elif self.canvas_uplateau[coordinate].est_plein:
                self.canvas_uplateau[coordinate].master["bg"] = "red"
            elif self.canvas_uplateau[coordinate].est_Active:
                self.canvas_uplateau[coordinate].master["bg"] = "green"
            elif self.canvas_uplateau[coordinate].est_Active == False:
                self.canvas_uplateau[coordinate].master["bg"] = "black"
            else:
                self.canvas_uplateau[coordinate].master["bg"] = "magenta"

    def DeterminerGagnant(self, event):
        """
        Cette méthode détermine si le plateau et la partie sont gagnants
        :param event: event envoyé par le plateau sélectionné
        :return: Rien
        """
        if self.partie.uplateau[event.widget.plateau.cordonnees_parent].est_gagnant(self.partie.joueur_courant.pion):
            print("{} a gagné un plateau.".format(self.partie.joueur_courant.nom))
            event.widget.est_gagne = True
            self.partie.uplateau[event.widget.plateau.cordonnees_parent].est_gagne_par = self.partie.joueur_courant.pion
            event.widget.est_gagne_par = self.partie.joueur_courant.pion
            if self.partie.est_gagne(self.partie.joueur_courant.pion):
                print("{} a gagné la partie!!!".format(self.partie.joueur_courant.nom))
        elif self.partie.uplateau[event.widget.plateau.cordonnees_parent].non_plein() == False:
            event.widget.est_plein = True
            print("Not Yet mais un plateau est plein")

        else:
            print("Not Yet")

    def SurbrillanceProchainPlateau(self, event):
        """
        Cette méthode mets en surbrillance le plateau qui va être actif si le joueur choisi cette case.
        :param event:
        :return: Rien
        """
        #Debug Print qui affiche les coordonnés dans la console
        #print(event.x, event.y)

        if isinstance(event.widget, CanvasPlateau):
            if event.widget.est_Active:
                ligne = event.y // event.widget.taille_case
                colonne = event.x // event.widget.taille_case
                self.UpdateBordureCouleur()
                event.widget.delete(self,'PionPreview')
                if ligne <= 2 and colonne <= 2:
                    self.canvas_uplateau[ligne, colonne].master["bg"] = "yellow"
                    self.appercu_pion(event, ligne, colonne)


    def LeaveCanvas(self, event):
        """
        Cette méthode est appelée losque la souris quitte la superficie couverte par un plateau.  Elle sert simplement à forcer l'update de couleur et faire en sorte
        Le feedback du prochain plateau actif soit enlevé ainsi qu'à enlever les preview de pion.
        :param event: Widget d'un des plateau de tic-tac-toe
        :return: Rien
        """
        self.UpdateBordureCouleur()
        event.widget.delete(self,'PionPreview')

    def appercu_pion(self, event, ligne, colonne):
        """
        Méthode qui fait afficher l'appercu du pion du joueur sur la case sur laquelle la souris se trouve.
        :param event:   Event envoyé par le plateau sur lequel la souris se trouve.
        :param ligne:   INT Ligne du plateau sur lequel se trouve présentement la souris.
        :param colonne: INT Colonne du plateau sur lequel se trouve présentement la souris.
        :return: Rien
        """

        coordonnee_y = ligne * event.widget.taille_case + event.widget.taille_case // 2
        coordonnee_x = colonne * event.widget.taille_case + event.widget.taille_case // 2

        if(event.widget.plateau.cases[ligne, colonne].est_vide()==False):
            event.widget.create_text(coordonnee_x, coordonnee_y, text=self.partie.joueur_courant.pion,font=('Helvetica', event.widget.taille_case//2), tags='PionPreview', fill='red')
        else:
            event.widget.create_text(coordonnee_x, coordonnee_y, text=self.partie.joueur_courant.pion,font=('Helvetica', event.widget.taille_case//2), tags='PionPreview', fill='gray', width = "200 p")

    def dessiner_pion(self, ligne, colonne, event):
        """
        Méthode permettant de dessiner le pion dans la case

        :param ligne:   INT Ligne à laquelle il faut dessiner le pion
        :param colonne: INT Colonne à laquelle il faut dessiner le pion

        :return: Rien
        """

        # On dessine le pion dans le canvas, au centre de la case.
        # On utilise l'attribut "tags" pour être en mesure de récupérer
        # les éléments dans le canvas afin de les effacer par exemple.
        coordonnee_y = ligne * event.widget.taille_case + event.widget.taille_case // 2
        coordonnee_x = colonne * event.widget.taille_case + event.widget.taille_case // 2
        event.widget.create_text(coordonnee_x, coordonnee_y, text=self.partie.joueur_courant.pion,
                                 font=('Helvetica', event.widget.taille_case//2), tags='pion')

    def ChangerJoueurCourant(self):
        if self.partie.joueur_courant == self.partie.joueurs[0]:
            self.partie.joueur_courant = self.partie.joueurs[1]
        else:
            self.partie.joueur_courant = self.partie.joueurs[0]

    def UpdatePlateauStatus(self, ligne, colonne):
        """
        Cette méthode permet d'updater l'état des différent plateaux à savoir s'il doivent être considérés comme actifs.
        À savoir si le joueur peux y jouer.

        On regarde si:
                Le plateau est Gagné : s'il y a un joueur qui a gagné le plateau
                Le plateau est Plein : si toutes les cases sont remplies
        :param ligne:   INT Représente la ligne qui a été sélectionnée par le joueur
        :param colonne: INT Représtent la colonne qui a été sélectionnée par le joueur.
        :return: Rien
        """
        for plateau in self.canvas_uplateau:
            self.canvas_uplateau[plateau].est_Active = False
            if self.canvas_uplateau[ligne, colonne].est_gagne:
                for plateau in self.canvas_uplateau:
                    self.canvas_uplateau[plateau].est_Active = True
                for plateau in self.canvas_uplateau:
                    if self.canvas_uplateau[plateau].est_gagne:
                        self.canvas_uplateau[plateau].est_Active = False
                    elif self.canvas_uplateau[plateau].est_plein:
                        self.canvas_uplateau[plateau].est_Active = False
                    else:
                        self.canvas_uplateau[plateau].est_active = True

            elif self.canvas_uplateau[ligne, colonne].est_plein:
                for plateau in self.canvas_uplateau:
                    self.canvas_uplateau[plateau].est_Active = True
                    self.canvas_uplateau[ligne, colonne].est_Active = False

            else:
                self.canvas_uplateau[ligne, colonne].est_Active = True


    def afficher_message(self, message, color='black'):
        """
            À completer !.
        """
        self.messages['foreground'] = color
        self.messages['text'] = message


