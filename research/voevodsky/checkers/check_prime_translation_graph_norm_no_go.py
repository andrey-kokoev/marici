#!/usr/bin/env python3
"""Audit divergence of the absolute prime-translation graph energy."""
import json,math
from pathlib import Path

def mangoldt_table(N):
 out=[0.0]*(N+1);prime=[True]*(N+1)
 for p in range(2,N+1):
  if not prime[p]:continue
  for k in range(p*p,N+1,p):prime[k]=False
  q=p
  while q<=N:out[q]=math.log(p);q*=p
 return out

def main():
 cutoffs=[10,100,1000,10000,100000,1000000];vm=mangoldt_table(cutoffs[-1]);s=0.0;vals=[];j=0
 for n in range(2,cutoffs[-1]+1):
  s+=vm[n]/math.sqrt(n)
  if n==cutoffs[j]:vals.append(s);j+=1
  if j==len(cutoffs):break
 assert all(vals[i+1]>vals[i] for i in range(len(vals)-1))
 # For any unit vector f, ||T_log(n) f||^2=1, so graph energy equals this sum.
 result={'schema':'marici.voevodsky.prime-translation-graph-norm-no-go.v1','cutoffs':cutoffs,'partial_weight_sums':vals,'strictly_increasing':True,'analytic_fact':'sum Lambda(n)/sqrt(n) diverges','unitary_translation_norm':'||T_log(n) f||_2 = ||f||_2','absolute_graph_energy':'||f||^2 sum Lambda(n)/sqrt(n)','finite_energy_vectors':'only f=0','rejected_completion':'independent square-summation of all prime translation channels','surviving_route':'joint regularization/cancellation of gamma and prime sectors before completion'}
 out=Path(__file__).parents[1]/'results'/'prime_translation_graph_norm_no_go.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
