"""Test direction-only boundary conservation without presupposing a connected ordered window record. Candidate list independent of balance; all four alternatives per control. Distinguish one arrow with multiple readers from separately charged occurrences."""
from pathlib import Path
from collections import Counter
import json
D=Path(__file__).resolve().parents[1];src=json.loads((D/'results/pne_unoriented_join.json').read_text());out={}
for label,rec in src.items():
 rows=[]
 for test in rec['tests']:
  ws=test['windows'];edges=[e for w in ws for e in zip(w,w[1:])];nodes=sorted(set(sum(ws,[])));internal=[s for s in nodes if sum(s in w for w in ws)>1];E=sorted(set(edges));
  def bal(es):return {s:sum(x==s for x,y in es)-sum(y==s for x,y in es) for s in nodes}
  d=bal(E);occ=bal(edges);keep=all(not d[s] for s in internal);trails=[]
  if keep:
   def walk(p,left):
    if not left:trails.append(p);return
    for x,y in left:
     if p[-1]==x:walk(p+[y],left-{(x,y)})
   starts=[s for s in nodes if d[s]==1];assert len(starts)==1;walk(starts,set(E));assert len(trails)==1 and all(any(trails[0][i:i+3]==w for i in range(len(trails[0])-2)) for w in ws)
  rows.append(dict(windows=ws,internal=internal,balance=d,occurrence_balance=occ,balanced=keep,trails=trails))
 assert sum(r['balanced'] for r in rows)==1;out[label]=rows
print([(k,[r['balance'] for r in v if r['balanced']],sum(all(not r['occurrence_balance'][s] for s in r['internal']) for r in v)) for k,v in out.items()]);(D/'results/pne_local_boundary_balance.json').write_text(json.dumps(out,indent=2)+'\n')
