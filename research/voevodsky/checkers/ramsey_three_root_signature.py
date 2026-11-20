"""Three successive roots = a minus triple. Classify remaining vertices by their three link signs; then actually root once more in the --- core."""
from collections import Counter
from itertools import combinations
from pathlib import Path
import json
D=Path(__file__).resolve().parents[1]/'results';E={tuple(e) for e in json.loads((D/'ramsey_39_glue_vs_circle.json').read_text())['plus_edges']};V=range(35)
def plus(i,j):return tuple(sorted((i,j))) in E
rows=Counter();sample=None
for t in combinations(V,3):
    if any(plus(*e) for e in combinations(t,2)):continue
    words={j:''.join('+' if plus(i,j) else '-' for i in t) for j in V if j not in t};hist=Counter(words.values());core=[j for j,s in words.items() if s=='---'];best=max(len(core)-1-sum(plus(i,j) for j in core) for i in core);rows[len(hist),len(core),best]+=1
    if t==(0,4,8):sample=dict(roots=t,words=dict(hist),fourth_max=best)
out=dict(by_class=[dict(occupied=k,third_core=n,best_fourth=m,triples=v) for (k,n,m),v in sorted(rows.items())],example=sample);print(out);(D/'ramsey_three_root_signature.json').write_text(json.dumps(out,indent=2)+'\n')
