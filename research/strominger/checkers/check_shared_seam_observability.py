"""Exact observability and reference-exchange audit; standard library only.
Imports the source arithmetic without running or rewriting its checker receipt.
Composition index n is not physical time.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / 'research/nima/checkers'
sys.path.insert(0, str(SOURCE))
from check_two_triangle_half_phase import (identity, power, mm, mv, transpose,
                                          add, sub, scale, rank)
from check_triangle_half_phase import TwoPacket, cycle_from_packets


def main():
    checks = []
    def check(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append(name)
    C = cycle_from_packets(tuple(TwoPacket(label, a, b) for label, a, b in
                                 [('AB', 'A', 'B'), ('BC', 'B', 'C'), ('CA', 'C', 'A')]))
    I3, I5 = identity(3), identity(5)
    Q = scale(add(add(I3, C), mm(C, C)), F(1, 3))
    S = add(add(Q, scale(sub(I3, Q), F(1, 2))),
            scale(sub(C, transpose(C)), F(1, 2)))
    check('source half-phase squares to cycle', mm(S, S) == C)
    R1 = (I5[0], I5[1], I5[2])
    R2 = (tuple(-v for v in I5[0]), I5[3], I5[4])
    M = add(R1, R2)
    K = (I3[0], I3[1], I3[2], tuple(-v for v in I3[1]), tuple(-v for v in I3[2]))
    J = (tuple(-v for v in I5[0]), I5[3], I5[4], I5[1], I5[2])
    check('opposite readings on K', mm(R1, K) == I3 and mm(R2, K) == scale(I3, -1))
    check('exchange involution and orthogonality', mm(J, J) == I5 and mm(transpose(J), J) == I5)
    check('exchange swaps restrictions', mm(R1, J) == R2 and mm(R2, J) == R1)
    check('exchange acts by minus identity on K', mm(J, K) == scale(K, -1))
    check('geometry imposes initial seam only', M[0] == (0, 0, 0, 0, 0) and rank(M) == 2)
    results = {}
    for name, T, obs_rank, constraint_rank in [('C', C, 3, 2), ('S', S, 3, 2), ('I', I3, 1, 0)]:
        O = tuple(power(T, n)[0] for n in range(3))
        constraints = mm(O, M)
        check(name + ' observability rank', rank(O) == obs_rank)
        check(name + ' global constraint rank', rank(constraints) == constraint_rank)
        check(name + ' K lies in compatibility kernel', mm(constraints, K) == scale(mm(constraints, K), 0))
        # Matrix identities, not sampled input vectors, establish sufficiency.
        check(name + ' left intertwining', mm(T, mm(R1, K)) == mm(R1, mm(K, T)))
        check(name + ' right intertwining', mm(T, mm(R2, K)) == mm(R2, mm(K, T)))
        results[name] = {'observability_matrix': O, 'rank': rank(O),
                         'unobservable_dimension': 3-rank(O),
                         'global_constraints': constraints,
                         'compatible_global_dimension': 5-rank(constraints)}
    # Hostile: initial seam agreement does not imply agreement after local composition.
    x = I5[1]
    z = mv(M, x)
    check('initial hostile seam agrees', z[0] == 0)
    check('cycle exposes mismatch', mv(C, z)[0] == 1)
    check('half-phase exposes mismatch', mv(S, z)[0] == F(2, 3))
    check('identity leaves mismatch invisible', mv(I3, z)[0] == 0 and z != (0, 0, 0))
    # O=0 alone is weaker than synchronization.
    balanced = (F(0), F(1), F(-1), F(0), F(0))
    check('zero outer circulation does not synchronize', sum(balanced[1:]) == 0 and mv(C, mv(M, balanced))[0] == 1)
    L, R = ((1, 1, 1, 0, 0),), ((-1, 0, 0, 1, 1),)
    outer = add(L, R)
    check('exchange swaps circulations', mm(L, J) == R and mm(R, J) == L)
    check('exchange preserves outer circulation', mm(outer, J) == outer)
    residuals = {}
    for name, T in [('C', C), ('S', S)]:
        def embed(restriction):
            return add(I5, mm(mm(transpose(restriction), sub(T, I3)), restriction))
        T1, T2 = embed(R1), embed(R2)
        defect = sub(mm(T2, T1), mm(T1, T2))
        check(name + ' local exchange covariance', mm(mm(J, T1), J) == T2)
        check(name + ' serial exchange covariance', mm(mm(J, mm(T2, T1)), J) == mm(T1, T2))
        check(name + ' noncommutation rank two', rank(defect) == 2)
        check(name + ' serial outer circulation not conserved', mm(outer, mm(T2, T1)) != outer)
        check(name + ' own local circulation conserved', mm(L, T1) == L and mm(R, T2) == R)
        residuals[name] = {'fixed_frame_defect_rank': rank(defect), 'hostile_defect': mv(defect, x)}
    check('serial cycle leaves synchronized carrier', mv(M, mv(mm(add(I5, mm(mm(transpose(R2), sub(C, I3)), R2)), add(I5, mm(mm(transpose(R1), sub(C, I3)), R1))), mv(K, I3[1]))) != (0, 0, 0))
    sources = ['research/nima/two-triangles-shared-edge-half-phase.md',
               'research/nima/checkers/check_two_triangle_half_phase.py',
               'research/nima/checkers/check_triangle_half_phase.py',
               'research/nima/checkers/check_four_packet_record_feedback.py',
               'research/strominger/checkers/check_shared_seam_observability.py']
    report = {'status': 'passed', 'check_count': len(checks), 'checks': checks,
              'operators': results, 'serial_residuals': residuals,
              'hostile_input': x, 'mismatch': z,
              'source_sha256': {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in sources},
              'scope': 'Exact finite-dimensional linear identities. All composition indices follow from Cayley-Hamilton, not finite sampling. No physical time, particle identities, protocol selection, or isotope census.'}
    dest = ROOT / 'research/strominger/results/shared-seam-observability.json'
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(report, indent=2, default=str) + '\n', encoding='utf-8')
    print(json.dumps({'status': 'passed', 'checks': len(checks), 'result': str(dest)}))


if __name__ == '__main__':
    main()
