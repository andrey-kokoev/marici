"""Direct projected integer deficit update. Variables are two-step test classes. Rows are distinct attachment requirements (vectors of class multiplicities); keep frequencies in gradient. No input certificates. Verify expanded final weights independently on original sets."""
import sys,gzip,json,collections
from pathlib import Path
root=Path(__file__).resolve().parents[2];p=root/'chatgpt/ramsey';sys.path.insert(0,str(p));from ramsey_r37_recursive_proof_verify import graph6,independent_fives
out=[]
for j,line in enumerate(gzip.open(p/'r36_16.g6.gz','rb'),1):
 A=graph6(line);n=len(A)
 if sum(t.bit_count() for t in A)!=66:continue
 mode='walk2' if '--walk2' in sys.argv else 'sum' if '--sum' in sys.argv else 'hist';F=independent_fives(A);D=[[h for h,b in enumerate(F) if not a&b] for a in F];profiles=[sum(len(D[h]) for h in v) if mode=='walk2' else (len(v),sum(len(D[h]) for h in v)) if mode=='sum' else tuple(sorted(len(D[h]) for h in v)) for v in D];keys=sorted(set(profiles));labels=[keys.index(v) for v in profiles];size=[labels.count(k) for k in range(len(keys))];rc=collections.Counter(tuple(sorted(collections.Counter(labels[h] for h in d).items())) for d in D);rows=list(rc);cols=[[(i,c*rc[v]) for i,v in enumerate(rows) for k,c in v if k==h] for h in range(len(keys))];Q=n**5;L=max(map(len,D))**2;z=[0]*len(keys)
 for t in range(n**3+1):
  cov=[sum(z[h]*c for h,c in v) for v in rows];m=min(cov);W=sum(a*b for a,b in zip(size,z))
  if W<6*m:break
  deficit=[max(0,Q-v) for v in cov];z=[max(0,old+(sum(deficit[i]*c for i,c in col)-size[h]*(Q//n))//(size[h]*L)) for h,(old,col) in enumerate(zip(z,cols))]
 else:
  if mode!='hist':out.append(dict(record=j,testClasses=len(keys),attachmentRows=len(rows),steps=-1));continue
  raise ValueError((j,'no certificate within cap'))
 assert W==sum(z[h] for h in labels) and m==min(sum(z[labels[h]] for h,b in enumerate(F) if not a&b) for a in F);out.append(dict(record=j,testClasses=len(keys),attachmentRows=len(rows),steps=t,W=W,m=m,weights=[(k,v) for k,v in zip(keys,z) if v]))
assert len(out)==39;print(sorted(x['steps'] for x in out));print([(x['record'],x['testClasses'],x['attachmentRows'],x['steps']) for x in out if x['testClasses']!=x['attachmentRows']]);(root/(f'voevodsky/results/ramsey_37_{mode}_generator.json' if mode!='hist' else 'voevodsky/results/ramsey_37_class_weight_generator.json')).write_text(json.dumps(out,indent=2)+'\n')
