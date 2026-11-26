"""Count labeled root positions in each stored catalogue record, not automorphism orbits. sigma is the core deficit M_prev - (n-1-d)."""
import collections,json,gzip
from ramsey_retention_slice import D,CAT,decode
M={3:5,4:8,5:13,6:17,7:22,8:27,9:35};out=[]
for k in range(4,10):
 p=next(CAT.glob(f'r3{k}_{M[k]}.g6*'),None);hist=collections.Counter();cnt=0
 if p:f=(gzip.open(p,'rt') if p.suffix=='.gz' else p.open());lines=(s.strip() for s in f)
 else:lines=[next(r['graph6'] for r in json.loads(D.read_text()) if r['l']==3 and r['k']==k)]
 for line in lines:
  a=decode(line);assert len(a)==M[k];cnt+=1
  for x in a:
   d=x.bit_count();sigma=M[k-1]-(len(a)-1-d);assert sigma>=0;hist[d,sigma]+=1
 if p:f.close()
 out.append(dict(k=k,source=str(p.name) if p else D.name,graphs=cnt,pairs=[dict(d=d,sigma=s,roots=v) for (d,s),v in sorted(hist.items())]));print(k,cnt,sum(hist.values()),sorted(hist),flush=True)
(D.parent/'ramsey_root_deficit_census.json').write_text(json.dumps(out,indent=1)+'\n')
