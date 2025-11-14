import sqlite3
from pathlib import Path

db = Path(__file__).resolve().parents[0].joinpath('..', 'db.sqlite3').resolve()
print('DB path:', db)
conn = sqlite3.connect(str(db))
cur = conn.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
tables = [r[0] for r in cur.fetchall()]
print('TABLES:', tables)

# check counts for tables that look like food tables
candidates = [t for t in tables if 'food' in t.lower() or 'canteen' in t.lower() or 'product' in t.lower()]
print('CANDIDATE TABLES:', candidates)
for t in candidates:
    try:
        cur.execute(f'SELECT COUNT(*) FROM "{t}"')
        print(t, 'COUNT', cur.fetchone()[0])
    except Exception as e:
        print('Error counting', t, e)

conn.close()
