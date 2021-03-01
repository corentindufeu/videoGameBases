from player import Player

#class du jeu

class Game():

    def __init__(self):
        #generer notre joueur
        self.player = Player()
        self.pressed = {
            "touche_fleche_gauche": True,
            "touche_fleche_droite": True
        }
