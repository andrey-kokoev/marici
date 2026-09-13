#!/usr/bin/env python3
"""Exhaustive noisy Bayesian placement of a limited movable-cutoff budget."""
import itertools,json,math
from pathlib import Path

def tr(A):return [list(x) for x in zip(*A)]
def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def inv(A):
 n=len(A);M=[r[:]+[float(i==j) for j in range(n)] for i,r in enumerate(A)]
 for j in range(n):
  p=max(range(j,n),key=lambda i:abs(M[i][j]));M[j],M[p]=M[p],M[j];q=M[j][j];M[j]=[x/q for x in M[j]]
  for i in range(n):
   if i!=j:
    q=M[i][j];M[i]=[x-q*y for x,y in zip(M[i],M[j])]
 return [r[n:] for r in M]
def posterior_trace(A,prior_var,noise2):
 n=len(prior_var);C=[[prior_var[i] if i==j else 0.0 for j in range(n)] for i in range(n)];AC=mm(A,C);S=mm(AC,tr(A))
 for i in range(len(S)):S[i][i]+=noise2
 gain=mm(mm(C,tr(A)),inv(S));post=[[C[i][j]-mm(gain,AC)[i][j] for j in range(n)] for i in range(n)]
 return sum(post[i][i] for i in range(n))
def main():
 n=12;rho=.8;noise=.1
 tails=[[0.0 if j<i else rho**(j-i) for j in range(n)] for i in range(n)]
 scenarios=[]
 for name,prior in [('uniform',[1.0]*n),('right_heavy',[1+.15*i for i in range(n)])]:
  rows=[]
  for m in range(1,7):
   best=min(((posterior_trace([tails[i] for i in S],prior,noise**2),S) for S in itertools.combinations(range(n),m)),key=lambda x:x[0])
   uniform=tuple(round(i*(n-1)/(m-1)) for i in range(m)) if m>1 else (n//2,)
   rows.append({'budget':m,'optimal_cutoffs':best[1],'optimal_posterior_trace':best[0],'uniform_cutoffs':uniform,'uniform_posterior_trace':posterior_trace([tails[i] for i in uniform],prior,noise**2)})
  scenarios.append({'prior':name,'variances':prior,'rows':rows})
 result={'schema':'marici.coherence.limited-cutoff-observer-budget.v1','contexts':n,'rho':rho,'noise_sd':noise,'scenarios':scenarios,'method':'exhaustive A-optimal design minimizing posterior trace','conclusion':'uniform priors spread cutoffs to reduce overlap; right-heavy priors concentrate cutoffs at high-variance states'}
 Path(__file__).with_name('limited-cutoff-observer-budget.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
