"""Exact pole and holomorphic soft coefficients, not near-pole sampling."""
from __future__ import annotations

import argparse
from dataclasses import asdict, is_dataclass
from fractions import Fraction as Q
import json
from pathlib import Path
import unittest

from qed_fermion_scattering import C, ZERO, dot
import gluon_spinor_helicity as S
import gluon_ordered_recursion as R
import gluon_bcfw as B
import gluon_pole_coefficients as P
from gluon_five_check import POINTS as FIVE_POINTS, mhv_reference, term_topologies, edge
from gluon_six_check import POINTS as SIX_POINTS


ALTERNATING = (-1,1,-1,1,-1,1)


def cut_case(ps,hs=ALTERNATING,rotation=0):
    zs = tuple(S.factor(p) for p in ps)
    node = B.evaluate(zs,hs,rotation)
    channels = tuple(c for c in node.channels if c.split==3)
    if len(channels)!=2:
        raise AssertionError("Expected both internal helicities")
    source = channels[0]
    shifted = source.left.spinors[:-1]+source.right.spinors[1:]
    shifted_hs = source.left.helicities[:-1]+source.right.helicities[1:]
    cut_ps = tuple(P.vector(z) for z in shifted)
    refs = S.references_for(shifted)
    eps = tuple(S.polarization(z,r,h) for z,r,h in zip(shifted,refs,shifted_hs))
    extracted = P.residue(cut_ps,eps,(0,1,2))
    products = tuple(S.parke_taylor(c.left.spinors,c.left.helicities)*
                     S.parke_taylor(c.right.spinors,c.right.helicities) for c in channels)
    return {"original_momenta":ps,"original_helicities":hs,"rotation":rotation,
            "shifted_spinors":shifted,"shifted_helicities":shifted_hs,
            "reference_spinors":refs,"polarizations":eps,
            "sewing_channels":channels,"four_point_products":products,
            "extracted_residue":extracted}


def lower_soft_reference(soft):
    i = soft.soft_label
    zs = soft.boundary_spinors[:i]+soft.boundary_spinors[i+1:]
    hs = soft.helicities[:i]+soft.helicities[i+1:]
    return mhv_reference(zs,hs)


class GluonLimitTests(unittest.TestCase):
    def test_three_independent_three_three_channels(self):
        for ps in SIX_POINTS:
            for rotation in (0,2,4):
                case = cut_case(ps,rotation=rotation)
                expected = sum(case["four_point_products"],ZERO)
                self.assertNotEqual(expected,ZERO)
                self.assertEqual(case["extracted_residue"].value,expected)
                self.assertEqual(sum((c.left.value*c.right.value for c in case["sewing_channels"]),ZERO),expected)

    def test_vanishing_helicity_residue(self):
        for ps in SIX_POINTS:
            hs = (-1,-1,-1,1,1,1)
            case = cut_case(ps,hs)
            self.assertEqual(case["extracted_residue"].value,ZERO)
            self.assertEqual(sum(case["four_point_products"],ZERO),ZERO)
            self.assertNotEqual(R.helicity(ps,hs)[0],ZERO)

    def test_residue_root_reference_and_ward(self):
        case = cut_case(SIX_POINTS[0])
        zs,hs = case["shifted_spinors"],case["shifted_helicities"]
        ps = tuple(P.vector(z) for z in zs)
        expected = case["extracted_residue"].value
        for offset in (0,1,3):
            refs = S.references_for(zs,offset)
            eps = tuple(S.polarization(z,r,h) for z,r,h in zip(zs,refs,hs))
            self.assertEqual(P.residue(ps,eps,(0,1,2)).value,expected)
        for offset in range(6):
            order = tuple(range(offset,6))+tuple(range(offset))
            self.assertEqual(P.residue(ps,eps,(0,1,2),order).value,expected)
        for leg in range(6):
            ward = eps[:leg]+(ps[leg],)+eps[leg+1:]
            self.assertEqual(P.residue(ps,ward,(0,1,2)).value,ZERO)
        with self.assertRaisesRegex(ValueError,"pole"):
            R.evaluate(ps,eps)

    def test_nmhv_positive_soft_coefficients(self):
        for ps in SIX_POINTS:
            zs = tuple(S.factor(p) for p in ps)
            for label in (1,3,5):
                soft = P.positive_soft(zs,ALTERNATING,label)
                expected = soft.soft_factor*lower_soft_reference(soft)
                self.assertNotEqual(expected,ZERO)
                self.assertEqual(soft.coefficient.value,expected)
                lower_ps = soft.momenta_zero[:label]+soft.momenta_zero[label+1:]
                lower_eps = soft.leading_polarizations[:label]+soft.leading_polarizations[label+1:]
                self.assertEqual(R.evaluate(lower_ps,lower_eps)[0],lower_soft_reference(soft))

    def test_mhv_exact_soft_family_at_finite_parameters(self):
        hs = (-1,-1,1,1,1)
        for ps in (FIVE_POINTS[0],FIVE_POINTS[-1]):
            zs = tuple(S.factor(p) for p in ps)
            for label in (2,4):
                soft = P.positive_soft(zs,hs,label)
                expected = soft.soft_factor*lower_soft_reference(soft)
                self.assertEqual(soft.coefficient.value,expected)
                # Special to this holomorphic MHV family: all lambda-only
                # hard factors are constant. Do NOT assert this for NMHV.
                for tau in (Q(1),Q(1,2),Q(1,3)):
                    shifted = P.soft_spinors(zs,label,C.of(tau))
                    shifted_ps = tuple(P.vector(z) for z in shifted)
                    eps = tuple(S.polarization(z,r,h) for z,r,h in zip(shifted,soft.reference_spinors,hs))
                    self.assertEqual(R.evaluate(shifted_ps,eps)[0]*tau*tau,expected)

    def test_soft_reference_and_ward(self):
        zs = tuple(S.factor(p) for p in SIX_POINTS[0])
        expected = P.positive_soft(zs,ALTERNATING,5).coefficient.value
        for offset in (0,1,3):
            soft = P.positive_soft(zs,ALTERNATING,5,offset)
            self.assertEqual(soft.coefficient.value,expected)
        for leg in range(6):
            p = P.vector(zs[leg]) if leg==5 else soft.momenta_zero[leg]
            eps = soft.leading_polarizations[:leg]+(p,)+soft.leading_polarizations[leg+1:]
            self.assertEqual(P.coefficient(soft.momenta_zero,eps,soft.coefficient.marks).value,ZERO)

    def test_both_soft_attachments_are_needed(self):
        zs = tuple(S.factor(p) for p in SIX_POINTS[0])
        soft = P.positive_soft(zs,ALTERNATING,5)
        parts = []
        for keep in (0,1):
            marks = tuple((labels,w if i==keep else ZERO) for i,(labels,w) in enumerate(soft.coefficient.marks))
            part = P.coefficient(soft.momenta_zero,soft.leading_polarizations,marks).value
            self.assertNotEqual(part,ZERO)
            self.assertNotEqual(part,soft.coefficient.value)
            parts.append(part)
        self.assertEqual(sum(parts,ZERO),soft.coefficient.value)
        graphs = tuple(g for t in soft.coefficient.root_terms for g in term_topologies(t,6))
        marks = tuple(edge(labels,6) for labels,_ in soft.coefficient.marks)
        incidences = [sum(mark in edges for mark in marks) for _,_,edges in graphs]
        self.assertEqual(len(graphs),38)
        self.assertEqual(incidences.count(1),20)
        self.assertEqual(incidences.count(0),18)
        self.assertTrue(all(i<=1 for i in incidences))
        self.assertTrue(all(sum(mark in edges for _,_,edges in graphs)==10 for mark in marks))

    def test_coefficient_histories(self):
        case = cut_case(SIX_POINTS[0])
        pending = [c for t in case["extracted_residue"].root_terms for c in t.children]
        seen = set()
        marked = 0
        while pending:
            current = pending.pop()
            if current.leaves in seen:
                continue
            seen.add(current.leaves)
            if current.marked_weight is not None:
                marked += 1
                self.assertEqual(current.denominator,ZERO)
                self.assertEqual(current.without_cut,R.ZERO_VECTOR)
                self.assertEqual(current.coefficient,tuple(current.marked_weight*x for x in R.vadd(t.without_cut for t in current.terms)))
            elif current.denominator is not None:
                self.assertNotEqual(current.denominator,ZERO)
                self.assertEqual(current.coefficient,tuple(x/current.denominator for x in R.vadd(t.coefficient for t in current.terms)))
            pending.extend(c for t in current.terms for c in t.children)
        self.assertEqual(marked,1)
        graphs = tuple(g for t in case["extracted_residue"].root_terms for g in term_topologies(t,6))
        self.assertEqual(sum((0,1,2) in edges for _,_,edges in graphs),9)

    def test_domain_guards(self):
        ps = SIX_POINTS[0]
        zs = tuple(S.factor(p) for p in ps)
        refs = S.references_for(zs)
        eps = tuple(S.polarization(z,r,h) for z,r,h in zip(zs,refs,ALTERNATING))
        with self.assertRaisesRegex(ValueError,"not on its pole"):
            P.residue(ps,eps,(0,1,2))
        with self.assertRaisesRegex(ValueError,"contiguous"):
            P.residue(ps,eps,(0,2))
        with self.assertRaisesRegex(ValueError,"Positive soft"):
            P.positive_soft(zs,ALTERNATING,0)
        collinear = tuple(tuple(C.of(w*x) for x in (1,1,0,0)) for w in (-3,-3,1,1,2,2))
        with self.assertRaisesRegex(ValueError,"higher-order"):
            P.coefficient(collinear,eps,(((0,1),C.of(1)),((0,1,2),C.of(1))))
        soft = P.positive_soft(zs,ALTERNATING,5)
        with self.assertRaisesRegex(ValueError,"Nonzero"):
            P.residue(soft.momenta_zero,soft.leading_polarizations,(0,1,2,3))
        # Split one outgoing four-point leg into a collinear pair. The soft
        # propagator then vanishes identically, outside the simple-pole domain.
        import yang_mills_four as YM
        four = tuple(YM.times(p,-1) for p in YM.kinematics())
        half = tuple(p/2 for p in four[2])
        five = four[:2]+(half,half)+four[3:]
        with self.assertRaisesRegex(ValueError,"Higher-order"):
            P.positive_soft(tuple(S.factor(p) for p in five),(-1,-1,1,1,1),2)


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
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(GluonLimitTests))
    if not result.wasSuccessful():
        raise SystemExit(1)
    residues = [cut_case(ps,rotation=r) for ps in SIX_POINTS for r in (0,2,4)]
    soft_records = []
    for ps in SIX_POINTS:
        zs = tuple(S.factor(p) for p in ps)
        for label in (1,3,5):
            soft = P.positive_soft(zs,ALTERNATING,label)
            soft_records.append({"history":soft,"independent_lower_amplitude":lower_soft_reference(soft),
                                 "predicted_leading_coefficient":soft.soft_factor*lower_soft_reference(soft)})
    report = {"status":"exact-computational-benchmark-passed",
              "method":"multilinear marked-edge coefficient extraction; no near-pole numerical fit",
              "residue_scope":"six nonzero 3|3 NMHV residues; two additional helicity-forbidden residues tested",
              "soft_scope":"six NMHV positive holomorphic soft coefficients; four MHV families also checked at three finite parameters",
              "soft_scaling":"lambda_s=tau lambda_s0, with adjacent tilde shifts conserving momentum; leading amplitude tau^-2",
              "domain":"simple isolated poles, or two mutually incompatible adjacent soft poles with nonzero slopes",
              "not_implemented":"negative-helicity soft extraction, subleading soft coefficients, multiple compatible cuts, general proofs, Agda bridge",
              "novel_physical_prediction":False,"residue_histories":residues,"soft_histories":soft_records,
              "tests_run":result.testsRun}
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(report,default=encode,indent=2)+"\n",encoding="utf-8")
    print("Exact gluon limits: six nonzero pole residues and six NMHV leading soft coefficients matched")


if __name__=="__main__":
    main()
