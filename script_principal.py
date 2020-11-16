from base_donnee import Base_donnee
from fichier_mail import Fichier
from apprenant import Apprenant

def main ():

    #On crée notre objet fichier.
    fichier = Fichier("apprenantmail.txt")
    
    #On extrait dans une liste les mails du fichier.
    liste_mails = fichier.creer_liste_lignes()

    #On referme notre fichier
    fichier.fermer()

    #On extrait dans une liste les noms du fichier des mails.
    liste_mail_et_noms = Fichier.extraire_noms(liste_mails)

    #On crée notre objet connexion mySQL.
    connexion = Base_donnee()

    #On se connecte à la BDD.
    connexion.gen_connexion()
    
    #On crée le curseur.
    curseur = connexion.creer_curseur()

    #On récupère tous les apprenants en base (id, nom, prenom & mail) et on charge une liste avec :
    liste_apprenants = connexion.recup_apprenants_base(curseur)

    #Avec la liste d'apprenants issue de la base, on crée nos objets apprenants qu'on met dans une liste.
    objets = [Apprenant(x) for x in liste_apprenants]

    #On enrichit nos objets apprenants de leurs addresses mails respectives.
    Apprenant.ajouter_mails(objets, liste_mail_et_noms)

    #On met à jour les mails en base à partir des objets apprenants :
    connexion.maj_mails_base(curseur, objets)

    #On ferme le curseur :
    connexion.fermer_curseur(curseur)

    #On ferme la connexion :
    connexion.fermer_connexion()

main()