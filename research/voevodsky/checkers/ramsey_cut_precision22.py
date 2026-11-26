"""Distinct unordered pairs per core, union over ALL minimum cuts. Scores based only on individual footprints' crossing counts, not mutual intersection. Lower score first, ties never broken using labels."""
import json,itertools,collections
from ramsey_retention_slice import CAT,D,decode
P=D.parent;cuts=json.loads((P/'ramsey_bisection_square22.json').read_text());A=[decode(l) for l in (CAT/'r37_22.g6').read_text().splitlines()];F=(1<<22)-1;out=[];hist=collections.defaultdict(lambda:[0,0]);tot=hits=0;best=collections.Counter();bests=collections.Counter();nchecks=0
for row,(a,r) in enumerate(zip(A,cuts,strict=True)):
 E=[(1<<i|1<<j,a[i]|a[j]) for i in range(22) for j in range(i) if a[i]>>j&1];baseline=sum(not e&f for (e,b),(f,c) in itertools.combinations(E,2));tot+=baseline;hits+=sum(not x['h'] for x in r['pairs']);score={}
 for m in r['mincuts']:
  X=[(i,(b&~m).bit_count(),(b&m).bit_count()) for i,(e,b) in enumerate(E) if e&m==e];Y=[(j,(c&m).bit_count(),(c&~m).bit_count()) for j,(f,c) in enumerate(E) if not f&m];
  for i,u,v in X:
   for j,w,z in Y:
    key=tuple(sorted((i,j)));s=u+w;possible=(u+z<=11 and w+v<=11);prev=score.get(key,99);score[key]=min(prev,s if possible else 99)
 h=collections.defaultdict(lambda:[0,0]);
 for (i,j),s in score.items():
  ok=int(not E[i][1]&E[j][1]);assert not ok or s<99;h[s][0]+=1;h[s][1]+=ok;hist[s][0]+=1;hist[s][1]+=ok
 elig=[s for s in h if s<99];b=min(elig,default=None)
 if b is not None:nchecks+=h[b][0];best[b]+=1;bests[b]+=bool(h[b][1]);
 out.append(dict(row=row,baseline=baseline,hist=h))
print('baseline',tot,hits,'hist',sorted(hist.items()),'first tier',nchecks,sum(bests.values()));(P/'ramsey_cut_precision22.json').write_text(json.dumps(out)+'\n')
