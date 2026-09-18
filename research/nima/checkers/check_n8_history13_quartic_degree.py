#!/usr/bin/env python3
"""Finite-field quartic implicit-degree test for history 13, G/alpha4 boundary."""
import itertools,json,random,os
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[3];P=int(os.environ.get('N8_PRIME','1000003'))
# History 13 embedding: G support [1,2,4,5,6,7,8], rotation 0. alpha4=0.
support=[1,2,4,5,6,7,8];Z=np.array([[pow(t,k,P) for k in range(6)] for t in range(1,9)],dtype=np.int64)
def coords(vals):
 a1,a2,a3,a5,a6,a7,a8=vals;a4=0
 G=[[1,a1,(a2+a3)%P,((a2+a3)*a5)%P,(a3*a6)%P,0,0],[0,0,1,a5,a6,a7,a8]]
 C=np.zeros((2,8),dtype=np.int64)
 for j,lab in enumerate(support):C[:,lab-1]=[G[0][j],G[1][j]]
 Y=(C@Z)%P
 # Pivot target columns 1,2.
 d=(int(Y[0,0])*int(Y[1,1])-int(Y[0,1])*int(Y[1,0]))%P
 if d==0:return None
 inv=pow(d,-1,P);Pinv=np.array([[Y[1,1],-Y[0,1]],[-Y[1,0],Y[0,0]]],dtype=np.int64)%P;N=((Pinv@Y)%P*inv)%P
 return [int(N[i,j]) for i in range(2) for j in range(6) if j not in (0,1)]
exps=[]
for d in range(5):
 for inds in itertools.combinations_with_replacement(range(8),d):
  e=[0]*8
  for i in inds:e[i]+=1
  exps.append(tuple(e))
rng=random.Random(271828);rows=[]
while len(rows)<510:
 cv=coords([rng.randrange(1,P) for _ in range(7)])
 if cv is None:continue
 row=[]
 for e in exps:
  v=1
  for i,k in enumerate(e):v=v*pow(cv[i],k,P)%P
  row.append(v)
 rows.append(row)
A=np.array(rows,dtype=np.int64);rank=0;pivots=[]
for c in range(A.shape[1]):
 nz=np.nonzero(A[rank:,c])[0]
 if len(nz)==0:continue
 q=rank+int(nz[0]);A[[rank,q]]=A[[q,rank]];A[rank]=(A[rank]*pow(int(A[rank,c]),-1,P))%P
 ids=np.nonzero(A[:,c])[0];ids=ids[ids!=rank]
 # bounded row loop avoids int64 overflow from broadcasting a 3D product.
 for i in ids:A[i]=(A[i]-int(A[i,c])*A[rank])%P
 pivots.append(c);rank+=1
 if rank==A.shape[1]:break
freecols=[c for c in range(A.shape[1]) if c not in pivots];kernel=[]
if len(freecols)==1:
 f=freecols[0];v=[0]*A.shape[1];v[f]=1
 for r,c in enumerate(pivots):v[c]=(-int(A[r,f]))%P
 kernel=[{'exponents':list(exps[i]),'coefficient_mod_p':int(c if c<=P//2 else c-P)} for i,c in enumerate(v) if c]
# Independent finite-field holdout evaluation of the recovered kernel.
holdout=[]
if len(freecols)==1:
 for _ in range(100):
  cv=coords([rng.randrange(1,P) for _ in range(7)])
  if cv is None:continue
  total=0
  for i,c in enumerate(v):
   if not c:continue
   term=c
   for j,k in enumerate(exps[i]):term=term*pow(cv[j],k,P)%P
   total=(total+term)%P
  holdout.append(total)
counts={str(d):sum(sum(e)<=d for e in exps) for d in range(5)}
checks={'quartic_monomial_count_495':len(exps)==495,'enough_samples':len(rows)>len(exps),'rank_not_above_columns':rank<=len(exps),'unique_quartic_candidate':len(freecols)==1,'quartic_candidate_vanishes_on_holdout':bool(holdout) and all(v==0 for v in holdout)}
out={'schema':'marici.nima.n8-history13-quartic-degree.v1','prime':P,'samples':len(rows),'monomials_degree_le_4':len(exps),'modular_rank':rank,'nullity':len(exps)-rank,'quartic_kernel_support_size':len(kernel),'quartic_kernel':kernel,'holdout_samples':len(holdout),'holdout_nonzero_count':sum(v!=0 for v in holdout),'checks':checks,'passed':all(checks.values()),'interpretation':'Full rank excludes quartic equations exactly. Positive nullity identifies quartic candidates but does not prove they vanish identically until reconstructed and substituted.'};p=ROOT/f'research/nima/results/n8-history13-quartic-degree-{P}.json';p.write_text(json.dumps(out,indent=2)+'\n');
if P==1000003:(ROOT/'research/nima/results/n8-history13-quartic-degree.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
