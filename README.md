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

## Déploiement sur Render

### Prérequis

- Compte [Render](https://render.com) (gratuit)
- Repository Git hébergé (GitHub, GitLab, etc.)
- Projet push vers le repository

### Configuration du Web Service

1. **Créer un nouveau Web Service sur Render** :
   - Connectez-vous à [Render Dashboard](https://dashboard.render.com)
   - Cliquez sur **"New"** → **"Web Service"**
   - Connectez votre repository Git

2. **Configurer le service** :
   - **Name** : `basicblogger` (ou votre choix)
   - **Environment** : `Python 3`
   - **Build Command** :
     ```bash
     pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
     ```
   - **Start Command** :
     ```bash
     gunicorn posts.wsgi:application
     ```

### Ajouter une base de données PostgreSQL

1. Dans le dashboard Render, cliquez sur **"New"** → **"PostgreSQL"**
2. Configurez la base de données :
   - **Name** : `basicblogger-db`
   - **Plan** : Free (ou selon vos besoins)
3. Créez la base de données
4. Une fois créée, copiez l'**Internal Database URL**
5. Retournez à votre Web Service → **Environment** → Ajoutez :
   - **Key** : `DATABASE_URL`
   - **Value** : Collez l'URL PostgreSQL copiée

### Variables d'environnement requises

Configurez ces variables dans **Environment** de votre Web Service :

| Variable | Valeur | Description |
|----------|--------|-------------|
| `SECRET_KEY` | `[générer une clé]` | Clé secrète Django ([générateur](https://djecrety.ir/)) |
| `DEBUG` | `False` | Mode debug (toujours False en production) |
| `DATABASE_URL` | `[auto par Render]` | URL PostgreSQL (ajoutée automatiquement) |
| `EMAIL_PASSWORD` | `[votre mot de passe]` | Mot de passe d'application Gmail (optionnel) |

> [!TIP]
> **Générer une SECRET_KEY** : Utilisez [Djecrety](https://djecrety.ir/) ou exécutez :
> ```python
> python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
> ```

### Déploiement

1. Cliquez sur **"Create Web Service"**
2. Render démarrera automatiquement le build et le déploiement
3. Attendez que le statut passe à **"Live"** (environ 2-5 minutes)
4. Votre application sera accessible à : `https://your-app-name.onrender.com`

### Checklist Post-Déploiement

Une fois le déploiement réussi, effectuez ces vérifications :

- [ ] **Accéder à l'application** : Ouvrez l'URL Render et vérifiez que la page de login s'affiche
- [ ] **Créer un superutilisateur** :
  ```bash
  # Via le Shell Render (dans l'onglet "Shell" de votre service)
  python manage.py createsuperuser
  ```
- [ ] **Tester l'authentification** :
  - Créer un compte utilisateur
  - Se connecter / Se déconnecter
  - Tester la réinitialisation de mot de passe (si EMAIL_PASSWORD configuré)
- [ ] **Tester les fonctionnalités** :
  - Créer un article de blog
  - Modifier et supprimer un article
  - Ajouter des commentaires
  - Uploader une image de profil
- [ ] **Vérifier les fichiers statiques** :
  - CSS/Bootstrap correctement chargés
  - Pas d'erreurs 404 dans la console navigateur

### Debug en Production

Si vous rencontrez des problèmes :

1. **Consulter les logs** :
   - Dans le dashboard Render, allez à l'onglet **"Logs"**
   - Cherchez les erreurs Django ou Gunicorn

2. **Accéder au Shell** :
   - Onglet **"Shell"** dans Render
   - Exécutez des commandes Django :
     ```bash
     python manage.py check
     python manage.py showmigrations
     ```

3. **Erreurs fréquentes** :
   - **500 Internal Server Error** : Vérifiez `SECRET_KEY` et `DATABASE_URL`
   - **CSS non chargé** : Vérifiez que `collectstatic` s'est exécuté dans le build
   - **CSRF Error** : Vérifiez `CSRF_TRUSTED_ORIGINS` dans settings.py

## Licence

Ce projet est un projet éducatif de démonstration.
