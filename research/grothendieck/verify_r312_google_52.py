"""Verify the Google Research ramsey_number_bounds/improved_bounds R(3,12)>=53 matrix."""
import re
from pathlib import Path
from collections import Counter
from search_r312_circulants import independent

text=Path(__file__).with_name('r312_google_52.txt').read_text()
rows=[list(map(int,r.split())) for r in re.findall(r'\[([01\s]+)\]',text)]
n=len(rows)
assert n==52 and all(len(r)==n for r in rows)
assert all(not rows[i][i] and all(x==rows[j][i] for j,x in enumerate(r)) for i,r in enumerate(rows))
adj=[sum(x<<j for j,x in enumerate(r)) for r in rows]
assert all(not(adj[i]&adj[j]) for i in range(n) for j in range(i) if rows[i][j])
assert independent((1<<n)-1,11,adj) and not independent((1<<n)-1,12,adj)
print(n,'vertices;',sum(map(sum,rows))//2,'edges; degrees',dict(sorted(Counter(map(sum,rows)).items())),'; triangle-free; alpha=11')
