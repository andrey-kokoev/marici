"""Can the exact capacity certificate survive forgetting set names? Average weights inside each profile, then verify every inequality with integer arithmetic. Failure of this certificate does not establish profile impossibility. Check separately whether the aggregation preserves all classwise neighbor counts (an equitable partition)."""
import sys,gzip,json,math,collections
from pathlib import Path
root=Path(__file__).resolve().parents[2];p=root/'chatgpt/ramsey';sys.path.insert(0,str(p));from ramsey_r37_recursive_proof_verify import graph6,independent_fives
D=root/'voevodsky/results';prior={r['record']:r for r in json.loads((D/'ramsey_37_weight_rule_replay.json').read_text())};rows=[]
for j,line in enumerate(gzip.open(p/'r36_16.g6.gz','rb'),1):
 if j not in prior:continue
 A=graph6(line);F=independent_fives(A);ds=[[h for h,b in enumerate(F) if not a&b] for a in F];deg=list(map(len,ds));cert=prior[j]['weights'];z=[cert.get(str(i),0) for i in F];rec={}
 for mode in ('sum','hist'):
  groups=collections.defaultdict(list)
  for i,d in enumerate(ds):groups[(deg[i],sum(deg[t] for t in d)) if mode=='sum' else tuple(sorted(deg[t] for t in d))].append(i)
  scale=math.lcm(*(len(g) for g in groups.values()));w=[0]*len(F)
  for g in groups.values():
   u=sum(z[i] for i in g)*(scale//len(g));
   for i in g:w[i]=u
  W=sum(w);m=min(sum(w[i] for i in d) for d in ds);labels={i:h for h,g in enumerate(groups.values()) for i in g};eq=all(len({tuple(sorted(labels[t] for t in ds[i])) for i in g})==1 for g in groups.values());rec[mode]=dict(classes=len(groups),W=W,m=m,passed=W<6*m,equitable=eq)
 rows.append(dict(record=j,sets=len(F),**rec))
for mode in ('sum','hist'):print(mode,sum(x[mode]['passed'] for x in rows),min(x[mode]['classes'] for x in rows),max(x[mode]['classes'] for x in rows),sum(x[mode]['classes'] for x in rows),sum(x['sets'] for x in rows));print([x['record'] for x in rows if not x[mode]['passed']]);
(D/'ramsey_37_two_step_resolution.json').write_text(json.dumps(rows,indent=2)+'\n');