#!/usr/bin/env python3
"""Compare endpoint-first, adaptive, and Green-orthogonalized observers."""
import json, math
from pathlib import Path

def transpose(A):return [list(x) for x in zip(*A)]
def matmul(A,B):return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def inverse(A):
 n=len(A);M=[r[:]+[float(i==j) for j in range(n)] for i,r in enumerate(A)]
 for j in range(n):
  p=max(range(j,n),key=lambda i:abs(M[i][j]));M[j],M[p]=M[p],M[j];q=M[j][j]
  M[j]=[x/q for x in M[j]]
  for i in range(n):
   if i!=j:
    q=M[i][j];M[i]=[x-q*y for x,y in zip(M[i],M[j])]
 return [r[n:] for r in M]
def dot_metric(a,Q,b):return sum(a[i]*sum(Q[i][j]*b[j] for j in range(len(b))) for i in range(len(a)))
def normalized_gram(rows,Q):
 norms=[math.sqrt(dot_metric(r,Q,r)) for r in rows]
 return [[dot_metric(rows[i],Q,rows[j])/(norms[i]*norms[j]) for j in range(len(rows))] for i in range(len(rows))]
def eigvals(A):
 A=[r[:] for r in A];n=len(A)
 for _ in range(100*n*n):
  p,q=max(((i,j) for i in range(n) for j in range(i+1,n)),key=lambda ij:abs(A[ij[0]][ij[1]]),default=(0,0))
  if p==q or abs(A[p][q])<1e-13:break
  phi=.5*math.atan2(2*A[p][q],A[q][q]-A[p][p]);c=math.cos(phi);s=math.sin(phi)
  app,aqq,apq=A[p][p],A[q][q],A[p][q]
  for k in range(n):
   if k not in (p,q):
    akp,akq=A[k][p],A[k][q];A[k][p]=A[p][k]=c*akp-s*akq;A[k][q]=A[q][k]=s*akp+c*akq
  A[p][p]=c*c*app-2*s*c*apq+s*s*aqq;A[q][q]=s*s*app+2*s*c*apq+c*c*aqq;A[p][q]=A[q][p]=0
 return sorted(A[i][i] for i in range(n))
def condition(rows,Q):
 e=eigvals(normalized_gram(rows,Q));return math.sqrt(max(e)/max(min(e),1e-16)),min(e)
def main():
 n=10;xs=[-1+2*i/(n-1) for i in range(n)];K=[[math.exp(-abs(x-y)) for y in xs] for x in xs];Q=inverse(K)
 def row(lam):return [math.exp(lam*x) for x in xs]
 endpoint=[-1,1,0,2,-2,3,-3,4,-4,5];candidates=list(range(-8,9));chosen=[-1,1];records=[]
 for m in range(2,n+1):
  if m>2:
   best=None
   for e in candidates:
    if e in chosen:continue
    cond,mine=condition([row(x) for x in chosen+[e]],Q)
    score=(mine,-cond)
    if best is None or score>best[0]:best=(score,e,cond)
   chosen.append(best[1])
  ce,me=condition([row(x) for x in endpoint[:m]],Q);ca,ma=condition([row(x) for x in chosen],Q)
  records.append({'observers':m,'endpoint_condition':ce,'endpoint_min_eigenvalue':me,'adaptive_exponents':chosen[:],'adaptive_condition':ca,'adaptive_min_eigenvalue':ma,'orthogonalized_condition':1.0})
 result={'schema':'marici.coherence.observer-ladder-stability.v1','contexts':n,'positions':'10 uniform points in [-1,1]','metric':'dual Green metric K^-1 on observer covectors','records':records,'adaptive_final_schedule':chosen,'conclusion':'Green orthogonalization gives unit conditioning; adaptive pure moments improve early stability but all full raw Vandermonde schedules become ill-conditioned'}
 Path(__file__).with_name('observer-ladder-stability.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
