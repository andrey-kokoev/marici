#!/usr/bin/env python3
"""Compute the simplicial boundary of the two source four-wall summands."""
import json
from collections import defaultdict
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research'/'benincasa'/'results'/'cosmology_two_four_wall_source_cells.json'
order={'g1':0,'g2':1,'g3':2,'g23':3,'g31':4}
def canonical(face):
 seq=list(face);inv=sum(order[seq[i]]>order[seq[j]] for i in range(len(seq)) for j in range(i+1,len(seq)));return tuple(sorted(seq,key=order.get)),(-1 if inv%2 else 1)
def boundary(chain):
 out=defaultdict(int)
 for simplex,coef in chain.items():
  for i in range(len(simplex)):
   face,sgn=canonical(simplex[:i]+simplex[i+1:]);out[face]+=coef*((-1)**i)*sgn
 return {k:v for k,v in out.items() if v}
def main():
 cells={('g1','g2','g3','g23'):1,('g1','g2','g3','g31'):1};faces=boundary(cells);vertices=boundary(boundary(cells));assert not vertices
 principal=('g1','g2','g3');mixed={k:v for k,v in faces.items() if k!=principal}
 assert faces[principal]==-2 and len(mixed)==6 and all(abs(v)==1 for v in mixed.values())
 prime_checks={str(p):{'principal_face_coefficient_mod_prime':faces[principal]%p,'nonzero':faces[principal]%p!=0} for p in (101,103)};assert all(x['nonzero'] for x in prime_checks.values())
 out={'schema':'marici.benincasa.cosmology-two-four-wall-source-cells.v1','source_summands':['(g1,g2,g3,g23)','(g1,g2,g3,g31)'],'source_origin':'(q_g23+q_g31)/(q_g1 q_g2 q_g3 q_g23 q_g31)=1/(q_g1 q_g2 q_g3 q_g31)+1/(q_g1 q_g2 q_g3 q_g23)','boundary_faces':{'/'.join(k):v for k,v in faces.items()},'principal_three_wall_face_coefficient':faces[principal],'mixed_exceptional_face_count':len(mixed),'mixed_exceptional_faces':{'/'.join(k):v for k,v in mixed.items()},'boundary_squared_zero':not vertices,'prime_checks':prime_checks,'principal_projection_is_unit':False,'mixed_faces_can_be_deleted':False,'interpretation':'the two sourced four-wall cells each contribute the same oriented principal face, so their sum reaches (g1,g2,g3) with coefficient -2 and also carries six unit mixed faces; this is the source origin of the parity obstruction','tau_p_unit_map_constructed':False,'physical_period_constructed':False,'next_gate':'test whether an independently sourced antisymmetric combination of the two four-wall cells exists; the physical source sum itself gives only the nonunit coefficient two','passed':True};OUT.parent.mkdir(exist_ok=True);OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
