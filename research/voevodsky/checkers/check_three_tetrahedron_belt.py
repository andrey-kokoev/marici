"""Test three tetrahedral pieces around the pair's central axis.
This is a 2-to-3 bistellar move, not an assigned neutron or charge model.
"""
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
from itertools import combinations
import json
from check_proton_merkle_reassembly import POINTS
from check_retained_barycenter_attachment import cells_of, topology
from check_three_arrow_receiver_geometry import boundary, sub, dot, cross, mean

BASE=Path(__file__).resolve().parents[1]

def main():
    P={k:tuple(map(Q,v)) for k,v in POINTS.items()}
    F=mean([P[k] for k in 'ABC']); P['e']=tuple(2*f-d for f,d in zip(F,P['D']))
    P['F']=F
    pair=[tuple('ABCD'),tuple('ABCe')]
    belt=[tuple('ABDe'),tuple('BCDe'),tuple('ACDe')]
    refined=[tuple(sorted(('F',a,b,apex))) for a,b in [('A','B'),('B','C'),('A','C')] for apex in ('D','e')]
    def signed_volume(t):
        a,b,c,d=[P[v] for v in t]
        return dot(sub(b,a),cross(sub(c,a),sub(d,a)))/6
    def oriented(tets): return {t:1 if signed_volume(t)>0 else -1 for t in tets}
    pair_boundary=boundary(oriented(pair)); belt_boundary=boundary(oriented(belt))
    old=cells_of(pair); new=cells_of(belt)
    core=frozenset(('D','e'))
    link={tuple(v for v in c if v not in core) for c in new if core<set(c)}
    faces={f:sum(set(f)<set(t) for t in belt) for f in new if len(f)==3}
    internal={f for f,n in faces.items() if n==2}
    bP=mean([P[k] for k in 'ABCD']); bQ=mean([P[k] for k in 'ABCe'])
    axis=sub(P['e'],P['D'])
    def axis_parameter(x): return dot(sub(x,P['D']),axis)/dot(axis,axis)
    # Full directed K4 carriers on the three pieces would require more
    # arrows than the existing directed receiver source supplies.
    source={(a,b) for a in 'ABCD' for b in 'ABCD' if a!=b}|{(a,'e') for a in 'ABC'}
    complete_belt=set().union(*({(a,b) for a in t for b in t if a!=b} for t in belt))
    pair_complete=set().union(*({(a,b) for a in t for b in t if a!=b} for t in pair))
    topo_pair=topology(old); topo_belt=topology(new); topo_link=topology(link)
    checks={
        'same_five_geometric_vertices':{v for t in pair for v in t}=={v for t in belt for v in t},
        'exact_same_oriented_outer_boundary':pair_boundary==belt_boundary and len(belt_boundary)==6,
        'equal_total_volume':sum(abs(signed_volume(t)) for t in pair)==sum(abs(signed_volume(t)) for t in belt)==Q(16,3),
        'three_equal_nondegenerate_belt_cells':all(abs(signed_volume(t))==Q(16,9) for t in belt),
        'triple_intersection_is_exactly_central_edge':set.intersection(*(set(t) for t in belt))==set(core),
        'three_pairwise_shared_internal_faces':internal=={tuple('ADe'),tuple('BDe'),tuple('CDe')},
        'central_edge_link_is_three_edge_circle':topo_link['cells']==[3,3,0,0] and topo_link['rational_betti']==[1,1,0,0],
        'filled_belt_has_ball_homology_not_annulus_homology':topo_belt['rational_betti']==[1,0,0,0],
        'both_barycenters_lie_on_core_axis':cross(sub(bP,P['D']),axis)==(0,0,0) and cross(sub(bQ,P['D']),axis)==(0,0,0),
        'center_segment_is_proper_subsegment_of_core_edge':Q(0)<axis_parameter(bP)<axis_parameter(F)<axis_parameter(bQ)<Q(1),
        'one_undirected_edge_is_added_by_the_move':{c for c in new-old if len(c)==2}=={tuple('De')},
        'internal_shared_face_replaced_not_retained':tuple('ABC') in old-new,
        'full_three_K4_completion_has_twenty_arrows':len(complete_belt)==20,
        'five_missing_primitive_arrows_are_identified':complete_belt-source=={('e','A'),('e','B'),('e','C'),('D','e'),('e','D')},
        'two_full_K4_pair_would_have_eighteen_arrows':len(pair_complete)==18,
        'common_six_cell_refinement_preserves_outer_boundary':boundary(oriented(refined))==pair_boundary,
        'common_refinement_has_six_equal_cells':len(refined)==6 and all(abs(signed_volume(t))==Q(8,9) for t in refined),
        'refinement_splits_each_old_cell_into_three':all(sum(abs(signed_volume(t)) for t in refined if apex in t)==Q(8,3) for apex in ('D','e')),
        'refinement_splits_each_belt_cell_into_two':all(sum(abs(signed_volume(t)) for t in refined if set((a,b))<=set(t))==Q(16,9) for a,b in [('A','B'),('B','C'),('A','C')]),
    }
    report={'verification_passed':all(checks.values()),'checks':checks,
        'pair_tetrahedra':[list(t) for t in pair],'belt_tetrahedra':[list(t) for t in belt],
        'coordinates':{k:list(map(str,p)) for k,p in P.items()},
        'pair_topology':topo_pair,'belt_topology':topo_belt,'core_link_topology':topo_link,
        'volume_per_belt_piece':'16/9','total_volume':'16/3',
        'common_refinement':[{'tetrahedron':list(t),'pair_parent':'ABCD' if 'D' in t else 'ABCe',
            'belt_parent':''.join(sorted((set(t)-{'F','D','e'})|{'D','e'}))} for t in refined],
        'common_refinement_topology':topology(cells_of(refined)),
        'axis_parameters':{'D':'0','proton_center':str(axis_parameter(bP)),'shared_face_center':str(axis_parameter(F)),
                           'other_center':str(axis_parameter(bQ)),'e':'1'},
        'primitive_counts':{'existing_three_arrow_receiver_source':15,'two_full_K4_tetrahedra':18,'three_full_K4_belt_tetrahedra':20},
        'outcome':'A three-tetrahedron ring exists around the barycenter axis, with a circular edge link. It is a retriangulation of the same filled body, not an added neutron carrier. A particle distinction needs the new internal incidence to carry an independently specified retained operation.',
        'scope':'no electric charges, quark identities, or expanded coefficient count assigned',
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (BASE/'results/three_tetrahedron_belt.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))
    if not report['verification_passed']: raise SystemExit(1)

if __name__=='__main__': main()
