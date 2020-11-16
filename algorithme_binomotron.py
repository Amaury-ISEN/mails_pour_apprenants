import random
import mysql.connector


#################
# Déclarations. #
#################

liste_app = []
liste_gpes = []

#variable qui fait la navette entre la liste d'apprenants et la liste de groupes pour la charger
groupe = []

libelle_gpe = []

#i sert à parcourir la liste d'apprenants.
i = 0


################################################################
# Connexion à la base et remplissage de la liste d'apprenants. #
################################################################

#Connexion à notre serveur sql et de notre objet connexion.
bdd = mysql.connector.connect(port=8081,
                                    host='localhost',
                                    user= 'root',
                                    password= 'root',
                                    database= 'Binomotron')

#Création de notre objet curseur sql
curseur = bdd.cursor()

#Récupération des id étudiants et chargement de ceux-ci dans le curseur :
curseur.execute("SELECT id_apprenant FROM apprenants;")

#On énumère le fetchall() du curseur pour ajouter à la liste d'apprenants les données récupérées depuis la BDD.
for x in curseur.fetchall():
    liste_app.append(x[0])

#On charge la longueur de la liste ainsi crée dans une variable qui servira à tester le parcours de notre liste.
tailleClasse = len(liste_app)


#######################
# Inputs utilisateur. #
#######################

#Saisie de la taille visée pour les groupes par l'utilisateur :
print("La liste d'étudiants est de la taille suivante:", tailleClasse)
tailleGpe = int(input("Veuillez indiquer la taille de groupe souhaitée."))

#Saisie du nom de projet qui sera envoyé comme libelle dans la table projets:
libelle_proj = input("Veuillez indiquer un nom pour le projet.")


#############################
# Constitution des groupes. #
#############################

#On mélange notre liste d'étudiants.
random.shuffle(liste_app)

#Point central de notre algorithme: on boucle tant qu'on a pas parcouru toute la liste de la classe.
while i < tailleClasse:
    
    #Si groupe pas fini, on lui ajoute l'étudiant de rang i et on incrémente i.
    if len(groupe) < tailleGpe:
        groupe.append(liste_app[i])
        i+=1
        
    #Si groupe a atteint la taille visée, on l'ajoute à la liste de groupes et on le vide.
    else:
        liste_gpes.append(groupe)
        groupe = []
        
#Ajout d'un éventuel dernier groupe réduit (+ rapide sans condition pour tester si un tel groupe existe).
liste_gpes.append(groupe)

#On crée nos libellés de groupes en fonction de la taille de la liste de groupes.
for x in liste_gpes:
    tuple_gpe = ( "Groupe "+str(1+liste_gpes.index(x)),)
    libelle_gpe.append(tuple_gpe)

#On envoie nos libellés de groupes dans la table groupe.
sql = "INSERT INTO groupes (libelle) VALUES (%s)"
var = libelle_gpe
curseur.executemany(sql, var)
bdd.commit()

#On envoie notre libellé de projet dans la table projets.
sql = "INSERT INTO projets (libelle) VALUES (%s)"
var = (libelle_proj,)
curseur.execute(sql, var)
bdd.commit()

#id_proj est chargé avec l'id obtenu par auto-incrémentation lors de l'insert de la ligne de la requête précédente.
id_proj = curseur.lastrowid

#On insère nos données dans la table d'association:
sql = "INSERT INTO apprenants_groupes (id_apprenant, id_groupe, id_projet) VALUES (%s, %s, %s)"
var = []
for x in liste_gpes:
    for y in x:
        var.append((y, 1+liste_gpes.index(x), id_proj))
curseur.executemany(sql,var)
bdd.commit()


####################################
# Rapport de création des groupes. #
####################################

# Chargement du nombre de groupes créés dans une variable:
nb_gpes_crees = len(liste_gpes)
print("Le projet", libelle_proj, "a les", nb_gpes_crees, "groupes suivants :")

#Requête 
sql = "SELECT prenom,nom, id_groupe FROM apprenants A, apprenants_groupes AG WHERE A.id_apprenant = AG.id_apprenant AND id_projet = %s"
var = (id_proj,)
curseur.execute(sql, var)
resultat = (curseur.fetchall())

#Enumération du nombre de groupes
for x in range(1,1+nb_gpes_crees):
    print("Groupe", x, ":")
    #Enumération du contenu du résultat de la requête:
    for y in resultat:
        #Si le numéro de groupe dans le tuple issu de la requête correspond à celui énuméré en x, alors afficher le prénom et le nom:
        if y[2] == x:
            print(list(y[0:2]))