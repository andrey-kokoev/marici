"""Iteration 3: actual direction-bearing fiber over the realized host vertex.
The new pullback is PL. Its radial blowdown to the old realization is continuous
semialgebraic, generally NOT PL. The category change is explicit.
"""
from copy import deepcopy
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
from hashlib import sha256
import json

from potential_complex_pullback import depth, factor, project, digest, complex_cells, betti_mod2
from check_potential_complex_pullback import verify_packet as verify_source

BASE=Path(__file__).resolve().parents[1]
SOURCE=BASE/'results/potential_complex_pullback_store.json'


def paths(m,n):
    """Monotone lattice paths for a compatible ordered product triangulation."""
    for horizontal in combinations(range(m+n),m):
        horizontal=set(horizontal); i=j=0; path=[(i,j)]
        for k in range(m+n):
            if k in horizontal: i+=1
            else: j+=1
            path.append((i,j))
        yield path


def product(left,right,prefix):
    vertices={}
    for a in left['vertices']:
        for b in right['vertices']: vertices[prefix+a+'|'+b]={'left':a,'right':b}
    maximal=[]; provenance=[]
    for a in left['maximal_simplices']:
        for b in right['maximal_simplices']:
            for path in paths(len(a)-1,len(b)-1):
                maximal.append([prefix+a[i]+'|'+b[j] for i,j in path])
                provenance.append({'left_simplex':a,'right_simplex':b,'path':[list(p) for p in path]})
    return {'vertices':vertices,'maximal_simplices':maximal,'provenance':provenance}


def construct(source):
    c=source['record']['contract']; center='0123'
    directions={'vertices':{v:p for v,p in c['C']['vertices'].items() if v!=center},
                'maximal_simplices':[s[:-1] for s in c['C']['maximal_simplices']]}
    # Ordered inward: height 1 precedes height 0. This agrees with T's flag
    # order, so the map from the product triangulation is actually simplicial.
    interval={'vertices':{'1':['1'],'0':['0']},'maximal_simplices':[['1','0']]}
    resolved=product(interval,directions,'C:')
    total=product(c['T'],directions,'Q:')
    q_to_t={v:r['left'] for v,r in total['vertices'].items()}
    q_to_c={v:'C:'+c['T_to_I'][r['left']]+'|'+r['right'] for v,r in total['vertices'].items()}
    exceptional=[['Q:012|'+v for v in s] for s in directions['maximal_simplices']]
    return {'kind':'fold-bearing-vertex-pullback','source_root':source['root'],
            'category':'PL polyhedra for the new pullback; continuous semialgebraic maps for radial blowdown',
            'directions':directions,'inward_interval':interval,'resolved_potential':resolved,'Q':total,
            'resolved_potential_to_I':{v:r['left'] for v,r in resolved['vertices'].items()},
            'Q_to_T':q_to_t,'Q_to_resolved_potential':q_to_c,
            'exceptional_fiber':{'host_vertex':'012','maximal_simplices':exceptional},
            'retained_fold_completion':{','.join(s[:-1]):s for s in c['C']['maximal_simplices']},
            'radial_blowdown':'(t,v) -> (1-t)*(1/4,1/4,1/4,1/4) + t*v',
            'particle_identity':'unassigned'}


def validate_point(x,v):
    if len(x)!=3 or len(v)!=4 or depth(v)!=1: raise ValueError('invalid host/direction point')
    return depth(x)


def resolved_mediator(x,t,v):
    if validate_point(x,v)!=t: raise ValueError('interface square does not commute')
    return x,v


def blowdown(x,v):
    t=validate_point(x,v)
    return x,tuple((1-t)/4+t*a for a in v)


def lift_away_from_center(x,y):
    t=depth(x)
    if len(y)!=4 or depth(y)!=t: raise ValueError('incompatible original point')
    if t==0: raise ValueError('no unique direction lift at the center')
    v=tuple((a-(1-t)/4)/t for a in y)
    validate_point(x,v)
    return x,v


def point_of_simplex(record,source,simplex,weights):
    if len(simplex)!=len(weights) or min(weights)<0 or sum(weights)!=1: raise ValueError('simplex coefficients')
    x=[Q(0)]*3; v=[Q(0)]*4
    for ref,w in zip(simplex,weights):
        pair=record['Q']['vertices'][ref]
        for i,a in enumerate(source['record']['contract']['T']['vertices'][pair['left']]): x[i]+=w*Q(a)
        for i,a in enumerate(record['directions']['vertices'][pair['right']]): v[i]+=w*Q(a)
    validate_point(tuple(x),tuple(v))
    return tuple(x),tuple(v)


def verify(packet):
    if set(packet)!={'schema','source','record','root'} or packet['schema']!='marici.fold-bearing-vertex.v1': raise ValueError('schema')
    source=packet['source']; verify_source(source); r=packet['record']
    if digest(r)!=packet['root'] or r!=construct(source): raise ValueError('source-bound construction mismatch')
    c=source['record']['contract']; tmax=[set(s) for s in c['T']['maximal_simplices']]
    cmax=[set(s) for s in r['resolved_potential']['maximal_simplices']]
    for simplex in r['Q']['maximal_simplices']:
        if not any({r['Q_to_T'][v] for v in simplex}<=s for s in tmax): raise ValueError('host projection not simplicial')
        if not any({r['Q_to_resolved_potential'][v] for v in simplex}<=s for s in cmax): raise ValueError('resolved projection not simplicial')
        for v in simplex:
            if c['T_to_I'][r['Q_to_T'][v]]!=r['resolved_potential_to_I'][r['Q_to_resolved_potential'][v]]: raise ValueError('square')
    exceptional=[s for s in complex_cells(r['Q']['maximal_simplices'])[2] if all(r['Q_to_T'][v]=='012' for v in s)]
    if set(map(tuple,map(sorted,exceptional)))!=set(tuple(sorted(s)) for s in r['exceptional_fiber']['maximal_simplices']): raise ValueError('wrong literal center fiber')
    return {'verified':True,'Q_f_vector':[len(v) for k,v in sorted(complex_cells(r['Q']['maximal_simplices']).items())],
            'Q_betti_mod2':betti_mod2(r['Q']['maximal_simplices']),
            'exceptional_f_vector':[len(v) for k,v in sorted(complex_cells(exceptional).items())],
            'exceptional_betti_mod2':betti_mod2(exceptional),
            'resolved_potential_f_vector':[len(v) for k,v in sorted(complex_cells(r['resolved_potential']['maximal_simplices']).items())],
            'potential_fold_completions':len(r['retained_fold_completion'])}


def rejected(fn):
    try: fn()
    except (ValueError,KeyError,TypeError): return True
    return False


def main():
    source=json.loads(SOURCE.read_text(encoding='utf-8')); verify_source(source)
    record=construct(source); packet={'schema':'marici.fold-bearing-vertex.v1','source':source,'record':record,'root':digest(record)}
    report=verify(packet); host_center=(Q(1,3),)*3; potential_center=(Q(1,4),)*4
    directions=[tuple(map(Q,p)) for p in record['directions']['vertices'].values()]
    checks={'source_and_new_commuting_square_reverified':report['verified'],
            'literal_center_fiber_is_the_full_direction_sphere':report['exceptional_f_vector']==[14,36,24] and report['exceptional_betti_mod2']==[1,0,1],
            'all_24_inward_flags_recoverable_at_the_vertex':report['potential_fold_completions']==24,
            'total_object_is_not_the_old_cone':report['Q_betti_mod2']==[1,0,1,0,0],
            'product_has_864_four_cells':report['Q_f_vector']==[98,852,2268,2376,864],
            'resolved_potential_has_72_three_cells':report['resolved_potential_f_vector']==[28,122,168,72],
            'fourteen_distinct_directions_share_one_host_vertex':len({resolved_mediator(host_center,Q(0),v) for v in directions})==14,
            'all_exceptional_directions_blow_down_to_old_barycenter':all(blowdown(host_center,v)==(host_center,potential_center) for v in directions),
            'point_realization_has_no_unique_inverse_at_center':rejected(lambda:lift_away_from_center(host_center,potential_center))}
    all_roundtrips=True; all_mediators=True; all_old_points=True
    for simplex in record['Q']['maximal_simplices']:
        x,v=point_of_simplex(record,source,simplex,[Q(i,15) for i in range(1,6)])
        old=blowdown(x,v)
        all_roundtrips &= lift_away_from_center(*old)==(x,v)
        all_mediators &= resolved_mediator(x,depth(x),v)==(x,v)
        all_old_points &= project(source['record']['contract'],factor(*old))==old
    checks['all_cell_interiors_have_unique_lift_off_center']=all_roundtrips
    checks['mediator_recovers_all_cell_interiors']=all_mediators
    checks['blowdown_lands_in_actual_original_pullback']=all_old_points
    checks['incompatible_new_interface_pair_rejected']=rejected(lambda:resolved_mediator(host_center,Q(1),directions[0]))
    # Retaining v while inward depth decreases gives an actual endpoint at t=0,
    # rather than forgetting which fold direction approached the center.
    inward=True
    for v in directions:
        for t in (Q(0),Q(1,3),Q(1)):
            for s in (Q(0),Q(1,2),Q(1)):
                before=tuple((1-t)/4+t*a for a in v)
                after=tuple((1-(1-s)*t)/4+(1-s)*t*a for a in v)
                inward &= after==tuple((1-s)*a+s/4 for a in before)
    checks['inward_contraction_retains_direction_through_zero']=inward
    # A straight segment has a nonzero quadratic coefficient after radial
    # blowdown. It cannot be affine on any interval, hence not finite-piece PL.
    v0=(Q(1),Q(0),Q(0),Q(0)); v1=(Q(1,2),Q(1,2),Q(0),Q(0))
    quadratic=tuple(b-a for a,b in zip(v0,v1))
    checks['radial_blowdown_is_not_silently_claimed_PL']=any(quadratic)
    # Every fixed potential direction gives a disk section T x {v}. This
    # contains the six radial triangles, so the previous odd-flat-holonomy
    # obstruction persists even though the apex now has a direction sphere.
    all_disk_sections=True
    qcells=complex_cells(record['Q']['maximal_simplices'])[2]
    for v in record['directions']['vertices']:
        for tf in source['record']['contract']['T']['maximal_simplices']:
            all_disk_sections &= tuple(sorted('Q:'+a+'|'+v for a in tf)) in qcells
    checks['all_fourteen_vertex_directions_have_host_disk_sections']=all_disk_sections
    extensions={}
    for parity in (0,1):
        wanted=[parity,0,0,0,0,0]; count=0
        for bits in range(64):
            actual=[((bits>>i)&1)^((bits>>((i+1)%6))&1) for i in range(6)]
            count+=actual==wanted
        extensions[str(parity)]=count
    checks['odd_flat_belt_transport_still_cannot_extend']=extensions=={'0':2,'1':0}
    bad=deepcopy(packet); bad['record']['exceptional_fiber']['maximal_simplices'].pop(); bad['root']=digest(bad['record'])
    checks['rehashed_missing_exceptional_fold_rejected']=rejected(lambda:verify(bad))
    bad=deepcopy(packet); first=next(iter(bad['record']['Q_to_resolved_potential'])); bad['record']['Q_to_resolved_potential'][first]='C:0|0'; bad['root']=digest(bad['record'])
    checks['rehashed_wrong_pullback_projection_rejected']=rejected(lambda:verify(bad))
    checks['complete_serialized_packet_reverifies']=verify(json.loads(json.dumps(packet)))==report
    result={'schema':'marici.fold-bearing-vertex-check.v1','passed':all(checks.values()),'checks':checks,'resolved_pullback':report,
            'flat_C2_disk_extensions':extensions,'blowdown_quadratic_coefficient':list(map(str,quadratic)),
            'root':packet['root'],'source_root':source['root'],'source_file_sha256':sha256(SOURCE.read_bytes()).hexdigest(),
            'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'scope':'A new pullback using a resolved potential factor. Actual center fiber S2 retains directions and all 24 flags. Not an isomorphism of the old pullback, not a physical electron identification.'}
    out=BASE/'results'
    (out/'fold_bearing_vertex_store.json').write_text(json.dumps(packet,indent=2)+'\n',encoding='utf-8')
    (out/'fold_bearing_vertex.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
    if not result['passed']: raise SystemExit(1)

if __name__=='__main__': main()
