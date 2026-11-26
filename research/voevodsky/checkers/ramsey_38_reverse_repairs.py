"""Keep the root and its two vertex sets fixed. Exhaust one old nonroot edge recoloring, retaining a legal 27-vertex graph. Count enlarged legal cores in the edge window, and possible red links to the seven neighbors. A red link alone does not ensure a legal endpoint."""
import json,itertools,collections
from ramsey_retention_slice import D,decode,check
P=D.parent;z=json.loads((P/'ramsey_38_reverse_seed.json').read_text());g=decode(next(r['graph6'] for r in json.loads(D.read_text()) if (r['l'],r['k'])==(3,8)));C=z['core_mask'];J=z['neighbor_mask'];x=z['root'];F=2**27-1;bits=lambda m:[i for i in range(27) if m>>i&1];old=z['best'][1]['red_core'];block={i:bits(g[i]&old) for i in bits(J)}
def candidates(a):
 ind=[0];e=sum((a[i]&C).bit_count() for i in bits(C))//2
 for i in bits(C):ind.extend([s|1<<i for s in ind if not s&a[i]])
 six=[s for s in ind if s.bit_count()==6];out=[]
 for s in ind:
  if not 45<=e+s.bit_count()<=49 or any(not s&q for q in six):continue
  out.append((s,[j for j in bits(J) if not s&a[j]]))
 return out
base=candidates(g);assert base==[(old,[])];out=[];hist=collections.Counter()
for i,j in itertools.combinations(bits(C|J),2):
 a=g.copy();a[i]^=1<<j;a[j]^=1<<i
 if not check(a,F,3,8):continue
 can=candidates(a);changed=[(s,l) for s,l in can if s!=old];live=[(s,l) for s,l in can if l];out.append(dict(edge=[i,j],candidates=can));hist['legal_flips']+=1;hist['two_or_more']+=len(can)>=2;hist['different']+=bool(changed);hist['live']+=bool(live)
print('baseline support',bits(old),'root blockers',block,'tested',325,'hist',hist);print([(r['edge'],r['candidates']) for r in out if len(r['candidates'])>=2 or any(l for s,l in r['candidates'])][:3]);(P/'ramsey_38_reverse_repairs.json').write_text(json.dumps(dict(support=bits(old),blockers=block,summary=hist,legal=out),indent=1)+'\n')
