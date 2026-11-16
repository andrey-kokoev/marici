"""Independent standard-library checks of the explicit witnesses and rejections.
Run exact_repair.cpp separately to replay exhaustive generation/completeness.
"""
from pathlib import Path
from itertools import combinations
from collections import Counter
from math import comb
import json, hashlib
P=Path(__file__).parent
rows=(P/'exoo_r310_39_matrix.txt').read_text().split();n=len(rows)
assert n==39 and all(len(s)==n and set(s)<=set('01') for s in rows)
assert all(rows[i][i]=='0' for i in range(n))
assert all(rows[i][j]==rows[j][i] for i in range(n) for j in range(n))
# The author's two-colour matrix uses zero for the sparse triangle-free colour.
E={e for e in combinations(range(n),2) if rows[e[0]][e[1]]=='0'}
def adj(edges,n):
 a=[0]*n
 for u,v in edges:a[u]|=1<<v;a[v]|=1<<u
 return a
def enum(a,k):
 out=[]
 def rec(q,left,m):
  if left==0:out.append(m);return
  while q.bit_count()>=left:
   b=q&-q;q-=b;v=b.bit_length()-1;rec(q&~a[v],left-1,m|b)
 rec((1<<len(a))-1,k,0);return out
a=adj(E,n);assert all(not a[u]&a[v] for u,v in E)
assert len(E)==167 and Counter(x.bit_count() for x in a)=={6:1,8:14,9:24}
assert not enum(a,10);nine=enum(a,9);assert len(nine)==4511
assert a==list(map(int,(P/'exoo39.adj').read_text().split()))
# Check each small witness family: every member has exactly the deleted edge,
# and the intersection is exactly that edge's endpoints.
locks=json.loads((P/'locked_edge_certificates.json').read_text());assert len(locks)==41
for item in locks:
 e=tuple(item['edge']);assert e in E
 intersection=set(range(n))
 for W in item['witnesses']:
  assert len(W)==len(set(W))==10
  W=set(W);intersection&=W
  assert {f for f in E if set(f)<=W}=={e}
 assert intersection==set(e)
counts=[];rejections=0
for r in range(4):
 stats=json.loads((P/f'radius{r}.json').read_text())
 assert stats['complete'] is True and stats['cases']==comb(167,r)
 assert stats['valid39']==stats['valid40']==0
 seen=set();num=0
 for line in (P/f'radius{r}_rejections.jsonl').read_text().splitlines():
  data=json.loads(line);D={tuple(e) for e in data['deleted']};B={tuple(e) for e in data['added']}
  assert len(D)==r and len(B)==r+4 and D<=E and not B&E
  F=(E-D)|B;assert len(F)==171;b=adj(F,n)
  assert all(not b[u]&b[v] for u,v in F)
  assert Counter(x.bit_count() for x in b)=={8:9,9:30}
  S={v for v in range(n) if b[v].bit_count()==8}
  assert not any(u in S and v in S for u,v in F)
  I=set(data['independent10']);assert len(I)==10
  assert not any(u in I and v in I for u,v in F)
  key=(tuple(sorted(D)),tuple(sorted(B)));assert key not in seen;seen.add(key);num+=1
 assert num==stats['independent_defect_sets']
 rejections+=num;counts.append(stats)
assert rejections==5211
# Recheck the best completed bounded 39-vertex walk, not as a Ramsey-40 witness.
other={}
for fn in ['seed39_171.adj','priority1_best39.adj','regular40_seed.adj','regwalk2_best.adj','exoomip_candidate0.adj','exoomip_candidate1.adj']:
 b=list(map(int,(P/fn).read_text().split()));m=len(b)
 assert all(not b[v]>>v&1 for v in range(m))
 assert all(bool(b[i]>>j&1)==bool(b[j]>>i&1) for i,j in combinations(range(m),2))
 assert all(not b[i]&b[j] for i,j in combinations(range(m),2) if b[i]>>j&1)
 inds=enum(b,10)
 info={'vertices':m,'edges':sum(x.bit_count() for x in b)//2,'independent10':len(inds)}
 if m==39:
  assert not inds;S={v for v in range(m) if b[v].bit_count()==8};mask=sum(1<<v for v in S)
  info['defect_vertices']=sorted(S)
  info['defect_internal_edges']=sum(1 for u,v in combinations(S,2) if b[u]>>v&1)
  info['independent9_outside_defect_set']=sum(not (I&mask) for I in enum(b,9))
  info['seed_edges_removed']=sum(not (b[u]>>v&1) for u,v in E)
 else:assert all(x.bit_count()==9 for x in b)
 other[fn]=info
summary={'seed_vertices':39,'seed_edges':167,'seed_independent9':4511,'locked_edges':len(locks),'total_deletion_cases':sum(s['cases'] for s in counts),'total_degree_profiles':sum(s['degree_profiles'] for s in counts),'explicit_independent10_rejections':rejections,'per_radius':counts,'candidate_checks':other,'source_sha256':hashlib.sha256((P/'exoo_r310_39_matrix.txt').read_bytes()).hexdigest(),'scope':'Witness checks independent; exhaustive-generation completeness requires the supplied enumeration argument and C++ replay.'}
(P/'verified_summary.json').write_text(json.dumps(summary,indent=2));print(json.dumps(summary,indent=2))
