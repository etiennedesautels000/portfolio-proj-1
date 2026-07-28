

# Application principale pour un serveur Flask

from app_calculer_moyenne.routes import app
from app_calculer_moyenne.dao.mod_dao import init_db

if __name__ == "__main__":
    with app.app_context(): # initialisation de la bdd
        init_db()
    app.run(debug=True, port=5600) # lancer le serveur flask

