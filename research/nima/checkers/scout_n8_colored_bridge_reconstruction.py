#!/usr/bin/env python3
"""Scout colored bridge reconstruction from affine cover chains."""
from pathlib import Path
import json
import sympy as s
R=Path(__file__).resolve().parents[3];D=json.loads((R/'research/nima/results/n8-positroid-bruhat-boundaries.json').read_text());n=8
def F(f,j):q,r=divmod(j-1,n);return f[r]+q*n
def length(f):return sum(F(f,i)>F(f,j) for i in range(1,n+1) for j in range(i+1,i+n+1))
def swap_cover(f,a,c):
 for q in (-1,0,1):
  g=list(f);g[a]=f[c]+q*n;g[c]=f[a]-q*n
  if all(i+1<=g[i]<=i+1+n for i in range(n)) and len({x%n for x in g})==n and length(g)==length(f)+1:return g
 return None
def decompose(f):
 st=[list(f)];w=[]
 while length(st[-1])<12:
  hit=None
  for a in range(n):
   for c in range(a+1,n):
    if all((st[-1][b]-1)%n==b for b in range(a+1,c)):
     g=swap_cover(st[-1],a,c)
     if g is not None:hit=(a,c,g);break
   if hit:break
  assert hit;a,c,g=hit;w.append((a,c));st.append(g)
 return w,st
def perm(C):
 B={(i+1,j+1) for i in range(n) for j in range(i+1,n) if s.det(C[:,[i,j]])!=0};zero={i for i in range(1,n+1) if not any(i in b for b in B)};neck=[]
 for a in range(1,n+1):
  pos=lambda x:(x-a)%n;neck.append(min(B,key=lambda z:sorted(map(pos,z))))
 out=[]
 for z in range(n):
  i=z+1;I=set(neck[z]);J=set(neck[(z+1)%n])
  if i not in I:out.append(i if i in zero else i+n)
  else:j=next(iter(J-I));out.append(j if j>i else j+n)
 return tuple(out)
def build(f):
 w,st=decompose(f);end=st[-1];src=[i for i,x in enumerate(end) if x==i+1+n];C=s.zeros(2,n);C[0,src[0]]=1;C[1,src[1]]=1;colored=[]
 for ri in range(7,-1,-1):
  a,c=w[ri];hits=[]
  for direction in ('c_from_a','a_from_c'):
   for sign in (1,-1):
    Q=C.copy()
    if direction=='c_from_a':Q[:,c]+=sign*(ri+2)*Q[:,a]
    else:Q[:,a]+=sign*(ri+2)*Q[:,c]
    try:g=perm(Q)
    except Exception:continue
    mins=[s.det(Q[:,[i,j]]) for i in range(n) for j in range(i+1,n)]
    if g==tuple(st[ri]):hits.append((direction,sign,all(x>=0 for x in mins),Q))
  positive=[z for z in hits if z[2]];assert len(positive)==1,(ri,a,c,hits,st[ri]);direction,sign,_,C=positive[0];colored.append({'cover_index':ri+1,'pair':[a+1,c+1],'direction':direction,'sign':sign})
 return C,list(reversed(colored)),w,st
rows=[]
for cell in D['cells']:
 C,cw,w,st=build(cell['affine_permutation']);rows.append({'history_index':cell['history_index'],'reconstructed_permutation':list(perm(C)),'colored_bridge_word':cw});print(cell['history_index'],[(z['pair'],z['direction'],z['sign']) for z in cw],flush=True)
checks={'twenty_reconstructed':len(rows)==20,'all_permutations_match':all(tuple(r['reconstructed_permutation'])==tuple(D['cells'][r['history_index']]['affine_permutation']) for r in rows),'eight_colored_bridges_each':all(len(r['colored_bridge_word'])==8 for r in rows)};out={'schema':'marici.nima.n8-colored-bridge-reconstruction-scout.v1','cells':rows,'checks':checks,'passed':all(checks.values()),'claim_boundary':'This reconstructs one positive colored bridge word from each lexicographic affine-cover chain at cyclic start 1. Eight-start atlas generation and symbolic dlog matrices remain next.'};p=R/'research/nima/results/n8-colored-bridge-reconstruction-scout.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'checks':checks,'passed':out['passed']},indent=2));raise SystemExit(0 if out['passed'] else 1)
