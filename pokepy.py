# -*- coding: utf-8 -*-
"""
Module utilisé pour le projet NSI POO
"""

import csv
import random
import pygame

ELEMENTS = ["plante", "feu", "eau", "foudre", "psy", "combat", "tenebre", "acier",
            "dragon", "normal", "sol", "poison"]

TABLE_TYPE_PUISSANT = {
        "plante": ["eau", "sol"],
        "feu": ["acier", "plante"],
        "eau": ["feu", "sol"],
        "foudre": ["eau"],
        "psy": ["combat", "poison"],
        "combat": ["acier", "normal", "sol", "tenebre"],
        "tenebre": ["psy"],
        "acier": ["sol"],
        "dragon": ["dragon"],
        "normal": [],
        "sol": ["acier", "foudre", "feu", "poison", "sol"],
        "poison": ["plante"]
        }

TABLE_TYPE_FAIBLE = {
        "plante": ["acier", "dragon", "feu", "plante", "poison"],
        "feu": ["dragon", "eau", "feu", "sol"],
        "eau": ["dragon", "eau", "plante"],
        "foudre": ["dragon", "foudre", "plante"],
        "psy": ["acier", "psy"],
        "combat": ["poison", "psy"],
        "tenebre": ["combat", "tenebre"],
        "acier": ["acier", "eau", "foudre", "feu"],
        "dragon": ["acier"],
        "normal": ["acier", "sol"],
        "sol": ["plante"],
        "poison": ["poison", "sol", "tenebre"]
        }

TABLE_TYPE_NUL = {
        "plante": [],
        "feu": [],
        "eau": [],
        "foudre": ["sol"],
        "psy": ["tenebre"],
        "combat": ["tenebre"],
        "tenebre": [],
        "acier": [],
        "dragon": [],
        "normal": ["tenebre"],
        "sol": [],
        "poison": ["acier"]
        }

class Pokemon(pygame.sprite.Sprite):

    def __init__(self, nom, id, element, pdv, attaque, degat, tauxc=5, poisoned=False, tpoison=0):
        assert element.lower() in ELEMENTS
        assert type(nom) == str
        assert type(element) == str
        assert type(pdv) == int
        assert type(degat) == int
        assert type(tauxc) == int
        assert type(poisoned) == bool
        assert type(tpoison) == int
        super().__init__()
        self.nom = nom
        self.id = id
        self.element = element.lower()
        self.pdv = pdv
        self.attaque = attaque
        self.degat = degat
        self.tauxc = tauxc
        self.poisoned = poisoned
        self.tpoison = tpoison
        self.image = pygame.image.load('assets/pokemons/img/' + str(id) + '.png')
        self.pos = []

    def __str__(self):
        return str("Nom: " + self.nom + "\nElement: " + self.element + "\nPdv: " + str(self.pdv)
                   + "\nAttaque: " + str(self.attaque) + "\nDegat: " + str(self.degat)
                   + "\nTauxc: " + str(self.tauxc) + "\nPoisoned: " + str(self.poisoned) + "\n")

    def get_nom(self):
        """
        Récupère le nom du pokemon
        """
        return self.nom

    def get_id(self):
        """
        Récupère l'id du pokemon
        """
        return self.id

    def get_element(self):
        """
        Récupère l'élément du pokemon
        """
        return self.element

    def get_pdv(self):
        """
        Récupère les poins de vie du pokemon
        """
        return self.pdv

    def get_attaque(self):
        """
        Récupère le nom de l'attaque du pokemon
        """
        return self.attaque

    def get_degat(self):
        """
        Récupère les dégats du pokemon
        """
        return self.degat

    def get_tauxc(self):
        """
        Récupère le taux de coup critique du pokemon
        """
        return self.tauxc

    def is_poisoned(self):
        """
        Vérifie si le pokemon est empoisonné
        """
        return self.poisoned

    def get_tpoison(self):
        """
        Récupère le nombre de tours empoisonnés du pokemon
        """
        return self.tpoison

    def get_image(self):
        """
        Récupère l'image du pokemon
        """
        return self.image

    def get_pos(self):
        """
        Récupère la position du pokemon sur l'écran
        """
        return self.pos

    def set_nom(self, newname):
        """
        Permet de changer le nom du pokemon
        """
        assert type(newname) == str
        self.nom = newname

    def set_element(self, newelement):
        """
        Permet de changer l'élément du pokemon
        """
        assert newelement.lower() in ELEMENTS
        assert type(newelement) == str
        self.element = newelement.lower()

    def set_pdv(self, newpdv):
        """
        Permet de changer les points de vie du pokemon
        """
        assert type(newpdv) == int
        self.pdv = newpdv

    def set_degat(self, newdegat):
        """
        Permet de changer les dégats du pokemon
        """
        assert type(newdegat) == int
        self.degat = newdegat

    def set_tauxc(self, newtaux):
        """
        Permet de changer le taux de coup critique du pokemon
        """
        assert type(newtaux) == int
        self.tauxc = newtaux

    def set_poisoned(self, etat):
        """
        Permet de changer l'état du pokemon pour l'empoisonné ou non
        """
        assert type(etat) == bool
        self.poisoned = etat

    def set_tpoison(self, nombre):
        """
        Permet de changer le nombre de tours restant empoisonnés du pokemon
        """
        assert type(nombre) == int
        self.tpoison = nombre

    def set_pos(self, posi):
        """
        Permet de changer la position du pokemon
        """
        assert type(posi) == list
        self.pos = posi

    def tour_passe(self):
        """
        Enlève un tour de poison au pokemon
        """
        self.tpoison = self.tpoison - 1


def start(joueur1, eqp1, joueur2, eqp2, liste_poke):
    """
    Permet de commencer la partie
    """
    for i in range(5):
        rng = random.randint(0, len(liste_poke) - 1)
        eqp1.append(liste_poke.pop(rng))

    for i in range(5):
        rng = random.randint(0, len(liste_poke) - 1)
        eqp2.append(liste_poke.pop(rng))


def attaque(envoyeur, cible):
    """
    Permet de faire envoyer une attaque d'un de ses pokemons sur un pokemon adverse
    """
    if cible.get_element() in TABLE_TYPE_PUISSANT[envoyeur.get_element()]:

        # ATTAQUE TRES EFFICACE

        if random.randint(1, 100) <= envoyeur.get_tauxc():
            degats_infliges = int(round(envoyeur.get_degat() * 2 * 1.5))

        else:
            degats_infliges = int(round(envoyeur.get_degat() * 1.5))

    elif cible.get_element() in TABLE_TYPE_FAIBLE[envoyeur.get_element()]:

        # ATTAQUE TRES FAIBLE
        if random.randint(1, 100) <= envoyeur.get_tauxc():
            degats_infliges = round(envoyeur.get_degat() / 2 * 2)

        else:
            degats_infliges = round(envoyeur.get_degat() / 2)

    elif cible.get_element() in TABLE_TYPE_NUL[envoyeur.get_element()]:

        # ATTAQUE NUL
        degats_infliges = round(envoyeur.get_degat() * 0)

    else:

        # ATTAQUE NORMAL
        if random.randint(1, 100) <= envoyeur.get_tauxc():
            degats_infliges = round(envoyeur.get_degat() * 2)
        else:
            degats_infliges = round(envoyeur.get_degat())

    return degats_infliges


def afficher_texte(screen, texte, font, xcoord, ycoord, color):
    """
    Permet d'afficher un texte à l'écran
    """
    texte_affiche = font.render(texte, True, color)
    texte_rect = texte_affiche.get_rect()
    texte_rect.center = (xcoord, ycoord)
    screen.blit(texte_affiche, texte_rect)


def check_fini(eqp_1, eqp_2):
    """
    Vérifie si la partie est finie
    """
    len_eq1 = 5
    len_eq2 = 5
    for i in eqp_1:
        if i.get_pdv() <= 0:
            len_eq1 = len_eq1 - 1
    for i in eqp_2:
        if i.get_pdv() <= 0:
            len_eq2 = len_eq2 - 1
    if ((len_eq1 == 0) or (len_eq2 == 0)):
        return True
    return False


def equipe_gagnante(eqp_1, eqp_2):
    """
    Vérifie l'équipe qui a gagné le match
    """
    len_eq1 = 5
    len_eq2 = 5
    for i in eqp_1:
        if i.get_pdv() <= 0:
            len_eq1 = len_eq1 - 1
    for i in eqp_2:
        if i.get_pdv() <= 0:
            len_eq2 = len_eq2 - 1
    if len_eq1 <= 0:
        return "Joueur 2"
    return "Joueur 1"


def len_equipe(eqp):
    """
    Calcul le nombre de pokemons en vie dans une équipe
    """
    l_eqp = 5
    for i in eqp:
        if i.get_pdv() <= 0:
            l_eqp = l_eqp - 1
    return l_eqp

def import_pokemons(fcsv):
    """
    Importe des pokemons à partir d'un fichier csv
    """
    liste_poke = []
    fichier_csv = open(fcsv)
    lecteur = csv.reader(fichier_csv, delimiter=";")
    nb_l = 0
    for ligne in lecteur:
        if nb_l == 0:
            nb_l = 1
        else:
            donnees = ligne[0].split(",")
            liste_poke.append(Pokemon(donnees[0], int(donnees[1]), donnees[2], int(donnees[3]), donnees[4], int(donnees[5]), int(donnees[6])))
    return liste_poke

def find_poke(equipe_e, equipe_c, last_poke):
    """
    Renvoie le choix d'attaque qui serait le plus optimisé à faire pour faire
    le plus de dégâts
    """
    best_degats = 0
    for i in equipe_e:
        for y in equipe_c:
            degats = attaque(i, y)
            if (degats > best_degats) and (y.get_pdv() > 0) and (i.get_pdv() > 0):
                if (last_poke != i) or (len_equipe(equipe_e) == 1):
                    b_envoyeur = i
                    b_cible = y
                    best_degats = degats
    return (b_envoyeur, b_cible, best_degats)