
# Database access object

from flask_sqlalchemy import SQLAlchemy
from app_calculer_moyenne.settings import app
import json
from app_calculer_moyenne.modele.mod_classes import Etudiant, Resultats
from datetime import datetime, timezone

db = SQLAlchemy(app)

class DAO(db.Model):
    __tablename__ = 'table'
    code_etudiant = db.Column(db.Integer, primary_key=True)
    nom_etudiant = db.Column(db.String, nullable=False)
    note_intra = db.Column(db.Float, nullable=False)
    note_finale = db.Column(db.Float, nullable=False)
    projet_session = db.Column(db.Float, nullable=False)
    date_creation = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        obj = {
            'code_etudiant': self.code_etudiant,
            'nom_etudiant': self.nom_etudiant,
            'note_intra': self.note_intra,
            'note_finale': self.note_finale,
            'projet_session': self.projet_session,
            'date_creation': str(self.date_creation)
        }
        return json.dumps(obj)

def init_db():
    '''
    Création de la table (si elle n'existe pas)
    '''
    db.create_all()

def enregistrer_etudiant(etudiant):
    '''
    Insertion (INSERT) d'un enregistrement à la bd
    :param etudiant: (objet) contient les informations de l'étudiant
    :return None
    '''
    nouvel_etudiant = DAO(
        code_etudiant=etudiant.code_etudiant,
        nom_etudiant=etudiant.nom_etudiant,
        note_intra=etudiant.note_intra,
        note_finale=etudiant.note_finale,
        projet_session=etudiant.note_projet
    )
    db.session.add(nouvel_etudiant)
    db.session.commit()

def exist_etudiant(code_etudiant):
    '''
    Vérifier si le code étudiant existe déjà dans la bdd
    :param code_etudiant: (string) code de l'étudiant
    :return (boolean) True si le code de l'étudiant existe, False s'il n'existe pas
    '''
    record = db.session.get(DAO, code_etudiant)
    return record is not None

def lister_etudiants():
    '''
    Récupérer (SELECT) la liste des étudiants enregistrés dans la bdd
    :return (liste de tuples) tableau des valeurs de la table de bdd
    '''
    table = DAO.query.all()

    table_resultats = []
    for record in table:
        obj_etudiant = Etudiant(
            record.code_etudiant,
            record.nom_etudiant,
            record.note_intra,
            record.note_finale,
            record.projet_session)

        obj_resultats = Resultats()
        obj_resultats.calculer(obj_etudiant)
        table_resultats.append((obj_etudiant.code_etudiant,
                                obj_etudiant.nom_etudiant,
                                obj_etudiant.note_intra,
                                obj_etudiant.note_finale,
                                obj_etudiant.note_projet,
                                obj_resultats.moyenne,
                                obj_resultats.resultat))

    return table_resultats
