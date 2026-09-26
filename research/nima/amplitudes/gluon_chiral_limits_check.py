"""Negative soft coefficients and six-point 2|4 factorization branches."""
from __future__ import annotations

import argparse
from dataclasses import asdict, is_dataclass
from fractions import Fraction as Q
import json
from pathlib import Path
import unittest

from qed_fermion_scattering import C, ZERO
import gluon_spinor_helicity as S
import gluon_ordered_recursion as R
import gluon_bcfw as B
import gluon_pole_coefficients as P
from gluon_five_check import POINTS as FIVE_POINTS, mhv_reference, term_topologies, edge
from gluon_six_check import POINTS as SIX_POINTS
from gluon_limits_check import ALTERNATING, lower_soft_reference


def reference(zs,hs):
    # Three-point amplitudes live on distinct complex branches. The wrong
    # branch is zero, not an evaluation of a 0/0 Parke-Taylor expression.
    return B.seed(zs,hs) if len(zs)==3 else mhv_reference(zs,hs)


CUT_CONFIGS = tuple((hs,rotation,split)
    for hs,rotations in ((ALTERNATING,(0,2,4)),(tuple(-h for h in ALTERNATING),(1,3,5)))
    for rotation in rotations for split in (2,4))


def two_four_case(ps,rotation,split,helicities=ALTERNATING):
    node = B.evaluate(tuple(S.factor(p) for p in ps),helicities,rotation)
    channels = tuple(c for c in node.channels if c.split==split)
    if len(channels)!=2:
        raise AssertionError("Both sewn helicities required")
    source = channels[0]
    zs = source.left.spinors[:-1]+source.right.spinors[1:]
    hs = source.left.helicities[:-1]+source.right.helicities[1:]
    cut_ps = tuple(P.vector(z) for z in zs)
    refs = S.references_for(zs)
    eps = tuple(S.polarization(z,r,h) for z,r,h in zip(zs,refs,hs))
    result = P.residue(cut_ps,eps,tuple(range(split)))
    products = tuple(reference(c.left.spinors,c.left.helicities)*
                     reference(c.right.spinors,c.right.helicities) for c in channels)
    return {"original_momenta":ps,"original_helicities":helicities,"rotation":rotation,"split":split,
            "shifted_spinors":zs,"helicities":hs,"references":refs,
            "polarizations":eps,"sewn_channels":channels,"reference_products":products,
            "residue":result}


class ChiralLimitTests(unittest.TestCase):
    def test_negative_nmhv_soft_coefficients(self):
        for ps in SIX_POINTS:
            zs = tuple(S.factor(p) for p in ps)
            for label in (0,2,4):
                soft = P.negative_soft(zs,ALTERNATING,label)
                expected = soft.soft_factor*lower_soft_reference(soft)
                self.assertNotEqual(expected,ZERO)
                self.assertEqual(soft.coefficient.value,expected)
                # The lower amplitude is MHV; omitting the soft minus sign
                # cannot be hidden by an overall phase or a squared comparison.
                self.assertNotEqual(soft.coefficient.value,-expected)
                hard_ps = soft.momenta_zero[:label]+soft.momenta_zero[label+1:]
                hard_eps = soft.leading_polarizations[:label]+soft.leading_polarizations[label+1:]
                self.assertEqual(R.evaluate(hard_ps,hard_eps)[0],lower_soft_reference(soft))

    def test_anti_mhv_finite_soft_family(self):
        hs = (1,1,-1,-1,-1)
        for ps in (FIVE_POINTS[0],FIVE_POINTS[-1]):
            zs = tuple(S.factor(p) for p in ps)
            for label in (2,4):
                soft = P.negative_soft(zs,hs,label)
                expected = soft.soft_factor*lower_soft_reference(soft)
                self.assertEqual(soft.coefficient.value,expected)
                for tau in (Q(1),Q(1,2),Q(1,3)):
                    shifted = P.soft_spinors(zs,label,C.of(tau),-1)
                    eps = tuple(S.polarization(z,r,h) for z,r,h in zip(shifted,soft.reference_spinors,hs))
                    self.assertEqual(R.evaluate(tuple(P.vector(z) for z in shifted),eps)[0]*tau*tau,expected)

    def test_negative_reference_and_ward(self):
        zs = tuple(S.factor(p) for p in SIX_POINTS[0])
        expected = P.negative_soft(zs,ALTERNATING,2).coefficient.value
        for offset in (0,1,3):
            soft = P.negative_soft(zs,ALTERNATING,2,offset)
            self.assertEqual(soft.coefficient.value,expected)
        for leg in range(6):
            momentum = P.vector(zs[leg]) if leg==2 else soft.momenta_zero[leg]
            eps = soft.leading_polarizations[:leg]+(momentum,)+soft.leading_polarizations[leg+1:]
            self.assertEqual(P.coefficient(soft.momenta_zero,eps,soft.coefficient.marks).value,ZERO)
        with self.assertRaisesRegex(ValueError,"Negative soft"):
            P.negative_soft(zs,ALTERNATING,1)
        with self.assertRaisesRegex(ValueError,"Valid soft helicity"):
            P.soft_spinors(zs,2,C.of(1),0)

    def test_two_four_factorization_all_adjacent_channels(self):
        count = 0
        covered = set()
        for ps in SIX_POINTS:
            for hs,rotation,split in CUT_CONFIGS:
                case = two_four_case(ps,rotation,split,hs)
                expected = sum(case["reference_products"],ZERO)
                self.assertNotEqual(expected,ZERO)
                self.assertEqual(case["residue"].value,expected)
                self.assertEqual(sum((c.left.value*c.right.value for c in case["sewn_channels"]),ZERO),expected)
                graphs = tuple(g for t in case["residue"].root_terms for g in term_topologies(t,6))
                marked = edge(tuple(range(split)),6)
                self.assertEqual(sum(marked in edges for _,_,edges in graphs),10)
                order = tuple(range(rotation,6))+tuple(range(rotation))
                covered.add(edge(order[:split],6))
                count += 1
        self.assertEqual(count,24)
        self.assertEqual(covered,{tuple(sorted((i,(i+1)%6))) for i in range(6)})

    def test_three_point_branches_and_internal_phase(self):
        branches = set()
        for split in (2,4):
            case = two_four_case(SIX_POINTS[0],0,split)
            for c,product in zip(case["sewn_channels"],case["reference_products"]):
                seed = c.left if split==2 else c.right
                angles = tuple(S.angle(seed.spinors[i],seed.spinors[(i+1)%3]) for i in range(3))
                squares = tuple(S.square(seed.spinors[i],seed.spinors[(i+1)%3]) for i in range(3))
                self.assertNotEqual(all(x==ZERO for x in angles),all(x==ZERO for x in squares))
                if product!=ZERO:
                    branches.add("anti" if all(x==ZERO for x in angles) else "mhv")
                # A non-real internal little-group rescaling must cancel
                # between opposite-helicity factors, including the -P leg.
                t = C(Q(1),Q(1))
                def scaled(z):
                    return S.Spinors(tuple(t*x for x in z.lam),tuple(x/t for x in z.tilde))
                left = c.left.spinors[:-1]+(scaled(c.left.spinors[-1]),)
                right = (scaled(c.right.spinors[0]),)+c.right.spinors[1:]
                self.assertEqual(reference(left,c.left.helicities)*reference(right,c.right.helicities),product)
        self.assertEqual(branches,{"mhv","anti"})

    def test_two_four_residue_ward_and_root(self):
        for split in (2,4):
            case = two_four_case(SIX_POINTS[0],0,split)
            ps = tuple(P.vector(z) for z in case["shifted_spinors"])
            eps = case["polarizations"]
            expected = case["residue"].value
            for offset in range(6):
                order = tuple(range(offset,6))+tuple(range(offset))
                self.assertEqual(P.residue(ps,eps,tuple(range(split)),order).value,expected)
            for leg in range(6):
                ward = eps[:leg]+(ps[leg],)+eps[leg+1:]
                self.assertEqual(P.residue(ps,ward,tuple(range(split))).value,ZERO)
            with self.assertRaisesRegex(ValueError,"pole"):
                R.evaluate(ps,eps)


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
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(ChiralLimitTests))
    if not result.wasSuccessful():
        raise SystemExit(1)
    soft_records = []
    for ps in SIX_POINTS:
        zs = tuple(S.factor(p) for p in ps)
        for label in (0,2,4):
            soft = P.negative_soft(zs,ALTERNATING,label)
            soft_records.append({"history":soft,"lower_reference":lower_soft_reference(soft),
                                 "predicted_coefficient":soft.soft_factor*lower_soft_reference(soft)})
    report = {"status":"exact-computational-benchmark-passed",
              "negative_soft_convention":"tilde_s=tau tilde_s0; factor -[ab]/([as][sb]) with reverse-determinant squares",
              "coverage":"six NMHV negative-soft coefficients; 24 2|4 residues, all six adjacent channels using two alternating helicity assignments at two starting points", 
              "sewing":"three-point complex branch seeds times five-point MHV/anti-MHV; explicit opposite internal helicities",
              "limitations":"finite checks only; no subleading soft, compatible multiple cuts, general proof or Agda bridge",
              "novel_physical_prediction":False,"soft_histories":soft_records,
              "residue_histories":[two_four_case(ps,r,s,hs) for ps in SIX_POINTS for hs,r,s in CUT_CONFIGS],
              "tests_run":result.testsRun}
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(report,default=encode,indent=2)+"\n",encoding="utf-8")
    print("Negative soft coefficients and both complex 2|4 factorization branches matched")


if __name__=="__main__":
    main()
