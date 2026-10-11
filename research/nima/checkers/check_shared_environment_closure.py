"""Exact shared-environment closure; no fitted mass or binding coefficients.

Finite candidate environment, fixed source amplitudes. The source density is
computed from the existing tetrahedral mode. Environment normalization is a
model choice; numbers below are response coefficients, not electron-mass units.
"""
from fractions import Fraction as F
from pathlib import Path
import json
from check_twelve_triangle_positive_geometry import (
    POINTS, ONE, OMEGA, compose, rotation, mean, transpose, zmv, zmul, znorm,
)


def source_blocks():
    group = {(0, 1, 2, 3)}
    queue = list(group)
    while queue:
        q = queue.pop()
        for g in ((1, 2, 0, 3), (3, 0, 2, 1)):
            p = compose(g, q)
            if p not in group:
                group.add(p)
                queue.append(p)
    assert len(group) == 12
    x0 = transpose((mean([POINTS[k] for k in 'ABC']), POINTS['A'], POINTS['B']))
    v0 = zmv(x0, (ONE, OMEGA, zmul(OMEGA, OMEGA)))
    permutations = sorted(group)
    u = [z for g in permutations for z in zmv(rotation(g), v0)]
    assert sum(map(znorm, u)) == 80
    weights = [znorm(z)/80 for z in u]
    labels = {
        'whole': [0]*36,
        'faces': [tuple(sorted(g[:3])) for g in permutations for _ in range(3)],
        'triangles': [i for i in range(12) for _ in range(3)],
        'axes': [i for _ in range(12) for i in range(3)],
        'ports': list(range(36)),
    }
    answer = {}
    for name, partition in labels.items():
        blocks = {}
        for label, weight in zip(partition, weights):
            blocks[label] = blocks.get(label, F(0))+weight
        answer[name] = list(blocks.values())
        assert sum(answer[name]) == 1
    return answer


def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), F(0))


def close(source, eta):
    # D = I - eta A, A the adjacency matrix of the complete graph.
    n = len(source)
    uniform = F(1)-eta*(n-1)
    contrast = F(1)+eta
    assert uniform > 0 and contrast > 0
    mean_source = sum(source)/n
    return [mean_source/uniform+(s-mean_source)/contrast for s in source]


def stiffness(x, eta):
    total = sum(x)
    return [v-eta*(total-v) for v in x]


def main():
    rows = []
    for name, w in source_blocks().items():
        n = len(w)
        # Freeze two models: independent probes, or all-to-all feedback with
        # row sum 1/2. This makes feedback contractive without target fitting.
        for model, eta in [('independent', F(0)),
                           ('all_to_all', F(1, 2*(n-1)) if n > 1 else F(0))]:
            def solve(s, t, sign=1, coupling=F(1)):
                j = [coupling*(s+sign*t)*v for v in w]
                x = close(j, eta)
                assert stiffness(x, eta) == j
                energy = dot(x, stiffness(x, eta))/2-dot(j, x)
                assert energy == -dot(j, x)/2
                return energy, x, j
            e00, _, _ = solve(0, 0)
            ep, xp, _ = solve(1, 0)
            ee, _, _ = solve(0, 1)
            epe, xpe, jpe = solve(1, 1)
            delta = epe-ep-ee+e00
            q = dot(w, close(w, eta))
            assert delta == -q and q > 0
            assert xpe == [2*v for v in xp]
            # s and t are squared amplitudes: the cross-term is quartic.
            assert solve(4, 9)[0]-solve(4, 0)[0]-solve(0, 9)[0] == 36*delta
            assert solve(1, 1, coupling=F(2))[0]-solve(1, 0, coupling=F(2))[0]-solve(0, 1, coupling=F(2))[0] == 4*delta
            opposite = solve(1, 1, sign=-1)[0]-solve(1, 0, sign=-1)[0]-solve(0, 1, sign=-1)[0]
            assert opposite == q
            # A fixed environment with no readjustment has zero mixed term.
            frozen = lambda s,t: dot(xp, stiffness(xp, eta))/2-(s+t)*dot(w, xp)
            assert frozen(1,1)-frozen(1,0)-frozen(0,1)+frozen(0,0) == 0
            # Positive stiffness certifies the unique minimum over environment
            # variables. Test the square-completion identity on a perturbation.
            h = [F(i+1, n) for i in range(n)]
            perturbed = [a+b for a,b in zip(xpe,h)]
            e_perturbed = dot(perturbed, stiffness(perturbed,eta))/2-dot(jpe,perturbed)
            assert e_perturbed-epe == dot(h,stiffness(h,eta))/2 > 0
            # Feedback iterate x_{k+1}=j+eta*A*x_k converges to same solution.
            iterate = [F(0)]*n
            initial_error = max(map(abs,xpe))
            rho = eta*(n-1)
            for k in range(1, 9):
                total = sum(iterate)
                iterate = [j+eta*(total-v) for j,v in zip(jpe,iterate)]
                assert max(abs(a-b) for a,b in zip(iterate,xpe)) <= rho**k*initial_error
            rows.append(dict(partition=name, model=model, blocks=n, eta=str(eta),
                             proton_self_response=str(ep), witness_self_response=str(ee),
                             joint_response=str(epe), binding_cross_term=str(delta),
                             binding_coefficient_decimal=float(delta)))
    result = dict(schema='marici.nima.shared-environment-closure.v1', status='pass',
                  rows=rows, response_law='D x = J, D=I-eta*A; J=g(s*a+t*b)',
                  eliminated_energy='-J^T D^-1 J/2',
                  cross_term='-g^2 s t a^T D^-1 b',
                  source='existing tetrahedral collective mode; dual witness has the same block intensities',
                  assumptions=['density coupling', 'quadratic positive environment stiffness',
                               'same-sign source couplings for the primary test',
                               'unit coupling coefficient; no conversion to electron-mass units',
                               'environment minimized at fixed source amplitudes'],
                  controls=['opposite source sign reverses attraction', 'frozen environment gives zero mixed term',
                            'quartic source-amplitude scaling', 'quadratic coupling scaling',
                            'square-completion minimum', 'contractive feedback agrees with exact closure'],
                  residual='WG has not selected the coupling, environment stiffness, sign, or physical energy normalization. No hydrogen mass is predicted.')
    out = Path(__file__).resolve().parents[1]/'results/shared-environment-closure.json'
    out.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
