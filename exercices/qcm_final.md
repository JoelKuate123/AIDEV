# QCM Final — Formation IA pour développeur (2 jours)

**Durée : 15 min. 10 questions. Une seule bonne réponse sauf mention contraire.**

---

**1. Lequel des éléments suivants n'est PAS un compteur de facturation distinct d'un LLM commercial ?**
a) Tokens d'entrée
b) Tokens de sortie
c) Tokens d'attention
d) Tokens de cache

**2. Un SLM (Small Language Model) :**
a) est obligatoirement entraîné par distillation d'un grand modèle
b) a typiquement moins de 10 milliards de paramètres
c) ne peut pas tourner localement
d) a un context window > 1 million de tokens

**3. Dans le canevas ROCDC-IO, le « D » désigne :**
a) Documentation
b) Domain
c) Definition of Done
d) Datatype

**4. Un prompt idempotent :**
a) génère un résultat différent à chaque appel
b) génère un résultat reproductible à entrée identique
c) ne fonctionne qu'avec un seed
d) impose temperature > 0

**5. Dans un pipeline RAG, le chunking sert à :**
a) accélérer l'inférence du LLM
b) découper les documents en morceaux indexables
c) supprimer les doublons
d) compresser la base vectorielle

**6. L'effet « lost in the middle » désigne :**
a) un bug du tokenizer
b) la dégradation de qualité quand le contexte est très long
c) une limite de l'attention sur GPU
d) un échec de cache

**7. MCP signifie :**
a) Multi-Channel Processor
b) Model Context Protocol
c) Managed Cloud Platform
d) Machine-Code Provider

**8. (Plusieurs réponses) Garde-fous indispensables pour un serveur MCP qui requête une base de données :**
a) Utilisateur DB read-only
b) LIMIT par défaut
c) Timeout de requête
d) Audit log

**9. Dans un agent ReAct, la séquence est :**
a) Action → Pensée → Observation
b) Pensée → Action → Observation
c) Observation → Action → Pensée
d) Action → Observation → Pensée

**10. Quel pattern multi-agents convient le mieux à une revue de code ?**
a) Pipeline
b) Router
c) Critique / Worker
d) Debate

---

## Corrigé
1c, 2b, 3c, 4b, 5b, 6b, 7b, 8 a+b+c+d (les 4), 9b, 10c

Barème : 1 pt / bonne réponse, Q8 : 1 pt si les 4 cochées, sinon 0. Total /10.
- 9-10 : niveau staff
- 7-8 : niveau opérationnel
- 5-6 : reprise des chapitres 1 et 4 conseillée
- ≤4 : reprise complète recommandée
