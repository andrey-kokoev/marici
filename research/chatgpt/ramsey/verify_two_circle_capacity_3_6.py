"""Finite certificate that M_2(3,6)=16 for the strict two-circle rule.

A(i,j) iff cos(theta_i-theta_j)+cos(phi_i-phi_j)<-1.

Exact logical test: every individual circle in a valid representation
has A-edge angles strictly between pi/2 and 3pi/2. Partition the circle
into four 90-degree sectors. The sector assignment is a proper 4-coloring;
strict adjacency between neighboring sectors forces a directed acyclic graph.
Conversely, every acyclic assignment can be realized by actual angles.

For each 17-vertex Ramsey(3,6) graph, either no such individual-circle
assignment exists, or a fixed 6-cycle has winding 2 or 4 in EVERY such
assignment. Convexity of {(u,v):cos(u)+cos(v)>1} implies at least one of
the TWO circles must have winding 3 on EVERY A-six-cycle; contradiction.

The seven graph6 strings encode the full McKay catalogue of 17-vertex
triangle-free graphs of independence number 5 (7 isomorphism classes).
The source files are also held in /mnt/data/ramsey36_two_circle_test.py.
"""
from itertools import permutations,combinations

G6 = [
    'P??GaOo`XMGsIcT?pSLaGuA?',
    'P?C?I_h`SDEQQcLAh`dU?tG?',
    'P@oGQA?`ACcdCtDYC]Ah?goC',
    'PG?OSAKccKGiGwJSI[@oWUA_',
    'PGD?OkeO_WAEGQobP_s`cgU?',
    'Ps`A?WIDGeCdGsQEKK?oLL_O',
    'Ps`A?_KChFCiBoQSKCOoXL_O',
]
# A hexagon with graph-invariant nonbalanced winding, if one-circle
# embeddings are possible. Cases 2 and 6 fail already in one circle.
WITNESSES = {
 1:(0,9,5,11,1,16),
 3:(0,4,1,7,12,9),
 4:(0,7,11,15,4,8),
 5:(0,13,6,8,2,16),
 7:(0,1,6,9,11,2),
}
EXPECTED_FEASIBLE=[812,0,886,842,826,0,798]

def decode_graph6(s):
 n=ord(s[0])-63
 assert n==17
 bits=[(ord(ch)-63>>p)&1 for ch in s[1:] for p in range(5,-1,-1)]
 edges=[(i,j) for j in range(1,n) for i in range(j) if bits[j*(j-1)//2+i]]
 return n,edges

def certify(idx,code):
 n,edges=decode_graph6(code)
 adj=[set() for _ in range(n)]
 for i,j in edges:adj[i].add(j);adj[j].add(i)
 assert all(not (adj[i]&adj[j]) for i,j in edges), 'A triangle'
 assert all(any(j in adj[i] for i,j in combinations(s,2)) for s in combinations(range(n),6)), 'B K6'
 if idx in WITNESSES:
  h=WITNESSES[idx]
  assert len(set(h))==6
  assert all(h[(k+1)%6] in adj[h[k]] for k in range(6))
 else:h=None

 order=sorted(range(n),key=lambda x:(-len(adj[x]),x))
 color=[-1]*n
 sector_orderings=[(0,)+p for p in permutations((1,2,3))]
 feasible=0
 seen_windings=set()
 canon4=0

 def test_complete():
  nonlocal feasible,canon4
  canon4+=1
  for sectors in sector_orderings:
   indegree=[0]*n
   succ=[[] for _ in range(n)]
   for i,j in edges:
    delta=(sectors[color[j]]-sectors[color[i]])%4
    if delta==1:
     succ[i].append(j);indegree[j]+=1
    elif delta==3:
     succ[j].append(i);indegree[i]+=1
   q=[v for v in range(n) if indegree[v]==0]
   count=0
   while q:
    v=q.pop();count+=1
    for w in succ[v]:
     indegree[w]-=1
     if indegree[w]==0:q.append(w)
   if count!=n:continue
   feasible+=1
   if h is not None:
    # Each A-edge traverses 1, 2, or 3 quadrants clockwise.
    # Offsets within quadrants telescope over a closed cycle.
    increments=[(sectors[color[h[(k+1)%6]]]-sectors[color[h[k]]])%4 for k in range(6)]
    winding=sum(increments)//4
    assert sum(increments)%4==0
    assert winding in (2,4), f'UNEXPECTED six-cycle winding={winding} graph={idx} sector={sectors} coloring={color}'
    seen_windings.add(winding)

 def assign(k,used):
  if k==n:
   assert used==4
   test_complete()
   return
  v=order[k]
  occupied={color[u] for u in adj[v] if color[u]>=0}
  for c in range(min(used+1,4)):
   if c not in occupied:
    color[v]=c
    assign(k+1,max(used,c+1))
  color[v]=-1

 assign(0,0)
 assert feasible==EXPECTED_FEASIBLE[idx-1],(idx,feasible)
 print(f'Graph {idx}: A edges {len(edges)}, canonical 4-colorings {canon4}, feasible one-circle orders {feasible}, winding witness {h}, allowed winding values {sorted(seen_windings)}')
 return feasible

if __name__=='__main__':
 for idx,code in enumerate(G6,1):certify(idx,code)
 print('CERTIFIED: no 17-node two-circle realization among all seven critical graphs')
 print('16-node existence: separately run verify_two_factor_16_exact.py')
