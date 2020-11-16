import mysql.connector as mysqlcon

#Cette classe centralise le travail sur bdd.
class Base_donnee:

    def __init__ (self):
        self.host = 'localhost'
        self.port = 8081
        self.user = 'root'
        self.mdp = 'root'
        self.nom = None
        self.db = 'binomotron'
        self.conn = None

    #############
    # CONNEXION #
    #############

    #Générer la connexion:
    def gen_connexion (self):

        #On teste si la connexion à la bdd n'existe pas :
        if self.conn == None:
            #Si pas de connexion, on en crée une à la bdd souhaitée en paramètre de la méthode :
            connexion = mysqlcon.connect(port = self.port,
                                        host = self.host,
                                        user = self.user,
                                        password = self.mdp,
                                        database = self.db)
                                        
            setattr(self, "conn", connexion)

            
    def fermer_connexion (self):
        self.conn.close()


    ###########
    # CURSEUR #
    ###########

    def creer_curseur (self):
        curseur = self.conn.cursor(buffered=True)
        return curseur

    def fermer_curseur (self, curseur):
        curseur.close()

    ########
    # BASE #
    ########

    def ajout_colonne (self, curseur, nom_table, nom_colonne):
        query = f"ALTER TABLE {nom_table} ADD COLUMN {nom_colonne} VARCHAR(255)"
        curseur.execute(query)
        del query

    #Méthode qui retourne une liste d'apprenants à partir de la bdd :
    def recup_apprenants_base (self, curseur):

        resultat = []
        curseur.execute('SELECT id_apprenant, nom, prenom, mail FROM apprenants;')

        for x in curseur.fetchall():
            resultat.append(x)

        return resultat

    #Méthode pour mettre à jour les mails en base via les objets apprenants
    def maj_mails_base (self, curseur, objets):
        
        sql = "UPDATE apprenants SET mail = %s WHERE id_apprenant = %s;"
        var = []
        for x in objets:
            var.append( (x.mail, x.id) )
        curseur.executemany(sql,var)
        self.conn.commit()
        del sql
        del var