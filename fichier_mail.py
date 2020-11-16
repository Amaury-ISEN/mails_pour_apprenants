class Fichier:

    def __init__ (self, source):
        self.fichier = open(source, 'r')
        self.chemin = source

    def fermer (self):
        self.fichier.close()

    def creer_liste_lignes (self):
        contenu = self.fichier.read().splitlines()
        return contenu

    #Cette méthode sert à retourner une liste qui associe les mails à des nom/prénoms générés via les mails.
    #La méthode est faite pour prendre une liste de mails générée via creer_liste_lignes en paramètre.
    @staticmethod
    def extraire_noms (liste_mails):

        #Création d'une liste de forme [ [mail_1, [prénom_généré_1, nom_généré_1]], etc. ]
        resultat = []

        for x in liste_mails:

            resultat.append(
                    #Chaque mail va ici:
                    [x,

                    #Création d'un prénom nettoyé à partir du mail :
                    [str(x).split("@")[0].split('.')[0].replace('-', ' ').replace("'", ' '),
                    
                    #Création d'un nom nettoyé à partir du mail :
                    str(x).split("@")[0].split('.')[1].replace('-', ' ').replace("'", ' ')]
                    ])
                    
        return resultat