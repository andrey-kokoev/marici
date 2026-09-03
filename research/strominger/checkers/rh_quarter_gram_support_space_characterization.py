import json
from itertools import combinations
from pathlib import Path

def rectangles(m,n):
 out=[]
 for rm in range(1,1<<m):
  I={i for i in range(m) if rm>>i&1}
  for cm in range(1,1<<n):
   J={j for j in range(n) if cm>>j&1};out.append(frozenset((i,j) for i in I for j in J))
 return out

def rectangular_closure(G):
 for e,f in combinations(G,2):
  i,j=e;k,l=f
  if (i,l) not in G or (k,j) not in G:return False
 return True
upper=frozenset((i,j) for i in range(3) for j in range(3) if i<=j)
diagonal=frozenset((i,i) for i in range(3)); rects=set(rectangles(3,3))
checks={'all_enumerated_rectangles_closed':all(rectangular_closure(r) for r in rects),'upper_interlacing_not_rectangle':upper not in rects and not rectangular_closure(upper),'diagonal_not_rectangle':diagonal not in rects and not rectangular_closure(diagonal),'rectangle_count_3x3':len(rects)==49,'full_rectangle_representable':frozenset((i,j) for i in range(3) for j in range(3)) in rects}
result={'schema':'marici.strominger.rh_quarter_gram_support_space_characterization.v1','status':'passed' if all(checks.values()) else 'failed','theorem':'If U tensor V equals the coordinate matrix space supported on a bipartite graph G, then U and V are coordinate subspaces and G=I x J is a complete bipartite rectangle; conversely every rectangle arises this way.','proof_core':'Every supported matrix unit e_i e_j^T in U tensor V forces e_i in U and e_j in V. Tensor closure then forces every cross unit e_i e_l^T for represented rows i and columns l.','consequence':'A single pair of singular endpoint Gram ranges cannot produce diagonal, triangular, staircase, or other nonrectangular interlacing support.','witnesses':{'upper_triangular_edges':sorted(upper),'diagonal_edges':sorted(diagonal),'rectangle_count_3x3':len(rects)},'checks':checks}
p=Path(__file__).parents[1]/'results'/'rh_quarter_gram_support_space_characterization.json';p.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
