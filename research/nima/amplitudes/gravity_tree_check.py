"""Four/five-graviton KLT versus independently sewn Einstein on-shell seeds."""
from __future__ import annotations

import argparse
from dataclasses import asdict, is_dataclass
from fractions import Fraction as Q
from itertools import permutations, product
import json
from pathlib import Path
import unittest

from qed_fermion_scattering import C, ZERO, dot
import gluon_spinor_helicity as S
import gluon_bcfw as B
import gravity_tree as G
import yang_mills_four as YM
from gluon_five_check import POINTS as FIVE_POINTS, complex_three_point


FOUR_POINTS = tuple(tuple(YM.times(p,-1) for p in YM.kinematics(d)) for d in YM.DIRECTIONS)
POINTS = FOUR_POINTS+(FIVE_POINTS[0],FIVE_POINTS[-1])


def audit(test,node):
    test.assertEqual(B.total(B.momenta(node.spinors)),(ZERO,)*4)
    if node.rule!="unordered-bcfw":
        return
    n = len(node.spinors)
    i,j = node.shift
    test.assertEqual((node.helicities[i],node.helicities[j]),(-2,2))
    test.assertEqual(len(node.channels),2*((1<<(n-2))-2))
    test.assertEqual(node.value,sum((c.contribution for c in node.channels),ZERO))
    # Gravity's improved 1/z^2 falloff gives the bonus residue identity.
    test.assertEqual(sum((c.pole*c.contribution for c in node.channels),ZERO),ZERO)
    partitions = set()
    for c in node.channels:
        partitions.add(c.left_labels)
        test.assertEqual(set(c.left_labels)|set(c.right_labels),set(range(n)))
        test.assertFalse(set(c.left_labels)&set(c.right_labels))
        test.assertIn(i,c.left_labels)
        test.assertIn(j,c.right_labels)
        test.assertEqual(c.propagator-c.pole*c.shift_coefficient,ZERO)
        test.assertEqual(c.contribution,c.left.value*c.right.value/c.propagator)
        test.assertIn(c.internal_helicity_left,(-2,2))
        test.assertEqual(c.left.helicities[-1],-c.right.helicities[0])
        internal = S.vector(S.outer(c.internal_spinors.lam,c.internal_spinors.tilde))
        test.assertEqual(dot(internal,internal),ZERO)
        test.assertEqual(B.momenta(c.left.spinors)[-1],tuple(-x for x in internal))
        test.assertEqual(B.momenta(c.right.spinors)[0],internal)
        audit(test,c.left)
        audit(test,c.right)
    test.assertEqual(len(partitions),(1<<(n-2))-2)


class GravityTreeTests(unittest.TestCase):
    def test_three_point_inputs(self):
        for anti,hs in ((False,(-2,-2,2)),(True,(2,2,-2))):
            _,zs = complex_three_point(anti)
            self.assertEqual(G.bcfw(zs,hs).value,C.of(1))
            for order in permutations(range(3)):
                self.assertEqual(G.bcfw(tuple(zs[i] for i in order),tuple(hs[i] for i in order)).value,C.of(1))

    def test_all_helicities_four_and_five(self):
        nonzero = 0
        comparisons = 0
        for ps in POINTS:
            zs = tuple(S.factor(p) for p in ps)
            for hs in product((-2,2),repeat=len(ps)):
                on_shell = G.bcfw(zs,hs)
                double_copy,_ = G.klt(zs,hs)
                self.assertEqual(on_shell.value,double_copy)
                nonzero += int(on_shell.value!=ZERO)
                comparisons += 1
        self.assertEqual(comparisons,128)
        self.assertEqual(nonzero,64)

    def test_sewing_and_bonus_identities(self):
        for ps in (FOUR_POINTS[0],FIVE_POINTS[-1]):
            zs = tuple(S.factor(p) for p in ps)
            for hs in ((-2,-2)+(2,)*(len(ps)-2),(2,2)+(-2,)*(len(ps)-2)):
                node = G.bcfw(zs,hs)
                audit(self,node)
                nonzero = [c for c in node.channels if c.contribution!=ZERO]
                self.assertGreaterEqual(len(nonzero),2)
                # Dropping one nonzero residue destroys the bonus identity.
                self.assertNotEqual(sum((c.pole*c.contribution for c in node.channels),ZERO)
                                    -nonzero[0].pole*nonzero[0].contribution,ZERO)

    def test_bose_symmetry(self):
        for ps in (FOUR_POINTS[0],FIVE_POINTS[-1]):
            zs = tuple(S.factor(p) for p in ps)
            hs = (-2,-2)+(2,)*(len(ps)-2)
            expected = G.bcfw(zs,hs).value
            if len(ps)==4:
                orders = tuple(permutations(range(4)))
            else:
                # Adjacent transpositions, not a claim of exhaustive S5 tests.
                orders = []
                for i in range(4):
                    order = list(range(5))
                    order[i],order[i+1] = order[i+1],order[i]
                    orders.append(tuple(order))
            for order in orders:
                z,h = tuple(zs[i] for i in order),tuple(hs[i] for i in order)
                self.assertEqual(G.bcfw(z,h).value,expected)
                self.assertEqual(G.klt(z,h)[0],expected)

    def test_shift_and_reference_independence(self):
        zs = tuple(S.factor(p) for p in FIVE_POINTS[-1])
        hs = (-2,-2,2,2,2)
        expected = G.klt(zs,hs)[0]
        for shift in ((0,2),(0,4),(1,3)):
            self.assertEqual(G.bcfw(zs,hs,shift).value,expected)
        for offsets in ((1,0),(0,3),(1,3)):
            self.assertEqual(G.klt(zs,hs,*offsets)[0],expected)
        with self.assertRaisesRegex(ValueError,"only"):
            G.bcfw(zs,hs,(2,0))

    def test_tensor_ward_in_either_copy(self):
        for ps in (FOUR_POINTS[0],FIVE_POINTS[-1]):
            zs = tuple(S.factor(p) for p in ps)
            hs = (-1,-1)+(1,)*(len(ps)-2)
            eps = tuple(S.polarization(z,r,h) for z,r,h in zip(zs,S.references_for(zs),hs))
            for leg in range(len(ps)):
                ward = eps[:leg]+(ps[leg],)+eps[leg+1:]
                self.assertEqual(G.klt_tensor(ps,ward,eps)[0],ZERO)
                self.assertEqual(G.klt_tensor(ps,eps,ward)[0],ZERO)

    def test_spin_two_weights_and_mass_dimension(self):
        for ps in (FOUR_POINTS[0],FIVE_POINTS[-1]):
            zs = tuple(S.factor(p) for p in ps)
            hs = (-2,-2)+(2,)*(len(ps)-2)
            expected = G.bcfw(zs,hs).value
            t = C(Q(1),Q(1))
            for leg in (0,len(ps)-1):
                scaled = list(zs)
                z = zs[leg]
                scaled[leg] = S.Spinors(tuple(t*x for x in z.lam),tuple(x/t for x in z.tilde))
                weight = C.of(1)
                for _ in range(abs(2*hs[leg])):
                    weight = weight/t if hs[leg]>0 else weight*t
                self.assertEqual(G.bcfw(scaled,hs).value,weight*expected)
                self.assertEqual(G.klt(scaled,hs)[0],weight*expected)
            # p -> 4p gives stripped mass-dimension-two amplitude -> 16M.
            balanced = tuple(S.Spinors(tuple(2*x for x in z.lam),tuple(2*x for x in z.tilde)) for z in zs)
            self.assertEqual(G.bcfw(balanced,hs).value,16*expected)
            self.assertEqual(G.klt(balanced,hs)[0],16*expected)

    def test_sign_kernel_and_domain_hostiles(self):
        zs = tuple(S.factor(p) for p in FOUR_POINTS[0])
        hs = (-2,-2,2,2)
        node = G.bcfw(zs,hs)
        value,terms = G.klt(zs,hs)
        self.assertEqual(node.value,C.of(-256))
        self.assertNotEqual(-value,node.value)
        self.assertNotEqual(terms[0].left_amplitude*terms[0].right_amplitude,node.value)
        with self.assertRaisesRegex(ValueError,"helicities"):
            G.bcfw(zs,(-1,-1,1,1))
        with self.assertRaisesRegex(ValueError,"conserve"):
            G.bcfw((zs[1],)+zs[1:],hs)


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
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(GravityTreeTests))
    if not result.wasSuccessful():
        raise SystemExit(1)
    samples = []
    for ps in POINTS:
        zs = tuple(S.factor(p) for p in ps)
        values,histories = [],[]
        for hs in product((-2,2),repeat=len(ps)):
            node = G.bcfw(zs,hs)
            value,terms = G.klt(zs,hs)
            values.append({"helicities":hs,"bcfw":node.value,"klt":value})
            if hs in ((-2,-2)+(2,)*(len(ps)-2),(2,2)+(-2,)*(len(ps)-2)):
                histories.append({"helicities":hs,"gravity_recursion":node,"yang_mills_klt_terms":terms})
        samples.append({"momenta":ps,"spinors":zs,"comparisons":values,"history_examples":histories})
    report = {"status":"exact-computational-benchmark-passed","theory":"four-dimensional two-derivative Einstein pure-graviton trees",
              "convention":"strip -i and (kappa/2)^(n-2); positive cubic seeds; +ML MR/P^2 sewing; KLT4=-s AA, KLT5=+ss AA+ss AA",
              "independent_paths":"unordered spin-two BCFW versus KLT using off-shell Yang-Mills Feynman currents",
              "coverage":"all 16 four-point helicities at four points; all 32 five-point helicities at two points; 128 comparisons, 64 nonzero",
              "internal_states":"BCFW +/-2 gravitons only; pure external graviton tree sector of YM double copy; no loop-purity claim",
              "physical_inputs":"Einstein cubic seeds, good-shift boundary theorem, same-helicity zero, KLT; none derived from an action here",
              "not_implemented":"Einstein off-shell vertices, matter/external dilaton or two-form amplitudes, gravity loops, general proofs, Agda bridge",
              "novel_physical_prediction":False,"samples":samples,"tests_run":result.testsRun}
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(report,default=encode,indent=2)+"\n",encoding="utf-8")
    print("Four/five gravitons: independent BCFW/KLT, spin-two weights, tensor Ward and gravity bonus checks passed")


if __name__=="__main__":
    main()
