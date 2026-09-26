"""Numerical tests of causal PV reconstruction, excision and off-axis limits."""
from __future__ import annotations

import argparse
from dataclasses import asdict, is_dataclass
import json
import math
from pathlib import Path
import unittest

import scalar_one_loop as L
import scalar_bubble_dispersion as D


PARAMETERS = tuple((ratio*m2,m2,scale*m2) for m2 in (1.0,2.25)
                   for scale in (1.0,4.0) for ratio in (4.01,5.0,9.0,25.0,100.0))
COMPLEX_RATIOS = (-3+0.7j,1+0.2j,4+0.5j,5+0.3j,9+0.25j)


class BubbleDispersionTests(unittest.TestCase):
    def test_above_threshold_three_representations(self):
        for s,m2,mu2 in PARAMETERS:
            result = D.above(s,m2,mu2)
            closed = L.bubble_closed(s,m2,mu2)
            parameter = L.bubble_parameter(s,m2,mu2)
            self.assertLess(abs(result.value-closed),3e-10)
            self.assertLess(abs(result.value-parameter.value),3e-10)
            self.assertLessEqual(result.smooth_integral.estimated_error,1.01e-11)

    def test_explicit_excision_and_window_recovery(self):
        for s in (5.0,9.0,25.0):
            expected = D.above(s).value.real
            b = D.pole(s,1.0,1.0)
            errors = []
            for divisor in (8,16,32):
                delta = min(b,1-b)/divisor
                result = D.symmetric_excision(s,delta)
                self.assertLess(abs(result.corrected_principal_value-expected),3e-10)
                error = expected-result.truncated_real_value
                self.assertGreater(error,0)
                self.assertLess(abs(error/(3*delta)-1),0.01)
                errors.append(error)
            self.assertTrue(all(1.9<a/b<2.1 for a,b in zip(errors,errors[1:])))

    def test_boundary_discontinuity_and_phase_space(self):
        for s,m2 in ((5.0,1.0),(9.0,1.0),(20.25,2.25)):
            upper = D.above(s,m2,4*m2,1)
            lower = D.above(s,m2,4*m2,-1)
            self.assertEqual(lower.value,upper.value.conjugate())
            # B's discontinuity before the diagram symmetry/coupling factor.
            phase_space_disc = 16j*math.pi**2*L.phase_space_two_body(s,m2)
            self.assertLess(abs(upper.value-lower.value-phase_space_disc),3e-12)
            self.assertGreater(abs(upper.value-upper.value.real),0.1)
            self.assertGreater(abs(upper.value-upper.value.conjugate()),0.1)
        result = D.above(9.0)
        without_boundary = result.subtraction_constant+result.smooth_integral.value.real
        self.assertGreater(abs(without_boundary-result.value.real),0.1)

    def test_off_axis_independent_integrals_and_schwarz_reflection(self):
        for mass in (1.0,2.25):
            for ratio in COMPLEX_RATIOS:
                z = mass*ratio
                upper = D.off_axis_dispersion(z,mass,4*mass)
                reference = D.off_axis_parameter(z,mass,4*mass)
                lower = D.off_axis_dispersion(z.conjugate(),mass,4*mass)
                lower_reference = D.off_axis_parameter(z.conjugate(),mass,4*mass)
                self.assertLess(abs(upper.value-reference.value),3e-10)
                self.assertLess(abs(lower.value-lower_reference.value),3e-10)
                self.assertLess(abs(lower.value-upper.value.conjugate()),3e-10)
                self.assertGreater(upper.value.imag,0)
                self.assertLess(lower.value.imag,0)

    def test_off_axis_approach_is_not_the_real_axis_prescription(self):
        boundary = D.above(9.0).value
        errors = []
        for eta in (1/16,1/32,1/64,1/128):
            spectral = D.off_axis_dispersion(9+1j*eta)
            logarithmic = D.off_axis_parameter(9+1j*eta)
            self.assertLess(abs(spectral.value-logarithmic.value),3e-10)
            error = abs(spectral.value-boundary)
            self.assertGreater(error,1e-6)
            self.assertLess(error,eta)
            errors.append(error)
        self.assertTrue(all(1.8<a/b<2.2 for a,b in zip(errors,errors[1:])))

    def test_scale_covariance_and_subtraction_ambiguity(self):
        value = D.above(9.0,1.0,1.0).value
        self.assertLess(abs(D.above(63.0,7.0,7.0).value-value),2e-13)
        changed = D.above(9.0,1.0,9.0).value
        self.assertLess(abs(changed-value-math.log(9)),2e-13)
        self.assertEqual(changed.imag,value.imag)
        # The same cut permits a shifted local real subtraction constant.
        # Unitarity alone does not select the MSbar value B(0).

    def test_domain_guards(self):
        for s in (-1.0,0.0,4.0):
            with self.assertRaisesRegex(ValueError,"above-threshold"):
                D.above(s)
        with self.assertRaisesRegex(ValueError,"endpoint"):
            D.above(1e20)
        for delta in (0.0,-0.01,0.5,math.nan):
            with self.assertRaises(ValueError):
                D.symmetric_excision(9.0,delta)
        with self.assertRaises(ValueError):
            D.above(9.0,rim=0)
        with self.assertRaisesRegex(ValueError,"non-real"):
            D.off_axis_dispersion(9.0)
        with self.assertRaises(ValueError):
            D.off_axis_parameter(complex(9,math.inf))


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
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(BubbleDispersionTests))
    if not result.wasSuccessful():
        raise SystemExit(1)
    real_records = [{"dispersion":D.above(s,m2,mu2),"closed":L.bubble_closed(s,m2,mu2),
                     "parameter_history":L.bubble_parameter(s,m2,mu2)} for s,m2,mu2 in PARAMETERS]
    exclusions = []
    for s in (5.0,9.0,25.0):
        b = D.pole(s,1.0,1.0)
        exclusions.extend(D.symmetric_excision(s,min(b,1-b)/d) for d in (8,16,32))
    complex_records = []
    for mass in (1.0,2.25):
        for ratio in COMPLEX_RATIOS:
            for z in (mass*ratio,mass*ratio.conjugate()):
                complex_records.append({"spectral":D.off_axis_dispersion(z,mass,4*mass),
                                        "parameter":D.off_axis_parameter(z,mass,4*mass)})
    approach = [{"eta":eta,"spectral":D.off_axis_dispersion(9+1j*eta),
                 "parameter":D.off_axis_parameter(9+1j*eta),"real_axis_boundary":D.above(9.0).value}
                for eta in (1/16,1/32,1/64,1/128)]
    report = {"status":"numerical-causal-bubble-dispersion-benchmark-passed",
              "method":"subtract the simple spectral pole, integrate the smooth remainder, add the analytic PV log and causal +/-i*pi*residue",
              "subtraction_input":"B(0)=-log(m^2/mu^2); the cut alone does not determine this local constant",
              "coverage":"20 real-axis triple comparisons, nine symmetric exclusions, 20 off-axis double comparisons and four approach-to-cut samples",
              "accuracy":"float arithmetic, quadrature target 1e-11, comparisons 3e-10; no certified intervals",
              "real_axis_prescription":"exact rim sign supplied analytically; finite complex-invariant tests are separate, not a numerical i0 replacement",
              "limitations":"one-loop massive bubble only; endpoint-merged charts rejected; no second-sheet continuation, light-loop IR or formal proof",
              "novel_physical_prediction":False,"real_axis_records":real_records,"excision_records":exclusions,
              "off_axis_records":complex_records,"approach_records":approach,"tests_run":result.testsRun}
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(report,default=encode,indent=2)+"\n",encoding="utf-8")
    print("Causal bubble dispersion: PV, explicit excision, phase-space discontinuity and off-axis checks passed")


if __name__=="__main__":
    main()
