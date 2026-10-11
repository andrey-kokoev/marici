"""Iteration 6: actual coefficient-matched base change over (F_ABC,A,B).
This tests the additional fixed-position readout j(x)=L_AB x. It is not an
assertion that port amplitude must equal the position of its base point.
"""
from fractions import Fraction as Q
from collections import Counter
from copy import deepcopy
from pathlib import Path
from hashlib import sha256
import json

from check_projector_fold_sheets import verify as verify_atlas, parameters, fiber
from check_fold_coefficient_attachment import mode, direction
from potential_complex_pullback import digest, depth, complex_cells, betti_mod2
from check_proton_six_belt import topology

BASE=Path(__file__).resolve().parents[1]
SOURCE=BASE/'results/projector_fold_sheets_store.json'


def source_host(packet):
    # atlas -> attachment -> resolved realization -> initial depth realization
    return packet['source']['source']['source']['record']['contract']['T']


def lifts(x):
    if len(x)!=3 or min(x)<0 or sum(x)!=1: raise ValueError('outside host triangle')
    f,a,b=x
    upper=(a+f/3,b+f/3,f/3,Q(0))
    lower=(a,b,Q(0),f)
    return [upper] if upper==lower else [lower,upper]


def host_mode(x,p): return mode(p,direction(lifts(x)[-1]))


def host_of_mode(z,p,n,recovery):
    upper=fiber(z,p,n,recovery)[-1]
    a,b,c,d=upper
    if d!=0: raise ValueError('upper endpoint is not on ABC')
    x=(3*c,a-c,b-c)
    if min(x)<0: raise ValueError('mode outside the selected small triangle')
    return x


def mediator(x,v,p):
    if v not in lifts(x) or mode(p,direction(v))!=host_mode(x,p): raise ValueError('incompatible coefficient pair')
    return x,v


def construct(source):
    atlas=source['record']; p,n,recovery=parameters(source['source']); host=source_host(source)
    host_coords={tuple(map(Q,v)):k for k,v in host['vertices'].items()}
    chosen={}
    for key,value in atlas['vertices'].items():
        v=tuple(map(Q,value['barycentric']))
        try: x=host_of_mode(mode(p,direction(v)),p,n,recovery)
        except ValueError: continue
        if x not in host_coords: raise ValueError('atlas not compatible with retained host flags')
        chosen[key]={'host_vertex':host_coords[x],'potential_vertex':key}
    faces=[]; provenance=[]
    for face,owner in zip(atlas['oriented_faces'],atlas['original_fold_owners']):
        if all(v in chosen for v in face): faces.append(face); provenance.append(owner)
    active={v for face in faces for v in face}
    if active!=set(chosen): raise ValueError('unaccounted boundary-only cells')
    mode_lookup={tuple(tuple(map(Q,a)) for a in value['value']):key for key,value in atlas['image']['vertices'].items()}
    host_to_mode={key:mode_lookup[tuple(host_mode(tuple(map(Q,coords)),p))] for key,coords in host['vertices'].items()}
    return {'kind':'fixed-position-coefficient-pullback','source_root':source['root'],
            'category':'PL polyhedra and PL maps',
            'additional_contract':'j(x)=L_AB applied to the actual geometric position in (F_ABC,A,B)',
            'host_to_mode_vertices':host_to_mode,'potential_to_mode_vertices':atlas['projection'],
            'vertices':chosen,'oriented_faces':faces,'original_fold_owners':provenance,
            'host_projection':{k:v['host_vertex'] for k,v in chosen.items()},
            'potential_projection':{k:k for k in chosen},
            'retained_atlas_faces':[i for i,face in enumerate(atlas['oriented_faces']) if all(v in chosen for v in face)],
            'seam_vertices':sorted(v for v in chosen if atlas['deck_vertex_map'][v]==v),
            'realized_host_vertex':'012',
            'center_fiber_vertices':sorted(v for v,r in chosen.items() if r['host_vertex']=='012'),
            'particle_interpretation':'none; a stricter attachment candidate, not the full fold-preserving realization'}


def verify(packet):
    if set(packet)!={'schema','source','record','root'} or packet['schema']!='marici.host-coefficient-pullback.v1': raise ValueError('schema')
    source=packet['source']; verify_atlas(source); record=packet['record']
    if digest(record)!=packet['root'] or record!=construct(source): raise ValueError('source-bound base change mismatch')
    host=source_host(source); hmax=[set(s) for s in host['maximal_simplices']]
    for face in record['oriented_faces']:
        if not any({record['host_projection'][v] for v in face}<=s for s in hmax): raise ValueError('host map not simplicial')
        for v in face:
            if record['host_to_mode_vertices'][record['host_projection'][v]]!=record['potential_to_mode_vertices'][record['potential_projection'][v]]: raise ValueError('square does not commute')
    return {'topology':topology(record['oriented_faces']),
            'betti_mod2':betti_mod2(record['oriented_faces']),
            'center_fiber_vertex_count':len(record['center_fiber_vertices']),
            'original_fold_interiors_retained':len({tuple(v) for v in record['original_fold_owners']})}


def rejected(fn):
    try: fn()
    except (ValueError,KeyError,TypeError): return True
    return False


def main():
    source=json.loads(SOURCE.read_text(encoding='utf-8')); verify_atlas(source)
    p,n,recovery=parameters(source['source']); atlas=source['record']; host=source_host(source)
    record=construct(source); packet={'schema':'marici.host-coefficient-pullback.v1','source':source,'record':record,'root':digest(record)}
    report=verify(packet); topo=report['topology']
    checks={'new_source_bound_square_reverified':True,
            'base_change_is_a_disk_not_the_full_direction_sphere':topo['disk'] and (topo['vertices'],topo['edges'],topo['faces'])==(11,22,12),
            'disk_boundary_has_eight_edges':topo['boundary_lengths']==[8],
            'realized_center_has_two_points_not_an_S2_fiber':report['center_fiber_vertex_count']==2,
            'only_eight_original_fold_interiors_survive':report['original_fold_interiors_retained']==8,
            'retained_refinement_has_two_upper_and_six_lower_owners':Counter(Counter(tuple(x) for x in record['original_fold_owners']).values())=={3:2,1:6}}
    q=(Q(1,3),)*3; center=lifts(q)
    expected=[(Q(1,3),Q(1,3),Q(0),Q(1,3)),(Q(4,9),Q(4,9),Q(1,9),Q(0))]
    checks['center_fiber_coordinates_derived_exactly']=center==expected
    checks['center_does_not_satisfy_matching_for_every_direction']=rejected(lambda:mediator(q,(Q(0),Q(0),Q(0),Q(1)),p))
    tests=0; exact=True; counts=Counter()
    for f in range(13):
        for a in range(13-f):
            b=12-f-a; x=(Q(f,12),Q(a,12),Q(b,12)); decoded=fiber(host_mode(x,p),p,n,recovery)
            exact &= decoded==lifts(x) and host_of_mode(host_mode(x,p),p,n,recovery)==x
            for v in decoded:
                exact &= mediator(x,v,p)==(x,v); tests+=1
            counts[len(decoded)]+=1
    checks['complete_host_grid_has_78_double_and_13_single_fibers']=exact and dict(counts)=={1:13,2:78}
    # Every retained triangle has a compatible interior, with the unique pair mediator.
    interiors=True
    for face in record['oriented_faces']:
        x=tuple(sum(Q(host['vertices'][record['host_projection'][v]][i]) for v in face)/3 for i in range(3))
        v=tuple(sum(Q(atlas['vertices'][ref]['barycentric'][i]) for ref in face)/3 for i in range(4))
        interiors &= mediator(x,v,p)==(x,v)
    checks['mediator_on_all_twelve_cell_interiors']=interiors
    # The common part is AB, subdivided once; it is an interval, not a belt circle.
    edges=complex_cells(record['oriented_faces'])[1]
    seam_edges=[e for e in edges if all(v in record['seam_vertices'] for v in e)]
    checks['seam_is_only_AB_with_its_midpoint']=len(record['seam_vertices'])==3 and len(seam_edges)==2 and all(host['vertices'][record['host_projection'][v]][0]=='0' for v in record['seam_vertices'])
    checks['seam_has_interval_homology_not_circle']=betti_mod2(seam_edges)==[1,0]
    # Both sections extend over the entire host disk and agree only on AB.
    circle=['0','01','1','12','2','02','0']; loop={0:[],1:[]}
    for ref in circle:
        u=tuple(map(Q,host['vertices'][ref])); x=tuple(Q(1,6)+a/2 for a in u); values=lifts(x)
        for i in (0,1): loop[i].append(list(map(str,values[i])))
    checks['actual_host_belt_loop_closes_on_each_lift']=all(path[0]==path[-1] for path in loop.values()) and loop[0]!=loop[1]
    # Depth and resolved radial data can be attached to R, but do not restore
    # excluded directions: the additional mode equation is a real restriction.
    checks['old_barycenter_blowdown_still_identifies_the_two_center_points']=all(tuple((1-depth(q))/4+depth(q)*v for v in point)==(Q(1,4),)*4 for point in center)
    # Mode-only matching fails the exact full-fold-retention requirement.
    all_owners={tuple(x+['0123']) for x in source['source']['source']['record']['directions']['maximal_simplices']}
    active_owners={tuple(x) for x in record['original_fold_owners']}; omitted=sorted(all_owners-active_owners)
    checks['sixteen_required_fold_interiors_are_explicitly_omitted']=len(omitted)==16
    bad=deepcopy(packet); bad['record']['center_fiber_vertices'].pop(); bad['root']=digest(bad['record'])
    checks['rehashed_single_center_lift_rejected']=rejected(lambda:verify(bad))
    bad=deepcopy(packet); bad['record']['seam_vertices']=source['record']['seam_vertices']; bad['root']=digest(bad['record'])
    checks['rehashed_full_potential_seam_substitution_rejected']=rejected(lambda:verify(bad))
    checks['complete_serialized_pullback_reverifies']=verify(json.loads(json.dumps(packet)))==report
    result={'schema':'marici.host-coefficient-pullback-check.v1','passed':all(checks.values()),'checks':checks,'pullback':report,
            'host_grid_fiber_census':dict(counts),'tested_compatible_pairs':tests,
            'center_fiber':[list(map(str,v)) for v in center],'omitted_fold_interiors':omitted,'closed_host_loop_lifts':loop,
            'root':packet['root'],'source_root':source['root'],'source_file_sha256':sha256(SOURCE.read_bytes()).hexdigest(),
            'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'disposition':'The stricter fixed-position coefficient pullback is a disk with two center lifts and an AB seam. It fails full inward-fold retention. This rejects that additional matching contract, not the original direction-bearing proposal.'}
    out=BASE/'results'
    (out/'host_coefficient_pullback_store.json').write_text(json.dumps(packet,indent=2)+'\n',encoding='utf-8')
    (out/'host_coefficient_pullback.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
    if not result['passed']: raise SystemExit(1)

if __name__=='__main__': main()
