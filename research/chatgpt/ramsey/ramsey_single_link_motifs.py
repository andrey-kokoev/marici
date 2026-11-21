"""Classify the160 small endpoint links of Hall191 switches up to exact graph isomorphism. Transfer independent-five templates from one representative per motif."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json
from ramsey_hall_center_conjecture import decode
from ramsey_defect_link_constructor import link_defects,independent_sets
D=Path(__file__).parent;A=decode((D/'pauli-realization-catalogues'/'r37_22.g6').read_bytes().splitlines()[190]);moves=json.loads((D/'ramsey_block_selection_repair_rules.json').read_text())[-1]['switches']
def invariant(G):
 n=len(G);R=[[(G[i]>>j&1,(G[i]&G[j]).bit_count()) for j in range(n)] for i in range(n)];S=[tuple(sorted(row)) for row in R];return R,S,tuple(sorted(S))
def isomorphism(G,H):
 if len(G)!=len(H):return None
 R,S,key=invariant(G);T,Q,other=invariant(H)
 if key!=other:return None
 n=len(G)
 def search(mapping,used):
  if len(mapping)==n:return mapping
  options=[]
  for i in range(n):
   if i in mapping:continue
   candidates=[j for j in range(n) if j not in used and S[i]==Q[j] and all(R[i][a]==T[j][b] for a,b in mapping.items())]
   if not candidates:return None
   options.append((len(candidates),i,candidates))
  _,i,candidates=min(options)
  for j in candidates:
   result=search(mapping|{i:j},used|{j})
   if result is not None:return result
  return None
 result=search({},set())
 if result is not None:assert all((G[i]>>j&1)==(H[result[i]]>>result[j]&1) for i,j in combinations(range(n),2))
 return result
motifs=[];links=[]
for i,s in enumerate(moves):
 _,records=link_defects(A,[s])
 for rec in records:
  vertices=rec['link_vertices'];G=[sum(1<<j for j,w in enumerate(vertices) if A[v]>>w&1) for v in vertices];hit=None
  for t,M in enumerate(motifs):
   mapping=isomorphism(M['adjacency'],G)
   if mapping is not None:hit=t;break
  if hit is None:
   hit=len(motifs);mapping={j:j for j in range(len(G))};sets=list(independent_sets(G,(1<<len(G))-1,5));motifs.append({'adjacency':G,'five_sets':sets,'count':0,'degree_sequence':sorted(n.bit_count() for n in G),'edges':sum(n.bit_count() for n in G)//2})
  motif=motifs[hit];motif['count']+=1;constructed={sum(1<<vertices[mapping[j]] for j in range(len(G)) if mask>>j&1) for mask in motif['five_sets']};actual=set(independent_sets(A,sum(1<<v for v in vertices),5));assert constructed==actual;links.append({'candidate':i,'deleted_edge':rec['deleted_edges'][0],'vertices':vertices,'motif':hit,'representative_to_link':mapping})
result={'motifs':motifs,'links':links};(D/'ramsey_single_link_motifs.json').write_text(json.dumps(result,indent=2)+'\n');print('motif count',len(motifs))
for i,m in enumerate(motifs):print(i,'n',len(m['adjacency']),'edges',m['edges'],'degrees',m['degree_sequence'],'five sets',len(m['five_sets']),'occurrences',m['count'])
