"""Five-point ordered recursion versus independent MHV/anti-MHV formulas.
No on-shell recursion or non-MHV closed formula is used by the Feynman engine.
"""
from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import asdict, is_dataclass
from fractions import Fraction as Q
from itertools import combinations, permutations, product
import json
from pathlib import Path
import unittest

from qed_fermion_scattering import C, ZERO, dot
import gluon_spinor_helicity as S
import gluon_ordered_recursion as R
import yang_mills_four as YM


def five_point(a=3,b=4,c=5,tilted=False):
    a,b,c = Q(a),Q(b),Q(c)
    if a<=0 or b<=0 or c<=0 or a*a+b*b!=c*c:
        raise ValueError("Positive Pythagorean energies required")
    if tilted:
        u,v = (Q(3,5),Q(4,5),Q(0)), (Q(-12,25),Q(9,25),Q(4,5))
    else:
        u,v = (Q(1),Q(0),Q(0)), (Q(0),Q(1),Q(0))
    energy = (a+b+c)/2
    return ((-energy,Q(0),Q(0),-energy),(-energy,Q(0),Q(0),energy),
            (a,)+tuple(a*x for x in u),(b,)+tuple(b*x for x in v),
            (c,)+tuple(-a*x-b*y for x,y in zip(u,v)))


POINTS = (five_point(),five_point(5,12,13),five_point(8,15,17),five_point(tilted=True))


def mhv_reference(spinors,helicities,order=None):
    n = len(spinors)
    order = tuple(range(n)) if order is None else tuple(order)
    if n<3 or len(helicities)!=n or sorted(order)!=list(range(n)) or any(h not in (-1,1) for h in helicities):
        raise ValueError("Valid helicities and cyclic ordering required")
    if any(sum((z.lam[i]*z.tilde[j] for z in spinors),ZERO)!=ZERO for i,j in product(range(2),repeat=2)):
        raise ValueError("Spinor momenta do not conserve momentum")
    negative = [i for i,h in enumerate(helicities) if h==-1]
    positive = [i for i,h in enumerate(helicities) if h==1]
    if len(negative)==2:
        bracket, pair, sign = S.angle,negative,1
    elif len(positive)==2:
        # Square brackets were defined with reverse determinant orientation.
        # The parity formula therefore carries (-1)^n in these conventions.
        bracket,pair,sign = S.square,positive,(-1)**n
    elif len(negative)<2 or len(positive)<2:
        return ZERO
    else:
        raise NotImplementedError("Neither MHV nor anti-MHV: independent reference not implemented")
    numerator = bracket(spinors[pair[0]],spinors[pair[1]])
    denominator = C.of(1)
    for i,j in zip(order,order[1:]+order[:1]):
        denominator *= bracket(spinors[i],spinors[j])
    if denominator==ZERO:
        raise ValueError("Reference formula at a bracket pole or wrong three-point branch")
    return sign*numerator*numerator*numerator*numerator/denominator


def edge(labels,n):
    other = tuple(i for i in range(n) if i not in labels)
    return min((tuple(sorted(labels)),other),key=lambda x:(len(x),x))


def current_topologies(current,n):
    if len(current.leaves)==1:
        yield 0,0,()
        return
    for term in current.terms:
        for cubic,quartic,edges in term_topologies(term,n):
            yield cubic,quartic,tuple(sorted(edges+(edge(current.leaves,n),)))


def term_topologies(term,n):
    for children in product(*(current_topologies(c,n) for c in term.children)):
        yield (int(term.vertex=="cubic")+sum(x[0] for x in children),
               int(term.vertex=="quartic")+sum(x[1] for x in children),
               tuple(sorted(e for child in children for e in child[2])))


def expected_topologies(order):
    pairs = tuple(tuple(sorted((a,b))) for a,b in zip(order,order[1:]+order[:1]))
    result = Counter((1,1,(p,)) for p in pairs)
    for left,right in combinations(pairs,2):
        if set(left).isdisjoint(right):
            result[(3,0,tuple(sorted((left,right))))] += 1
    return result


def complex_three_point(anti=False):
    zs = tuple(S.Spinors(tuple(map(C.of,a)),tuple(map(C.of,(1,0))))
               for a in ((1,0),(0,1),(-1,-1)))
    if anti:
        zs = tuple(S.Spinors(z.tilde,z.lam) for z in zs)
    return tuple(S.vector(S.outer(z.lam,z.tilde)) for z in zs),zs


class FiveGluonTests(unittest.TestCase):
    def test_three_point_sign_seeds(self):
        for anti,hs in ((False,(-1,-1,1)),(True,(1,1,-1))):
            ps,zs = complex_three_point(anti)
            eps = tuple(S.polarization(z,r,h) for z,r,h in zip(zs,S.references_for(zs),hs))
            actual,_ = R.evaluate(ps,eps)
            self.assertEqual(actual,C.of(1))
            self.assertEqual(actual,mhv_reference(zs,hs))
        # These are complex three-point branches, not real noncollinear scattering.
        self.assertTrue(any(x.imag!=0 for p in complex_three_point()[0] for x in p))

    def test_four_point_regression(self):
        for direction in YM.DIRECTIONS:
            ps = tuple(YM.times(p,-1) for p in YM.kinematics(direction))
            zs = tuple(S.factor(p) for p in ps)
            for hs in product((-1,1),repeat=4):
                self.assertEqual(R.helicity(ps,hs)[0],S.ordered_feynman(ps,zs,hs))

    def test_all_five_helicities(self):
        nonzero = 0
        for ps in POINTS:
            zs = tuple(S.factor(p) for p in ps)
            for hs in product((-1,1),repeat=5):
                actual,_ = R.helicity(ps,hs)
                expected = mhv_reference(zs,hs)
                self.assertEqual(actual,expected)
                nonzero += int(actual!=ZERO)
        self.assertEqual(nonzero,80)  # 10 MHV + 10 anti-MHV per point.
        self.assertEqual(R.helicity(POINTS[0],(-1,-1,1,1,1))[0],C(Q(-48,125),Q(264,125)))
        self.assertEqual(R.helicity(POINTS[0],(1,1,-1,-1,-1))[0],C(Q(-1,15),Q(-11,30)))

    def test_all_orders_and_topology_multisets(self):
        ps = POINTS[-1]
        zs = tuple(S.factor(p) for p in ps)
        for order in permutations(range(5)):
            expected_graphs = expected_topologies(order)
            self.assertEqual(len(expected_graphs),10)
            self.assertEqual(Counter((x[0],x[1]) for x in expected_graphs),Counter({(3,0):5,(1,1):5}))
            for hs in ((-1,-1,1,1,1),(1,1,-1,-1,-1)):
                actual,terms = R.helicity(ps,hs,order)
                self.assertEqual(actual,mhv_reference(zs,hs,order))
                self.assertEqual(Counter(g for t in terms for g in term_topologies(t,5)),expected_graphs)

    def test_cyclic_root_and_odd_reflection(self):
        ps = POINTS[0]
        for hs in product((-1,1),repeat=5):
            expected = R.helicity(ps,hs)[0]
            for offset in range(5):
                order = tuple(range(offset,5))+tuple(range(offset))
                self.assertEqual(R.helicity(ps,hs,order)[0],expected)
            self.assertEqual(R.helicity(ps,hs,(4,3,2,1,0))[0],-expected)

    def test_reference_and_ward_identities(self):
        missing_contact_witness = False
        for ps in POINTS:
            zs = tuple(S.factor(p) for p in ps)
            for hs in ((-1,-1,1,1,1),(-1,1,-1,1,1),(1,1,-1,-1,-1)):
                expected = mhv_reference(zs,hs)
                for offset in (0,1,3):
                    refs = S.references_for(zs,offset)
                    eps = tuple(S.polarization(z,r,h) for z,r,h in zip(zs,refs,hs))
                    self.assertEqual(R.evaluate(ps,eps)[0],expected)
                for leg in range(5):
                    ward_eps = eps[:leg]+(ps[leg],)+eps[leg+1:]
                    actual,terms = R.evaluate(ps,ward_eps)
                    self.assertEqual(actual,ZERO)
                    incomplete = C.of(dot(R.vadd(t.numerator for t in terms if t.vertex=="cubic"),ward_eps[-1]))/16
                    missing_contact_witness |= incomplete!=ZERO
        self.assertTrue(missing_contact_witness)

    def test_current_transversality(self):
        for ps in POINTS:
            _,terms = R.helicity(ps,(-1,1,-1,1,1))
            pending = [c for t in terms for c in t.children]
            seen = set()
            while pending:
                c = pending.pop()
                if c.leaves in seen:
                    continue
                seen.add(c.leaves)
                self.assertEqual(C.of(dot(c.momentum,c.value)),ZERO)
                pending.extend(child for t in c.terms for child in t.children)

    def test_five_point_bcj_relation(self):
        # Move leg 0 through the fixed ordering (1,2,3,4). Test the
        # Feynman recursion itself, not just the closed reference formula.
        orders = ((1,0,2,3,4),(1,2,0,3,4),(1,2,3,0,4))
        for ps in POINTS:
            s01,s02,s03 = (C.of(2*dot(ps[0],ps[i])) for i in (1,2,3))
            weights = (s01,s01+s02,s01+s02+s03)
            for hs in product((-1,1),repeat=5):
                self.assertEqual(sum((w*R.helicity(ps,hs,order)[0]
                                      for w,order in zip(weights,orders)),ZERO),ZERO)

    def test_balanced_scaling_and_anti_sign_hostile(self):
        ps = POINTS[-1]
        zs = tuple(S.factor(p) for p in ps)
        scaled_ps = tuple(tuple(4*x for x in p) for p in ps)
        scaled_zs = tuple(S.Spinors(tuple(2*x for x in z.lam),tuple(2*x for x in z.tilde)) for z in zs)
        for hs in ((-1,-1,1,1,1),(1,1,-1,-1,-1)):
            refs = S.references_for(zs)
            eps = tuple(S.polarization(z,r,h) for z,r,h in zip(zs,refs,hs))
            expected = mhv_reference(zs,hs)/4  # mass dimension 4-n=-1.
            self.assertEqual(R.evaluate(scaled_ps,eps)[0],expected)
            self.assertEqual(mhv_reference(scaled_zs,hs),expected)
        anti = R.helicity(ps,(1,1,-1,-1,-1))[0]
        self.assertNotEqual(anti,ZERO)
        self.assertNotEqual(anti,-mhv_reference(zs,(1,1,-1,-1,-1)))

    def test_invalid_inputs_and_non_mhv_guard(self):
        ps = POINTS[0]
        with self.assertRaisesRegex(ValueError,"cyclic order"):
            R.helicity(ps,(-1,-1,1,1,1),(0,1,2,3,3))
        with self.assertRaisesRegex(ValueError,"helicity"):
            R.helicity(ps,(-1,-1,1,1))
        from scalar_tree_baseline import SIX
        zs6 = tuple(S.factor(p) for p in SIX)
        with self.assertRaisesRegex(NotImplementedError,"Neither MHV"):
            mhv_reference(zs6,(-1,-1,-1,1,1,1))
        collinear = tuple(tuple(Q(x) for x in p) for p in ((-2,0,0,-2),(-1,0,0,1),(1,0,0,1),(1,0,0,1),(1,0,0,-1)))
        with self.assertRaisesRegex(ValueError,"pole"):
            R.helicity(collinear,(-1,-1,1,1,1))


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
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(FiveGluonTests))
    if not result.wasSuccessful():
        raise SystemExit(1)
    samples = []
    for ps in POINTS:
        zs = tuple(S.factor(p) for p in ps)
        refs = S.references_for(zs)
        records = []
        for hs in product((-1,1),repeat=5):
            value,terms = R.helicity(ps,hs,references=refs)
            records.append({"helicities":hs,"ordered_amplitude":value,
                            "independent_reference":mhv_reference(zs,hs),"root_terms":terms})
        samples.append({"all_outgoing_momenta":ps,"spinors":zs,"reference_spinors":refs,"amplitudes":records})
    report = {"status":"exact-computational-benchmark-passed","theory":"five-gluon color-ordered tree",
              "normalization":"i and coupling stripped; integer tensors and unnormalized spinor polarizations divided by 2^(n-1)",
              "anti_mhv_convention":"(-1)^n [ij]^4/product cyclic square brackets; reverse-determinant square orientation",
              "coverage":"all 32 helicities at four real rational points; all 120 orders for one MHV and one anti-MHV assignment at the tilted point",
              "topologies":"five cubic trees and five cubic/quartic trees, each once",
              "three_point_seeds":"nonzero complex MHV and anti-MHV branches checked independently",
              "not_implemented":"general analytic proof, full five-gluon color reconstruction, on-shell recursion, six-point NMHV reference, Agda bridge",
              "novel_physical_prediction":False,"samples":samples,"tests_run":result.testsRun}
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(report,default=encode,indent=2)+"\n",encoding="utf-8")
    print("Five gluons: all helicity sectors matched, 10 planar diagrams audited, Ward/reference and odd-point sign checks passed")


if __name__=="__main__":
    main()
