#!/usr/bin/env python3
"""Recover the prior shared-edge photon construction into the arrow collection."""
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations
import hashlib
import json
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/voevodsky/checkers'))
from assemble_relative_geometry import assemble
from check_neutrino_arrow_seed_science import rank

def boundary(cell):
    out=Counter()
    for i in range(len(cell)):
        face=cell[:i]+cell[i+1:]
        inversions=sum(face[a]>face[b] for a in range(len(face)) for b in range(a+1,len(face)))
        out[tuple(sorted(face))]+=(-1)**(i+inversions)
    return out

def add(x,y):return (x[0]+y[0],x[1]+y[1])
def mul(x,y):return (x[0]*y[0]-3*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def conj(x):return (x[0],-x[1])
def dot(row,v):
    out=(Q(0),Q(0))
    for coefficient,x in zip(row,v):out=add(out,(coefficient*x[0],coefficient*x[1]))
    return out

def main():
    manifest_path=ROOT/'research/strominger/inputs/photon-shared-edge-seed.json'
    seed=json.loads(manifest_path.read_text())
    geometry_path=ROOT/seed['geometry_source']; native=json.loads(geometry_path.read_text())
    mode_path=ROOT/seed['mode_source'];mode=json.loads(mode_path.read_text())
    arrows=[tuple(a) for a in seed['arrows']];vertices=seed['vertex_labels']
    cells=[tuple(c[:-1]) for c in seed['retained_face_cycles']]
    edges=sorted({tuple(sorted(e)) for e in arrows})
    d1=[[int(v==b)-int(v==a) for a,b in edges] for v in vertices]
    face_boundaries=[boundary(c) for c in cells]
    d2=[[b.get(e,0) for b in face_boundaries] for e in edges]
    outer=Counter()
    for b in face_boundaries:
        for edge,value in b.items():outer[edge]+=value
    outer={edge:value for edge,value in outer.items() if value}
    assert all(sum(d1[i][k]*d2[k][j] for k in range(len(edges)))==0 for i in range(4) for j in range(2))
    K=[[Q(a[1]==b[0]) for a in arrows] for b in arrows]
    pairs=[(i,j) for i,a in enumerate(arrows) for j,b in enumerate(arrows) if a[1]==b[0]]
    L=[[Q(i==parent) for i in range(6)] for parent,child in pairs]
    A=[[Q(j==child) for parent,child in pairs] for j in range(6)]
    AL=[[sum(A[i][k]*L[k][j] for k in range(len(pairs))) for j in range(6)] for i in range(6)]
    plus=[(Q(x['real']),Q(x['imaginary_sqrt3_coefficient'])) for x in mode['candidate_plus']['coefficients']]
    minus=[conj(x) for x in plus]
    omega=(-Q(1,2),Q(1,2))
    plane=[[x[0],x[1]] for x in plus]
    metric=[[Q(3),Q(0)],[Q(0),Q(1)]]
    T=[[-Q(1,2),Q(1,2)],[-Q(3,2),-Q(1,2)]]
    transformed_metric=[[sum(T[k][i]*metric[k][l]*T[l][j] for k in range(2) for l in range(2)) for j in range(2)] for i in range(2)]
    coordinates={k:tuple(map(Q,p)) for k,p in native['vertices'].items()}
    distances=[[sum((x-y)**2 for x,y in zip(coordinates[a],coordinates[b])) for b in vertices] for a in vertices]
    full_source_path=ROOT/'research/voevodsky/inputs/relative-proton.json'
    full=assemble(json.loads(full_source_path.read_text()))
    checks={
        'same_six_primitive_arrows_as_proton':Counter(arrows)==Counter(tuple(a) for a in native['arrows']),
        'mode_order_matches_registered_occurrences':[''.join(a) for a in arrows]==mode['packet_order'],
        'each_face_cycle_uses_existing_arrows':all((a,b) in arrows for c in seed['retained_face_cycles'] for a,b in zip(c,c[1:])),
        'shared_AB_cancels':('A','B') not in outer,
        'outer_boundary_has_four_edges':len(outer)==4,
        'filled_seed_has_disk_homology':[4-rank(d1),len(edges)-rank(d1)-rank(d2),len(cells)-rank(d2)]==[1,0,0],
        'no_CD_seed_arrow':('C','D') not in edges,
        'retained_span_has_ten_rows':len(pairs)==10,
        'prefix_lift_injective':rank(L)==6,
        'aggregate_factors_as_AL':AL==K,
        'continuation_rank_four':rank(K)==4,
        'plus_is_existing_cyclic_eigenvector':[dot(row,plus) for row in K]==[mul(omega,x) for x in plus],
        'minus_is_conjugate_eigenvector':[dot(row,minus) for row in K]==[mul(conj(omega),x) for x in minus],
        'selected_real_plane_rank_two':rank(plane)==2,
        'existing_averaged_metric_invariant':transformed_metric==metric,
        'source_tetrahedron_all_squared_edges_eight':all(distances[i][j]==8 for i,j in combinations(range(4),2)),
        'common_processor_completion_has_four_faces':full['counts']['carrier_facets']==4,
    }
    out={'schema':'marici.strominger.photon-shared-edge-seed.v1','status':'passed' if all(checks.values()) else 'failed','label':'photon candidate','source_path':str(manifest_path.relative_to(ROOT)).replace('\\','/'),'effective_source':seed,'seed_cycles':seed['retained_face_cycles'],'arrows':seed['arrows'],'assembly_stage':seed['assembly_stage'],'geometry':{'intrinsic_affine_dimension_in_existing_source':3,'retained_complex_dimension':2,'vertices':{k:list(map(str,p)) for k,p in coordinates.items()},'oriented_faces':[list(c) for c in cells],'edge_supports':[list(e) for e in edges],'f_vector':[4,5,2],'nonempty_cells':11,'betti':[1,0,0],'outer_boundary':{''.join(e):value for e,value in outer.items()},'missing_edge':'CD','full_completion_counts':full['counts'],'shape_description':'two triangular faces hinged along AB, using the existing tetrahedral metric; a topological disk, not a newly flattened diamond'},'continuation':{'matrix':[[int(x) for x in row] for row in K],'composable_pair_rows':[list(p) for p in pairs],'prefix_rank':rank(L),'aggregation_rank':rank(A),'continuation_rank':rank(K),'kernel_dimension':6-rank(K)},'modes':{'source':seed['mode_source'],'plus':mode['candidate_plus'],'minus':mode['candidate_minus'],'plane_dimension':2,'existing_invariant_metric':[[3,0],[0,1]],'return_steps':3},'checks':checks,'distinction_from_proton':'Same primitive arrow set and source metric. This entry retains two supplied face cycles and the existing conjugate continuation plane; proton assembly includes the completed tetrahedral structure. Stopping at the seed stage is recorded, not a new particle-dependent assembler rule.','physical_identification_derived':False,'arrow_reversal_of':None}
    deps=[Path(__file__),manifest_path,geometry_path,mode_path,full_source_path,ROOT/'research/voevodsky/checkers/assemble_relative_geometry.py',ROOT/'research/strominger/checkers/check_neutrino_arrow_seed_science.py']
    out['source_hashes']={str(p.relative_to(ROOT)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in deps}
    out['source_sha256']=hashlib.sha256(manifest_path.read_bytes()).hexdigest()
    (ROOT/'research/strominger/results/photon_shared_edge_seed.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':out['status'],'checks':checks,'geometry':out['geometry']},indent=2))
    if not all(checks.values()):raise SystemExit(1)
if __name__=='__main__':main()
