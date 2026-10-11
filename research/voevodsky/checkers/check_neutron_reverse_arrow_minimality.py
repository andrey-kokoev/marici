"""Reverse the retained neutron panels into arrow occurrences and certify
minimal generator sets under explicit rotation-only replay grammars.
This is not a bit-complexity or unrestricted construction-minimality theorem.
"""
from fractions import Fraction as F
from itertools import permutations,product,combinations
from collections import Counter
from pathlib import Path
from hashlib import sha256
import json
from check_belt_operator_inputs import frame,action,det,mode,mean
from check_belt_three_by_twelve import decode
from check_coupled_six_piece_belt import R,Z,norm

BASE=Path(__file__).resolve().parents[1]
ROOT=BASE.parents[1]


def record(triangle):
    center,a,b=triangle
    face=tuple(center[2:].split('_'))
    assert a in face and b in face and a!=b
    return face,a,b


def move(r,rename):
    face,a,b=r
    return tuple(sorted(rename[x] for x in face)),rename[a],rename[b]


def closure(seeds,renames):
    out=set(seeds);todo=list(seeds)
    while todo:
        r=todo.pop()
        for rename in renames:
            image=move(r,rename)
            if image not in out:out.add(image);todo.append(image)
    return out


def triangle(r):
    face,a,b=r
    return ('F_'+'_'.join(face),a,b)


def encoded_record(r):
    face,a,b=r
    return dict(face_vertices=list(face),tail=a,head=b)


def main():
    geometry_path=BASE/'results/four_six_center_cones.json'
    ambient_path=BASE/'results/coupled_six_piece_belt_store.json'
    intrinsic_path=BASE/'results/belt_three_by_twelve_store.json'
    geometry=json.loads(geometry_path.read_text(encoding='utf-8'))
    packet=json.loads(ambient_path.read_text(encoding='utf-8'));source=packet['record']
    assert sha256(json.dumps(source,sort_keys=True,separators=(',',':')).encode()).hexdigest()==packet['root']
    assert source['geometry_sha256']==sha256(geometry_path.read_bytes()).hexdigest()
    intrinsic=json.loads(intrinsic_path.read_text(encoding='utf-8'))
    assert intrinsic['source_root']==packet['root']
    target={record(t) for t in source['triangles']}
    assert len(target)==18
    points={k:tuple(map(F,v)) for k,v in geometry['belt_scaled_coordinates'].items() if k!='O'}
    coords={k:frame(v) for k,v in points.items()};inverse={v:k for k,v in coords.items()}
    identity={k:k for k in points}
    rotation=((F(0),F(0),F(1)),(F(1),F(0),F(0)),(F(0),F(1),F(0)))
    c3={k:inverse[action(rotation,v)] for k,v in coords.items()}
    # Recover the previously audited six proper source-frame symmetries. No
    # face or triangle mapping is stored in a replay rule: only vertex action.
    symmetries=[]
    for p in permutations(range(3)):
        for signs in product((-1,1),repeat=3):
            matrix=tuple(tuple(F(signs[i] if j==p[i] else 0) for j in range(3)) for i in range(3))
            if det(matrix)!=1:continue
            changed={k:action(matrix,v) for k,v in coords.items()}
            if not all(v in inverse for v in changed.values()):continue
            rename={k:inverse[v] for k,v in changed.items()}
            if {move(r,rename) for r in target}==target:symmetries.append(rename)
    assert len(symmetries)==6
    reference_indices=intrinsic['triangle_order'][:6]
    c3_seeds=[record(source['triangles'][i]) for i in reference_indices]
    assert closure(c3_seeds,[c3])==target
    reports=[]
    for name,rules in [('explicit_occurrences',[identity]),('sector_C3',[c3]),('proper_source_symmetries',symmetries)]:
        remaining=set(target);orbits=[]
        while remaining:
            orbit=closure([min(remaining)],rules)
            assert orbit<=remaining
            remaining-=orbit;orbits.append(orbit)
        seeds=c3_seeds if name=='sector_C3' else [min(o) for o in orbits]
        assert len(seeds)==len(orbits) and closure(seeds,rules)==target
        missing=[len(target-closure(seeds[:i]+seeds[i+1:],rules)) for i in range(len(seeds))]
        assert all(n>0 for n in missing)
        # Exhaustively test all smaller subsets for the 3- and 6-seed claims.
        # Orbit invariance is also a general proof: a seed cannot leave its orbit.
        tested=0
        if len(orbits)<=6:
            orbit_id={r:i for i,o in enumerate(orbits) for r in o}
            for size in range(len(orbits)):
                for candidates in combinations(sorted(target),size):
                    assert len({orbit_id[r] for r in candidates})<len(orbits)
                    tested+=1
        reports.append(dict(grammar=name,orbit_sizes=sorted(map(len,orbits)),minimum_seed_occurrences=len(orbits),
            seeds=[encoded_record(r) for r in seeds],missing_after_each_seed_deletion=missing,
            smaller_subsets_checked=tested,vertex_actions=rules))
    assert [r['minimum_seed_occurrences'] for r in reports]==[18,6,3]
    # Reassemble each oriented face from its three boundary occurrences.
    recovered_faces={}
    for face in {r[0] for r in target}:
        arrows={(a,b) for f,a,b in target if f==face}
        assert len(arrows)==3
        assert Counter(a for a,b in arrows)==Counter(b for a,b in arrows)==Counter(face)
        start=min(face);nxt=dict(arrows)
        cycle=(start,nxt[start],nxt[nxt[start]])
        assert nxt[cycle[-1]]==start
        recovered_faces[face]=cycle
    assert set(recovered_faces)=={tuple(sorted(f)) for f in geometry['belt_faces']}
    edges=Counter(tuple(sorted((a,b))) for _,a,b in target)
    assert len(edges)==12 and Counter(edges.values())=={1:6,2:6}
    directed={(a,b) for _,a,b in target}
    assert len(directed)==18
    directed_triangles=set()
    for a,b,c in permutations(sorted(points),3):
        if a==min(a,b,c) and all(edge in directed for edge in ((a,b),(b,c),(c,a))):
            directed_triangles.add(tuple(sorted((a,b,c))))
    assert len(directed_triangles)==8
    extra_cycles=directed_triangles-set(recovered_faces)
    assert extra_cycles=={('U0','U1','U2'),('L0','L1','L2')}
    # A directed cycle alone is not an admitted filled face. The extra cap
    # cycles do not silently supply the missing face witnesses or orientations.
    # Losing incident-face identity is a real lossy map if face reconstruction
    # rules are not additionally admitted: the two shared-edge occurrences differ.
    collisions=[(edge,[r for r in target if tuple(sorted(r[1:]))==edge]) for edge,n in edges.items() if n==2]
    assert len(collisions)==6 and all(rows[0][0]!=rows[1][0] for _,rows in collisions)
    # Rebuild all native local modes from reconstructed arrow records and the
    # existing frame/character rule, not from a new fitted coefficient table.
    rebuilt_points=dict(points)
    for face in recovered_faces:rebuilt_points['F_'+'_'.join(face)]=mean([points[k] for k in face])
    modes={}
    for r in target:
        re,im=mode(triangle(r),rebuilt_points)
        modes[triangle(r)]=tuple((R(*a),R(*b)) for a,b in zip(re,im))
    expected=tuple(decode(z) for z in source['collective_vector'])
    recovered=tuple(z for t in source['triangles'] for z in modes[tuple(t)])
    assert recovered==expected
    reversed_controls=0
    for r in target:
        f,a,b=r
        re,im=mode(triangle((f,b,a)),rebuilt_points)
        reversed_mode=tuple((R(*x),R(*y)) for x,y in zip(re,im))
        assert reversed_mode!=modes[triangle(r)]
        assert sum(norm(z) for z in reversed_mode)==sum(norm(z) for z in modes[triangle(r)])
        reversed_controls+=1
    # Stronger geometric replay need not preserve the separately retained native
    # adjacent-pair grouping. Count that explicitly rather than calling it a
    # symmetry of the entire operator implementation.
    groups={frozenset(record(source['triangles'][i]) for i in intrinsic['triangle_order'][j:j+6]) for j in range(0,18,6)}
    group_preservers=sum({frozenset(move(r,s) for r in group) for group in groups}==groups for s in symmetries)
    ordered=[tuple(source['triangles'][i]) for i in intrinsic['triangle_order']]
    slots={t:i for i,t in enumerate(ordered)}
    values=[(F(c['d']),tuple(map(F,c['selected_numerator']))) for c in intrinsic['coordinates']]
    operators={(a['stage'],a['target'],a['source']):tuple(map(F,a['numerator'])) for a in intrinsic['arrows']}
    for rename in symmetries:
        permutation=[2*slots[triangle(move(record(t),rename))]+axis for t in ordered for axis in range(2)]
        assert all(values[i]==values[permutation[i]] for i in range(36))
        moved={(stage,permutation[i],permutation[j]):value for (stage,i,j),value in operators.items()}
        assert moved==operators
    counts=Counter(a['stage'] for a in intrinsic['arrows'])
    assert counts=={'L':432,'G':108,'N':1296}
    result=dict(verification_passed=True,shape_to_arrow_roundtrip=True,native_54_coordinate_mode_roundtrip=True,
        full_occurrences=18,distinct_directed_endpoint_pairs=18,distinct_undirected_segments=12,
        single_incidence_rim_edges=6,double_incidence_stitches=6,orientation_loss_controls=reversed_controls,
        endpoint_graph_triangle_cycles=8,extra_unadmitted_cap_cycles=[list(f) for f in sorted(extra_cycles)],
        all_six_symmetries_preserve_intrinsic_metric_modes_and_operators=True,
        replay_contract='Only supplied rotations create new occurrence records; closure/relabeling preserves face provenance. No endpoint composition, reversal, convex-hull inference, or face inference is implicit.',
        minimality_reports=reports,proper_symmetries_preserving_native_pair_partition=group_preservers,
        supplementary_retained_data=['vertex metric/coordinates','rotation actions','native phase character and coefficient frame','chosen adjacent-pair grouping for native operators','occurrence and identification provenance'],
        fixed_intrinsic_coefficient_arrow_counts=dict(counts),fixed_intrinsic_coefficient_arrow_total=1836,
        unrestricted_program_minimality_proved=False,physical_neutron_identification=False,
        source_hashes={str(p.relative_to(ROOT)).replace('\\','/'):sha256(p.read_bytes()).hexdigest() for p in
            [Path(__file__),geometry_path,ambient_path,intrinsic_path,BASE/'checkers/check_belt_operator_inputs.py']})
    (BASE/'results/neutron_reverse_arrow_minimality.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
