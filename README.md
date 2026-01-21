# BasicBlogger

## Description

BasicBlogger est une plateforme de blog développée avec Django permettant aux utilisateurs de créer, modifier et supprimer des articles, de commenter les publications et de gérer leur profil. L'application offre une interface responsive et intuitive pour partager des idées et interagir avec la communauté.

## Fonctionnalités

- **CRUD des articles** : Création, lecture, modification et suppression d'articles de blog
- **Système de commentaires** : Ajout de commentaires sur les articles
- **Authentification utilisateurs** : Inscription, connexion et déconnexion sécurisées
- **Gestion de profil** : Modification du profil utilisateur avec upload d'image (PNG, JPG)
- **Réinitialisation du mot de passe** : Récupération du mot de passe par email (SMTP Gmail)
- **Permissions et sécurité** : Protection des routes avec `@login_required` decorator
- **Interface responsive** : Design adaptatif utilisant Bootstrap 4

## Stack technique

- **Backend** : Django 5.0.3, Python
- **Frontend** : HTML5, CSS3, JavaScript, Bootstrap 4, Crispy Forms
- **Base de données** : SQLite3
- **Gestion des formulaires** : Django Crispy Forms avec Bootstrap 4
- **Médias** : Gestion des images de profil avec validation d'extensions

## Installation & Lancement

### Prérequis
- Python 3.8+
- pip

### Étapes d'installation

1. **Cloner le dépôt**
   ```bash
   git clone <repository-url>
   cd posts
   ```

2. **Créer un environnement virtuel**
   ```bash
   python -m venv venv
   ```

3. **Activer l'environnement virtuel**
   - Windows :
     ```bash
     venv\Scripts\activate
     ```
   - Linux/Mac :
     ```bash
     source venv/bin/activate
     ```

4. **Installer les dépendances**
   ```bash
   pip install django crispy-bootstrap4 Pillow
   ```

5. **Configurer les variables d'environnement (optionnel)**
   
   Pour la fonctionnalité de réinitialisation du mot de passe par email :
   ```bash
   set EMAIL_PASSWORD=votre_mot_de_passe_gmail
   ```

6. **Appliquer les migrations**
   ```bash
   python manage.py migrate
   ```

7. **Créer un superutilisateur (optionnel)**
   ```bash
   python manage.py createsuperuser
   ```

8. **Collecter les fichiers statiques**
   ```bash
   python manage.py collectstatic
   ```

9. **Lancer le serveur de développement**
   ```bash
   python manage.py runserver
   ```

10. **Accéder à l'application**
    
    Ouvrez votre navigateur et allez à : `http://127.0.0.1:8000/`

## Structure du projet

```
posts/
├── blog/                  # App principale pour les articles et commentaires
│   ├── models.py         # Modèles Post et Comment
│   ├── views.py          # Vues CRUD pour les articles
│   ├── forms.py          # Formulaires PostForm, PostUpdate, CommentForm
│   └── urls.py           # Routes de l'application blog
├── users/                 # App pour la gestion des utilisateurs
│   ├── models.py         # Modèle ProfileModel
│   ├── views.py          # Vues d'authentification et profil
│   ├── forms.py          # Formulaires d'inscription et profil
│   └── urls.py           # Routes d'authentification
├── templates/             # Templates HTML
│   ├── blog/             # Templates pour les articles
│   ├── users/            # Templates pour l'authentification
│   └── partials/         # Composants réutilisables
├── static/                # Fichiers CSS/JS personnalisés
├── media/                 # Fichiers uploadés (images de profil)
├── posts/                 # Configuration du projet Django
│   └── settings.py       # Paramètres de configuration
├── db.sqlite3            # Base de données SQLite
└── manage.py             # Script de gestion Django
```

## Améliorations futures

- Ajout de catégories et tags pour les articles
- Pagination des articles et commentaires
- Système de likes/réactions sur les articles
- Recherche et filtrage des articles
- Upload d'images dans le contenu des articles
- Notifications pour les nouveaux commentaires
- API REST avec Django REST Framework

## Licence

Ce projet est un projet éducatif de démonstration.
