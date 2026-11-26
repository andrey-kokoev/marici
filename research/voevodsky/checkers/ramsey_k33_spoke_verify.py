"""Separate SAT replay of the three-panel join. Keep only the 36 possible X-X edges and require prescribed single-vertex degrees, three cross-edge counts, triangle-freeness, alpha(X)<=5, and codegree<=4 between a single and each base vertex. The other side need not even be chosen. Validate marked catalogue closure and the positive-control codegree of the negative templates."""
from ramsey_retention_slice import D
from pysat.solvers import Solver
from pysat.card import CardEnc
import itertools,collections,json
from concurrent.futures import ProcessPoolExecutor
P=D.parent;comb=itertools.combinations

def solve(t):
 h,ks,groups=t;S=sum(groups,());E={(i,j):1+n for n,(i,j) in enumerate([(i,j) for i,j in comb(range(9),2) if i//3!=j//3 and not S[i]&S[j]]+[(i,9+i//3) for i in range(9)])};n=len(E);cs=[]
 def card(xs,k,eq):
  nonlocal n
  if k<0 or eq and k>len(xs):return False
  if not xs or not eq and k>=len(xs):return True
  b=(CardEnc.equals if eq else CardEnc.atmost)(xs,k,top_id=n);cs.extend(b.clauses);n=max(n,b.nv);return True
 for i,s in enumerate(S):
  xs=[w for e,w in E.items() if i in e]
  if not card(xs,7-s.bit_count(),True):return 'counts'
 for a,b in comb(range(3),2):
  cnt=[w for (u,v),w in E.items() if (v<9 and u//3==a and v//3==b) or (v>=9 and u//3 in (a,b))];
  if not card(cnt,ks[3-a-b],True):return 'counts'
 for i,s in enumerate(S):
  for u,row in enumerate(h):
   vs=[E[p] for j in range(9) if j!=i and S[j]>>u&1 and (p:=tuple(sorted((i,j)))) in E];
   if not card(vs,4-(s&row).bit_count(),False):return 'common'
 for q in comb(range(9),3):
  es=list(comb(q,2));
  if all(p in E for p in es):cs.append([-E[p] for p in es])
 for q in comb(range(12),6):cs.append([E[p] for p in comb(q,2) if p in E]);
 with Solver(name='cadical195',bootstrap_with=cs) as sl:return 'feasible' if sl.solve() else 'unsat'

def tasks(src):
 for z in src:
  h=[0]*17
  for i,j in z['h']:h[i]|=1<<j;h[j]|=1<<i
  rows=sorted((p['k'],tuple(s)) for p in z['panels'] for s in p['rows']);
  for i,(a,u) in enumerate(rows):
   if a*3>len(z['h'])-11:break
   for j in range(i,len(rows)):
    b,v=rows[j]
    if a+2*b>len(z['h'])-11:break
    for c,w in rows[j:]:
     if a+b+c>len(z['h'])-11:break
     yield h,(a,b,c),(u,v,w)
if __name__=='__main__':
 src=json.loads((P/'ramsey_k33_three_spokes.json').read_text());
 with ProcessPoolExecutor(8) as ex:h=collections.Counter(ex.map(solve,tasks(src),chunksize=64));print(h);assert not h['feasible'];(P/'ramsey_k33_spoke_verify.json').write_text(json.dumps(h)+'\n')
