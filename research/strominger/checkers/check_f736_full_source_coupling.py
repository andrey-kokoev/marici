"""Exact arithmetic for v30; not a native operation-admission or analytical proof."""
from fractions import Fraction as F
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[3]

def mv(matrix, vector):
    return [sum(a * b for a, b in zip(row, vector)) for row in matrix]

def main():
    encoder = json.loads((ROOT / 'research/strominger/results/finite-observer-encoder.json').read_text())
    audit = json.loads((ROOT / 'research/strominger/results/f736-observer-closure/audit.json').read_text())
    T = [[F(x) for x in row] for row in encoder['analyticReadoutMatrix']]
    collision = audit['observationCollision']
    constant = [F(x) for x in collision['constant']]
    rho_coefficient = [F(x) for x in collision['rhoCoefficient']]
    checks = []

    def check(label, condition):
        if not condition:
            raise AssertionError(label)
        checks.append(label)

    check('prepared p0 observations', mv(T, [F(1), F(0), F(0), F(0), F(0)]) == [1, 1, 1, 0, 0])
    check('product constant observation coefficient', mv(T, constant) == [1, 1, 0, 0, 0])
    check('product rho observation coefficient', mv(T, rho_coefficient) == [0, 0, 1, 0, 0])
    oc = mv(T, [2*x for x in constant])
    orho = mv(T, [2*x for x in rho_coefficient])
    check('2p0 convolution changes both endpoint observations', oc[:2] == [2, 2] and orho[:2] == [0, 0])
    # Norm polynomial of oc + rho*orho, ordered by ascending powers of rho.
    norm = [sum(x*x for x in oc), 2*sum(x*y for x, y in zip(oc, orho)), sum(y*y for y in orho)]
    check('output norm polynomial is 8+4rho^2', norm == [8, 0, 4])
    check('input norm squared is 3', sum(x*x for x in mv(T, [1, 0, 0, 0, 0])) == 3)
    difference = [norm[0] - 3, norm[1], norm[2]]
    check('strict norm increase for every real rho', difference[0] > 0 and difference[1] == 0 and difference[2] >= 0)
    print(json.dumps({'status': 'passed', 'check_count': len(checks), 'checks': checks,
                      'norm_difference_coefficients': [str(x) for x in difference],
                      'scope': 'Exact observation arithmetic under the documented source/metric hypotheses; no higher filler or native update admitted.'}, indent=2))

if __name__ == '__main__':
    main()
