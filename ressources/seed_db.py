"""Crée exemple.db pour le TP 4 — 50 users + 50 orders."""
import sqlite3, random
from pathlib import Path

DB = Path(__file__).parent / "exemple.db"
if DB.exists():
    DB.unlink()

con = sqlite3.connect(DB)
c = con.cursor()
c.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, email TEXT, name TEXT, role TEXT)")
c.execute("CREATE TABLE orders (id INTEGER PRIMARY KEY, user_id INTEGER, amount REAL, status TEXT)")

PRENOMS = ["Aïcha", "Lucas", "Fatima", "Yann", "Maya", "Tarek", "Léa", "Idriss", "Ines", "Hugo"]
NOMS    = ["Diallo", "Martin", "Sow", "Dupont", "Nguyen", "Garcia", "Petit", "Bah", "Bernard", "Roy"]
ROLES   = ["admin", "user", "user", "user", "viewer"]

random.seed(42)
for i in range(1, 51):
    prenom = random.choice(PRENOMS)
    nom    = random.choice(NOMS)
    c.execute("INSERT INTO users (id, email, name, role) VALUES (?, ?, ?, ?)",
              (i, f"{prenom.lower()}.{nom.lower()}@example.com", f"{prenom} {nom}", random.choice(ROLES)))

STATUSES = ["pending", "paid", "paid", "paid", "canceled"]
for i in range(1, 51):
    c.execute("INSERT INTO orders (id, user_id, amount, status) VALUES (?, ?, ?, ?)",
              (i, random.randint(1, 50), round(random.uniform(10, 500), 2), random.choice(STATUSES)))

con.commit()
con.close()
print(f"Base créée : {DB}")
