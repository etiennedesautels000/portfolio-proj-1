
# Labels et champs de formulaire html

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, IntegerField
from wtforms.validators import DataRequired

class Form_Fields(FlaskForm):
    id_etudiant = IntegerField('ID étudiant: ', validators=[DataRequired()])
    nom = StringField('Nom: ', validators=[DataRequired()])
    examen_intra = FloatField('Examen intra: ', validators=[DataRequired()])
    examen_final = FloatField('Examen final: ', validators=[DataRequired()])
    projet_session = FloatField('Projet de session: ', validators=[DataRequired()])

    moyenne = StringField('Moyenne: ')
    resultat = StringField('Resultat: ')

    quitter = SubmitField('Quitter')
    enregistrer = SubmitField('Enregistrer')
    effacer = SubmitField('Effacer')
    calculer = SubmitField('Calculer')
