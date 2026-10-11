"""Exact source five-cycle transport of the existing pentachoron mismatch modes.
Reuses the predecessor's arithmetic and geometric interface convention.
No fitted energy/rank or physical clock is introduced. The additional
cycle-defect energy is an explicitly declared conditional extension.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
from hashlib import sha256
import json
from check_pentachoron_spin_interfaces import (
    A, S2, S3, S5, CI, ZERO, ONE, I, dot, sub, wedge, chiral,
    pauli, add, scale, mm, adj, rank, constraints,
)

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / 'research/voevodsky'


def eye(n):
    return tuple(tuple(A(i == j) for j in range(n)) for i in range(n))


def power(m, n):
    out = eye(len(m))
    for _ in range(n):
        out = mm(m, out)
    return out


def trace(m):
    return sum((m[i][i] for i in range(len(m))), ZERO)


def act(m, v):
    return tuple(dot(row, v) for row in m)


def record(m):
    return [[x.record() for x in row] for row in m]


def main():
    source_path = BASE / 'inputs/relative-electron.json'
    source = json.loads(source_path.read_text(encoding='utf-8'))
    assert len(source['generators']) == 1
    assert source['seeds'] == [{'point': [0, 0, 0, 0], 'role': 'attachment_pole'}]
    vertices = [tuple(A(x) for x in v)+(ZERO,) for v in
                [(1,1,1), (1,-1,-1), (-1,1,-1), (-1,-1,1)]]
    vertices.append((ZERO, ZERO, ZERO, S5))
    center = (ZERO, ZERO, ZERO, S5/5)
    axes = eye(4)
    # H_04 H_03 H_02 H_01 sends A->B->C->D->E->A.
    ns = [tuple(x/(2*S2) for x in sub(vertices[0], vertices[j])) for j in range(1,5)]
    reflections = [tuple(tuple(A(i == j)-2*n[i]*n[j] for j in range(4)) for i in range(4)) for n in ns]
    rotation = eye(4)
    for h in reflections:
        rotation = mm(h, rotation)
    assert mm(adj(rotation), rotation) == eye(4)
    assert power(rotation, 5) == eye(4)
    for c in range(5):
        assert act(rotation, sub(vertices[c], center)) == sub(vertices[(c+1)%5], center)
    # Source origin is the attachment pole E; the four affine columns are A-E,...,D-E.
    basis = tuple(zip(*(sub(vertices[j], vertices[4]) for j in range(4))))
    metric = tuple(tuple(A(x) for x in row) for row in source['metric'])
    generator = tuple(tuple(A(x) for x in row) for row in source['generators'][0]['matrix'])
    translation = tuple(A(x) for x in source['generators'][0]['translation'])
    assert mm(adj(basis), basis) == metric
    assert mm(rotation, basis) == mm(basis, generator)
    assert act(basis, translation) == sub(vertices[0], vertices[4])

    normals = [tuple(-S5*x/4 for x in sub(v, center)) for v in vertices]
    edges = list(combinations(range(5), 2))
    triangles = {}
    for c in range(5):
        facet = [i for i in range(5) if i != c]
        for j,d in enumerate(facet):
            f = [i for i in facet if i != d]
            triangles[c,d] = scale(A((-1)**(c+j+1)), wedge(sub(vertices[f[1]],vertices[f[0]]), sub(vertices[f[2]],vertices[f[0]])))
    i10 = eye(10)
    constant = tuple(tuple(A(F(1,5)) if i%2 == j%2 else ZERO for j in range(10)) for i in range(10))
    cell4 = tuple(tuple(A(i == j and i >= 8) for j in range(10)) for i in range(10))
    results = []
    for sign in (1, -1):
        # A pair of reflections has a chiral lift <a,b>I+i s(a wedge b).sigma.
        def pair(a,b):
            return add(scale(dot(a,b), I), scale(CI, pauli(chiral(wedge(a,b), sign))))
        spin = mm(pair(ns[3], ns[2]), pair(ns[1], ns[0]))
        assert mm(adj(spin), spin) == I
        assert spin[0][0]*spin[1][1]-spin[0][1]*spin[1][0] == 1
        for a,b in combinations(range(4),2):
            before = pauli(chiral(wedge(axes[a], axes[b]), sign))
            after = pauli(chiral(wedge(act(rotation, axes[a]), act(rotation, axes[b])), sign))
            assert mm(mm(spin, before), adj(spin)) == after
        assert power(spin, 5) == scale(A(-1), I)
        assert power(scale(A(-1), spin), 5) == I

        projectors = {key: scale(A(F(1,2)), add(I, scale(A(-1), pauli(tuple(x/(4*S3) for x in chiral(b,sign)))))) for key,b in triangles.items()}
        folds = {}
        cosine = S2*S3/4
        for a,b in edges:
            k = tuple(x/(2*cosine) for x in chiral(wedge(normals[a], normals[b]), sign))
            folds[a,b] = add(scale(cosine,I), scale(-CI,pauli(k)))
            folds[b,a] = adj(folds[a,b])
        assert any(projectors[c,d] != projectors[(c+1)%5,(d+1)%5] for c,d in projectors), 'Bare cell permutation must fail the face-frame covariance control'
        for c,d in projectors:
            nxt = ((c+1)%5, (d+1)%5)
            assert mm(mm(spin, projectors[c,d]), adj(spin)) == projectors[nxt]
            assert mm(mm(spin, folds[c,d]), adj(spin)) == folds[nxt]
        full = constraints({(a,b):(folds[a,b], I) for a,b in edges})
        inherited = constraints({(a,b):(mm(folds[a,b], projectors[a,b]), projectors[b,a]) for a,b in edges})
        assert rank(full) == rank(inherited) == 10
        laplacian = mm(adj(full), full)
        low_energy, high_energy = A(4)-S2*S3, A(4)+2*S2*S3/3
        low = scale((high_energy-low_energy).inverse(), add(scale(high_energy,i10), scale(A(-1),laplacian)))
        assert adj(low) == low and mm(low,low) == low and rank(low) == 4
        assert mm(laplacian, low) == scale(low_energy, low)
        assert mm(laplacian, add(i10,scale(A(-1),low))) == scale(high_energy,add(i10,scale(A(-1),low)))
        transport = tuple(tuple(spin[i%2][j%2] if i//2 == (j//2+1)%5 else ZERO for j in range(10)) for i in range(10))
        assert mm(adj(transport), transport) == i10
        assert power(transport,5) == scale(A(-1), i10)
        assert power(transport,10) == i10
        assert mm(transport,laplacian) == mm(laplacian,transport)
        assert mm(transport,low) == mm(low,transport)
        # Reverse every prefix, not only the final endpoint.
        for t in range(11):
            forward = power(transport,t)
            assert mm(adj(forward),mm(forward,low)) == low

        assert mm(low,constant) == constant
        residual = add(low, scale(A(-1),constant))
        for p in (constant,residual):
            assert adj(p) == p and mm(p,p) == p and rank(p) == 2
            assert mm(transport,p) == mm(p,transport)
            assert mm(laplacian,p) == scale(low_energy,p)
            # Each doublet separately extends the old ABCD logical spinor;
            # local amplitude alone does not choose between the extensions.
            extension = tuple(tuple(S5*row[8+j] for j in range(2)) for row in p)
            assert mm(adj(extension),extension) == I
            assert mm(extension,adj(extension)) == p
            assert extension[8:10] == scale(ONE/S5,I)
        assert mm(constant,residual) == scale(ZERO,i10)
        traces = [trace(mm(transport,p)) for p in (constant,residual)]
        assert traces[0] != traces[1]

        # One attachment cell cannot encode the four-dimensional low space.
        assert rank(low[8:10]) == 2
        accessible = scale(A(F(5,2)), mm(mm(low,cell4),low))
        invisible = add(low,scale(A(-1),accessible))
        assert mm(invisible,invisible) == invisible and rank(invisible) == 2
        assert rank(invisible[8:10]) == 0
        assert rank(mm(transport,invisible)[8:10]) == 2
        pairs = {f'{a},{b}': rank(low[2*a:2*a+2]+low[2*b:2*b+2]) for a,b in edges}
        assert set(pairs.values()) == {4}
        # Stacked amplitude readouts at a fixed cell over the source cycle.
        # This is an observability identity, NOT five nondestructive quantum copies.
        observations = tuple(row for t in range(5) for row in mm(power(transport,t),low)[8:10])
        assert rank(observations) == 4
        assert mm(adj(observations), observations) == low
        # The old mismatch energy is scalar on this space; it cannot generate
        # the non-scalar cycle as time evolution there, even up to global phase.
        restricted = mm(transport,low)
        assert restricted != scale(trace(restricted)/4,low)
        # A conditional constructive continuation, not a claim of necessity:
        # reuse the prior positive defect rule D^dagger D with D=T-I.
        # In the shared pi/4 normalization the dimensionless sum is L+X.
        cycle_defect = add(transport,scale(A(-1),i10))
        cycle_energy = mm(adj(cycle_defect),cycle_defect)
        assert cycle_energy == add(scale(A(2),i10),scale(A(-1),add(transport,adj(transport))))
        a,b,c = (A(3)-S5)/2, (A(3)+S5)/2, A(4)
        def spectral_projector(value, others):
            p = i10
            for other in others:
                p = mm(p,scale((value-other).inverse(),add(cycle_energy,scale(-other,i10))))
            return p
        cycle_projectors = [spectral_projector(a,(b,c)),spectral_projector(b,(a,c)),spectral_projector(c,(a,b))]
        assert add(add(cycle_projectors[0],cycle_projectors[1]),cycle_projectors[2]) == i10
        joint_rows = []
        for label,p,base_energy in [('low',low,low_energy),('high',add(i10,scale(A(-1),low)),high_energy)]:
            for x,q in zip((a,b,c),cycle_projectors):
                joint = mm(p,q)
                assert adj(joint) == joint and mm(joint,joint) == joint
                assert mm(cycle_energy,joint) == scale(x,joint)
                assert mm(laplacian,joint) == scale(base_energy,joint)
                dimension = rank(joint)
                joint_rows.append(dict(seam_sector=label,cycle_energy=x.record(),dimension=dimension,
                                       total_energy=(base_energy+x).record()))
        assert [r['dimension'] for r in joint_rows] == [2,2,0,2,2,2]
        selected = mm(low,cycle_projectors[0])
        opposite_selected = mm(low,cycle_projectors[1])
        assert selected == (constant if sign == 1 else residual)
        assert opposite_selected == (residual if sign == 1 else constant)
        assert mm(selected,opposite_selected) == scale(ZERO,i10)
        assert mm(add(laplacian,cycle_energy),selected) == scale(low_energy+a,selected)
        opposite_energy = add(laplacian,add(scale(A(4),i10),scale(A(-1),cycle_energy)))
        assert mm(opposite_energy,opposite_selected) == scale(low_energy+4-b,opposite_selected)
        assert mm(transport,selected) != scale(trace(mm(transport,selected))/2,selected)
        # -T gives X'=4I-X. With equal weights its ground switches doublets.
        # Its possible high-sector minimum is high_energy; compare exactly using
        # sqrt(6)>12/5 and sqrt(5)>2: 5sqrt(6)/3-(5-sqrt(5))/2 > 5/2.
        assert (S2*S3)*(S2*S3) == 6 and F(144,25) < 6
        assert S5*S5 == 5 and F(4) < 5
        assert high_energy-(low_energy+4-b) == 5*S2*S3/3-(5-S5)/2
        assert 5*F(12,5)/3-(5-F(2))/2 > 0
        def export_attachment(p):
            cell_map = tuple(tuple(S5*row[8+j] for j in range(2)) for row in p)
            face_keys = sorted(projectors)
            face_map = tuple(row for c,d in face_keys for row in scale(ONE/S2,mm(projectors[c,d],cell_map[2*c:2*c+2])))
            assert mm(adj(cell_map),cell_map) == I
            assert mm(adj(face_map),face_map) == I
            return dict(cell_isometry=record(cell_map),face_order=[list(key) for key in face_keys],face_isometry=record(face_map))
        results.append(dict(chirality=sign,spin_lift=record(spin),spin_trace=trace(spin).record(),
            source_cycle_power_5='-I for displayed lift; +I for opposite lift',
            low_dimension=4,low_energy=low_energy.record(),
            invariant_doublet_cycle_traces=[x.record() for x in traces],
            single_cell_rank=2,single_cell_invisible_dimension=2,
            two_cell_ranks=pairs,five_step_observation_gram='Q_low',
            inherited_matching_dimension=0,full_parallel_dimension=0,
            source_cycle_generated_by_existing_mismatch_energy=False,
            conditional_cycle_defect_extension=dict(rule='L+(T-I)^dagger(T-I), one common coefficient; overall pi/4 omitted',
                complete_joint_spectrum=joint_rows,ground_dimension=2,
                ground_energy=(low_energy+a).record(),opposite_lift_ground_energy=(low_energy+4-b).record(),
                ground_doublet='ambient constant' if sign == 1 else 'complementary low doublet',
                opposite_lift_selects_orthogonal_doublet=True,
                attachment_encoding=export_attachment(selected),
                opposite_lift_attachment_encoding=export_attachment(opposite_selected),
                both_doublets_extend_attachment_isometrically=True,
                bare_cell_permutation_fails_face_covariance=True,
                physical_coupling_admitted=False)))
    bindings = [source_path, Path(__file__), BASE/'checkers/check_pentachoron_spin_interfaces.py', BASE/'results/pentachoron_spin_interfaces.json']
    result = dict(verification_passed=True,exact_arithmetic='Q(sqrt(2),sqrt(3),sqrt(5),i)',
        source_frame='source pole -> E; source affine columns -> A-E,B-E,C-E,D-E',
        source_and_interface_covariance=True,metric_and_mismatch_energy_preserved=True,
        reversible_prefixes_checked=list(range(11)),chirality_results=results,
        source_hashes={str(p.relative_to(ROOT)).replace('\\','/'):sha256(p.read_bytes()).hexdigest() for p in bindings},
        physical_particle_identification=False,physical_clock_derived=False,
        scope='Exact symmetry transport and a conditional cycle-defect energy extension of the prior full-spinor mismatch model; not an exact-matching repair, physical clock, or cross-carrier interaction.')
    output = BASE/'results/pentachoron_cycle_transport.json'
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
