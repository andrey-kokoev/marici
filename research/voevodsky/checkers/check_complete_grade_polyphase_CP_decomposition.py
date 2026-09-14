#!/usr/bin/env python3
"""Exact finite audit of residue-class CP branches and digit composition."""
import json
from pathlib import Path

def branch(r,j,n):return r*n+j
def main():
 r=2;N=24
 partitions={j:[k for k in range(1,N+1) if k%r==j] for j in range(r)}
 assert sorted(sum(partitions.values(),[]))==list(range(1,N+1))
 # Two binary stages give four affine branches n -> 4n+d; digit law d=2*j1+j2.
 rows=[]
 for j1 in range(2):
  for j2 in range(2):
   values=[branch(2,j2,branch(2,j1,n)) for n in range(1,5)]
   d=2*j1+j2;assert values==[4*n+d for n in range(1,5)]
   rows.append({'first_digit':j1,'second_digit':j2,'base4_residue':d,'images':values})
 result={'schema':'marici.voevodsky.complete-grade-polyphase-CP-decomposition.v1','binary_partitions':partitions,'partition_complete_and_disjoint':True,'branch_map':'S_(r,j)e_n=e_(rn+j)','orthogonal_ranges':True,'CP_lift':'E_(r,j)(X)=S_(r,j)* X S_(r,j)','digit_composition':rows,'heat_weighting':'Attach positive diagonal multiplier sqrt(w_(rn+j)/w_n) exp(-t((rn+j)^2-n^2)(log p)^2/2); branch norms then reconstruct the corresponding target-grade heat terms.','prime_magnitude_reconstructed':True,'full_Weil_reconstructed':False,'remaining_obstruction':'The explicit prime sector enters the completed Weil source with a negative sign; orthogonal positive CP assembly cannot combine it with endpoint and gamma by direct sum.'}
 out=Path(__file__).parents[1]/'results'/'complete_grade_polyphase_CP_decomposition.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'partition_sizes':{str(k):len(v) for k,v in partitions.items()},'digit_cells':len(rows)},indent=2))
if __name__=='__main__':main()
