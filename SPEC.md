# Ajout de la route GET /nightly et tests associés

Implémentation d'un endpoint unique `/nightly` dans `app/main.py` renvoyant un JSON spécifique, accompagné de sa validation par des tests unitaires dans `tests/test_app.py`.

## Objectifs
- Ajouter la route GET `/nightly`
- Retourner le payload JSON exact : {"status": "ok", "source": "collegue"}
- Garantir la conformité via des tests automatisés

## Périmètre
Inclus : modification de `app/main.py` et `tests/test_app.py`. Exclus : toute autre modification de la logique métier, l'ajout de nouvelles routes ou l'ajout de dépendances.

## Contraintes
- Aucune nouvelle dépendance autorisée
- Le JSON de réponse doit être strictement identique à la spécification
- Le code HTTP doit être 200
- La tâche doit rester atomique

## Hypothèses
- Le projet utilise un framework web (type FastAPI ou Flask) déjà présent
- Un framework de test (type pytest) est déjà configuré
- La structure des fichiers `app/main.py` et `tests/test_app.py` est conforme à l'énoncé

## Critères d'acceptation
- [ ] Une requête GET sur `/nightly` renvoie un code de statut HTTP 200
- [ ] Le corps de la réponse à `/nightly` est strictement `{"status": "ok", "source": "collegue"}`
- [ ] L'exécution des tests (ex: `pytest`) est concluante (success)
- [ ] Aucune nouvelle dépendance n'apparaît dans les fichiers de gestion de dépendances (requirements.txt, pyproject.toml, etc.)
- [ ] Aucune autre route ou fonctionnalité existante n'a été modifiée
