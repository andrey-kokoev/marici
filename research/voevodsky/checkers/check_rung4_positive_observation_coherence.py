#!/usr/bin/env python3
"""Audit the rung-3 observation / rung-4 positive-coherence model."""
import json
from fractions import Fraction
from pathlib import Path

def q(A,x):return sum(x[i]*A[i][j]*x[j] for i in range(len(x)) for j in range(len(x)))
def restrict(A):return [row[:-1] for row in A[:-1]]
def main():
 r=Fraction(-3,5)
 G3=[[Fraction(1) if i==j else r for j in range(3)] for i in range(3)]
 G=[[[Fraction(1)]],restrict(G3),G3]
 # Rung-4 cells: extension by zero makes successor observation exactly old observation.
 cells=[]
 for k in (1,2):
  probes=[[Fraction(i+1) for i in range(k)], [Fraction((-1)**i) for i in range(k)]]
  ok=all(q(G[k],[*x,Fraction(0)])==q(G[k-1],x) for x in probes)
  assert ok;cells.append({'from_rank':k,'to_rank':k+1,'restriction_coherent':ok})
 # Rank 1 and 2 are positive; rank 3 has negative all-ones direction.
 assert q(G[0],[1])>0
 assert q(G[1],[1,1])>0 and q(G[1],[1,-1])>0
 bad=q(G[2],[1,1,1]);assert bad<0
 # Nonfaithful hostile: coherent positive observations x -> x_1^2 ignore all later coordinates.
 invisible=[0,1,0,0];assert invisible[0]**2==0 and any(invisible[1:])
 result={'schema':'marici.voevodsky.rung4-positive-observation-coherence.v1','rung3':'O_k(x)=x* G_k x is the observation point at finite packet rank k','rung4':'O_(k+1)(u_k x)=O_k(x), together with cone admission O_k>=0','successor_cells':cells,'signed_coherence_hostile':{'all_cells_commute':True,'first_cone_failure_rank':3,'negative_witness':[1,1,1],'negative_value':str(bad)},'nonfaithful_positive_hostile':{'rule':'O_k(x)=x_1^2','positive_and_successor_coherent':True,'invisible_nonzero_vector':invisible},'rh_contract':['source identity identifies O_k with the Gaussian Weil form','cone admission holds at every finite rung','successor restriction cells commute','Gaussian translate union is dense and observation is continuous/faithful at completion'],'conclusion':'RH is represented by all-rung cone-valued rung-4 observation coherence only after source identity and faithful completion; signed coherence alone survives the negative hostile.'}
 out=Path(__file__).parents[1]/'results'/'rung4_positive_observation_coherence.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
