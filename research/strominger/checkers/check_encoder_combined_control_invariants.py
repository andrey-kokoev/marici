"""Exact invariant falsification attempt; not a compiler or Lie-closure certificate.

Control model: independent phase families of the stored 21 seam projectors,
18 framed bank projectors, and 21 local record-write projectors. Frame pulses
are conjugates of frame-zero pulses by the retained native rotation. Independent
switching is a declared mathematical capability, not a hardware conclusion.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
from check_witnessed_interface_compiler import (
    ROOT, BASE, eye, tr, mm, minus, scale, blockdiag, rat, enc,
    rank, inverse, compile_interface,
)
from check_neutron_rest_energy_preflight import nullspace


def zero(a):
    return all(not x for row in a for x in row)


def main():
    hashes = {}
    def load(name):
        path = BASE / 'results' / name
        raw = path.read_bytes()
        hashes[path.relative_to(ROOT).as_posix()] = hashlib.sha256(raw).hexdigest()
        return json.loads(raw)
    source = load('neutron-seam-control-transport.json')
    memory = load('neutron-comparison-memory.json')
    assert source['status'] == memory['status'] == 'passed'
    M = rat(source['metric'])
    B = rat(memory['residual_incidence'])
    Gamma = rat(memory['memory_metric'])
    metric = blockdiag(M, Gamma)
    sharpB = mm(mm(inverse(M), tr(B)), Gamma)
    assert mm(B, sharpB) == rat(memory['rational_memory_operator'])
    native = [rat(x['projector']) for x in source['seam_controls']]
    pulses = [rat(x['projector']) for x in source['source_pulses']]
    assert len(native) == 21 and len(pulses) == 18
    I = eye(45)
    graph = eye(24) + B
    projectors = []
    names = []
    for kind, family in [('seam', native), ('bank', pulses)]:
        for i, P in enumerate(family):
            assert mm(P, P) == P and mm(tr(P), M) == mm(M, P)
            assert rank(P) == 1
            projectors.append(blockdiag(P, [[F(0)] * 21 for _ in range(21)]))
            names.append(f'{kind}:{i}')
    write_graph_checks = []
    for i, row in enumerate(B):
        c = compile_interface(M, [row])
        assert c['memory_metric'][0][0] == Gamma[i][i]
        U = eye(45)
        A = c['injection']
        for k in range(24):
            for j in range(24):
                U[k][j] -= A[k][0] * row[j]
            U[k][24+i] = A[k][0]
            U[24+i][k] = row[k]
        U[24+i][24+i] = F(0)
        assert mm(U, U) == I
        assert mm(tr(U), metric) == mm(metric, U)
        write_graph_checks.append(mm(U, graph) == graph)
        P = scale(F(1, 2), minus(I, U))
        assert mm(P, P) == P and rank(P) == 1
        projectors.append(P)
        names.append(f'write:{i}')
    assert all(write_graph_checks)
    graph_breakers = [names[i] for i, P in enumerate(projectors) if not zero(mm(P, graph))]
    # One direction per rank-one generator, in unchanged rational charts.
    directions = []
    for P in projectors:
        directions.append(next(col for col in tr(P) if any(col)))
    gram = mm(mm(directions, metric), tr(directions))
    adjacency = [[j for j in range(len(directions)) if j != i and gram[i][j]]
                 for i in range(len(directions))]
    pending = set(range(len(directions)))
    components = []
    while pending:
        seed = min(pending)
        seen = {seed}
        frontier = [seed]
        while frontier:
            i = frontier.pop()
            for j in adjacency[i]:
                if j not in seen:
                    seen.add(j)
                    frontier.append(j)
        pending -= seen
        components.append(sorted(seen))
    fixed = nullspace(mm(directions, metric), 45)
    active_rank = rank(directions)
    assert active_rank + len(fixed) == 45
    # Polar U fixes (x,0) whenever Bx=0: W x=0 and N x=x.
    polar_fixes_common = all(not any(v[24:]) and zero(mm(B, tr([v[:24]]))) for v in fixed)
    for v in fixed:
        assert all(zero(mm(P, tr([v]))) for P in projectors)
    fixed_native_energy = all(zero(mm(rat(source['native_energy']), tr([v[:24]]))) for v in fixed)
    fixed_rotation = all(mm(rat(source['native_rotation']), tr([v[:24]])) == tr([v[:24]]) for v in fixed)
    # Verify the frame conjugation policy, rather than treating new matrices as
    # unrelated arbitrary controls. All stored labels occur at frames 0,1,2.
    R = rat(source['native_rotation'])
    Rinv = mm(R, R)
    assert mm(Rinv, R) == eye(24)
    by_key = {(p['label'], p['frame']): rat(p['projector']) for p in source['source_pulses']}
    for (label, frame), P in by_key.items():
        assert mm(mm(R, P), Rinv) == by_key[label, (frame + 1) % 3]
    assert graph_breakers and polar_fixes_common
    assert active_rank == 44 and len(fixed) == 1 and len(components) == 1
    assert fixed_native_energy and fixed_rotation
    own = Path(__file__).resolve()
    hashes[own.relative_to(ROOT).as_posix()] = hashlib.sha256(own.read_bytes()).hexdigest()
    for path, digest in hashes.items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest
    report = {
        'status': 'pass',
        'scientific_disposition': 'Common-fixed-space and orthogonal-component falsifiers do not separate the polar target under the declared combined continuous control model.',
        'dimension': 45, 'rank_one_generators': len(projectors),
        'active_span_dimension': active_rank, 'common_fixed_dimension': len(fixed),
        'nonorthogonality_graph_components': components,
        'generator_names': names, 'common_fixed_basis': enc(fixed),
        'all_local_writes_fix_residual_graph': all(write_graph_checks),
        'residual_graph_breakers_in_combined_family': graph_breakers,
        'polar_encoder_fixes_common_space': polar_fixes_common,
        'native_energy_annihilates_common_space': fixed_native_energy,
        'native_rotation_fixes_common_space': fixed_rotation,
        'framed_controls_are_rotation_conjugates': True,
        'source_hashes': hashes,
        'scope': 'Exact rational finite-dimensional invariant audit. No numerical polar approximation, Lie algebra computation, control-word synthesis, hardware switching authority, arbitrary-accuracy or WG completeness certificate. Source receipts were consumed and hashed; their predecessor suites were not rerun.',
    }
    out = BASE / 'results/encoder-combined-control-invariants.json'
    out.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({k: report[k] for k in ['status', 'active_span_dimension', 'common_fixed_dimension', 'polar_encoder_fixes_common_space']}))
    print('nonorthogonality_components=', len(components), 'graph_breakers=', len(graph_breakers))


if __name__ == '__main__':
    main()
