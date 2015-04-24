__author__ = 'IFT-1004-H2015'
__date__ = "05 avril 2015"

"""Ce fichier représente le point d'entrée principal du TP3.
Il ne sert qu'à exécuter votre programme du jeu Ultimate Tic-Tac-Toe"""

from interface.jeu_utictactoe import FenetreJeu
from interface.jeu_utictactoe import ParametrePartie
from interface.jeu_utictactoe import info_joueur
from interface.jeu_utictactoe import choisir_types

if __name__ == '__main__':

    parametres = ParametrePartie()

    fen_adversaire = choisir_types()
    fen_adversaire.wait_window()
    parametres.ChoixAdversaire = fen_adversaire.choix

    fen_joueur = info_joueur(parametres.ChoixAdversaire)
    fen_joueur.wait_window()
    if parametres.ChoixAdversaire == 1:
        parametres.PremierJoueur.nom = fen_joueur.NomJoueur1
        parametres.PremierJoueur.pion = fen_joueur.choix
        parametres.DeuxiemeJoueur.nom = "Colosse"
    else:
        parametres.PremierJoueur.nom = fen_joueur.NomJoueur1
        parametres.PremierJoueur.pion = fen_joueur.choix
        parametres.DeuxiemeJoueur.nom = fen_joueur.NomJoueur2
        parametres.DeuxiemeJoueur.type = "Personne"
        if fen_joueur.choix == "O":
            parametres.DeuxiemeJoueur.pion = "X"





    ma_fenetre = FenetreJeu(parametres)
    ma_fenetre.mainloop()