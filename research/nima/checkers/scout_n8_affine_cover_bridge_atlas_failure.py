#!/usr/bin/env python3
"""NEGATIVE SCOUT: arbitrary affine-cover reversal does not reconstruct BCFW charts."""
from pathlib import Path
import json,itertools
import sympy as S
R=Path(__file__).resolve().parents[3];data=json.loads((R/'research/nima/results/n8-positroid-bruhat-boundaries.json').read_text());n=8;k=2
def F(f,j):q,r=divmod(j-1,n);return f[r]+q*n
def length(f):return sum(F(f,i)>F(f,j) for i in range(1,n+1) for j in range(i+1,i+n+1))
def swap_cover(f,a,c):
 for q in (-1,0,1):
  g=list(f);g[a]=f[c]+q*n;g[c]=f[a]-q*n
  if all(i+1<=g[i]<=i+1+n for i in range(n)) and len({x%n for x in g})==n and length(g)==length(f)+1:return g
 return None
def decompose(f):
 states=[list(f)];word=[]
 while length(states[-1])<k*(n-k):
  cur=states[-1];hit=None
  for a in range(n):
   for c in range(a+1,n):
    if all((cur[b]-1)%n==b for b in range(a+1,c)):
     g=swap_cover(cur,a,c)
     if g is not None:hit=(a,c,g);break
   if hit:break
  assert hit is not None
  a,c,g=hit;word.append((a,c));states.append(g)
 assert len(word)==8 and all((states[-1][i]-1)%n==i for i in range(n));return word,states
def rotate(f,s):
 # New label i is old affine label i+s, where s is zero-based.
 out=[]
 for i in range(1,n+1):
  v=F(f,i+s)-s
  while v<i:v+=n
  while v>i+n:v-=n
  out.append(v)
 return out
def matrix_chart(f,values,zero=None):
 word,states=decompose(f);end=states[-1];sources=[i for i,x in enumerate(end) if x==i+1+n];assert len(sources)==2
 C=S.zeros(2,n);C[0,sources[0]]=1;C[1,sources[1]]=1
 # Reverse bridge removals. q is counted in the lower-dimensional state.
 for ri in range(7,-1,-1):
  a,c=word[ri];lower=states[ri+1];q=sum(lower[b]==b+1+n for b in range(a+1,c));alpha=S.Integer(0) if zero==ri else S.Integer(values[ri]);C[:,c]=C[:,c]+(-1)**q*alpha*C[:,a]
 return C,word,states
def bases(C):return {(i+1,j+1) for i in range(n) for j in range(i+1,n) if S.det(C[:,[i,j]])!=0}
def perm(C):
 B=bases(C);neck=[]
 for a in range(1,n+1):
  pos=lambda x:(x-a)%n;neck.append(min(B,key=lambda z:sorted(map(pos,z))))
 out=[]
 for z in range(n):
  i=z+1;I=set(neck[z]);J=set(neck[(z+1)%n])
  if i not in I:out.append(i if not any(i in b for b in B) else i+n)
  else:
   j=next(iter(J-I));out.append(j if j>i else j+n)
 return tuple(out)
def unrotate(C,s):
 O=S.zeros(2,n)
 for i in range(n):O[:,(i+s)%n]=C[:,i] # signs irrelevant to matroid/permutation validation
 return O
pr=[2,3,5,7,11,13,17,19];rows=[]
for cell in data['cells']:
 f=cell['affine_permutation'];charts=[];covered=set()
 for s in range(n):
  fr=rotate(f,s);C,w,states=matrix_chart(fr,pr)
  try:got=perm(unrotate(C,s))
  except Exception as e:raise AssertionError(('permutation reconstruction',cell['history_index'],s,fr,C.tolist(),bases(C))) from e
  assert got==tuple(f),(cell['history_index'],s,got,f)
  # Signed construction must make every ordered nonzero minor positive.
  mins=[S.det(C[:,[i,j]]) for i in range(n) for j in range(i+1,n)];assert all(x>=0 for x in mins)
  exposed=[]
  for z in range(8):
   Cz,_,_=matrix_chart(fr,pr,z);g=perm(unrotate(Cz,s))
   if g in {tuple(x) for x in cell['bruhat_facets']}:covered.add(g);exposed.append({'coordinate':z+1,'boundary_permutation':list(g)})
  charts.append({'cyclic_start':s+1,'bridge_word':[[a+1,c+1] for a,c in w],'decorated_identity':states[-1],'exposed_facets':exposed})
 rows.append({'history_index':cell['history_index'],'seed':cell['seed'],'facet_count':cell['bruhat_facet_count'],'covered_facet_count':len(covered),'charts':charts})
checks={'twenty_cells':len(rows)==20,'eight_charts_each':all(len(r['charts'])==8 for r in rows),'all_166_incidences_exposed':sum(r['covered_facet_count'] for r in rows)==166,'every_facet_exposed':all(r['covered_facet_count']==r['facet_count'] for r in rows)};out={'schema':'marici.nima.n8-cyclic-bcfw-chart-atlas.v1','cells':rows,'checks':checks,'passed':all(checks.values()),'construction':'Lexicographically first separated swap that raises affine length by one; reverse swaps act by c_c -> c_c + (-1)^q alpha c_a, with q shifted fixed points between a,c.'};p=R/'research/nima/results/n8-cyclic-bcfw-chart-atlas.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'coverage':[(r['history_index'],r['covered_facet_count'],r['facet_count']) for r in rows],'checks':checks,'passed':out['passed']},indent=2));raise SystemExit(0 if out['passed'] else 1)
