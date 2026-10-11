"""Exact S4 stabilizer covariance, NOT an ADM or Poisson constraint algebra.
The old report is preserved under quarantine/20261007-constraint-evidence/.
Run: python research/nima/checkers/check_discrete_constraint_algebra.py
"""
from itertools import permutations
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
pts = list(range(4))
s4 = list(permutations(pts))


def mul(g,h):
    return tuple(g[h[i]] for i in pts)


def inv(g):
    return tuple(g.index(i) for i in pts)


def stabilizer(point):
    return [g for g in s4 if g[point] == point]


def check_transport(g,point,target=None):
    actual = {mul(mul(g,h),inv(g)) for h in stabilizer(point)}
    expected = set(stabilizer(g[point])) if target is None else set(target)
    if actual != expected:
        raise AssertionError('Stabilizer conjugation must transport the anchor')
    return True


def verify():
    rows = [{'g':g,'anchor':point,'transported_anchor':g[point],
             'conjugation_preserves_stabilizer':check_transport(g,point)}
            for point in pts for g in s4]
    g,h = (1,0,2,3),(0,2,1,3)
    commutator = mul(mul(mul(g,h),inv(g)),inv(h))
    if h not in stabilizer(0) or commutator != (2,0,1,3):
        raise AssertionError('Noncommuting source pair changed')
    rejected = False
    try:
        check_transport(g,0,stabilizer(0))
    except AssertionError:
        rejected = True
    if not rejected:
        raise AssertionError('Incorrect fixed-anchor target was accepted')
    return {'schema':'marici.nima.stabilizer-covariance-repaired.v1','status':'pass',
            'classification':'finite stabilizer covariance, not a Poisson constraint algebra',
            'closure_checks':rows,'nontrivial_group_commutator':commutator,
            'fixed_anchor_hostile_rejected':rejected,
            'not_supplied':['constraint functions on a symplectic phase space',
                            'field-phase-space comparison','ADM hypersurface deformation brackets'],
            'comparison_packet':'finite-canonical-actions-versus-adm-constraints.md'}


def main():
    result = verify()
    (ROOT/'results/discrete-stabilizer-covariance-repaired.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
