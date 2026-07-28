
# Routes web

from flask import render_template, flash
from werkzeug.utils import redirect
from app_calculer_moyenne.form_fields import Form_Fields
from app_calculer_moyenne.modele.mod_classes import Etudiant, Resultats
from app_calculer_moyenne.dao.mod_dao import enregistrer_etudiant, exist_etudiant, lister_etudiants
from app_calculer_moyenne.settings import app


# Route principale (index)
# Liste des étudiants enregistrés
@app.route("/")
@app.route("/index")
@app.route("/index.html")
def index():
    etudiants = lister_etudiants()
    if not etudiants:
        flash("Aucun enregistrement")
    return render_template('index.html', title='Application de calcul de notes étudiant', etudiants=etudiants)


# Route secondaire
# Formulaire de saisie des données des étudiants
@app.route("/formulaire" , methods=['GET', 'POST'])
def formulaire():
    form_obj = Form_Fields()

    # boutons quitter ou effacer
    if form_obj.is_submitted():
        # quitter
        if form_obj.quitter.data:
            return redirect('/')
        # effacer
        if form_obj.effacer.data:
            return redirect('/formulaire')

    # bouton calculer ou enregistrer
    if form_obj.validate_on_submit():
        objEtudiant = Etudiant(
            form_obj.id_etudiant.data,
            form_obj.nom.data,
            form_obj.examen_intra.data,
            form_obj.examen_final.data,
            form_obj.projet_session.data
        )
        objResultats = Resultats()
        objResultats.calculer(objEtudiant)

        # calculer moyenne et résultat
        if form_obj.calculer.data:

            form_obj.moyenne.data = objResultats.moyenne
            form_obj.resultat.data = objResultats.resultat

        # enregistrer données
        if form_obj.enregistrer.data:

            form_obj.moyenne.data = objResultats.moyenne
            form_obj.resultat.data = objResultats.resultat

            if exist_etudiant(objEtudiant.code_etudiant):
                flash(
                    f"L'étudiant avec le code {objEtudiant.code_etudiant} existe déjà.")
            else:
                enregistrer_etudiant(objEtudiant)
                flash("Resultat enregistré.")
            return redirect('/formulaire')

    return render_template('form.html', title='Formulaire de calcul de notes', form=form_obj)



