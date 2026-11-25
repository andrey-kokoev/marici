"""Independent Python replay of the documented integer deficit rule; stop at the first certificate and verify its inequalities against the sets directly."""
from pathlib import Path
import sys,gzip,json
D=Path(__file__).resolve().parents[2];p=D/'chatgpt/ramsey';sys.path.insert(0,str(p));from ramsey_r37_recursive_proof_verify import graph6,independent_fives
rows=[]
for j,line in enumerate(gzip.open(p/'r36_16.g6.gz','rb'),1):
 A=graph6(line);n=len(A)
 if sum(x.bit_count() for x in A)!=66:continue
 F=independent_fives(A);ds=[[i for i,b in enumerate(F) if not a&b] for a in F];Q=n**5;L=max(map(len,ds))**2;z=[0]*len(F)
 for t in range(n**3+1):
  v=[sum(map(z.__getitem__,d)) for d in ds];m=min(v);W=sum(z)
  if W<6*m:break
  r=[max(0,Q-x) for x in v];z=[max(0,old+(sum(map(r.__getitem__,d))-Q//n)//L) for old,d in zip(z,ds)]
 else:raise ValueError(j)
 assert all(6*sum(w for b,w in zip(F,z) if not a&b)>W for a in F);rows.append(dict(record=j,steps=t,W=W,m=m,weights={b:w for b,w in zip(F,z) if w}))
assert len(rows)==39;print(sorted(x['steps'] for x in rows));(D/'voevodsky/results/ramsey_37_weight_rule_replay.json').write_text(json.dumps(rows,indent=2)+'\n')
