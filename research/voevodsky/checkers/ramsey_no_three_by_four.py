"""Global K3,4 exclusion using only the degree sequences around a marked vertex in the two sparsest 21-vertex (3,7) layers. Suppose three blue roots have four common red neighbors. By codegree <=4 the three private red fours are disjoint. Their union P is blue to the four common vertices, hence (3,5)-legal. Its red degrees are 3..4 by R(3,4)=9. The common blue graph for any two roots is a 21-type with e=44+k, k the cross edges between their private sets. Thus each of the three cross counts is >=7. The third root has degree four in this 21-type; its neighbors there have degrees 8-d_P, i.e. four or five, with at most two fives because their sum of P-degrees is >=14. Test k=7 directly. Then if each k>=8, e(P)<=24 forces all k=8, all P-degrees four. Now test e=52 with four neighbors of degree four."""
import itertools,collections,json,gzip
from ramsey_retention_slice import CAT,D,decode
P=D.parent;cnt=collections.Counter();hist=collections.Counter();hits=[];trans=bytes((x-63).bit_count() if 63<=x<127 else 0 for x in range(256))
for ix,l in enumerate(gzip.open(CAT.parent/'r37_21.g6.gz','rb')):
 l=l.strip();e=sum(l[1:].translate(trans));hist[e]+=1
 if e>52:continue
 a=decode(l.decode());assert len(a)==21 and sum(x.bit_count() for x in a)==2*e
 for r,v in enumerate(a):
  if v.bit_count()!=4:continue
  nb=sorted(a[j].bit_count() for j in range(21) if v>>j&1);cnt[e,tuple(nb)]+=1
  if (e==51 and max(nb)<=5 and min(nb)>=4 and nb.count(5)<=2) or (e==52 and nb==[4]*4):hits.append((e,ix,r,nb))
assert min(hist)==51 and not hits;g=decode(json.loads((P/'ramsey_incidence35_endpoint.json').read_text())['graph6']);ctrl=collections.Counter((g[i]&g[j]&g[k]).bit_count() for i,j,k in itertools.combinations(range(35),3));assert max(ctrl)<=3;out=dict(edge_hist=hist,degree4_marks={str(k):v for k,v in cnt.items()},hits=hits,known_triple_common_red=ctrl);print({k:hist[k] for k in (51,52)},hits,ctrl);(P/'ramsey_no_three_by_four.json').write_text(json.dumps(out)+'\n')
