"""Lift each integer dual witness to every peak schedule it certifies, using exact scalar sums. A candidate peak is safe for that exclusion if no positive-margin interval contains it. Count union of product sets via inclusion-exclusion; count schedules, not distinct profiles."""
import gzip,json,itertools,math,sys
from pathlib import Path
from collections import Counter
root=Path(__file__).resolve().parents[2];p=root/'chatgpt/ramsey';sys.path.insert(0,str(p));from ramsey_r37_recursive_proof_verify import graph6,independent_fives
D=root/'voevodsky/results';prior=json.loads((D/'ramsey_37_triple_peak_refit.json').read_text());rows={};keys=set()
for j,line in enumerate(gzip.open(p/'r36_16.g6.gz','rb'),1):
 if j not in prior['records']:continue
 A=graph6(line);F=independent_fives(A);ds=[[h for h,b in enumerate(F) if not a&b] for a in F];K=[(len(d),sum(len(ds[h]) for h in d)) for d in ds];counts=Counter(K);keys.update(K)
 for t,d in zip(F,ds):
  hits=Counter(K[h] for h in d);rows[j,t]={k:6*hits[k]-n for k,n in counts.items()}
branches={d:sorted(v for i,v in keys if i==d) for d in sorted({i for i,v in keys})};boxes=[];details=[]
for proof in prior['fixedProof']:
 col=Counter()
 for rec,t,w in proof['multipliers']:
  assert w>0
  for k,v in rows[rec,t].items():col[k]+=v*w
 box={};bad={}
 for d,values in branches.items():
  pp=[0];
  for v in values:pp.append(pp[-1]+col[d,v])
  # largest interval sum containing position i: best allowed right endpoint minus best left prefix
  safe={v for i,v in enumerate(values) if max(pp[i+1:])-min(pp[:i+1])<=0};box[d]=safe
  if len(safe)<len(values):bad[d]=[v for v in values if v not in safe]
 assert all(s in box[d] for d,s in proof['peaks']);boxes.append(box);details.append(dict(excluded=math.prod(map(len,box.values())),escapePositions=bad))
total=math.prod(map(len,branches.values()));union=sum((-1)**(k+1)*math.prod(len(set.intersection(*(b[d] for b in sub))) for d in branches) for k in range(1,len(boxes)+1) for sub in itertools.combinations(boxes,k));summary=dict(branches=branches,total=total,eliminated=union,remaining=total-union,proofs=details);print('counts',len(keys),len(branches),total,union,(total-union)/total);print([(v['excluded']/total,{d:len(s) for d,s in v['escapePositions'].items()}) for v in details]);(D/'ramsey_37_peak_proof_ranges.json').write_text(json.dumps(summary,indent=2)+'\n')
