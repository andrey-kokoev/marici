"""Check one six-vertex obstruction to extending the stored order-39 parent."""
import csv
from pathlib import Path

path = Path(__file__).resolve().parents[2] / 'chatgpt/ramsey/ramsey_3_10_witness_39.csv'
with path.open() as f:
    rows = [list(map(int, row)) for row in csv.reader(f) if row]
assert len(rows) == 39 and all(len(row) == 39 for row in rows)
assert all(rows[i][i] == 0 and all(x in (0, 1) and x == rows[j][i]
           for j, x in enumerate(row)) for i, row in enumerate(rows))
S = {2, 9, 13, 24, 26, 32}
assert all(sum(rows[v]) == 9 and rows[20][v] for v in S)
assert all(not rows[u][v] for u in S for v in S)
blue = [u for u in range(39) if u not in S and not any(rows[u][v] for v in S)]
assert blue == [10, 15, 19, 21, 22, 35, 36, 38]
print('Six degree-nine vertices, mutually blue; eight common blue neighbors:', blue)
