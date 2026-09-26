"""Executable finite exact tests of four-point Parke-Taylor conventions."""
from __future__ import annotations

import argparse
from dataclasses import asdict, is_dataclass
from fractions import Fraction as Q
from itertools import product, permutations
import json
from pathlib import Path
import unittest

import gluon_spinor_helicity as S
import yang_mills_four as YM
from qed_fermion_scattering import C, ZERO, I, dot


def point(direction):
    ps = tuple(YM.times(p,-1) for p in YM.kinematics(direction))
    return ps, tuple(S.factor(p) for p in ps)


def power(z, exponent):
    z = C.of(z)
    if exponent < 0:
        return C.of(1)/power(z,-exponent)
    value = C.of(1)
    for _ in range(exponent):
        value *= z
    return value


def reconstructed_color(spinors, helicities, colors):
    cs, ct, _ = YM.SU3.factors(colors)
    return -2*YM.COUPLING**2*(cs*S.parke_taylor(spinors,helicities)
                              +ct*S.parke_taylor(spinors,helicities,(0,2,1,3)))


class ParkeTaylorTests(unittest.TestCase):
    def test_factorization_and_bracket_conventions(self):
        for direction in YM.DIRECTIONS:
            ps, zs = point(direction)
            for p,z in zip(ps,zs):
                self.assertEqual(S.outer(z.lam,z.tilde), S.bispinor(p))
                self.assertEqual(S.vector(S.bispinor(p)), tuple(C.of(x) for x in p))
            for i,j in product(range(4),repeat=2):
                self.assertEqual(S.angle(zs[i],zs[j])*S.square(zs[j],zs[i]), C.of(2*dot(ps[i],ps[j])))
                self.assertEqual(S.angle(zs[i],zs[j]), -S.angle(zs[j],zs[i]))
                self.assertEqual(S.square(zs[i],zs[j]), -S.square(zs[j],zs[i]))

    def test_polarization_conventions(self):
        for direction in YM.DIRECTIONS:
            ps,zs = point(direction)
            for p,z,r in zip(ps,zs,S.references_for(zs)):
                plus, minus = S.polarization(z,r,1), S.polarization(z,r,-1)
                ref_p = S.vector(S.outer(r.lam,r.tilde))
                for eps in (plus,minus):
                    self.assertEqual(dot(p,eps), ZERO)
                    self.assertEqual(dot(ref_p,eps), ZERO)
                    self.assertEqual(dot(eps,eps), ZERO)
                self.assertEqual(dot(plus,minus), C.of(-2))

    def test_all_helicities_and_all_orders(self):
        # 4 points x 16 helicities x 24 orders = 1536 exact complex comparisons.
        nonzero = 0
        for direction in YM.DIRECTIONS:
            ps,zs = point(direction)
            for hs in product((-1,1),repeat=4):
                for order in permutations(range(4)):
                    actual = S.ordered_feynman(ps,zs,hs,order)
                    expected = S.parke_taylor(zs,hs,order)
                    self.assertEqual(actual, expected)
                    nonzero += int(expected != ZERO)
        self.assertEqual(nonzero, 4*6*24)

    def test_reference_independence(self):
        for direction in YM.DIRECTIONS:
            ps,zs = point(direction)
            for hs in ((-1,-1,1,1),(-1,1,-1,1),(-1,1,1,-1)):
                expected = S.parke_taylor(zs,hs)
                for offset in range(len(S.REFERENCES)):
                    self.assertEqual(S.ordered_feynman(ps,zs,hs,references=S.references_for(zs,offset)), expected)

    def test_little_group_weights(self):
        scales = (C(1,1), 2*I, C.of(Q(3,2)), C(1,-1))
        for direction in YM.DIRECTIONS:
            ps,zs = point(direction)
            shifted = tuple(S.Spinors(tuple(t*x for x in z.lam),tuple(x/t for x in z.tilde))
                            for z,t in zip(zs,scales))
            for hs in product((-1,1),repeat=4):
                weight = C.of(1)
                for t,h in zip(scales,hs):
                    weight *= power(t,-2*h)
                expected = weight*S.parke_taylor(zs,hs)
                self.assertEqual(S.parke_taylor(shifted,hs), expected)
                self.assertEqual(S.ordered_feynman(ps,shifted,hs), expected)

    def test_order_relations(self):
        for direction in YM.DIRECTIONS:
            ps,zs = point(direction)
            s,t,_ = YM.invariants(ps)
            for hs in product((-1,1),repeat=4):
                a = S.parke_taylor(zs,hs)
                b = S.parke_taylor(zs,hs,(0,2,1,3))
                c = S.parke_taylor(zs,hs,(0,1,3,2))
                self.assertEqual(S.parke_taylor(zs,hs,(1,2,3,0)), a)
                self.assertEqual(S.parke_taylor(zs,hs,(3,2,1,0)), a)
                self.assertEqual(a+b+c, ZERO)  # U(1) decoupling at four points.
                self.assertEqual(s*a, t*b)    # Four-point BCJ relation.

    def test_color_reconstruction_and_physical_basis_bridge(self):
        for direction in YM.DIRECTIONS:
            ps,zs = point(direction)
            for hs in product((-1,1),repeat=4):
                adapters = S.circular_adapter(ps,zs,hs)
                factor = C.of(1)
                for p,record in zip(ps,adapters):
                    factor *= record["alpha"]
                    self.assertEqual(record["spinor_polarization"],
                        tuple(record["alpha"]*e+record["beta"]*x
                              for e,x in zip(record["circular_polarization"],p)))
                eps = tuple(r["spinor_polarization"] for r in adapters)
                for colors in ((0,1,0,1),(0,0,1,1),(0,3,5,7),(3,4,3,4)):
                    actual = C.of(YM.amplitude(ps,eps,colors))/4
                    self.assertEqual(actual, reconstructed_color(zs,hs,colors))
                    self.assertEqual(actual, factor*YM.helicity_amplitude(ps,hs,colors))

    def test_normalization_hostile_and_invalid_inputs(self):
        ps,zs = point(YM.DIRECTIONS[0])
        hs = (-1,-1,1,1)
        expected = S.parke_taylor(zs,hs)
        self.assertNotEqual(expected,ZERO)
        self.assertNotEqual(4*S.ordered_feynman(ps,zs,hs),expected)
        with self.assertRaisesRegex(ValueError,"null"):
            S.factor((Q(1),Q(0),Q(0),Q(0)))
        with self.assertRaisesRegex(ValueError,"Zero momentum"):
            S.factor((Q(0),)*4)
        with self.assertRaisesRegex(ValueError,"Collinear"):
            S.polarization(zs[0],zs[0],1)
        with self.assertRaisesRegex(ValueError,"factor the supplied"):
            S.ordered_feynman(ps,(zs[1],zs[0],zs[2],zs[3]),hs)
        with self.assertRaisesRegex(ValueError,"reference"):
            S.ordered_feynman(ps,zs,hs,references=S.references_for(zs)[:3])
        with self.assertRaisesRegex(ValueError,"conserve"):
            S.parke_taylor((zs[0],zs[0],zs[2],zs[3]),hs)
        pole_ps = ((Q(1),Q(0),Q(0),Q(1)),)*2+((Q(-1),Q(0),Q(0),Q(-1)),)*2
        with self.assertRaisesRegex(ValueError,"pole"):
            S.parke_taylor(tuple(S.factor(p) for p in pole_ps),hs)


def encode(value):
    if isinstance(value,Q):
        return str(value)
    if is_dataclass(value):
        return asdict(value)
    raise TypeError(type(value).__name__)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output",type=Path)
    args = parser.parse_args()
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(ParkeTaylorTests))
    if not result.wasSuccessful():
        raise SystemExit(1)
    samples = []
    for direction in YM.DIRECTIONS:
        ps,zs = point(direction)
        records = []
        for hs in product((-1,1),repeat=4):
            records.append({"helicities_all_outgoing":hs,
                            "ordered_1234_feynman":S.ordered_feynman(ps,zs,hs),
                            "ordered_1234_exchange_exchange_contact":S.ordered_feynman_parts(ps,zs,hs),
                            "ordered_1234_parke_taylor":S.parke_taylor(zs,hs),
                            "ordered_1324_parke_taylor":S.parke_taylor(zs,hs,(0,2,1,3)),
                            "circular_basis_adapters":S.circular_adapter(ps,zs,hs),
                            "color_0101_reconstruction":reconstructed_color(zs,hs,(0,1,0,1))})
        samples.append({"all_outgoing_momenta":ps,"spinors":zs,"references":S.references_for(zs),
                        "angle_bracket_matrix":tuple(tuple(S.angle(a,b) for b in zs) for a in zs),
                        "square_bracket_matrix":tuple(tuple(S.square(a,b) for b in zs) for a in zs),
                        "amplitudes":records})
    report = {"status":"exact-computational-benchmark-passed",
              "theory":"four-gluon tree, SU(3) color reconstruction",
              "ordered_convention":"i and g stripped; A=<ij>^4/(<12><23><34><41>); full M=-2 g^2(Cs A1234+Ct A1324)",
              "normalization":"rational spinor charts; explicit per-leg scale/phase and gauge adapter to physical circular basis",
              "exact_order_helicity_comparisons":1536,"nonzero_comparisons":576,
              "formal_agda_bridge":"not implemented","novel_physical_prediction":False,
              "scope":"four rational kinematic points, all four-point orders/helicities; not a general analytic proof",
              "samples":samples,"tests_run":result.testsRun}
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(report,default=encode,indent=2)+"\n",encoding="utf-8")
    print("Four-point Parke-Taylor: 1536 full complex comparisons, reference/little-group checks and SU(3) reconstruction passed")


if __name__ == "__main__":
    main()
