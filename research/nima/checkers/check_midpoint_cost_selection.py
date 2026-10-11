"""Countermodels to selecting route cost from midpoint certificates alone."""
from fractions import Fraction as F
from pathlib import Path
import json
from check_midpoint_route_statistics import enumerate_routes
from check_twelve_triangle_positive_geometry import POINTS, dot, sub

ROOT = Path(__file__).resolve().parents[1]


def main():
    levels, routes = enumerate_routes(POINTS, 'ABCD')
    defects = []
    for depth in range(1, 4):
        for i, m in enumerate(levels[depth]):
            a, b = levels[depth-1][i:i+2]
            residual = tuple(2*m[j]-a[j]-b[j] for j in range(3))
            defects.append(dot(residual, residual))
    assert defects == [F(0)]*6
    energies = []
    for r in routes:
        edges = [sub(b, a) for a, b in zip(r['nodes'], r['nodes'][1:])]
        quadratic = sum(dot(d, d) for d in edges)
        quartic = sum(dot(d, d)**2 for d in edges)
        anisotropic = sum(2*d[0]**2+d[1]**2+d[2]**2 for d in edges)
        assert quadratic == r['cost'] and quadratic > 0 and quartic > 0
        # Both costs are positive, translation/rotation invariant, reversal
        # invariant and additive under concatenation of retained edge lists.
        reversed_edges = [tuple(-x for x in d) for d in reversed(edges)]
        assert sum(dot(d,d) for d in reversed_edges) == quadratic
        assert sum(dot(d,d)**2 for d in reversed_edges) == quartic
        # A concrete orthogonal permutation and translation leave edge norms.
        rotated = [(-d[1], d[0], d[2]) for d in edges]
        assert [dot(d,d) for d in rotated] == [dot(d,d) for d in edges]
        energies.append(dict(route=r['route'], stage=r['stage'],
                             quadratic=quadratic, quartic=quartic,
                             anisotropic_quadratic=anisotropic))
    ratios = {r['quartic']/r['quadratic'] for r in energies}
    assert len(ratios) > 1  # Not just an energy-unit rescaling.
    # A unit edge gives both candidates the same normalization, yet two
    # perpendicular unit edges combined into one distinguish their laws.
    x, y = (F(1), F(0), F(0)), (F(0), F(1), F(0))
    plus = tuple(a+b for a,b in zip(x,y));minus = sub(x,y)
    q = lambda v: dot(v,v)
    fourth = lambda v: q(v)**2
    assert q(x) == fourth(x) == 1
    parallelogram_q = q(plus)+q(minus)-2*q(x)-2*q(y)
    parallelogram_fourth = fourth(plus)+fourth(minus)-2*fourth(x)-2*fourth(y)
    assert parallelogram_q == 0 and parallelogram_fourth == 4
    # Neither unweighted edge action descends under midpoint subdivision.
    half = tuple(v/2 for v in x)
    assert 2*q(half) == F(1,2) != q(x)
    assert 2*fourth(half) == F(1,8) != fourth(x)
    # Deliberately false midpoint equation is detected by its defect norm.
    a, b = levels[0][:2];m = levels[1][0]
    bad = (m[0]+1,m[1],m[2])
    residual = tuple(2*bad[j]-a[j]-b[j] for j in range(3))
    assert dot(residual,residual) == 4
    result = dict(schema='marici.nima.midpoint-cost-selection.v1',status='pass',
                  scope='six midpoint equations and eight ancestry routes of fixed ABCD',
                  obligation='forward realization and readout selection; no native-to-affine obstruction comparison assumed',
                  affine_midpoint_defects=defects, wrong_midpoint_defect=4,
                  route_costs=energies, quartic_to_quadratic_ratios=sorted(ratios),
                  parallelogram_residuals={'quadratic':parallelogram_q,'quartic':parallelogram_fourth},
                  unit_edge_subdivision_costs={'quadratic':F(1,2),'quartic':F(1,8)},
                  disposition='Midpoint certificates and Euclidean symmetry do not select squared-displacement action, even with unit-edge normalization.',
                  source_boundary='The native positive defect is an obstruction norm and vanishes for fillable comparisons in the stated realization. The affine residual here is not identified with that obstruction.',
                  missing='A source-selected cost law or quadratic/parallelogram axiom, normalization, and retained-presentation or subdivision convention; physical energy interpretation remains separate.')
    def enc(x):
        if isinstance(x,F):return str(x)
        if isinstance(x,dict):return {k:enc(v) for k,v in x.items()}
        if isinstance(x,(list,tuple)):return [enc(v) for v in x]
        return x
    result=enc(result)
    (ROOT/'results/midpoint-cost-selection.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
