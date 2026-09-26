"""Exact four-gluon tree benchmark, including SU(3) color.

All momenta incoming, metric +---, delta-stripped i M. Cubic rule g f V,
gluon propagator -i g_mu_nu/q^2 and quartic rule -i g^2 times color tensor.
Eight SU(3) generators use a rational orthogonal basis: the last generator
has norm 3, not 1. Color averages explicitly include inverse color metrics.
"""
from __future__ import annotations

import argparse
from dataclasses import asdict, is_dataclass
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product, permutations
import json
from pathlib import Path
import unittest

from qed_fermion_scattering import C, ZERO, I, PAULI, matrix, scale, multiply, add, trace, dagger, dot, plus, minus
from qed_compton import transverse


class ColorAlgebra:
    def __init__(self, name, generators):
        self.name = name
        self.generators = generators
        self.dimension = len(generators)
        self.metric = tuple((2*trace(multiply(t, t))).real for t in generators)

    @lru_cache(None)
    def commutator(self, a, b):
        ta, tb = self.generators[a], self.generators[b]
        return add(multiply(ta, tb), scale(multiply(tb, ta), -1))

    @lru_cache(None)
    def pair(self, a, b, c, d):
        # -2 Tr([Ta,Tb][Tc,Td]) = f_ab,e kappa^{ef} f_cd,f.
        if a == b or c == d:
            return Q(0)
        first, second = self.commutator(a, b), self.commutator(c, d)
        value = -2*sum((first[i][j]*second[j][i]
                        for i in range(len(first)) for j in range(len(first))), ZERO)
        if value.imag != 0:
            raise ValueError("Non-real color contraction")
        return value.real

    def factors(self, colors):
        a, b, c, d = colors
        return self.pair(a, b, c, d), self.pair(a, c, b, d), self.pair(a, d, b, c)

    @lru_cache(None)
    def gram(self):
        result = [[Q(0) for _ in range(3)] for _ in range(3)]
        for colors in product(range(self.dimension), repeat=4):
            fs = self.factors(colors)
            norm = Q(self.dimension**2)
            for c in colors:
                norm *= self.metric[c]
            for a, b in product(range(3), repeat=2):
                result[a][b] += fs[a]*fs[b]/norm
        return tuple(tuple(row) for row in result)


SU2 = ColorAlgebra("SU(2)", tuple(scale(t, Q(1, 2)) for t in PAULI))
h = Q(1, 2)
SU3 = ColorAlgebra("SU(3)", (
    matrix(((0,h,0),(h,0,0),(0,0,0))),
    matrix(((0,-I*h,0),(I*h,0,0),(0,0,0))),
    matrix(((h,0,0),(0,-h,0),(0,0,0))),
    matrix(((0,0,h),(0,0,0),(h,0,0))),
    matrix(((0,0,-I*h),(0,0,0),(I*h,0,0))),
    matrix(((0,0,0),(0,0,h),(0,h,0))),
    matrix(((0,0,0),(0,0,-I*h),(0,I*h,0))),
    matrix(((h,0,0),(0,h,0),(0,0,-1))),
))
COUPLING = Q(1, 3)
DIRECTIONS = ((Q(1), Q(0), Q(0)), (Q(3, 5), Q(4, 5), Q(0)),
              (Q(2, 3), Q(1, 3), Q(2, 3)), (Q(4, 5), Q(0), Q(3, 5)))
PAIRINGS = (((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2)))


def times(v, scalar):
    return tuple(x*scalar for x in v)


def kinematics(direction=DIRECTIONS[0]):
    if sum((x*x for x in direction), Q(0)) != 1:
        raise ValueError("Unit direction required")
    return ((Q(1),Q(0),Q(0),Q(1)), (Q(1),Q(0),Q(0),Q(-1)),
            (Q(-1),) + tuple(-x for x in direction), (Q(-1),) + direction)


def invariants(ps):
    return tuple(dot(plus(ps[0], ps[i]), plus(ps[0], ps[i])) for i in (1, 2, 3))


def validate(ps):
    if len(ps) != 4 or any(len(p) != 4 or p[0] == 0 or dot(p, p) != 0 for p in ps):
        raise ValueError("Four nonzero-energy on-shell massless momenta required")
    if any(sum((p[mu] for p in ps), Q(0)) for mu in range(4)):
        raise ValueError("All-incoming conservation failed")
    if 0 in invariants(ps):
        raise ValueError("Internal massless propagator pole")


def polarizations(ps):
    return tuple(transverse(p if p[0] > 0 else times(p, -1)) for p in ps)


def cubic_current(pi, pj, ei, ej):
    # Internal momentum is -pi-pj; no transversality simplification is used.
    a = dot(ei, ej)
    b = dot(ei, plus(pi, times(pj, 2)))
    c = dot(ej, minus(times(pi, -2), pj))
    return tuple(a*x + b*y + c*z for x, y, z in zip(minus(pi, pj), ej, ei))


def lorentz_parts(ps, eps):
    validate(ps)
    exchanges = []
    for ((i,j),(k,l)), denominator in zip(PAIRINGS, invariants(ps)):
        left = cubic_current(ps[i], ps[j], eps[i], eps[j])
        right = cubic_current(ps[k], ps[l], eps[k], eps[l])
        exchanges.append(dot(left, right)/denominator)
    a01, a02, a03 = (dot(eps[0], eps[j]) for j in (1,2,3))
    a12, a13, a23 = dot(eps[1],eps[2]), dot(eps[1],eps[3]), dot(eps[2],eps[3])
    contact = (a02*a13-a03*a12, a01*a23-a03*a12, a01*a23-a02*a13)
    return tuple(exchanges), contact


def diagrams(ps, eps, colors, group=SU3, coupling=COUPLING):
    if len(colors) != 4 or any(c not in range(group.dimension) for c in colors):
        raise ValueError("Invalid color labels")
    fs = group.factors(colors)
    exchange, contact = lorentz_parts(ps, eps)
    return tuple(-coupling**2*f*x for f, x in zip(fs, exchange)) + (
        -coupling**2*sum((f*x for f, x in zip(fs, contact)), Q(0)),)


def amplitude(ps, eps, colors, group=SU3, coupling=COUPLING):
    return sum(diagrams(ps, eps, colors, group, coupling), Q(0))


def averaged_squared(ps, group=SU3, coupling=COUPLING):
    # Physical linear polarization sum; factor 1/4 averages initial spins.
    # gram already averages initial colors and normalizes every color leg.
    gram = group.gram()
    result = ZERO
    for eps in product(*polarizations(ps)):
        exchange, contact = lorentz_parts(ps, eps)
        ks = tuple(C.of(x+y) for x, y in zip(exchange, contact))
        result += sum((gram[a][b]*ks[a]*ks[b].conjugate()
                       for a, b in product(range(3), repeat=2)), ZERO)
    result *= coupling**4/4
    if result.imag != 0:
        raise ValueError("Non-real unpolarized result")
    return result.real


def invariant_average(ps, group=SU3, coupling=COUPLING):
    validate(ps)
    s, t, u = invariants(ps)
    n = {"SU(2)": 2, "SU(3)": 3}[group.name]
    return Q(4*n*n, n*n-1)*coupling**4*(3-t*u/s**2-s*u/t**2-s*t/u**2)


def helicity_amplitude(ps, helicities, colors, group=SU3):
    # All-OUTGOING helicity labels: incoming physical helicities are reversed.
    # A physical outgoing polarization is conjugated. Both conventions give
    # e1-i*h*e2 for the future-directed representatives used here.
    if len(helicities) != 4 or any(h not in (-1, 1) for h in helicities):
        raise ValueError("Four +/-1 helicities required")
    eps = tuple(tuple(C.of(x)-I*h*y for x, y in zip(e1, e2))
                for (e1, e2), h in zip(polarizations(ps), helicities))
    # Each circular vector omitted 1/sqrt(2): four legs give exactly 1/4.
    return C.of(amplitude(ps, eps, colors, group))/4


class YangMillsTests(unittest.TestCase):
    def test_color_metric_and_jacobi(self):
        for group in (SU2, SU3):
            for a, b in product(range(group.dimension), repeat=2):
                self.assertEqual(dagger(group.generators[a]), group.generators[a])
                self.assertEqual(trace(group.generators[a]), ZERO)
                self.assertEqual(2*trace(multiply(group.generators[a], group.generators[b])),
                                 C.of(group.metric[a] if a == b else 0))
            for colors in product(range(group.dimension), repeat=4):
                s, t, u = group.factors(colors)
                self.assertEqual(s-t+u, 0)
        self.assertEqual(SU3.metric, (Q(1),)*7+(Q(3),))

    def test_color_gram(self):
        base = ((Q(1),Q(1,2),Q(-1,2)), (Q(1,2),Q(1),Q(1,2)), (Q(-1,2),Q(1,2),Q(1)))
        for group, diagonal in ((SU2,Q(4,3)), (SU3,Q(9,8))):
            self.assertEqual(group.gram(), tuple(tuple(diagonal*x for x in row) for row in base))

    def test_quartic_vertex_from_action(self):
        # Differentiate L4=-g^2/4 f_ab,e kappa^ef f_cd,f
        # A_a.mu A_b.nu A_c^mu A_d^nu: sum all 24 labelled assignments.
        ps = kinematics(DIRECTIONS[2])
        for colors in ((0,1,0,1), (0,0,1,1), (0,3,5,7)):
            for eps in product(*polarizations(ps)):
                coefficient = -COUPLING**2/4 * sum(
                    (SU3.pair(colors[a],colors[b],colors[c],colors[d])
                     *dot(eps[a],eps[c])*dot(eps[b],eps[d])
                     for a,b,c,d in permutations(range(4))), Q(0))
                self.assertEqual(diagrams(ps,eps,colors)[-1], coefficient)

    def test_color_normalization_hostile(self):
        wrong = sum((SU3.factors(colors)[0]**2
                     for colors in product(range(8), repeat=4)), Q(0))/64
        self.assertNotEqual(wrong, SU3.gram()[0][0])

    def test_standard_unpolarized_result(self):
        for group in (SU2, SU3):
            for direction in DIRECTIONS:
                ps = kinematics(direction)
                self.assertEqual(sum(invariants(ps)), 0)
                self.assertEqual(averaged_squared(ps, group), invariant_average(ps, group))
        self.assertEqual(averaged_squared(kinematics(), SU3), Q(3,8))
        self.assertEqual(averaged_squared(kinematics(), SU2), Q(4,9))

    def test_ward_and_contact_hostile(self):
        witnessed = False
        # Color assignments span the two independent Jacobi color tensors;
        # an additional assignment explicitly involves the eighth generator.
        for colors in ((0,1,0,1), (0,0,1,1), (0,3,5,7)):
            for direction in DIRECTIONS[:3]:
                ps = kinematics(direction)
                for eps in product(*polarizations(ps)):
                    for leg in range(4):
                        replaced = eps[:leg]+(ps[leg],)+eps[leg+1:]
                        terms = diagrams(ps, replaced, colors)
                        self.assertEqual(sum(terms), 0)
                        if terms[-1] != 0:
                            witnessed = True
                            self.assertNotEqual(sum(terms[:3]), 0)
                            self.assertNotEqual(sum(terms[:3])-terms[-1], 0)
        self.assertTrue(witnessed)

    def test_gauge_shifts(self):
        ps = kinematics(DIRECTIONS[2])
        for eps in product(*polarizations(ps)):
            shifted = tuple(plus(e, times(p, Q(i+1,7))) for i, (e,p) in enumerate(zip(eps,ps)))
            self.assertEqual(amplitude(ps, shifted, (0,1,0,1)), amplitude(ps, eps, (0,1,0,1)))

    def test_helicity_selection(self):
        nonzero = False
        for direction in DIRECTIONS:
            ps = kinematics(direction)
            for hs in product((-1,1), repeat=4):
                value = helicity_amplitude(ps, hs, (0,1,0,1))
                if hs.count(-1) != 2:
                    self.assertEqual(value, ZERO)
                elif value != ZERO:
                    nonzero = True
        self.assertTrue(nonzero)

    def test_helicity_basis_normalization(self):
        for direction in DIRECTIONS:
            ps = kinematics(direction)
            for colors in ((0,1,0,1), (0,3,5,7)):
                linear = sum((C.of(amplitude(ps,eps,colors)).abs2()
                              for eps in product(*polarizations(ps))), Q(0))/4
                circular = sum((helicity_amplitude(ps,hs,colors).abs2()
                                for hs in product((-1,1),repeat=4)), Q(0))/4
                self.assertEqual(circular, linear)

    def test_bose_relabeling_and_scaling(self):
        ps = kinematics(DIRECTIONS[2])
        colors = (0,3,5,7)
        for eps in product(*polarizations(ps)):
            expected = amplitude(ps, eps, colors)
            for order in ((1,0,2,3), (0,2,1,3), (3,2,1,0)):
                self.assertEqual(amplitude(tuple(ps[i] for i in order), tuple(eps[i] for i in order),
                                           tuple(colors[i] for i in order)), expected)
        self.assertEqual(averaged_squared(tuple(times(p,Q(5,3)) for p in ps)), averaged_squared(ps))
        self.assertEqual(averaged_squared(ps,coupling=2*COUPLING), 16*averaged_squared(ps))

    def test_invalid_inputs(self):
        for direction in ((Q(0),Q(0),Q(1)), (Q(0),Q(0),Q(-1))):
            ps = kinematics(direction)
            with self.assertRaisesRegex(ValueError,"pole"):
                averaged_squared(ps)
        ps = kinematics()
        with self.assertRaisesRegex(ValueError,"color"):
            amplitude(ps, tuple(p[0] for p in polarizations(ps)), (0,1,0,8))


def encode(value):
    if isinstance(value, Q):
        return str(value)
    if is_dataclass(value):
        return asdict(value)
    raise TypeError(type(value).__name__)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(YangMillsTests))
    if not result.wasSuccessful():
        raise SystemExit(1)
    samples = []
    for direction in DIRECTIONS:
        ps = kinematics(direction)
        records = []
        for colors in ((0,1,0,1), (0,0,1,1), (0,3,5,7)):
            norm = Q(1)
            for c in colors:
                norm *= SU3.metric[c]
            for labels in product((0,1),repeat=4):
                eps = tuple(pair[label] for pair,label in zip(polarizations(ps),labels))
                terms = diagrams(ps,eps,colors)
                value = sum(terms)
                records.append({"colors_zero_based": colors, "color_factors": SU3.factors(colors),
                                "color_norm_product": norm, "polarization_labels": labels,
                                "polarizations": eps, "exchange_s_t_u_and_contact": terms,
                                "basis_component_amplitude": value,
                                "unit_color_component_squared": C.of(value).abs2()/norm,
                                "ward_diagrams_by_leg": [diagrams(ps,eps[:leg]+(ps[leg],)+eps[leg+1:],colors)
                                                         for leg in range(4)]})
        samples.append({"all_incoming_momenta": ps, "invariants_s_t_u": invariants(ps),
                        "component_records": records,
                        "helicity_components_colors_0101": [{"all_outgoing_helicities": hs,
                            "amplitude": helicity_amplitude(ps,hs,(0,1,0,1))}
                            for hs in product((-1,1),repeat=4)],
                        "su3_averaged_squared": averaged_squared(ps),
                        "su3_invariant_result": invariant_average(ps)})
    report = {"status": "exact-computational-benchmark-passed", "theory": "pure SU(3) Yang-Mills, tree four-gluon scattering",
              "coupling": COUPLING, "su3_generators": SU3.generators, "su3_color_metric": SU3.metric,
              "su3_color_gram_initial_averaged": SU3.gram(),
              "color_convention": "rational orthogonal basis; eighth generator not unit-normalized; inverse metrics included",
              "formal_agda_bridge": "not implemented", "novel_physical_prediction": False,
              "scope": "finite exact Ward and helicity tests; no Parke-Taylor comparison or general proof yet",
              "samples": samples, "tests_run": result.testsRun}
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report,default=encode,indent=2)+"\n",encoding="utf-8")
    print(f"SU(3) four gluons: first averaged |M|^2 = {samples[0]['su3_averaged_squared']}")


if __name__ == "__main__":
    main()
