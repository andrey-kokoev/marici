"""Do not prespecify even which species is first. Seek any chain of three directed contiguous windows with nonempty successive suffix-prefix overlaps. Keep fixed the full sets, typed words, and distinct N legs shared by P,E. Reverse electron word as a chirality control."""
from itertools import product,permutations
from pathlib import Path
import json
D=Path(__file__).resolve().parents[1];T=json.loads((D/'results/pne_body_membership_decoder.json').read_text())['template'];B=[[s for s,t in T.items() if t[i]=='1'] for i in range(3)];legs=lambda w:{frozenset(x) for x in zip(w,w[1:])};ol=lambda u,v:max([0]+[k for k in (1,2) if u[-k:]==v[:k]])
def solve(ew):
 words=['CMC','MCM',ew];choices=[[p[:3] for p in permutations(b) if ''.join(v[0] for v in p[:3])==w] for b,w in zip(B,words)];tests=[];fit=[]
 for W in product(*choices):
  p,n,e=map(legs,W);l,r=p&n,e&n
  if len(l)!=1 or len(r)!=1 or l==r:continue
  arcs={i+j:ol(W['PNE'.index(i)],W['PNE'.index(j)]) for i,j in permutations('PNE',2)};found=[]
  for x,y,z in permutations('PNE'):
   if arcs[x+y] and arcs[y+z]:found.append(x+y+z);fit.append(dict(order=x+y+z,windows=W,overlaps=[arcs[x+y],arcs[y+z]]))
  tests.append(dict(windows=W,arcs=arcs,chains=found))
 return dict(candidates=len(tests),fits=fit,tests=tests)
o={w:solve(w) for w in ['MCC','CCM']};assert [(len(v['fits']),v['fits'][0]['order']) for v in o.values()]==[(1,'PNE'),(1,'ENP')];print([(w,v['candidates'],v['fits']) for w,v in o.items()]);(D/'results/pne_unoriented_join.json').write_text(json.dumps(o,indent=2)+'\n')
