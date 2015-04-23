__author__ = 'IFT-1004-H2015'
__date__ = "05 avril 2015"

"""Ce fichier représente le point d'entrée principal du TP3.
Il ne sert qu'à exécuter votre programme du jeu Ultimate Tic-Tac-Toe"""

from interface.jeu_utictactoe import FenetreJeu
from interface.jeu_utictactoe import info_joueur
from interface.jeu_utictactoe import choisir_types

if __name__ == '__main__':

    fen_joueur = info_joueur()
    fen_joueur.mainloop()

    ma_fenetre = FenetreJeu()
    ma_fenetre.mainloop()