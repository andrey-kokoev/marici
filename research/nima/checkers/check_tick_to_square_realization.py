"""Finite numerical consistency of the supplied two-parameter matrix model.

Does not evaluate native Agda Tick terms or prove their faithful realization.
Full Bool source classification: TickRetainedStructure.agda. Stronger declared-
class interpolation result: check_tick_interpretation_nonuniqueness.py.
The pre-repair source/receipt are retained under quarantine/20261007-tick-evidence.
"""
import argparse
import cmath
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / 'results/tick-to-square-realization-consistency.json'
EPS = 1e-12


def scale(s, matrix):
    return tuple(tuple(s*x for x in row) for row in matrix)


def add(a, b):
    return tuple(tuple(x+y for x, y in zip(r, s)) for r, s in zip(a, b))


def mm(a, b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(4))
                       for j in range(4)) for i in range(4))


def distance(a, b):
    return math.sqrt(sum(abs(a[i][j]-b[i][j])**2
                         for i in range(4) for j in range(4)))


I = tuple(tuple(F(i == j) for j in range(4)) for i in range(4))
L = tuple(tuple(F(i == (j ^ 2)) for j in range(4)) for i in range(4))
R = tuple(tuple(F(i == (j ^ 1)) for j in range(4)) for i in range(4))
LR = mm(L, R)
PL = scale(F(1, 2), add(I, scale(-1, L)))
PR = scale(F(1, 2), add(I, scale(-1, R)))


def U(alpha, beta):
    left = add(I, scale(cmath.exp(-1j*alpha)-1, PL))
    right = add(I, scale(cmath.exp(-1j*beta)-1, PR))
    return mm(left, right)


def generator(a, b):
    return add(scale(a, PL), scale(b, PR))


def p1():
    return distance(U(0, 0), I) < EPS


def p2():
    return distance(U(math.pi, math.pi), LR) < EPS


def p3():
    return distance(U(math.pi, 0), L) < EPS


def p4():
    return distance(U(0, math.pi), R) < EPS


def p5():
    intermediate = U(math.pi, 0)
    return (distance(intermediate, L) < EPS
            and distance(mm(U(0, math.pi), intermediate), LR) < EPS)


def p6():
    intermediate = U(0, math.pi)
    return (distance(intermediate, R) < EPS
            and distance(mm(U(math.pi, 0), intermediate), LR) < EPS)


def p7():
    left_first = mm(U(0, math.pi), U(math.pi, 0))
    right_first = mm(U(math.pi, 0), U(0, math.pi))
    return distance(left_first, right_first) < EPS and distance(left_first, LR) < EPS


def p8():
    # Explicit inverse execution; angle is not physical duration.
    for a, b in ((math.pi, math.pi), (0.37, 0.61)):
        returned = mm(U(-a, 0), mm(U(0, -b), U(a, b)))
        if not distance(returned, I) < EPS:
            return False
    return True


def p9():
    return distance(U(math.pi, 0), U(0, math.pi)) > EPS


def p10():
    # Compare DERIVATIVES, not an O(epsilon) error against a loose absolute
    # tolerance that would accept even the zero or wrong-sign generator.
    epsilon = 1e-5
    for a, b in ((1, 0), (0, 1), (1, 1), (2, -3)):
        derivative = scale(1/(2*epsilon),
                           add(U(epsilon*a, epsilon*b),
                               scale(-1, U(-epsilon*a, -epsilon*b))))
        if not distance(derivative, scale(-1j, generator(a, b))) < 1e-8:
            return False
    return True


def run_checks():
    properties = (
        ('P1_source_corner', p1), ('P2_target_corner', p2),
        ('P3_left_intermediate', p3), ('P4_right_intermediate', p4),
        ('P5_leftFirst_path', p5), ('P6_rightFirst_path', p6),
        ('P7_comparison', p7), ('P8_return', p8),
        ('P9_distinct_paths', p9), ('P10_generator_form', p10),
    )
    checks = []
    for name, predicate in properties:
        try:
            checks.append({'property': name, 'passed': bool(predicate())})
        except Exception as error:
            checks.append({'property': name, 'passed': False,
                           'error': f'{type(error).__name__}: {error}'})
    passed = sum(row['passed'] for row in checks)
    return {
        'schema': 'marici.nima.tick-to-square-realization-consistency.v3',
        'status': 'pass' if passed == len(checks) else 'fail',
        'passed': passed == len(checks),
        'passed_count': passed, 'failed_count': len(checks)-passed,
        'check_count': len(checks), 'checks': checks,
        'model_checks': {row['property']: row['passed'] for row in checks},
        'scope': 'supplied 4x4 matrix model; no native Tick evaluator or faithfulness theorem',
        'arithmetic': 'Fraction operators and finite complex floating-point samples',
        'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args(argv)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    # Unexpected errors must not leave an earlier success receipt in place.
    args.output.unlink(missing_ok=True)
    result = run_checks()
    args.output.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(f"{result['status'].upper()}: {result['passed_count']}/{result['check_count']} matrix-model checks")
    return 0 if result['passed'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
