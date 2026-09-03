#!/usr/bin/env python3
"""Check tau_p closure obstruction under all ordered vertex relabelings."""
import itertools,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
d=json.loads((R/'cosmology_principal_wall_partial_fraction_cech_gate.json').read_text());M=d['edge_to_vertex_matrix'];a=d['p_partial_fraction_pair_vector'];edges=[(0,1),(0,2),(1,2)]
def mv(x):return [sum(M[i][j]*x[j] for j in range(3)) for i in range(3)]
b=mv(a);assert b==[0,2,-2]
runs=[]
for p in itertools.permutations(range(3)):
    ap=[0,0,0]
    for c,(i,j) in zip(a,edges):
        u,v=p[i],p[j];sgn=1 if u<v else -1;key=(min(u,v),max(u,v));ap[edges.index(key)]+=sgn*c
    bp=mv(ap);pb=[0,0,0]
    for i,x in enumerate(b):pb[p[i]]=x
    assert bp==pb and bp!=[0,0,0]
    runs.append({'permutation':list(p),'transported_pair_vector':ap,'transported_boundary':bp})
out={'schema':'marici.benincasa.cosmology-tau-p-orientation-naturality.v1','problem':'can an admissible simultaneous relabeling and orientation transport remove the tau_p closure obstruction?','bold_conjecture':'the residual is a convention artifact and vanishes in some ordered labeling','rivals':['simultaneous relabeling transports the nonzero residual naturally','an independent fitted edge sign change forces closure'],'risky_consequences':'one of the six induced ordered transports must send the boundary to zero','strongest_falsification_attempt':{'ordered_vertex_permutations_tested':6,'base_boundary':b,'runs':runs},'exact_residual':'every admissible ordered transport has boundary equal to the corresponding vertex permutation of (0,2,-2), hence remains nonzero','conjecture_disposition':'falsified','surviving_scope':'the obstruction is natural under ordered relabeling; closure requires new source content, not a convention change','unauthorized_alternative':'independent edge-sign fitting is not induced by simultaneous transport of vertices, edges, and coefficients','passed':True};(R/'cosmology_tau_p_orientation_naturality.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
