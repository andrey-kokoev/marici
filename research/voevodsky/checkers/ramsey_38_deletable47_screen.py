"""Batch the exact six-clique screen on canonical 47-edge augmentation output. Supply compiled ramsey_38_six_screen.rs executable as argv[1]."""
import sys,json,gzip,subprocess,collections
from pathlib import Path
P=Path(__file__).resolve().parents[1]/'results';src=json.load(gzip.open(P/'ramsey_38_layer47_deletable.json.gz'));counts=collections.Counter();passes=[];E=[(u,v) for v in range(20) for u in range(v)]
for start in range(0,len(src),2048):
 batch=src[start:start+2048];rows=[];degrees=[]
 for h in batch:
  m=int(h,16);a=[0]*20
  for k,(u,v) in enumerate(E):
   if m>>k&1:a[u]|=1<<v;a[v]|=1<<u
  degrees.append(min(x.bit_count() for x in a));rows.append(' '.join(map(str,a)))
 vals=list(map(int,subprocess.check_output([sys.argv[1]],input='\n'.join(rows)+'\n',text=True).split()));assert len(vals)==len(batch)
 for h,d,val in zip(batch,degrees,vals):
  counts[d,val]+=1
  if val:passes.append([h,d])
print(counts);(P/'ramsey_38_deletable47_sixes.json').write_text(json.dumps(dict(counts={str(k):v for k,v in counts.items()},survivors=passes))+'\n')
