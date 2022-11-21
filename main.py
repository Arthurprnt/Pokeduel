# -*- coding: utf-8 -*-
"""
Projet NSI POO
"""

import pokepy as ppy
import pygame
pygame.init()

BOUTON_COOP = pygame.image.load('assets/coop_locale.png')
BOUTON_IA = pygame.image.load('assets/affronte_ia.png')
CADRE_IMAGE = pygame.image.load('assets/picked.png')
POISON_IMAGE = pygame.image.load('assets/poison.png')
EQUIPE1 = []
EQUIPE2 = []
FONT = pygame.font.Font('assets/Montserrat-Black.ttf', 31)
ICON = pygame.image.load('assets/icon.png')
LISTE_POKE = ppy.import_pokemons("assets/liste_poke.csv")
P1_ALIVE = 5
P2_ALIVE = 5
SCREEN = pygame.display.set_mode()
X, Y = SCREEN.get_size()
CHOIX_MADE = False

fond = pygame.image.load('assets/background.png')
fond = pygame.transform.scale(fond, (X, Y))

pygame.display.set_icon(ICON)
pygame.display.set_caption('Pokemon')
pygame.display.flip()
pygame.mixer.music.load("assets/battle.mp3")
pygame.mixer.music.set_volume(0.5)

ppy.start("J1", EQUIPE1, "J2", EQUIPE2, LISTE_POKE)

presentation = [False, 0]
TXT_EQUIPE1 = ""
for i in EQUIPE1:
    TXT_EQUIPE1 = TXT_EQUIPE1 + i.get_nom() + ", "
TXT_EQUIPE1 = TXT_EQUIPE1[:-2]
TXT_EQUIPE2 = ""
for i in EQUIPE2:
    TXT_EQUIPE2 = TXT_EQUIPE2 + i.get_nom() + ", "
TXT_EQUIPE2 = TXT_EQUIPE2[:-2]
phrases_presentation = ["Les équipes ont été formées !", "Equipe n°1:", TXT_EQUIPE1, "Equipe n°2:", TXT_EQUIPE2, "  "]
PHRASE = ""

STATS = 0
textes_stats = ["Joueur 1 choisissez le Pokemon que vous voulez faire attaquer", "Choisissez maintenant la cible de l'attaque", "", "Joueur 2 choisissez le Pokemon que vous voulez faire attaquer", "Choisissez maintenant la cible de l'attaque", "", "", ""]
ENVOYEUR1 = ""
CIBLE1 = ""
ENVOYEUR2 = ""
CIBLE2 = ""
TEXTE_MID = ""

RUNNING = True

while RUNNING:

    SCREEN.blit(fond, (0, 0))

    if(CHOIX_MADE is False):
        ppy.afficher_texte(SCREEN, "Comment souhaitez vous jouer ?", FONT, X//2, Y//4, (255, 255, 255))
        ZONE_B_CO = [[round(X/2)-round(225*X/1920), round(X/2)-round(225*X/1920)+round(X/4)], [round(Y/1.8), round(Y/1.8)+round(Y/4)]]
        ZONE_B_IA = [[round(X/2)-round(225*X/1920), round(X/2)-round(225*X/1920)+round(X/4)], [round(Y/2)-round(Y/5.5), round(Y/2)-round(Y/5.5)+round(Y/4)]]
        SCREEN.blit(pygame.transform.scale(BOUTON_COOP, (round(X/4), round(Y/4))), (round(X/2)-round(225*X/1920), round(Y/1.8)))
        SCREEN.blit(pygame.transform.scale(BOUTON_IA, (round(X/4), round(Y/4))), (round(X/2)-round(225*X/1920), round(Y/2)-round(Y/5.5)))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                """
                print("souris:", event.pos[0], event.pos[1])
                print("bouton:", ZONE_B_CO[0][0], ZONE_B_CO[0][1])
                print("bouton:", ZONE_B_CO[1][0], ZONE_B_CO[1][1])
                """
                if (event.pos[0] <= ZONE_B_CO[0][1]) and (event.pos[0] >= ZONE_B_CO[0][0]):
                    if (event.pos[1] <= ZONE_B_CO[1][1]) and (event.pos[1] >= ZONE_B_CO[1][0]):
                        CHOIX_MADE = True
                        IS_IA = False
                if (event.pos[0] <= ZONE_B_IA[0][1]) and (event.pos[0] >= ZONE_B_IA[0][0]):
                    if (event.pos[1] <= ZONE_B_IA[1][1]) and (event.pos[1] >= ZONE_B_IA[1][0]):
                        CHOIX_MADE = True
                        IS_IA = True

    if CHOIX_MADE is True:

        """
        print("lenEquipe1: " + str(ppy.len_equipe(EQUIPE1)))
        print("lenEquipe2: " + str(ppy.len_equipe(EQUIPE2)))
        print("stats: " + str(STATS))
        """

        # Affiche le texte de l'état
        if STATS != 3 and STATS != 6 and STATS < 7:
            ppy.afficher_texte(SCREEN, textes_stats[STATS-1], FONT, X//2, Y//2, (255, 255, 255))
        else:
            # Etat 3 ou 6 => Affichage des degats de l'attaque
            if STATS in (3, 6):
                ppy.afficher_texte(SCREEN, TEXTE_MID, FONT, X//2, Y//2, (255, 255, 255))
            elif STATS == 7:
                ppy.afficher_texte(SCREEN, str(ppy.equipe_gagnante(EQUIPE1, EQUIPE2)) + " a gagné le combat !", FONT, X//2, Y//2, (255, 255, 255))
        
        if presentation[0] is True:
        
            # Affiche les pokémons de l'équipe 2
            xpoke = round(X/8.533)
            for i in EQUIPE2:
                if i.get_pdv() > 0:
                    poke = pygame.transform.scale(i.get_image(), (round(X/7.314), round(X/7.314)))
                    SCREEN.blit(poke, (xpoke, round(X/20)))
                    i.set_pos([[xpoke, xpoke+round(X/7.314)], [round(X/20), round(X/20)+round(X/7.314)]])
                    ppy.afficher_texte(SCREEN, str(i.get_nom()), FONT, xpoke+round(X/14.9), round(X/20)+round(X/7.314)+round(X/365.714), (255, 255, 255))
                    ppy.afficher_texte(SCREEN, "PV: " + str(i.get_pdv()), FONT, xpoke + round(X/14.9), round(X/20)+round(X/7.314)+round(X/54.857), (255, 255, 255))
                    ppy.afficher_texte(SCREEN, "ATQ: " + str(i.get_degat()), FONT, xpoke + round(X / 14.9),round(X/20) + round(X / 7.314) + round(X/54.857*1.87), (200, 200, 200))
                    if(STATS == 5 and ENVOYEUR2 == i):
                        SCREEN.blit(pygame.transform.scale(CADRE_IMAGE, (round(X/7.314), round(X/7.314))), (xpoke, round(X/20)))
                    if i.is_poisoned():
                        SCREEN.blit(pygame.transform.scale(POISON_IMAGE, (round(X/7.314), round(X/7.314))), (xpoke, round(X/20)))
                xpoke = xpoke + round(X/6.4)

            # Affiche les pokémons de l'équipe 1
            xpoke = round(X/8.533)
            for i in EQUIPE1:
                if i.get_pdv() > 0:
                    poke = pygame.transform.scale(i.get_image(), (round(X/7.314), round(X/7.314)))
                    SCREEN.blit(poke, (xpoke, Y-round(X/15.058)-round(X/6.214)))
                    i.set_pos([[xpoke, xpoke + round(X / 7.314)], [Y-round(X/15.058)-round(X/6.214), Y-round(X/15.058)-round(X/6.214) + round(X / 6.214)]])
                    ppy.afficher_texte(SCREEN, str(i.get_nom()), FONT, xpoke+round(X/14.9), Y-round(X/6.214)-round(X/11.058)+round(X/6.214)+round(X/365.714), (255, 255, 255))
                    ppy.afficher_texte(SCREEN, "PV: " + str(i.get_pdv()), FONT, xpoke + round(X/14.9), Y - round(X/6.214) - round(X/11.058) + round(X/6.214)+round(X / 54.857), (255, 255, 255))
                    ppy.afficher_texte(SCREEN, "ATQ: " + str(i.get_degat()), FONT, xpoke + round(X / 14.9), Y - round(X / 6.214) - round(X / 11.058) + round(X / 6.214) + round(X/54.857*1.87),(200, 200, 200))
                    if STATS == 2 and ENVOYEUR1 == i:
                        SCREEN.blit(pygame.transform.scale(CADRE_IMAGE, (round(X/7.314), round(X/7.314))), (xpoke, Y-round(X/15.058)-round(X/6.214)))
                    if i.is_poisoned():
                        SCREEN.blit(pygame.transform.scale(POISON_IMAGE, (round(X/7.314), round(X/7.314))), (xpoke, Y-round(X/15.058)-round(X/6.214)))
                xpoke = xpoke + round(X/6.4)

        ppy.afficher_texte(SCREEN, PHRASE, FONT, X//2, Y//2, (255, 255, 255))

        ppy.afficher_texte(SCREEN, phrases_presentation[presentation[1]], FONT, X//2, Y//2, (255, 255, 255))

        if STATS == 4 and IS_IA is True:
            REPONSE_IA = ppy.find_poke(EQUIPE2, EQUIPE1, ENVOYEUR2)
            REPONSE_IA[1].set_pdv(REPONSE_IA[1].get_pdv() - REPONSE_IA[2])
            pygame.mixer.Sound("assets/pokemons/son/" + str(REPONSE_IA[0].get_id()) + ".mp3").play()
            TEXTE_MID = str(REPONSE_IA[0].get_nom()) + " utilise " + REPONSE_IA[0].get_attaque() + " et inflige " + str(REPONSE_IA[2]) + " dégâts à " + str(REPONSE_IA[1].get_nom())
            ENVOYEUR2 = REPONSE_IA[0]
            STATS = 6

        if STATS == 10:
            STATS = 1
            for i in EQUIPE1:
                if i.is_poisoned():
                    i.set_pdv(i.get_pdv()-10)
                    i.tour_passe()
                    if i.get_tpoison() < 1:
                        i.set_poisoned(False)
            for i in EQUIPE2:
                if i.is_poisoned():
                    i.set_pdv(i.get_pdv()-10)
                    i.tour_passe()
                    if i.get_tpoison() < 1:
                        i.set_poisoned(False)

    for event in pygame.event.get():

        if presentation[0] is False and CHOIX_MADE is True:
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_SPACE, pygame.K_RETURN):
                    presentation[1] = presentation[1] + 1
                    if presentation[1] == 5:
                        presentation[0] = True
                        pygame.mixer.music.play()
                        STATS = 1
                elif event.key == pygame.K_ESCAPE:
                    RUNNING = False

        else:
            if event.type == pygame.QUIT:
                RUNNING = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Passage à l'etat 4
                    if STATS == 3:
                        STATS = 4
                    # Passage à l'etat 1
                    if STATS == 6:
                        STATS = 10
                    if STATS == 7:
                        STATS = 8
                    if STATS == 8:
                        STATS = 9
                    if STATS == 9:
                        RUNNING = False
                elif event.key == pygame.K_ESCAPE:
                    RUNNING = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i in EQUIPE1:
                    if(event.pos[0] <= i.get_pos()[0][1]) and (event.pos[0] >= i.get_pos()[0][0]):
                        if(event.pos[1] <= i.get_pos()[1][1]) and (event.pos[1] >= i.get_pos()[1][0]):
                            print(i.get_nom() + " a été cliqué")
                            if i.get_pdv() > 0:
                                # Etat 1 => Choix de l'attaqueur 1
                                if(STATS == 1 and ENVOYEUR1 != i) or (ppy.len_equipe(EQUIPE1) == 1 and STATS == 1):
                                    ENVOYEUR1 = i
                                    STATS = 2
                                # Etat 5 => Choix de la cible 2
                                if STATS == 5:
                                    CIBLE2 = i
                                    CIBLE2.set_pdv(CIBLE2.get_pdv() - ppy.attaque(ENVOYEUR2, CIBLE2))
                                    # Check si l'envoyeur est de type poison
                                    if(ENVOYEUR2.get_element() == "poison") and (CIBLE2.is_poisoned() is False):
                                        CIBLE2.set_poisoned(True)
                                        CIBLE2.set_tpoison(3)
                                    TEXTE_MID = str(ENVOYEUR2.get_nom()) + " utilise " + ENVOYEUR2.get_attaque() + " et inflige " + str(ppy.attaque(ENVOYEUR2, CIBLE2)) + " dégâts à " + str(CIBLE2.get_nom())
                                    pygame.mixer.Sound("assets/pokemons/son/" + str(ENVOYEUR2.get_id()) + ".mp3").play()
                                    STATS = 6
                for i in EQUIPE2:
                    if(event.pos[0] <= i.get_pos()[0][1]) and (event.pos[0] >= i.get_pos()[0][0]):
                        if(event.pos[1] <= i.get_pos()[1][1]) and (event.pos[1] >= i.get_pos()[1][0]):
                            print(i.get_nom() + " a été cliqué")
                            if i.get_pdv() > 0:
                                # Etat 2 => Choix de la cible 1
                                if STATS == 2:
                                    CIBLE1 = i
                                    CIBLE1.set_pdv(CIBLE1.get_pdv() - ppy.attaque(ENVOYEUR1, CIBLE1))
                                    # Check si l'envoyeur est de type poison
                                    if(ENVOYEUR1.get_element() == "poison") and (CIBLE1.is_poisoned() is False):
                                        CIBLE1.set_poisoned(True)
                                        CIBLE1.set_tpoison(3)
                                    TEXTE_MID = str(ENVOYEUR1.get_nom()) + " utilise " + ENVOYEUR1.get_attaque() + " et inflige " + str(ppy.attaque(ENVOYEUR1, CIBLE1)) + " dégâts à " + str(CIBLE1.get_nom())
                                    pygame.mixer.Sound("assets/pokemons/son/" + str(ENVOYEUR1.get_id()) + ".mp3").play()
                                    STATS = 3
                                # Etat 4 => Choix de l'envoyeur 2
                                if (STATS == 4 and ENVOYEUR2 != i) or (ppy.len_equipe(EQUIPE2) == 1 and STATS == 4):
                                    ENVOYEUR2 = i
                                    STATS = 5

    pygame.display.flip()

    if ppy.check_fini(EQUIPE1, EQUIPE2) is True:
        STATS = 7

pygame.quit()
