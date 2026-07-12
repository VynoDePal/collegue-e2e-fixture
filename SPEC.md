# Ajout de la route GET /nightly et de son test unitaire

Implémentation d'un endpoint unique `/nightly` renvoyant un JSON spécifique et ajout d'un test de validation pour garantir la conformité du code de statut et du contenu.

## Objectifs
- Ajouter la route GET `/nightly` dans `app/main.py`
- Retourner le payload JSON exact : {"status": "ok", "source": "collegue"}
- Implémenter ou mettre à jour `tests/test_app.py` pour valider la nouvelle route

## Périmètre
Inclus : modification de `app/main.py` et `tests/test_app.py`. Exclus : toute autre modification de la logique métier, l'ajout de nouvelles routes ou l'ajout de dépendances.

## Contraintes
- Aucune nouvelle dépendance ne doit être ajoutée
- Aucun autre comportement existant ne doit être modifié
- La tâche doit rester strictement atomique

## Hypothèses
- Le projet utilise un framework web standard (type FastAPI ou Flask) déjà configuré
- Un framework de test (type pytest) est déjà présent et fonctionnel
- Le fichier `app/main.py` et `tests/test_app.py` existent déjà

## Critères d'acceptation
- [ ] Une requête GET sur `/nightly` renvoie un code de statut HTTP 200
- [ ] Le corps de la réponse de `/nightly` est strictement égal à {"status": "ok", "source": "collegue"}
- [ ] L'exécution de la commande de test (ex: pytest) confirme le succès du test pour la route `/nightly`
- [ ] L'ajout de la route ne modifie pas le résultat des tests existants
