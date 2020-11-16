#Unidecode sert à nettoyer les noms/prénoms issus de la base de leurs éventuels accents.
from unidecode import unidecode as ud

#Cette classe centralise le travail sur les apprenants. Son objet est l'objet apprenant, instancié pour chaque personne.
class Apprenant:

    #Pour instancier chaque objet apprenant, on utilise un tuple (id, nom, prenom, mail) issu de la requête SQL sur la table apprenants
    def __init__ (self, tuple_apprenant):
        setattr(self, "id", tuple_apprenant[0])
        setattr(self, "nom", tuple_apprenant[1])
        setattr(self, "prenom", tuple_apprenant[2])
        setattr(self, "mail", tuple_apprenant[3])

    #La méthode suivante est statique pour être plus simple à utiliser.
    #Elle prend en paramètre la liste d'objets apprenants et une liste de mails + noms/prénoms générés.
    @staticmethod
    def ajouter_mails (liste_objets, liste_mail_et_noms):
        
        #On parcourt nos instances d'apprenants dans la liste d'objets apprenants :
        for x in liste_objets:

            #On boucle sur la liste de mails qui doit être structurée ainsi [ mail, [ nom_généré, prenom_généré]]
            for y in liste_mail_et_noms:
                
                #On vérifie si le prénom (nettoyé) de l'objet est égal au prénom généré à partir du mail
                if ud(x.prenom.lower()).replace("'", '') == y[1][0]:

                    #On vérifie si le nom (nettoyé) de l'objet est égal au nom généré à partir du mail
                    if ud(x.nom.lower()).replace("'", '') == y[1][1]:
    
                        #Si tout correspond, on peut attribuer le mail de rang y à l'objet en question.
                        setattr(x,"mail", y[0])

        return liste_objets