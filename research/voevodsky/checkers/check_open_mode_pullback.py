"""Iteration 7: a mode-bearing host interface, without fixing value=position.
H=T x Z -> I x Z <- I x B. Its actual PL pullback is T x B.
The original geometric and coefficient witnesses remain source-bound.
"""
from fractions import Fraction as Q
from collections import Counter
from copy import deepcopy
from pathlib import Path
from hashlib import sha256
import json

from check_host_coefficient_pullback import verify as verify_fixed, source_host, host_mode
from check_projector_fold_sheets import parameters, fiber
from check_fold_coefficient_attachment import mode, direction
from check_fold_bearing_vertex import product
from potential_complex_pullback import digest, depth, complex_cells, betti_mod2

BASE=Path(__file__).resolve().parents[1]
SOURCE=BASE/'results/host_coefficient_pullback_store.json'


def construct(source):
    atlas_packet=source['source']; atlas=atlas_packet['record']; t=source_host(atlas_packet)
    # Order B vertices by their image in Z. Gamma then preserves the ordering
    # on each triangle; there is no vertex collapse inside a triangle.
    b={'vertices':atlas['vertices'],
       'maximal_simplices':[sorted(face,key=lambda v:atlas['projection'][v]) for face in atlas['oriented_faces']]}
    z={'vertices':atlas['image']['vertices'],'maximal_simplices':[sorted(face) for face in atlas['image']['faces']]}
    interval={'vertices':{'1':['1'],'0':['0']},'maximal_simplices':[['1','0']]}
    h=product(t,z,'H:'); c=product(interval,b,'C:'); j=product(interval,z,'J:'); q=product(t,b,'Q:')
    height={v:('0' if v=='012' else '1') for v in t['vertices']}
    gamma=atlas['projection']
    h_to_j={v:'J:'+height[r['left']]+'|'+r['right'] for v,r in h['vertices'].items()}
    c_to_j={v:'J:'+r['left']+'|'+gamma[r['right']] for v,r in c['vertices'].items()}
    q_to_h={v:'H:'+r['left']+'|'+gamma[r['right']] for v,r in q['vertices'].items()}
    q_to_c={v:'C:'+height[r['left']]+'|'+r['right'] for v,r in q['vertices'].items()}
    q_to_t={v:r['left'] for v,r in q['vertices'].items()}
    q_owners=[atlas['original_fold_owners'][i] for tf in t['maximal_simplices'] for i,face in enumerate(b['maximal_simplices']) for _ in range(6)]
    return {'kind':'open-mode-fold-preserving-pullback','source_root':source['root'],
            'category':'PL polyhedra and PL maps',
            'interface_contract':'host location x and coefficient value z are separate typed coordinates',
            'T':t,'B':b,'Z':z,'I':interval,'H':h,'resolved_potential':c,'interface':j,'Q':q,
            'H_to_interface':h_to_j,'potential_to_interface':c_to_j,
            'Q_to_H':q_to_h,'Q_to_potential':q_to_c,'Q_to_host_location':q_to_t,
            'Q_fold_owners':q_owners,
            'exceptional_fiber_faces':[['Q:012|'+v for v in face] for face in b['maximal_simplices']],
            'equations':{'host':'(x,z) -> (h_T(x),z)','potential':'(t,v) -> (t,Gamma(v))',
                         'mediator':'((x,z),(t,v)) -> (x,v), when h_T(x)=t and z=Gamma(v)',
                         'inverse':'(x,v) -> ((x,Gamma(v)),(h_T(x),v))'},
            'realization':'host barycenter q with retained direction fiber; radial blowdown gives the old single point',
            'physical_identity':'not assigned'}


def check_simplicial(source,target,mapping):
    if set(mapping)!=set(source['vertices']) or not set(mapping.values())<=set(target['vertices']): raise ValueError('typed map domain/codomain')
    # Inverted index avoids a quadratic search through all maximal cells.
    containing={v:set() for v in target['vertices']}
    for i,s in enumerate(target['maximal_simplices']):
        for v in s: containing[v].add(i)
    for simplex in source['maximal_simplices']:
        images={mapping[v] for v in simplex}
        if not set.intersection(*(containing[v] for v in images)): raise ValueError('map is not simplicial')


def verify(packet):
    if set(packet)!={'schema','source','record','root'} or packet['schema']!='marici.open-mode-pullback.v1': raise ValueError('schema')
    verify_fixed(packet['source']); r=packet['record']
    if digest(r)!=packet['root'] or r!=construct(packet['source']): raise ValueError('source-bound open-mode construction mismatch')
    for a,b,m in [('H','interface','H_to_interface'),('resolved_potential','interface','potential_to_interface'),
                  ('Q','H','Q_to_H'),('Q','resolved_potential','Q_to_potential'),('Q','T','Q_to_host_location')]:
        check_simplicial(r[a],r[b],r[m])
    for v in r['Q']['vertices']:
        if r['H_to_interface'][r['Q_to_H'][v]]!=r['potential_to_interface'][r['Q_to_potential'][v]]: raise ValueError('noncommuting square')
    # A vertex-level bijection is checked in addition to the geometric product
    # proof; it is not substituted for the PL universal property.
    compatible={(a,b) for a in r['H']['vertices'] for b in r['resolved_potential']['vertices']
                if r['H_to_interface'][a]==r['potential_to_interface'][b]}
    realized={(r['Q_to_H'][v],r['Q_to_potential'][v]) for v in r['Q']['vertices']}
    if realized!=compatible or len(realized)!=len(r['Q']['vertices']): raise ValueError('vertex mediator not bijective')
    return {'Q_f_vector':[len(v) for k,v in sorted(complex_cells(r['Q']['maximal_simplices']).items())],
            'Q_betti_mod2':betti_mod2(r['Q']['maximal_simplices']),
            'center_fiber_f_vector':[len(v) for k,v in sorted(complex_cells(r['exceptional_fiber_faces']).items())],
            'center_fiber_betti_mod2':betti_mod2(r['exceptional_fiber_faces']),
            'retained_original_fold_owners':len({tuple(v) for v in r['Q_fold_owners']}),
            'compatible_vertex_pairs':len(compatible)}


def mediator(x,z,t,v,p):
    if len(x)!=3 or len(v)!=4 or depth(v)!=1 or depth(x)!=t or mode(p,direction(v))!=list(z): raise ValueError('incompatible interface pair')
    return x,v


def projections(x,v,p):
    if len(x)!=3 or len(v)!=4 or depth(v)!=1: raise ValueError('invalid point')
    return (x,mode(p,direction(v))),(depth(x),v)


def point_of_cell(r,simplex):
    weights=[Q(i,15) for i in range(1,6)]; x=[Q(0)]*3; v=[Q(0)]*4
    for ref,w in zip(simplex,weights):
        pair=r['Q']['vertices'][ref]
        for i,a in enumerate(r['T']['vertices'][pair['left']]): x[i]+=w*Q(a)
        for i,a in enumerate(r['B']['vertices'][pair['right']]['barycentric']): v[i]+=w*Q(a)
    return tuple(x),tuple(v)


def rejected(fn):
    try: fn()
    except (ValueError,KeyError,TypeError): return True
    return False


def main():
    source=json.loads(SOURCE.read_text(encoding='utf-8')); verify_fixed(source)
    record=construct(source); packet={'schema':'marici.open-mode-pullback.v1','source':source,'record':record,'root':digest(record)}
    report=verify(packet); atlas_packet=source['source']; atlas=atlas_packet['record']; p,n,recovery=parameters(atlas_packet['source'])
    checks={'all_five_maps_are_typed_simplicial_and_square_commutes':True,
            'all_compatible_vertex_pairs_have_unique_mediators':report['compatible_vertex_pairs']==140,
            'full_pullback_has_1296_four_cells':report['Q_f_vector']==[140,1266,3396,3564,1296],
            'all_twenty_four_original_fold_interiors_retained':report['retained_original_fold_owners']==24,
            'literal_center_fiber_is_full_refined_sphere':report['center_fiber_f_vector']==[20,54,36] and report['center_fiber_betti_mod2']==[1,0,1],
            'same_underlying_direction_bearing_homology':report['Q_betti_mod2']==[1,0,1,0,0]}
    exact=True
    for simplex in record['Q']['maximal_simplices']:
        x,v=point_of_cell(record,simplex); (xx,z),(t,vv)=projections(x,v,p)
        exact &= mediator(xx,z,t,vv,p)==(x,v) and projections(*mediator(xx,z,t,vv,p),p)==((xx,z),(t,vv))
    checks['mediator_and_inverse_round_trip_every_cell_interior']=exact
    q=(Q(1,3),)*3
    center_owners=set(); center_modes=set(); center_ok=True
    for face,owner in zip(record['B']['maximal_simplices'],atlas['original_fold_owners']):
        v=tuple(sum(Q(record['B']['vertices'][a]['barycentric'][i]) for a in face)/3 for i in range(4))
        (_,z),(t,_) = projections(q,v,p)
        center_ok &= mediator(q,z,t,v,p)==(q,v)
        center_owners.add(tuple(owner)); center_modes.add(tuple(z))
    checks['every_original_fold_has_an_active_interior_over_q']=center_ok and len(center_owners)==24
    checks['host_mode_is_not_silently_fixed_at_q']=len(center_modes)>1
    zero_mode=[(Q(0),Q(0))]*3
    checks['fixed_mode_fibers_remain_two_or_one_not_entire_sphere']=len(fiber(zero_mode,p,n,recovery))==2 and len(fiber(mode(p,direction((Q(1),Q(0),Q(0),Q(0)))),p,n,recovery))==1
    # The rejected fixed-position construction is exactly an added section
    # constraint, not an alternative labeling of this whole object.
    fixed_vertices={v for v,pair in record['Q']['vertices'].items()
                    if mode(p,direction(tuple(map(Q,record['B']['vertices'][pair['right']]['barycentric']))))==host_mode(tuple(map(Q,record['T']['vertices'][pair['left']])),p)}
    expected={'Q:'+source['record']['host_projection'][v]+'|'+v for v in source['record']['vertices']}
    checks['fixing_mode_to_position_recovers_previous_eleven_vertices']=fixed_vertices==expected and len(fixed_vertices)==11
    restored_owners={tuple(v) for v in record['Q_fold_owners']}-{tuple(v) for v in source['record']['original_fold_owners']}
    checks['sixteen_previously_excluded_fold_interiors_restored']=len(restored_owners)==16
    center_direction=(Q(0),Q(0),Q(0),Q(1))
    checks['previously_rejected_direction_now_has_its_own_mode']=mediator(q,zero_mode,Q(0),center_direction,p)==(q,center_direction)
    checks['wrong_mode_not_accepted_as_same_interface_value']=rejected(lambda:mediator(q,host_mode(q,p),Q(0),center_direction,p))
    checks['wrong_depth_rejected']=rejected(lambda:mediator(q,zero_mode,Q(1),center_direction,p))
    # Host-belt paths can hold their full potential direction fixed; the
    # inherited coefficient readout then also stays fixed.
    circle=['0','01','1','12','2','02','0']; loop_ok=True
    for vrec in record['B']['vertices'].values():
        v=tuple(map(Q,vrec['barycentric'])); z=mode(p,direction(v)); path=[]
        for ref in circle:
            u=tuple(map(Q,record['T']['vertices'][ref])); x=tuple(Q(1,6)+a/2 for a in u)
            path.append(mediator(x,z,depth(x),v,p))
        loop_ok &= path[0]==path[-1]
    checks['host_belt_loops_admit_fixed_direction_and_mode']=loop_ok
    # Kernel/sheet distinction is retained rather than identifying equal modes.
    first,second=fiber(zero_mode,p,n,recovery)
    checks['equal_modes_do_not_merge_distinct_direction_witnesses']=mediator(q,zero_mode,Q(0),first,p)!=mediator(q,zero_mode,Q(0),second,p)
    bad=deepcopy(packet); key=next(iter(bad['record']['Q_to_H'])); bad['record']['Q_to_H'][key]='H:012|missing'; bad['root']=digest(bad['record'])
    checks['rehashed_wrong_host_interface_projection_rejected']=rejected(lambda:verify(bad))
    bad=deepcopy(packet); bad['record']['Q_fold_owners'].pop(); bad['root']=digest(bad['record'])
    checks['rehashed_missing_fold_owner_rejected']=rejected(lambda:verify(bad))
    checks['complete_serialized_construction_reverifies']=verify(json.loads(json.dumps(packet)))==report
    result={'schema':'marici.open-mode-pullback-check.v1','passed':all(checks.values()),'checks':checks,'pullback':report,
            'root':packet['root'],'source_root':source['root'],'source_file_sha256':sha256(SOURCE.read_bytes()).hexdigest(),
            'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'scope':'An actual mode-bearing PL pullback retaining all original inward flags. One visible host center has a sphere of internal directions; a fixed host-plus-mode point has one or two. No physical electron or neutron identification.'}
    out=BASE/'results'
    (out/'open_mode_pullback_store.json').write_text(json.dumps(packet,indent=2)+'\n',encoding='utf-8')
    (out/'open_mode_pullback.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
    if not result['passed']: raise SystemExit(1)

if __name__=='__main__': main()
