"""Coefficient-matched pullback of the actual host root link and electron
sphere. No host inward-depth map, phase twist, or isotope label is inserted.
"""
from fractions import Fraction as Q
from itertools import permutations
from pathlib import Path
from hashlib import sha256
import json
from check_geometric_cycle_reversal import geo, SOURCE, verify, ONE, conj
from check_reversed_coefficient_attachment import weight, ZERO, times, div, multiply
from check_retained_barycenter_attachment import cells_of, topology, rank_columns

BASE=Path(__file__).resolve().parents[1]

def bary(ids): return tuple(Q(i in ids,len(ids)) for i in range(4))
def swap(v): return (v[1],v[0],v[2],v[3])
def quotient(v): return tuple(v[i]+v[3]/3 for i in range(3))
def host_lift(u):
    m=min(u)
    return tuple(x-m/4 for x in u)+(3*m/4,)
def upper(u): return tuple(u)+(Q(0),)
def lower(u):
    m=min(u)
    return tuple(x-m for x in u)+(3*m,)
def xyz(v): return tuple(sum(v[i]*geo.POINTS['ABCD'[i]][j] for i in range(4)) for j in range(3))
def average(points): return tuple(sum(p[i] for p in points)/len(points) for i in range(len(points[0])))
def apply(p,v): return [row[0] for row in multiply(p,[[(x,Q(0))] for x in v])]
def contained(v,order):
    return v[order[3]]==0 and v[order[0]]>=v[order[1]]>=v[order[2]]>=0

def main():
    original=SOURCE.read_bytes(); source=json.loads(original); evidence,rows=verify(source)
    p=[[ZERO]*3 for _ in range(3)]
    for r in rows:
        if r['source'][:2]==['raw','AB'] and r['target'][:2]==['local','AB']:
            p['xyz'.index(r['target'][2])]['xyz'.index(r['source'][2])]=weight(r)
    F=xyz(bary((0,1,2)))
    X=geo.transpose((F,geo.POINTS['A'],geo.POINTS['B']))
    c=(ONE,geo.OMEGA,geo.zmul(geo.OMEGA,geo.OMEGA)); v=geo.zmv(X,c)
    D=[div(x,conj(x)) for x in v]
    reversed_p=[[conj(x) for x in row] for row in p]
    aligned=[[times(D[i],x) for x in row] for i,row in enumerate(reversed_p)]
    reflection=geo.rotation((1,0,2,3))
    orders=list(permutations(range(4)))
    pairs={}; faces=[]; owners=[]; image_faces=[]; host_faces=[]
    def put(e):
        u=quotient(swap(e)); h=host_lift(u)
        key='e:'+','.join(map(str,e)); pairs[key]=(h,e,u); return key
    # The lower disk has 18 original triangles. Its projected image supplies
    # a common refinement of the upper disk and the host's six-triangle link.
    for order in orders:
        if order[3]==3: continue
        low=[bary(order[:k]) for k in (1,2,3)]
        for points in (low,[upper(quotient(x)) for x in low]):
            es=[swap(x) for x in points]
            refs=tuple(sorted(put(e) for e in es)); faces.append(refs)
            matches=[o for o in orders if all(contained(e,o) for e in es)]
            assert len(matches)==1
            owners.append(matches[0])
            us=[quotient(swap(e)) for e in es]
            host_owner=[o for o in permutations(range(3)) if all(u[o[0]]>=u[o[1]]>=u[o[2]] for u in us)]
            assert len(host_owner)==1
            image_faces.append(tuple(sorted('u:'+','.join(map(str,u)) for u in us)))
            host_faces.append(tuple(sorted('h:'+','.join(map(str,host_lift(u))) for u in us)))
    qtop=topology(cells_of(faces)); htop=topology(cells_of(host_faces)); itop=topology(cells_of(image_faces))
    mode_ok=True; affine=True; seam=set()
    for refs in faces:
        us=[pairs[r][2] for r in refs]
        common_min=set(range(3))
        for u in us: common_min &= {i for i in range(3) if u[i]==min(u)}
        affine &= bool(common_min)
        samples=[pairs[r][1] for r in refs]+[average([pairs[r][1] for r in refs])]
        for e in samples:
            u=quotient(swap(e)); h=host_lift(u)
            host_vector=tuple(x-y for x,y in zip(xyz(h),F))
            mode_ok &= apply(p,host_vector)==apply(aligned,xyz(e))
            if min(u)==0: seam.add(tuple(e))
    original_e={bary(o[:k]) for o in orders for k in (1,2,3)}
    original_h={bary((0,1,2,3))}|{bary(o[:k]) for o in permutations(range(3)) for k in (1,2)}
    fiber_tests=[]
    for a in range(13):
        for b in range(13-a):
            u=(Q(a,12),Q(b,12),Q(12-a-b,12))
            es=[swap(upper(u)),swap(lower(u))]
            fiber_tests.append(len(set(es))==(1 if min(u)==0 else 2)
                and all(quotient(swap(e))==u for e in es)
                and quotient(host_lift(u))==u)
    # Exact real rank of the local mode, not an assumption from a drawing.
    real_columns=[{i:p[i%3][j][i//3] for i in range(6)} for j in range(3)]
    checks={
        'source_verified':evidence['verified'],
        'phase_aligned_reverse_mode_equals_projector_after_real_AB_reflection':
            aligned==multiply(p,[[(x,Q(0)) for x in row] for row in reflection]),
        'local_mode_real_rank_is_two':rank_columns(real_columns)==2,
        'root_displacement_is_in_projector_kernel':apply(p,F)==[ZERO]*3,
        'paired_vertices_and_cells_match_actual_coefficients':mode_ok,
        'maps_affine_on_every_refined_cell':affine,
        'pullback_direction_complex_is_sphere':qtop['cells']==[20,54,36,0] and qtop['rational_betti']==[1,0,1,0],
        'refined_host_link_is_disk':htop['cells']==[13,30,18,0] and htop['rational_betti']==[1,0,0,0],
        'common_coefficient_chart_is_disk':itop==htop,
        'electron_projection_is_bijective_on_atlas_vertices':len({e for h,e,u in pairs.values()})==len(pairs),
        'all_original_electron_direction_vertices_retained':original_e<={e for h,e,u in pairs.values()},
        'all_original_host_link_vertices_retained':original_h<={h for h,e,u in pairs.values()},
        'all_twenty_four_electron_flags_have_refined_owners':set(owners)==set(orders),
        'six_atlas_seam_vertices_are_single_not_double':len(seam)==6,
        'exact_image_grid_has_two_interior_and_one_boundary_preimages':all(fiber_tests),
        'source_unchanged':SOURCE.read_bytes()==original,
    }
    packet={'kind':'retained-direction-coefficient-pullback',
        'source_root':source['root'],
        'maps':{'host':'L_AB (x - F_ABC), x in the actual host root link',
                'electron':'D_AB conjugate(L_AB) d, d on the electron direction sphere',
                'relation':'equality in the same complex three-coordinate output space'},
        'vertices':{key:{'host_barycentric':list(map(str,h)),'electron_barycentric':list(map(str,e)),
                         'image_chart':list(map(str,u))} for key,(h,e,u) in sorted(pairs.items())},
        'triangles':[list(f) for f in faces],
        'original_electron_flag_owners':[''.join('ABCD'[i] for i in o) for o in owners],
        'host_refined_triangles':[list(f) for f in sorted(set(host_faces))]}
    result={'verification_passed':all(checks.values()),'checks':checks,
        'topology':{'direction_pullback':qtop,'host_link':htop,'coefficient_chart':itop},
        'formulas':{'u':'quotient of electron barycentrics after swapping A and B',
                    'm':'min(u_A,u_B,u_C)',
                    'host':'(u_A-m/4,u_B-m/4,u_C-m/4,3m/4)',
                    'electron_upper':'swap_AB(u_A,u_B,u_C,0)',
                    'electron_lower':'swap_AB(u_A-m,u_B-m,u_C-m,3m)'},
        'outcome':'The direction interaction is an explicit pullback sphere, projecting bijectively to the electron sphere and two-to-one to the host link interior. '
                  'The two sheets meet along their seam; they are not two isotope closures.',
        'scope':'direction links only; no identification of radial depths and no new solid carrier',
        'source_sha256':sha256(original).hexdigest(),
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (BASE/'results/retained_direction_attachment_store.json').write_text(json.dumps(packet,indent=2)+'\n',encoding='utf-8')
    (BASE/'results/retained_direction_attachment.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
    if not result['verification_passed']: raise SystemExit(1)

if __name__=='__main__': main()
