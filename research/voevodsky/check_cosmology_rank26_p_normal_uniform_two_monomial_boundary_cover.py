"""Verify the sharp arbitrary-degree threshold for the two-square-monomial boundary cover."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_rank26_p_normal_uniform_two_monomial_boundary_cover.json'
def boundary(A):return [(i,d-i) for d in range(max(0,A-6),A-3) for i in range(d+1)]
def uncovered(A):return [e for e in boundary(A) if e[0]<2 and e[1]<2]
def main():
 records=[]
 for A in range(6,501):records.append({'ambient':A,'targets':len(boundary(A)),'uncovered':uncovered(A)})
 assert uncovered(8)==[(1,1)] and not uncovered(9) and all(not uncovered(A) for A in range(9,501))
 # Symbolic bound: if both coordinates are <2 then i+j<=2; boundary has i+j>=A-6, hence impossible when A-6>=3.
 out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-uniform-two-monomial-boundary-cover.v1','status':'sharp_uniform_boundary_cover_threshold_proved','all_integer_ambient_threshold':9,'even_ambient_threshold':10,'sharp_failure':{'ambient':8,'uncovered_exponent':[1,1]},'symbolic_argument':'Every boundary exponent has total degree at least A-6. If neither coordinate is at least 2, its total degree is at most 2. Therefore the two square-monomial images cover every boundary exactly when A-6>=3, i.e. A>=9; A=8 fails at (1,1).','checked_range':[6,500],'decision':'For every integer ambient degree A>=9, and hence every even A>=10, each top-three-degree boundary coordinate is the image of at least one lower boundary coordinate under an axis-square inclusion.','limitations':['combinatorial cover only','does not prove lower-degree contraction seeds exist','overlap descent and source naturality are separate prerequisites'],'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
