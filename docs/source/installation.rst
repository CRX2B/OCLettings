Installation du Projet
======================

Ce guide rapide décrit les étapes pour installer et configurer l'application Orange County Lettings en environnement de développement local.

Instructions d'installation
---------------------------

1.  **Cloner le dépôt et se positionner dans le dossier :**

    .. code-block:: bash

       git clone https://github.com/CRX2B/OCLettings.git
       cd OCLettings

2.  **Créer et activer un environnement virtuel :**

    .. code-block:: bash

       python -m venv env
       source env/bin/activate  # Pour macOS/Linux
       # Pour Windows CMD: env\Scripts\activate

3.  **Installer les dépendances :**

    .. code-block:: bash

       pip install -r requirements.txt

4.  **Initialiser la base de données :**

    .. code-block:: bash

       python manage.py migrate

Après ces étapes, lancez le serveur de développement comme indiqué dans le :doc:`guide_demarrage`. 