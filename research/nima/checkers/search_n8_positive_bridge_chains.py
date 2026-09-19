#!/usr/bin/env python3
"""Search positive single-column bridge chains for the twenty n=8 cells."""
from pathlib import Path
import json,itertools,collections
R=Path(__file__).resolve().parents[3];D=json.loads((R/'research/nima/results/n8-positroid-bruhat-boundaries.json').read_text());n=8
def F(f,j):q,r=divmod(j-1,n);return f[r]+q*n
def length(f):return sum(F(f,i)>F(f,j) for i in range(1,n+1) for j in range(i+1,i+n+1))
def det(C,i,j):return C[0][i]*C[1][j]-C[0][j]*C[1][i]
def perm(C):
 B={(i+1,j+1) for i in range(n) for j in range(i+1,n) if det(C,i,j)!=0};zero={i for i in range(1,n+1) if not any(i in b for b in B)}
 if not B:return None
 neck=[]
 for a in range(1,n+1):
  pos=lambda x:(x-a)%n;neck.append(min(B,key=lambda z:sorted(map(pos,z))))
 out=[]
 for z in range(n):
  i=z+1;I=set(neck[z]);J=set(neck[(z+1)%n])
  if J==I:out.append(i+n if i in I else i)
  elif i not in I:return None
  else:
   d=J-I
   if len(d)!=1:return None
   j=next(iter(d));out.append(j if j>i else j+n)
 return tuple(out)
def positive(C):return all(det(C,i,j)>=0 for i in range(n) for j in range(i+1,n))
targets={tuple(c['affine_permutation']):c['history_index'] for c in D['cells']};found={};front={}
for src in itertools.combinations(range(n),2):
 C=[[0]*n for _ in range(2)];C[0][src[0]]=1;C[1][src[1]]=1;f=tuple(i+1+n if i in src else i+1 for i in range(n));front[f]=(C,[],[src[0]+1,src[1]+1])
for depth in range(8):
 nxt={}
 for f,(C,w,identity_sources) in front.items():
  fixed=lambda b:(f[b]-1)%n==b
  for a in range(n):
   for c in range(a+1,n):
    if not all(fixed(b) for b in range(a+1,c)):continue
    for source,dest in ((a,c),(c,a)):
     for sign in (1,-1):
      Q=[row[:] for row in C]
      for rr in range(2):Q[rr][dest]+=sign*(depth+2)*Q[rr][source]
      if not positive(Q):continue
      g=perm(Q)
      if g is None or length(g)!=length(f)-1:continue
      nw=w+[{'source':source+1,'destination':dest+1,'sign':sign}]
      if g not in nxt:nxt[g]=(Q,nw,identity_sources)
      if g in targets and g not in found:found[g]=(Q,nw,identity_sources)
 front=nxt;print('depth',depth+1,'states',len(front),'targets',len(found),flush=True)
rows=[]
for c in D['cells']:
 f=tuple(c['affine_permutation']);hit=found.get(f);rows.append({'history_index':c['history_index'],'found':hit is not None,'decorated_identity_sources':None if hit is None else hit[2],'bridge_word':None if hit is None else hit[1]})
checks={'twenty_targets':len(rows)==20,'all_targets_bridge_reconstructed':all(r['found'] for r in rows),'eight_bridges_each':all(len(r['bridge_word'])==8 for r in rows if r['found'])};out={'schema':'marici.nima.n8-positive-bridge-chain-search.v1','cells':rows,'search_frontier_size':len(front),'checks':checks,'passed':all(checks.values()),'claim_boundary':'Chains use positive sample shifts and affine-length descent. Symbolic parameters, source lexicographic tie-breaking, cyclic starts, and complete facet exposure remain separate.'};p=R/'research/nima/results/n8-positive-bridge-chain-search.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'found_histories':[r['history_index'] for r in rows if r['found']],'checks':checks,'passed':out['passed']},indent=2));raise SystemExit(0 if out['passed'] else 1)
