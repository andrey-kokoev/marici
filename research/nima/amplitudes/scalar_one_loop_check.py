"""Numerical massive phi^4 bubble, MSbar bookkeeping and unitarity tests."""
from __future__ import annotations

import argparse
from dataclasses import asdict, is_dataclass
from itertools import permutations
import json
import math
from pathlib import Path
import unittest

import scalar_one_loop as L


RATIOS = (-16.0,-1.0,0.0,1.0,3.0,4.0,5.0,9.0,25.0)
PARAMETERS = tuple((ratio*m2,m2,scale*m2) for m2 in (1.0,2.25) for scale in (1.0,4.0) for ratio in RATIOS)


class ScalarLoopTests(unittest.TestCase):
    def test_parameter_integral_against_closed_form(self):
        for s,m2,mu2 in PARAMETERS:
            result = L.bubble_parameter(s,m2,mu2)
            self.assertLess(abs(result.value-L.bubble_closed(s,m2,mu2)),3e-10)
            self.assertLessEqual(result.estimated_error,1.01e-11)
            self.assertEqual(len(result.intervals),len(result.quadratures))
            for q in result.quadratures:
                self.assertLess(abs(sum((p.value for p in q.panels),0j)-q.value),2e-13)

    def test_subtracted_dispersion_below_threshold(self):
        for m2 in (1.0,2.25):
            for ratio in (-16.0,-1.0,0.0,1.0,3.0,3.9):
                value,q = L.bubble_dispersion_below(ratio*m2,m2,4*m2)
                self.assertLess(abs(value-L.bubble_closed(ratio*m2,m2,4*m2)),3e-10)
                self.assertLessEqual(q.estimated_error,1.01e-11)
        with self.assertRaisesRegex(ValueError,"below threshold"):
            L.bubble_dispersion_below(5.0)

    def test_threshold_and_boundary_values(self):
        self.assertEqual(L.bubble_closed(0.0),0j)
        self.assertEqual(L.bubble_closed(4.0),2+0j)
        self.assertLess(abs(L.bubble_closed(4-1e-8)-2),2e-4)
        self.assertLess(abs(L.bubble_closed(4+1e-8)-2),2e-4)
        for s in (5.0,9.0,25.0):
            upper = L.bubble_parameter(s)
            lower = L.bubble_parameter(s,rim=-1)
            self.assertLess(abs(lower.value-upper.value.conjugate()),3e-10)
            self.assertGreater(upper.value.imag,0)
            expected = 2j*math.pi*math.sqrt(1-4/s)
            self.assertLess(abs(upper.value-lower.value-expected),3e-10)

    def test_optical_theorem_and_identical_state_factor(self):
        for m2 in (1.0,2.25):
            for ratio in (5.0,9.0,25.0):
                for coupling in (0.3,0.7):
                    s = ratio*m2
                    invariants = L.physical_invariants(s,m2,1.0)  # forward scattering
                    amplitude = L.amplitude(invariants,m2,4*m2,coupling)
                    cut = L.optical_cut(s,m2,coupling)
                    self.assertAlmostEqual(2*amplitude.loop.imag,cut,places=12)
                    numerical_bubble = L.bubble_parameter(s,m2,4*m2).value
                    self.assertLess(abs(coupling**2*numerical_bubble.imag/(16*math.pi**2)-cut),1e-11)
                    # Omitting 1/2! for identical intermediate particles fails.
                    self.assertGreater(abs(2*amplitude.loop.imag-2*cut),1e-5)
                    self.assertGreater(abs(-2*amplitude.loop.imag-cut),1e-5)
        self.assertEqual(L.optical_cut(4.0,1.0,0.7),0)
        self.assertEqual(L.optical_cut(3.0,1.0,0.7),0)

    def test_dimensional_regulator_before_subtraction(self):
        finite = L.bubble_closed(-3.0,1.0,2.0)
        approximations = []
        errors = []
        for epsilon in (1/128,1/256,1/512,1/1024):
            bare,_ = L.bubble_regulated_spacelike(-3.0,1.0,2.0,epsilon)
            subtracted = bare-L.uv_delta(epsilon)
            approximations.append(subtracted)
            errors.append(abs(subtracted-finite))
            self.assertLess(abs(epsilon*bare-1),4*epsilon)
        self.assertTrue(all(1.8<a/b<2.2 for a,b in zip(errors,errors[1:])))
        # Richardson is a convergence test, not an exact finite-epsilon equality.
        extrapolated = 2*approximations[-1]-approximations[-2]
        self.assertLess(abs(extrapolated-finite),2e-5)

    def test_uv_counterterm_and_scale_running(self):
        invariants = L.physical_invariants(9.0,1.0,0.3)
        coupling = 0.7
        a = L.amplitude(invariants,1.0,1.0,coupling)
        for epsilon in (0.1,0.01,0.001):
            # Laurent coefficients through epsilon^0 only: not a claim about
            # cancellation of finite-epsilon O(epsilon) terms.
            bare = a.total+a.uv_pole_coefficient*L.uv_delta(epsilon)
            counterterm = -3*coupling**2/(32*math.pi**2)*L.uv_delta(epsilon)
            self.assertLess(abs(bare+counterterm-a.total),2e-13)
        b = L.amplitude(invariants,1.0,9.0,coupling)
        # beta_lambda=3 lambda^2/(16 pi^2), expanded consistently to lambda^2.
        running_tree_change = -3*coupling**2/(16*math.pi**2)*math.log(3)
        self.assertLess(abs(b.total+running_tree_change-a.total),2e-13)
        self.assertGreater(abs(b.total-a.total),1e-4)

    def test_crossing_and_dimensionless_scaling(self):
        invariants = L.physical_invariants(9.0,1.0,0.3)
        expected = L.amplitude(invariants).total
        for order in permutations(invariants):
            self.assertLess(abs(L.amplitude(order).total-expected),2e-13)
        self.assertLess(abs(L.amplitude(tuple(7*x for x in invariants),7,7).total-expected),2e-13)
        self.assertAlmostEqual(sum(invariants),4.0)

    def test_quadrature_and_physical_domain_guards(self):
        for m2,mu2 in ((0.0,1.0),(-1.0,1.0),(1.0,0.0),(math.inf,1.0)):
            with self.assertRaises(ValueError):
                L.bubble_closed(1.0,m2,mu2)
        with self.assertRaises(ValueError):
            L.bubble_parameter(math.nan)
        with self.assertRaises(ValueError):
            L.bubble_closed(5.0,rim=0)
        with self.assertRaisesRegex(ValueError,"On-shell"):
            L.amplitude((1.0,1.0,1.0))
        with self.assertRaisesRegex(ValueError,"Physical"):
            L.physical_invariants(3.0,1.0,0.0)
        with self.assertRaisesRegex(ValueError,"Spacelike"):
            L.bubble_regulated_spacelike(5.0)
        with self.assertRaisesRegex(ArithmeticError,"depth exhausted"):
            L.integrate(math.exp,tolerance=1e-30,max_depth=0)


def encode(value):
    if isinstance(value,complex):
        return {"real":value.real,"imag":value.imag}
    if is_dataclass(value):
        return asdict(value)
    raise TypeError(type(value).__name__)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output",type=Path)
    args = parser.parse_args()
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(ScalarLoopTests))
    if not result.wasSuccessful():
        raise SystemExit(1)
    records = []
    for s,m2,mu2 in PARAMETERS:
        q = L.bubble_parameter(s,m2,mu2)
        record = {"invariant":s,"mass_squared":m2,"scale_squared":mu2,"closed_form":L.bubble_closed(s,m2,mu2),
                  "parameter_history":q,"absolute_discrepancy":abs(q.value-L.bubble_closed(s,m2,mu2))}
        if s<4*m2:
            value,dispersion = L.bubble_dispersion_below(s,m2,mu2)
            record.update({"dispersion_value":value,"dispersion_history":dispersion})
        records.append(record)
    amplitudes = []
    for m2 in (1.0,2.25):
        for ratio in (5.0,9.0,25.0):
            a = L.amplitude(L.physical_invariants(ratio*m2,m2,1.0),m2,4*m2,0.7)
            amplitudes.append({"amplitude":a,"twice_imaginary_part":2*a.loop.imag,
                               "identical_two_body_tree_cut":L.optical_cut(ratio*m2,m2,0.7)})
    regulated = []
    for epsilon in (1/128,1/256,1/512,1/1024):
        bare,q = L.bubble_regulated_spacelike(-3.0,1.0,2.0,epsilon)
        regulated.append({"epsilon":epsilon,"bare_bubble":bare,"delta":L.uv_delta(epsilon),
                          "subtracted":bare-L.uv_delta(epsilon),"quadrature":q})
    report = {"status":"floating-point-one-loop-benchmark-passed",
              "theory":"massive real phi^4, tree plus order lambda^2 four-point amplitude",
              "scheme":"d=4-2epsilon, MSbar coupling, pole mass; tadpole mass subtraction assumed and not evaluated independently",
              "normalization":"M_tree=-lambda; each channel lambda^2/(32pi^2) B; delta_lambda=3lambda^2 Delta/(32pi^2)",
              "analytic_continuation":"physical upper s rim gives Im B=+pi sqrt(1-4m^2/s); lower rim is its conjugate",
              "unitarity":"2 Im M_loop=(1/2!) integral dPhi_2 |M_tree|^2; no loop amplitude on cut RHS",
              "accuracy":"float arithmetic; quadrature target 1e-11, comparisons 3e-10; error estimates are not certified bounds",
              "coverage":"36 parameter/closed bubble comparisons, subthreshold dispersion, finite-epsilon convergence, subtraction/running and optical checks",
              "not_implemented":"massless infrared limits, above-threshold principal-value dispersion, higher loops, complete tadpole calculation, Agda bridge",
              "novel_physical_prediction":False,"bubble_records":records,"physical_amplitudes":amplitudes,
              "regulated_spacelike_examples":regulated,"tests_run":result.testsRun}
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(report,default=encode,indent=2)+"\n",encoding="utf-8")
    print("Massive scalar one loop: numerical bubble/dispersion, MSbar running and two-body optical checks passed")


if __name__=="__main__":
    main()
