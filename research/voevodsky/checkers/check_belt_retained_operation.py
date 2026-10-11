"""Compare cyclic operations and retention on a common six-cell geometry.
The observables are volume averages of cell-amplitude fields, not charges.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
from hashlib import sha256
import json
from check_geometric_cycle_reversal import geo, ONE, ZERO
from check_reversed_coefficient_attachment import multiply, rank, times, encode
from check_retained_barycenter_attachment import cells_of, topology
from check_three_arrow_receiver import simple_cycles

BASE=Path(__file__).resolve().parents[1]
SOURCE=BASE/'results/three_tetrahedron_belt.json'

def real(a): return [[(x,Q(0)) for x in row] for row in a]
def apply(a,v): return [row[0] for row in multiply(a,[[x] for x in v])]
def transpose(a): return [list(row) for row in zip(*a)]
def mm(a,b): return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def plus(a,b): return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def minus(a,b): return [[x-y for x,y in zip(r,s)] for r,s in zip(a,b)]
def trace(a): return sum(a[i][i] for i in range(len(a)))
def identity(n): return [[Q(i==j) for j in range(n)] for i in range(n)]
def nerve(cover):
    faces=[]
    for k in range(1,len(cover)+1):
        for ids in combinations(range(len(cover)),k):
            if set.intersection(*(set(cover[i]) for i in ids)): faces.append(tuple(str(i) for i in ids))
    return set(faces)

def main():
    original=SOURCE.read_bytes(); source=json.loads(original)
    if not source['verification_passed']: raise ValueError('geometry not verified')
    old_parents=['ABCD','ABCe']; belt_parents=['ABDe','BCDe','ACDe']
    rows=sorted(source['common_refinement'],key=lambda r:(old_parents.index(r['pair_parent']),belt_parents.index(r['belt_parent'])))
    if len(rows)!=6: raise ValueError('common refinement')
    for i,row in enumerate(rows):
        side=old_parents[i//3]; sector=belt_parents[i%3]
        expected=(set(sector)-{'D','e'})|{'F',('D' if side=='ABCD' else 'e')}
        if set(row['tetrahedron'])!=expected or row['pair_parent']!=side or row['belt_parent']!=sector: raise ValueError('parent binding')
    positions={k:tuple(map(Q,v)) for k,v in source['coordinates'].items()}
    volumes=[]
    for row in rows:
        a,b,c,d=[positions[k] for k in row['tetrahedron']]
        sub=lambda x,y:tuple(p-q for p,q in zip(x,y))
        volumes.append(abs(geo.dot(sub(b,a),geo.cross(sub(c,a),sub(d,a))))/6)
    Aold=[[Q(i//3==j,3) for i in range(6)] for j in range(2)]
    Abelt=[[Q(i%3==j,2) for i in range(6)] for j in range(3)]
    Uold=[[Q(i//3==j) for j in range(2)] for i in range(6)]
    Ubelt=[[Q(i%3==j) for j in range(3)] for i in range(6)]
    Po=mm(Uold,Aold); Pb=mm(Ubelt,Abelt); Pc=[[Q(1,6)]*6 for _ in range(6)]
    Join=minus(plus(Po,Pb),Pc)
    Mixed=minus(identity(6),Join)
    rotation={'A':'B','B':'C','C':'A','D':'D','e':'e','F':'F'}
    cells=[frozenset(r['tetrahedron']) for r in rows]
    image=[cells.index(frozenset(rotation[v] for v in cell)) for cell in cells]
    # Pullback action on scalar cell fields: (T f)(cell)=f(rotation(cell)).
    T=[[Q(j==image[i]) for j in range(6)] for i in range(6)]
    C=[[Q(0),Q(1),Q(0)],[Q(0),Q(0),Q(1)],[Q(1),Q(0),Q(0)]]
    omega=geo.OMEGA; omega2=times(omega,omega)
    mode=[ONE,omega,omega2]*2
    conjugate=[(z[0],-z[1]) for z in mode]
    # Real contrasts suffice to distinguish the retention profiles.
    contrast=[(Q(x),Q(0)) for x in (1,-1,0,1,-1,0)]
    mixed=[(Q(x),Q(0)) for x in (1,-1,0,-1,1,0)]
    old_nerve=topology(nerve(source['pair_tetrahedra']))
    belt_nerve=topology(nerve(source['belt_tetrahedra']))
    belt_graph=topology({c for c in nerve(source['belt_tetrahedra']) if len(c)<=2})
    primitive={(a,b) for a in 'ABCD' for b in 'ABCD' if a!=b}|{(a,'e') for a in 'ABC'}
    returning=primitive|{('e','D')}; sinking=primitive|{('D','e')}
    return_paths=[[a,'e','D',a] for a in 'ABC']
    before_cycles=simple_cycles(primitive); after_cycles=simple_cycles(returning)
    checks={
        'six_children_have_equal_exact_volume':volumes==[Q(8,9)]*6,
        'source_rotation_permutations_are_derived_from_vertices':image==[1,2,0,4,5,3],
        'two_cell_and_three_cell_averages_are_projectors':mm(Po,Po)==Po and mm(Pb,Pb)==Pb,
        'the_two_averaging_projections_commute':mm(Po,Pb)==mm(Pb,Po)==Pc,
        'retention_dimensions_are_two_three_and_common_one':trace(Po)==2 and trace(Pb)==3 and trace(Pc)==1,
        'joint_retention_is_a_rank_four_projector':mm(Join,Join)==Join and trace(Join)==4,
        'two_mixed_degrees_remain_outside_both_summaries':mm(Mixed,Mixed)==Mixed and trace(Mixed)==2,
        'cyclic_action_has_order_three':mm(mm(T,T),T)==identity(6) and T!=identity(6),
        'old_summary_sees_rotation_as_identity':mm(Aold,T)==Aold,
        'belt_summary_intertwines_actual_three_cycle':mm(Abelt,T)==mm(C,Abelt),
        'omega_mode_is_preserved_by_belt_and_lost_by_old_summary':apply(real(T),mode)==[times(omega,z) for z in mode]
            and apply(real(Pb),mode)==mode and apply(real(Po),mode)==[ZERO]*6,
        'opposite_character_is_preserved_too':apply(real(T),conjugate)==[times(omega2,z) for z in conjugate],
        'explicit_real_pair_distinguished_by_belt_not_pair_summary':apply(real(Aold),contrast)==[ZERO]*2 and apply(real(Abelt),contrast)!=[ZERO]*3,
        'joint_observation_does_not_replace_full_retention':apply(real(Aold),mixed)==[ZERO]*2 and apply(real(Abelt),mixed)==[ZERO]*3 and mixed!=[ZERO]*6,
        'operation_already_lifts_to_retained_refinement':mm(T,Ubelt)==mm(Ubelt,C) and mm(T,Po)==mm(Po,T) and mm(T,Pb)==mm(Pb,T),
        'all_three_belt_cells_intersect_so_full_nerve_fills_cycle':belt_nerve['cells']==[3,3,1,0] and belt_nerve['rational_betti']==[1,0,0,0],
        'graph_only_loop_is_not_full_intersection_topology':belt_graph['rational_betti']==[1,1,0,0],
        'core_edge_as_return_creates_three_internal_face_cycles':all(all((a,b) in returning for a,b in zip(path,path[1:])) for path in return_paths),
        'opposite_core_orientation_does_not_close_receiver_paths':simple_cycles(sinking)==before_cycles,
        'single_return_extends_fifteen_to_sixteen_generators':len(returning)==16 and all(any(set(edge)<=set(cycle) and edge in set(zip(cycle,cycle[1:]+cycle[:1])) for cycle in after_cycles) for edge in returning),
        'source_artifact_unchanged':SOURCE.read_bytes()==original,
    }
    result={'verification_passed':all(checks.values()),'checks':checks,
        'contract':{'state':'one real or complex amplitude per common-refinement cell',
                    'old_observation':'equal-volume average over the three children of each old tetrahedron',
                    'belt_observation':'equal-volume average over the two children of each belt tetrahedron',
                    'operation':'the existing 120-degree vertex rotation, acting on cell-amplitude fields',
                    'not_assigned':'electric charge, quark species, transport phases, or coefficient-arrow costs'},
        'common_cell_order':rows,
        'old_average':[[str(x) for x in r] for r in Aold],
        'belt_average':[[str(x) for x in r] for r in Abelt],
        'retention_ranks':{'common':1,'old_side_contrast':1,'belt_contrast':2,'mixed':2,'old_plus_belt':4,'full':6},
        'cyclic_mode':encode(mode),'old_readout_of_mode':encode(apply(real(Aold),mode)),
        'belt_readout_of_mode':encode(apply(real(Abelt),mode)),
        'nerve_topology':{'old':old_nerve,'belt_full':belt_nerve,'belt_graph_only':belt_graph},
        'core_return_candidate':{'added_primitive_arrow':['e','D'],'primitive_count':len(returning),
            'new_short_cycles':return_paths,'all_new_simple_cycles':len(after_cycles-before_cycles),
            'status':'tested directed connectivity; coefficient weights and positive weighted closure not yet assigned'},
        'outcome':'The belt summary preserves a cyclic contrast plane erased by the two-cell summary, but that operation already lifts to their common refinement. Independently, directing its new central edge e->D closes the three receiving legs through the three internal belt faces.',
        'next_obligation':'generate the coefficient transports of the new internal-face cycles and test weighted closure; do not infer it from directed connectivity alone',
        'source_sha256':sha256(original).hexdigest(),'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (BASE/'results/belt_retained_operation.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('common_cell_order','old_average','belt_average')},indent=2))
    if not result['verification_passed']: raise SystemExit(1)

if __name__=='__main__': main()
