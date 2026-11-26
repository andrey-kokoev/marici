"""At best feasible leakage score per pair, distinguish direct endpoint contacts from length-two bridges. Detail all score-two pairs in one optimal cut each."""
import json,itertools,collections
from ramsey_retention_slice import CAT,D,decode
P=D.parent;F=(1<<22)-1;A=[decode(l) for l in (CAT/'r37_22.g6').read_text().splitlines()];cuts=json.loads((P/'ramsey_bisection_square22.json').read_text());out=[];h=collections.defaultdict(collections.Counter);detail=[];motifs=collections.defaultdict(collections.Counter)
def bits(s):return [i for i in range(22) if s>>i&1]
for r,a in zip(cuts,A,strict=True):
 E=[(1<<i|1<<j,a[i]|a[j]) for i in range(22) for j in range(i) if a[i]>>j&1];score={}
 for m in r['mincuts']:
  X=[(i,b&~m,b&m) for i,(e,b) in enumerate(E) if e&m==e];Y=[(j,c&m,c&~m) for j,(f,c) in enumerate(E) if not f&m]
  for i,u,v in X:
   for j,w,z in Y:
    if u.bit_count()+z.bit_count()>11 or w.bit_count()+v.bit_count()>11:continue
    s=(u|w).bit_count();k=tuple(sorted((i,j)))
    if k not in score or s<score[k][0]:score[k]=(s,m)
 for (i,j),(s,m) in score.items():
  e,b=E[i];f,c=E[j];direct=bool(b&f);mid=(b&c)&~(e|f);kind=('direct+middle' if mid else 'direct') if direct else ('middle' if mid else 'square');h[s][kind]+=1
  if mid and not direct:
   bridges=[(i,j) for t in bits(mid) for i in bits(e&a[t]) for j in bits(f&a[t])];pentagon=any((i==k)^(j==l) for (i,j),(k,l) in itertools.combinations(bridges,2));motifs[s][f'{len(bridges)} bridges, C5={pentagon}']+=1
  if s==2:
   side=m if m&e else F^m;detail.append(dict(row=r['row'],e=bits(e),f=bits(f),leaks=[bits(b&~side),bits(c&side)],intersection=bits(b&c),kind=kind,cut=bits(side),paths=[[i,t,j] for t in bits(mid) for i in bits(e&a[t]) for j in bits(f&a[t])]))
print(dict(sorted(h.items())));print([d for d in detail if d['kind']!='square']);(P/'ramsey_cut_collision22.json').write_text(json.dumps(dict(hist=h,score2=detail,indirect_motifs=motifs))+'\n')
