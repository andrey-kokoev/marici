"""Mode-derived oriented area, radial flux, and paired opposite circulation.
The observable is declared: radial solid-angle flux at unit collective
amplitude. Its local orientation comes from the existing cyclic mode, not
from assigning a charge to a named particle. Opposite branches are tested
as a new belt mode, without overwriting the all-same-branch source.
"""
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
from math import sqrt,atan2,pi
from collections import Counter
import json
from check_coupled_six_piece_belt import R,Z,ONE,add,mul,conj,scale,norm,encoded
from check_belt_three_by_twelve import sparse_product,decode
from check_belt_operator_inputs import mean,frame,action

BASE=Path(__file__).resolve().parents[1]

def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def vecscale(s,a):return tuple(s*x for x in a)
def solid_angle(a,b,c):
    la,lb,lc=[sqrt(dot(v,v)) for v in (a,b,c)]
    return 2*atan2(dot(a,cross(b,c)),la*lb*lc+dot(a,b)*lc+dot(b,c)*la+dot(c,a)*lb)
def area_identity(triangle):
    f,a,b=triangle;r=sub(f,vecscale(Q(1,2),tuple(x+y for x,y in zip(a,b))));s=vecscale(Q(1,2),sub(a,b))
    area=vecscale(Q(1,2),cross(sub(a,f),sub(b,f)))
    assert cross(r,s)==area
    assert cross(r,vecscale(-1,s))==vecscale(-1,area)
    # A common complex amplitude changes area by |z|², never its sign.
    for x,y in [(Q(1),Q(0)),(-Q(1,2),Q(1,2)),(Q(2),-Q(1))]:
        rr=tuple(x*a-3*y*b for a,b in zip(r,s));ss=tuple(y*a+x*b for a,b in zip(r,s))
        assert cross(rr,ss)==vecscale(x*x+3*y*y,area)
    return area

def main():
    paths={name:BASE/f'results/{name}.json' for name in ['four_six_center_cones','belt_three_by_twelve','belt_three_by_twelve_store','coupled_six_piece_belt_store','belt_operator_inputs']}
    raw={k:p.read_bytes() for k,p in paths.items()};data={k:json.loads(v) for k,v in raw.items()}
    geo=data['four_six_center_cones'];intr=data['belt_three_by_twelve_store'];ambient=data['coupled_six_piece_belt_store']['record']
    assert intr['source_root']==data['coupled_six_piece_belt_store']['root']
    points={k:tuple(map(Q,v)) for k,v in geo['belt_scaled_coordinates'].items()}
    physical=lambda p:(sqrt(3)*float(p[0]),float(p[1]),float(p[2]))
    faces=geo['belt_faces'];signs=[];angles=[];vector_sum=(Q(0),)*3
    for f in faces:
        vertices=[points[k] for k in f];F=mean(vertices)
        sign=1 if F[1]>0 else -1;signs.append(sign)
        for j in range(3):
            area=area_identity((F,vertices[j],vertices[(j+1)%3]));vector_sum=tuple(x+y for x,y in zip(vector_sum,area))
        angles.append(solid_angle(*map(physical,vertices)))
    assert vector_sum==(0,0,0) and Counter(signs)=={-1:3,1:3}
    # Equal solid angles are certified by the actual proper rotations, not
    # merely a floating-point comparison of six decimal values.
    coords={k:frame(v) for k,v in points.items()};inv={v:k for k,v in coords.items()}
    rotations=[tuple(tuple(Q(x) for x in row) for row in r) for r in data['belt_operator_inputs']['group_matrices']]
    orbit={frozenset(inv[action(r,coords[k])] for k in faces[0]) for r in rotations}
    assert orbit=={frozenset(f) for f in faces}
    pairs=data['belt_three_by_twelve']['adjacent_face_matchings'][0]
    assert all(signs[a]+signs[b]==0 for a,b in pairs)
    belt_edges=[(i,j) for i in range(6) for j in range(i+1,6) if len(set(faces[i])&set(faces[j]))==2]
    assert len(belt_edges)==6 and all(signs[i]==-signs[j] for i,j in belt_edges)
    # Derive the alternating pattern from shared-face adjacency, independently
    # of the vertical coordinate used above. Connected C6 has exactly two
    # nonzero +/- patterns; they differ only by overall reversal.
    patterns=[[1 if mask&(1<<i) else -1 for i in range(6)] for mask in range(64)]
    alternating=[p for p in patterns if all(p[i]==-p[j] for i,j in belt_edges)]
    assert len(alternating)==2 and signs in alternating
    proton_edges=[(i,j) for i in range(4) for j in range(i+1,4)]
    proton_alternating=[[1 if mask&(1<<i) else -1 for i in range(4)] for mask in range(16)]
    proton_alternating=[p for p in proton_alternating if all(p[i]==-p[j] for i,j in proton_edges)]
    # Proton flux: original regular tetrahedron, oriented outward; subdivision
    # into centroid-edge triangles is identical to the source construction.
    P={'A':(Q(1),Q(1),Q(1)),'B':(Q(1),-Q(1),-Q(1)),
       'C':(-Q(1),Q(1),-Q(1)),'D':(-Q(1),-Q(1),Q(1))}
    proton_faces=[tuple('ABC'),tuple('ADB'),tuple('ACD'),tuple('BDC')]
    proton_angles=[];pv=(Q(0),)*3
    for f in proton_faces:
        vertices=[P[k] for k in f];F=mean(vertices)
        for j in range(3):
            a=area_identity((F,vertices[j],vertices[(j+1)%3]));pv=tuple(x+y for x,y in zip(pv,a))
        proton_angles.append(solid_angle(*[tuple(map(float,p)) for p in vertices]))
    assert pv==(0,0,0)
    proton_flux=sum(proton_angles)/(4*pi);uniform_flux=sum(angles)/(4*pi)
    paired_flux=sum(s*a for s,a in zip(signs,angles))/(4*pi)
    cap_angles=[abs(solid_angle(*[physical(points[k]) for k in cap[1:]])) for cap in geo['missing_cap_tetrahedra']]
    assert abs(sum(angles)+sum(cap_angles)-4*pi)<1e-12
    # Construct the new opposite-branch intrinsic mode in the SAME 36 ports.
    # Its embedding, metric factors and placements are unchanged.
    d=tuple(Q(c['d']) for c in intr['coordinates']);oldz=tuple(decode(c['selected_numerator']) for c in intr['coordinates'])
    owner=ambient['face_owners'];coordinate_signs=[signs[owner[c['triangle']]] for c in intr['coordinates']]
    z=tuple(v if s==1 else conj(v) for v,s in zip(oldz,coordinate_signs))
    assert z[:12]==z[12:24]==z[24:] and z!=oldz
    n=sum(norm(z[i])/d[i] for i in range(12));assert n==sum(norm(oldz[i])/d[i] for i in range(12))
    L={(i,j):scale(1/n,mul(z[i],conj(z[j]))) for i in range(36) for j in range(36) if i//12==j//12}
    G={(i,j):(R(d[i]/3),R()) for i in range(36) for j in range(36) if i%12==j%12}
    N={(i,j):scale(1/(3*n),mul(z[i],conj(z[j]))) for i in range(36) for j in range(36)}
    assert sparse_product(G,L,d)==sparse_product(L,G,d)==N and sparse_product(N,N,d)==N
    used=[set(),set(),set()];cycle_sum=Z
    for (i,k),g in G.items():
        for j in range(12*(k//12),12*(k//12+1)):
            w=scale(1/(d[i]*d[j]*d[k]),mul(N[j,i],mul(g,L[k,j])))
            assert w[1]==0 and w[0].b==0 and w[0].a>0
            cycle_sum=add(cycle_sum,w);used[0].add((k,j));used[1].add((i,k));used[2].add((j,i))
    assert cycle_sum==ONE and all(set(m)==s for m,s in zip((L,G,N),used))
    old_matrices={s:{} for s in ('L','G','N')}
    for a in intr['arrows']:old_matrices[a['stage']][a['target'],a['source']]=decode(a['numerator'])
    changes={s:sum(v!=old_matrices[s][e] for e,v in m.items()) for s,m in zip(('L','G','N'),(L,G,N))}
    # The old local triangle selector does not accept the opposite branch.
    u=tuple(decode(x) for x in ambient['collective_vector']);rejected=0
    for t in range(18):
        v=u[3*t:3*t+3];vbar=tuple(map(conj,v));ns=sum(map(norm,v))
        overlap=Z
        for a,b in zip(v,vbar):overlap=add(overlap,mul(conj(a),b))
        projected=tuple(scale(1/ns,mul(a,overlap)) for a in v)
        if signs[owner[t]]<0:
            assert projected!=vbar;rejected+=1
    # This particular flux direction is signed by chirality. Electrical phase
    # rotations cannot provide the cancellation; conjugation reverses it.
    checks={
        'local_mode_area_equals_oriented_geometric_triangle_area':True,
        'conjugation_reverses_area_but_phase_multiplication_does_not':True,
        'plain_vector_area_sum_vanishes_for_both_figures':pv==vector_sum==(0,0,0),
        'outward_proton_radial_flux_is_one':abs(proton_flux-1)<1e-12,
        'all_same_branch_belt_has_nonzero_radial_flux':0<uniform_flux<1,
        'six_face_fluxes_equal_by_exact_rotation_witness':len(orbit)==6,
        'each_geometric_pair_has_opposite_branches':all(signs[a]+signs[b]==0 for a,b in pairs),
        'whole_belt_face_adjacency_derives_two_alternating_patterns':len(alternating)==2 and signs in alternating,
        'proton_K4_adjacency_cannot_alternate_on_every_interface':len(proton_alternating)==0,
        'paired_belt_flux_cancels_exactly_by_signed_equal_face_counts':sum(signs)==0,
        'new_mode_preserves_three_identical_twelve_coordinate_sectors':z[:12]==z[12:24]==z[24:],
        'new_operators_have_exact_rank_one_return':sparse_product(G,L,d)==N,
        'new_support_counts_remain_432_108_1296':list(map(len,(L,G,N)))==[432,108,1296],
        'positive_cycle_deletion_certificate_survives':cycle_sum==ONE,
        'old_local_selectors_reject_all_nine_conjugated_triangles':rejected==9,
        'source_files_unchanged':all(paths[k].read_bytes()==v for k,v in raw.items()),
    }
    report={'verification_passed':all(checks.values()),'checks':checks,
        'observable':'Q=sum of mode-oriented radial solid angles / (4*pi), at unit collective amplitude; not an assumed identity charge operator',
        'results':{'proton_all_outward':'1','conjugated_proton':'-1','original_belt_all_same_branch_approx':uniform_flux,
                   'paired_opposite_branch_belt':'0','paired_flux_decimal_control':paired_flux},
        'belt_face_signs':signs,'sector_pairs':pairs,'pairwise_cancellation':['0']*3,
        'adjacency_comparison':{'belt':'C6; exactly two alternating branch patterns','proton':'K4; no fully alternating branch pattern',
                                'belt_shared_face_edges':belt_edges,'belt_patterns':alternating},
        'branch_rule_status':'Alternation across every shared face is a tested additional rule, not a consequence of the old all-positive mode constructor. Its impossibility on K4 does not by itself select the proton positive branch.',
        'new_intrinsic_operator_support':{'L':len(L),'G':len(G),'N':len(N),'total':sum(map(len,(L,G,N)))},
        'changed_existing_coefficients':changes,
        'what_changed':'Conjugate the three face modes on one side of the belt midplane. Each two-face sector then has opposite circulation. Geometry, intrinsic coordinates and counts remain fixed; local and collective selectors change.',
        'what_did_not_work':'Openings alone did not give neutrality. The old all-same-branch belt has about half a unit of this flux, and multiplying its amplitudes by phases cannot reverse local flux.',
        'remaining_generation_question':'Does the endpoint assembly select the opposite branch on the opposite side, rather than this being an additional branch-selection rule?',
        'source_roots':{'ambient':intr['source_root']},'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    store={'source_root':intr['source_root'],'source_intrinsic_sha256':sha256(raw['belt_three_by_twelve_store']).hexdigest(),
        'face_signs':signs,'coordinates':intr['coordinates'],'selected_numerators':[encoded(v) for v in z],
        'coefficient_convention':intr['coefficient_convention'],
        'arrows':[{'stage':s,'target':i,'source':j,'numerator':encoded(v)} for s,m in zip(('L','G','N'),(L,G,N)) for (i,j),v in sorted(m.items())]}
    (BASE/'results/mode_flux_charge.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    (BASE/'results/opposite_branch_belt_store.json').write_text(json.dumps(store,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))
    if not report['verification_passed']:raise SystemExit(1)

if __name__=='__main__':main()
