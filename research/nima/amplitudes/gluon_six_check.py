"""Six-gluon NMHV: off-shell currents versus independent BCFW sewing."""
from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import asdict, is_dataclass
from fractions import Fraction as Q
from itertools import combinations, product
import json
from pathlib import Path
import unittest

from qed_fermion_scattering import C, ZERO, dot
import gluon_spinor_helicity as S
import gluon_ordered_recursion as R
import gluon_bcfw as B
from gluon_five_check import POINTS as FIVE_POINTS, mhv_reference, term_topologies, edge
import yang_mills_four as YM


def six_point(a,b,u,v):
    a,b = Q(a),Q(b)
    u,v = tuple(map(Q,u)),tuple(map(Q,v))
    if a<=0 or b<=0 or sum(x*x for x in u)!=1 or sum(x*x for x in v)!=1:
        raise ValueError("Positive energies and unit directions required")
    energy = a+b
    return ((-energy,Q(0),Q(0),-energy),(-energy,Q(0),Q(0),energy)) + tuple(
        (weight,)+tuple(sign*weight*x for x in direction)
        for weight,direction in ((a,u),(b,v)) for sign in (-1,1))


EXCEPTIONAL_POINT = six_point(Q(3,2),Q(5,4),
    (Q(2,3),Q(1,3),Q(2,3)),(Q(0),Q(5,13),Q(12,13)))


def generic_six(weights):
    directions = ((Q(1),Q(0),Q(0)),(Q(0),Q(1),Q(0)),
                  (Q(0),Q(0),Q(1)),(Q(3,5),Q(4,5),Q(0)))
    outgoing = tuple((Q(w),)+tuple(Q(w)*x for x in d) for w,d in zip(weights,directions))
    total = tuple(sum((p[mu] for p in outgoing),Q(0)) for mu in range(4))
    direction = (Q(2,3),Q(1,3),Q(2,3))
    energy = dot(total,total)/(2*(total[0]-sum(x*y for x,y in zip(total[1:],direction))))
    incoming = (energy,)+tuple(energy*x for x in direction)
    other = tuple(x-y for x,y in zip(total,incoming))
    return (tuple(-x for x in incoming),tuple(-x for x in other))+outgoing


POINTS = (generic_six((1,2,3,5)),generic_six((2,3,5,7)))
NMHV = tuple(hs for hs in product((-1,1),repeat=6) if hs.count(-1)==3)


def polygon_topologies(n=6):
    """Independent finite polygon dissection enumeration, not current recursion.
    Cubic/quartic vertices correspond to triangular/quadrilateral faces.
    """
    diagonals = tuple((a,b) for a in range(n) for b in range(a+2,n) if (a,b)!=(0,n-1))
    result = Counter()
    for mask in range(1<<len(diagonals)):
        chosen = tuple(d for i,d in enumerate(diagonals) if mask & (1<<i))
        if any(a<c<b<d or c<a<d<b for (a,b),(c,d) in combinations(chosen,2)):
            continue
        faces = [tuple(range(n))]
        for a,b in chosen:
            for index,face in enumerate(faces):
                if a in face and b in face:
                    x,y = sorted((face.index(a),face.index(b)))
                    left,right = face[x:y+1],face[y:]+face[:x+1]
                    if len(left)>=3 and len(right)>=3:
                        faces[index:index+1] = [left,right]
                        break
            else:
                raise AssertionError("Dissection did not split a face")
        if all(len(face) in (3,4) for face in faces):
            channels = tuple(sorted(edge(tuple(range(a,b)),n) for a,b in chosen))
            result[(sum(len(f)==3 for f in faces),sum(len(f)==4 for f in faces),channels)] += 1
    return result


def audit_node(test,node):
    test.assertEqual(B.total(B.momenta(node.spinors)),(ZERO,)*4)
    if node.rule!="bcfw":
        return
    test.assertEqual(node.value,sum((c.contribution for c in node.channels),ZERO))
    offset = node.rotation
    zs = node.spinors[offset:]+node.spinors[:offset]
    hs = node.helicities[offset:]+node.helicities[:offset]
    test.assertNotEqual((hs[0],hs[-1]),(1,-1))
    for channel in node.channels:
        test.assertEqual(channel.status,"sewn-residue")
        test.assertNotEqual(channel.shift_coefficient,ZERO)
        test.assertEqual(channel.propagator-channel.pole*channel.shift_coefficient,ZERO)
        internal = S.vector(S.outer(channel.internal_spinors.lam,channel.internal_spinors.tilde))
        test.assertEqual(dot(internal,internal),ZERO)
        test.assertEqual(channel.left.helicities[-1],-channel.right.helicities[0])
        test.assertEqual(B.momenta(channel.left.spinors)[-1],tuple(-x for x in internal))
        test.assertEqual(B.momenta(channel.right.spinors)[0],internal)
        test.assertEqual(channel.contribution,channel.left.value*channel.right.value/channel.propagator)
        # Shift conserves total momentum and all external mass shells.
        first = S.Spinors(zs[0].lam,tuple(a-channel.pole*b for a,b in zip(zs[0].tilde,zs[-1].tilde)))
        last = S.Spinors(tuple(a+channel.pole*b for a,b in zip(zs[-1].lam,zs[0].lam)),zs[-1].tilde)
        test.assertEqual(channel.left.spinors[0],first)
        test.assertEqual(channel.right.spinors[-1],last)
        audit_node(test,channel.left)
        audit_node(test,channel.right)


class SixGluonTests(unittest.TestCase):
    def test_four_and_five_point_calibration(self):
        four = tuple(YM.times(p,-1) for p in YM.kinematics(YM.DIRECTIONS[2]))
        for ps in (four,FIVE_POINTS[-1]):
            zs = tuple(S.factor(p) for p in ps)
            for hs in product((-1,1),repeat=len(ps)):
                node = B.evaluate(zs,hs)
                self.assertEqual(node.value,mhv_reference(zs,hs))

    def test_all_twenty_nmhv_at_two_points(self):
        for ps in POINTS:
            zs = tuple(S.factor(p) for p in ps)
            for hs in NMHV:
                on_shell = B.evaluate(zs,hs)
                off_shell,_ = R.helicity(ps,hs)
                self.assertEqual(on_shell.value,off_shell)
                self.assertNotEqual(off_shell,ZERO)

    def test_other_helicity_sectors(self):
        ps = POINTS[0]
        zs = tuple(S.factor(p) for p in ps)
        for hs in ((-1,-1,1,1,1,1),(1,1,-1,-1,-1,-1),(-1,1,1,1,1,1),(1,)*6):
            expected = mhv_reference(zs,hs)
            self.assertEqual(B.evaluate(zs,hs).value,expected)
            self.assertEqual(R.helicity(ps,hs)[0],expected)

    def test_independent_polygon_diagram_count(self):
        expected = polygon_topologies()
        self.assertEqual(len(expected),38)
        self.assertTrue(all(count==1 for count in expected.values()))
        self.assertEqual(Counter((c,q) for c,q,_ in expected),Counter({(4,0):14,(2,1):21,(0,2):3}))
        _,terms = R.helicity(POINTS[0],NMHV[0])
        self.assertEqual(Counter(g for t in terms for g in term_topologies(t,6)),expected)

    def test_full_sewing_audit(self):
        ps = POINTS[0]
        zs = tuple(S.factor(p) for p in ps)
        for hs in ((-1,-1,-1,1,1,1),(-1,1,-1,1,-1,1)):
            audit_node(self,B.evaluate(zs,hs))

    def test_different_good_shifts(self):
        ps = POINTS[0]
        zs = tuple(S.factor(p) for p in ps)
        hs = (-1,1,-1,1,-1,1)
        expected = R.helicity(ps,hs)[0]
        for rotation in (0,2,4):
            self.assertEqual(B.evaluate(zs,hs,rotation).value,expected)
        with self.assertRaisesRegex(ValueError,"Bad"):
            B.evaluate(zs,hs,1)

    def test_ward_and_reference_on_off_shell_side(self):
        ps = POINTS[-1]
        zs = tuple(S.factor(p) for p in ps)
        hs = (-1,1,-1,1,-1,1)
        expected = B.evaluate(zs,hs).value
        for offset in (0,1,3):
            refs = S.references_for(zs,offset)
            eps = tuple(S.polarization(z,r,h) for z,r,h in zip(zs,refs,hs))
            self.assertEqual(R.evaluate(ps,eps)[0],expected)
        for leg in range(6):
            self.assertEqual(R.evaluate(ps,eps[:leg]+(ps[leg],)+eps[leg+1:])[0],ZERO)

    def test_exceptional_shift_guard_and_fallback(self):
        # Retain the symmetric input that exposed the zero-coefficient bug.
        # Some amplitudes can switch charts; others must be explicitly refused.
        zs = tuple(S.factor(p) for p in EXCEPTIONAL_POINT)
        hs = (-1,-1,-1,1,1,1)
        node = B.evaluate(zs,hs)
        self.assertEqual(node.value,R.helicity(EXCEPTIONAL_POINT,hs)[0])
        pending = [node]
        failures = []
        while pending:
            current = pending.pop()
            failures.extend(reason for _,reason in current.failed_rotations)
            for channel in current.channels:
                pending.extend((channel.left,channel.right))
        self.assertTrue(any("Zero shift coefficient" in reason for reason in failures))
        refused = (-1,-1,1,1,-1,1)
        self.assertNotEqual(R.helicity(EXCEPTIONAL_POINT,refused)[0],ZERO)
        with self.assertRaisesRegex(B.ExceptionalKinematics,"All admitted"):
            B.evaluate(zs,refused)

    def test_sewing_sign_hostile(self):
        zs = tuple(S.factor(p) for p in POINTS[0])
        node = B.evaluate(zs,(-1,-1,-1,1,1,1))
        self.assertNotEqual(node.value,ZERO)
        self.assertNotEqual(-sum((c.contribution for c in node.channels),ZERO),node.value)
        with self.assertRaisesRegex(ValueError,"conserve"):
            B.evaluate((zs[1],)+zs[1:],(-1,-1,-1,1,1,1))


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
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(SixGluonTests))
    if not result.wasSuccessful():
        raise SystemExit(1)
    samples = []
    for ps in POINTS:
        zs = tuple(S.factor(p) for p in ps)
        values = []
        retained = []
        for hs in NMHV:
            node = B.evaluate(zs,hs)
            off,terms = R.helicity(ps,hs)
            values.append({"helicities":hs,"bcfw":node.value,"off_shell":off})
            if hs in ((-1,-1,-1,1,1,1),(-1,1,-1,1,-1,1)):
                retained.append({"helicities":hs,"bcfw_history":node,"off_shell_history":terms})
        samples.append({"all_outgoing_momenta":ps,"spinors":zs,"nmhv_values":values,
                        "full_history_examples":retained})
    exceptional_zs = tuple(S.factor(p) for p in EXCEPTIONAL_POINT)
    refused = (-1,-1,1,1,-1,1)
    try:
        B.evaluate(exceptional_zs,refused)
    except B.ExceptionalKinematics as exc:
        refusal = str(exc)
    else:
        raise AssertionError("Exceptional-chart regression unexpectedly changed")
    report = {"status":"exact-computational-benchmark-passed","theory":"six-gluon ordered tree, NMHV",
              "exceptional_chart_regression":{"momenta":EXCEPTIONAL_POINT,"refused_helicities":refused,
                  "finite_off_shell_value":R.helicity(EXCEPTIONAL_POINT,refused)[0],"bcfw_refusal":refusal,
                  "successful_fallback_history":B.evaluate(exceptional_zs,(-1,-1,-1,1,1,1))},
              "scope":"all 20 NMHV helicity assignments at two rational points; selected other sectors and good shifts",
              "on_shell_algorithm":"adjacent BCFW using only three-point seeds and same-helicity zero sectors",
              "large_z_input":"vanishing boundary for admitted Yang-Mills shifts is assumed, not proved by finite tests",
              "sewing_convention":"left -P=(-lambda_P,tilde_P), right P=(lambda_P,tilde_P), opposite helicities; +AL*AR/P^2",
              "off_shell_topologies":{"four_cubic":14,"two_cubic_one_quartic":21,"two_quartic":3},
              "formal_agda_bridge":"not implemented","novel_physical_prediction":False,
              "samples":samples,"tests_run":result.testsRun}
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(report,default=encode,indent=2)+"\n",encoding="utf-8")
    print("Six-gluon NMHV: 40 independent comparisons, 38 planar diagrams, BCFW sewing audits passed")


if __name__=="__main__":
    main()
