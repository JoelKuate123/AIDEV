# Mapping — Programme source → Notebooks (version DÉBUTANT, organisée par jours)

**Formation : IA pour développeur (2 jours)**
**Niveau pédagogique : DÉBUTANT**
**Fichier source : `programme 2 jours.txt`**


Ce document trace, ligne à ligne, comment chaque élément du programme source a été transformé en contenu pédagogique débutant.

---

## Vue d'ensemble

La formation est organisée en **2 jours** × **2 demi-journées** = **4 notebooks principaux** :

| Jour | Période | Chapitre source | Notebook | Corrigé | Durée |
|---|---|---|---|---|---|
| **Jour 1** | Matin (9h-12h30) | Ch.1 Fondamentaux LLM | `notebooks/jour1/01_fondamentaux_llm.ipynb` | `corriges/jour1/CORRIGE_chapitre1.ipynb` | ~3h30 |
| **Jour 1** | Après-midi (14h-18h) | Ch.2 Prompting avancé | `notebooks/jour1/02_prompting_avance.ipynb` | `corriges/jour1/CORRIGE_chapitre2.ipynb` | ~3h30 |
| **Jour 2** | Matin (9h-12h30) | Ch.3 RAG et MCP | `notebooks/jour2/03_rag_mcp.ipynb` | `corriges/jour2/CORRIGE_chapitre3.ipynb` | ~3h30 |
| **Jour 2** | Après-midi (14h-18h) | Ch.4 Serveur MCP & Agents | `notebooks/jour2/04_serveur_mcp_agents.ipynb` | `corriges/jour2/CORRIGE_chapitre4.ipynb` | ~3h30 |
| — | — | Ressources complémentaires | `ressources/ressources.md` + `seed_db.py` | — | — |

**Ordre des chapitres conservé à 100 %.** Aucune réorganisation pédagogique nécessaire — la progression du programme source est cohérente.

## Caractéristiques de la version DÉBUTANT

- ✅ **Glossaire** en début de chaque chapitre (8-10 mots définis simplement).
- ✅ **Analogies du quotidien** pour chaque concept abstrait (cuisine, restaurant, bibliothécaire, freelance, voiture…).
- ✅ **Code Python commenté ligne par ligne**, avec étapes numérotées.
- ✅ **Multiples exemples** par concept (3-5 plutôt que 1).
- ✅ **Pré-requis et checkpoints** pour s'autoévaluer en cours de chapitre.
- ✅ **Planning horaire détaillé** par section (estimation en minutes).
- ✅ **Aucune connaissance préalable** mathématique requise — les formules sont expliquées.

---

## Détail Chapitre 1 → Notebook 1

| Ligne(s) du programme | Élément source | Section du notebook |
|---|---|---|
| L.3 | « Comprendre l'architecture neuronale : du perceptron au LLM » | §1 Du perceptron au LLM + cellule code perceptron |
| L.4 | « Maîtriser les concepts clés : poids, biais, descente de gradient, backpropagation » | §2 Apprentissage + démo gradient descent |
| L.5 | « Distinguer distillation et SLM » | §3 Distillation vs SLM (tableau) |
| L.6 | « Analyser le modèle économique : tokens (entrée/sortie/cache), context window, rate limits » | §4 Économie des tokens + §5 Context window et rate limits |
| L.7 | « Découvrir les assistants GenAI intégrés à l'IDE : installation et configuration » | §6 Assistants GenAI dans l'IDE (tableau comparatif) |
| L.8–9 | « TP : Configurer son environnement IA, observer impact paramètres sur coûts » | TP 1.1 (config) + TP 1.2 (impact coût) |

---

## Détail Chapitre 2 → Notebook 2

| Ligne(s) | Source | Section |
|---|---|---|
| L.11 | « Structurer un prompt efficace : Rôle, Objectif, Contraintes, DoD, Contexte, I/O » | §1 Canevas ROCDC-IO + exemple |
| L.12 | « patterns avancés : prompts itérables et prompts idempotents » | §2 Patterns avancés |
| L.13 | « Pratiquer la décharge mentale : faire réécrire et affiner les prompts par l'IA » | §3 Décharge mentale et méta-prompting |
| L.14 | « Organiser son travail avec les skills et subagents » | §4 Skills, subagents et orchestration |
| L.15 | « Optimiser ses prompts pour la génération de code » | §5 Prompts pour la génération de code |
| L.16–17 | « TP : bibliothèque de prompts (refactoring, tests, doc, review) » | TP 2 + 4 prompts modèles dans le corrigé |

---

## Détail Chapitre 3 → Notebook 3

| Ligne(s) | Source | Section |
|---|---|---|
| L.19 | « Comprendre le RAG : embedding → base vectorielle → retrieval → augmentation » | §1 Le problème + §2 Pipeline RAG |
| L.20 | « Identifier les cas d'usage et limites du RAG en entreprise » | §4 Limites du RAG |
| L.21 | « Découvrir le protocole MCP et son architecture » | §5 MCP — architecture |
| L.22 | « Explorer les serveurs MCP de la marketplace (GitHub, filesystem, bases) » | §6 Marketplace MCP |
| L.23 | « Intégrer un serveur MCP dans son workflow » | §6 + TP partie B |
| L.24–25 | « TP : RAG sans framework + serveur MCP marketplace » | TP 3 partie A (RAG) + partie B (MCP) |

---

## Détail Chapitre 4 → Notebook 4

| Ligne(s) | Source | Section |
|---|---|---|
| L.27 | « Concevoir l'architecture d'un serveur MCP custom » | §1 Architecture serveur MCP custom |
| L.28–29 | « Implémenter un serveur MCP connecté à une base : connexion, schémas, requêtes » | §2 MCP + SQLite + code FastMCP |
| L.30 | « Comprendre les agents autonomes : boucle perception → réflexion → action » | §3 Boucle ReAct |
| L.31 | « Maîtriser l'orchestration multi-agents et ses patterns » | §4 Patterns multi-agents (tableau) |
| L.32 | « Identifier les limites et risques : hallucinations, boucles infinies, sécurité » | §5 Risques et garde-fous |
| L.33–34 | « TP : serveur MCP DB + démo agent autonome » | TP 4 (4 étapes) + seed_db.py |

---

## Ressources complémentaires (lignes 35–39)

| Source | Destination |
|---|---|
| Documentation des assistants GenAI (GitHub Copilot, Continue, Cursor) | `ressources/ressources.md` §Assistants GenAI |
| Spécification MCP | `ressources/ressources.md` §Protocole MCP |
| Exemples de serveurs MCP open source | `ressources/ressources.md` §Protocole MCP |
| Guides de prompting pour développeurs | `ressources/ressources.md` (lien implicite via Anthropic/OpenAI guides) |

---

## Éléments ajoutés (non présents dans le programme source)

Ces éléments **complètent** le programme sans le contredire. Toute hypothèse est documentée.

| Ajout | Justification |
|---|---|
| QCM final 10 questions (`exercices/qcm_final.md`) | Évaluation des acquis non précisée dans la source — hypothèse pédagogique standard |
| Objectifs pédagogiques mesurables en tête de chaque notebook | Non explicités dans la source — déduits du contenu |
| Tarifs Claude Sonnet/Haiku 2026 dans les exemples | Source : tarification publique Anthropic (à actualiser le jour J) |
| Référence Ollama + Llama-3.1-8B pour le TP local | Hypothèse : poste avec ≥ 16 Go RAM. À adapter si machines plus modestes |
| Pattern « critique / worker » dans multi-agents | Présent dans la littérature 2024-2026 — non cité tel quel dans la source |

