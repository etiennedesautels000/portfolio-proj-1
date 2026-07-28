
# Classes
# - Etudiant (code_etudiant, nom_etudiant, note_intra, note_finale, note_projet)
# - Resultats (moyenne, resultat)

class Etudiant:
    def __init__(self, code_etudiant=None, nom_etudiant=None, note_intra=None, note_finale=None, note_projet=None):
        self.code_etudiant = code_etudiant
        self.nom_etudiant = nom_etudiant
        self.note_intra = note_intra
        self.note_finale = note_finale
        self.note_projet = note_projet

class Resultats:
    def __init__(self, moyenne=None, resultat=None):
        self.moyenne = moyenne
        self.resultat = resultat

    def calculer(self,obj_etudiant):
        self.moyenne = round((obj_etudiant.note_intra * 0.3 + obj_etudiant.note_finale * 0.4 + obj_etudiant.note_projet * 0.3), 2)
        self.resultat = "Réussi" if self.moyenne >= 60 else "Échec"

