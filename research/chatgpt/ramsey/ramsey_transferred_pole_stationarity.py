"""Test whether any center-transfer marking map preserves the seed's row-stationary entry/exit poles, without adding an anchor convention."""
from pathlib import Path
from itertools import combinations
import json
D=Path(__file__).parent;P=list(combinations(range(6),2));r=(1,0,2,3,5,4);R=[0]+[1+r[i] for i in range(6)]+[7+P.index(tuple(sorted(r[x] for x in d))) for d in P]
entry_pole=7;exit_pole=frozenset((11,14,16));assert R[entry_pole]==entry_pole and frozenset(R[v] for v in exit_pole)==exit_pole
rows=[]
for item in json.loads((D/'ramsey_row_center_calculus.json').read_text())['mark_transports']:
 K=item['permutation'];entry=K[entry_pole];exit=frozenset(K[v] for v in exit_pole);rows.append({'phase':item['phase'],'entry_pole':entry,'entry_row_fixed':R[entry]==entry,'exit_pole':sorted(exit),'row_image_exit':sorted(R[v] for v in exit),'exit_row_fixed':frozenset(R[v] for v in exit)==exit})
assert not any(row['exit_row_fixed'] for row in rows)
(D/'ramsey_transferred_pole_stationarity.json').write_text(json.dumps(rows,indent=2)+'\n');print(rows)
