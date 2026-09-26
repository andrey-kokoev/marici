"""Audit the mass/tadpole/LSZ assumptions of the scalar loop benchmarks."""
from __future__ import annotations

import argparse
from dataclasses import asdict, is_dataclass
from fractions import Fraction as Q
import json
import math
from pathlib import Path
import unittest

import scalar_one_loop as L
import scalar_portal_eft as E
import scalar_mass_renormalization as M


class ScalarMassTests(unittest.TestCase):
    def test_wick_contraction_factors(self):
        # Two labelled external contractions; the remaining pair is internal.
        self.assertEqual(Q(4*3,math.factorial(4)),Q(1,2))  # phi^4/4!
        self.assertEqual(Q(math.factorial(2),math.factorial(2)**2),Q(1,2))  # phi^2 chi^2/(2!2!)

    def test_proper_time_against_gamma_and_split_independence(self):
        for mass in (1.0,2.25):
            for mu2 in (mass,4*mass):
                for epsilon in (1/8,1/32,1/128,1/512,1.5):
                    expected = M.tadpole_gamma(mass,mu2,epsilon)
                    for split in (0.5,1.0,2.0):
                        result = M.tadpole_proper_time(mass,mu2,epsilon,split)
                        self.assertLess(abs(result.tadpole-expected),5e-9)
                        self.assertLess(result.propagated_error_estimate,5e-9)

    def test_convergent_one_dimensional_euclidean_anchor(self):
        for mass in (1.0,2.25):
            for mu2 in (mass,4*mass):
                # d=1, epsilon=3/2: q=sqrt(mass)*v/(1-v) gives
                # J_E=mu^3/pi integral_0^1 dv/[sqrt(mass)(v^2+(1-v)^2)].
                radial = L.integrate(lambda v:1/(math.sqrt(mass)*(v*v+(1-v)**2)))
                euclidean = mu2**1.5/math.pi*radial.value.real
                tadpole = M.tadpole_proper_time(mass,mu2,1.5)
                self.assertGreater(euclidean,0)
                self.assertLess(abs(-tadpole.tadpole/(16*math.pi**2)-euclidean),2e-11)
                self.assertAlmostEqual(euclidean,mu2**1.5/(2*math.sqrt(mass)),places=11)
        # Analytic continuation across the d=2 pole changes the DR sign.
        self.assertGreater(M.tadpole_gamma(1.0,1.0,0.01),0)
        self.assertLess(M.tadpole_gamma(1.0,1.0,1.5),0)

    def test_laurent_finite_part_convergence(self):
        values,errors = [],[]
        finite = M.tadpole_finite(1.0,1.0)
        for epsilon in (1/128,1/256,1/512,1/1024):
            result = M.tadpole_proper_time(1.0,1.0,epsilon)
            value = result.tadpole-L.uv_delta(epsilon)
            values.append(value)
            errors.append(abs(value-finite))
            self.assertLess(abs(epsilon*result.tadpole-1),4*epsilon)
        self.assertTrue(all(1.8<a/b<2.2 for a,b in zip(errors,errors[1:])))
        self.assertLess(abs(2*values[-1]-values[-2]-finite),3e-5)

    def test_mass_counterterms_poles_and_lsz(self):
        for coupling,loop_mass,target in ((0.7,1.0,1.0),(0.4,2.25,0.0)):
            for mu2 in (loop_mass,4*loop_mass):
                record = M.mass_renormalization(coupling,loop_mass,mu2)
                for epsilon in (0.1,0.01,0.001):
                    self.assertLess(abs(record.bare_laurent(epsilon)+record.counterterm(epsilon,"MSbar")-record.sigma_finite),2e-13)
                    self.assertLess(abs(record.bare_laurent(epsilon)+record.counterterm(epsilon,"on-shell")),2e-13)
                    self.assertGreater(abs(record.bare_laurent(epsilon)-record.counterterm(epsilon,"on-shell")),1e-3)
                tuned = record.tuned_msbar_parameter(target)
                self.assertAlmostEqual(record.pole_mass_squared(tuned,"MSbar"),target,places=14)
                self.assertEqual(record.pole_mass_squared(target,"on-shell"),target)
                for scheme,parameter in (("MSbar",tuned),("on-shell",target)):
                    self.assertAlmostEqual(record.inverse_propagator(target,parameter,scheme),0,places=14)
                    values = [record.self_energy(p,scheme) for p in (-3.0,0.0,2.0)]
                    self.assertEqual(values[0],values[1])
                    self.assertEqual(values[1],values[2])
                    slope = (record.inverse_propagator(target+0.01,parameter,scheme)
                             -record.inverse_propagator(target-0.01,parameter,scheme))/0.02
                    self.assertAlmostEqual(slope,1,places=12)
                self.assertEqual(record.momentum_derivative,0)
                self.assertEqual(record.lsz_residue_through_one_loop,1)

    def test_mass_running_keeps_the_pole_fixed_at_this_order(self):
        for coupling,loop_mass,parameter in ((0.7,1.0,1.0),(0.4,2.25,0.03)):
            a = M.mass_renormalization(coupling,loop_mass,loop_mass)
            b = M.mass_renormalization(coupling,loop_mass,9*loop_mass)
            change = M.running_mass_change(coupling,loop_mass,loop_mass,9*loop_mass)
            self.assertGreater(change,0)
            self.assertAlmostEqual(a.pole_mass_squared(parameter,"MSbar"),b.pole_mass_squared(parameter+change,"MSbar"),places=14)
            self.assertGreater(abs(a.pole_mass_squared(parameter,"MSbar")-b.pole_mass_squared(parameter,"MSbar")),1e-4)

    def test_tadpole_mass_derivative_is_zero_momentum_bubble(self):
        for mass in (1.0,2.25):
            mu2 = 4*mass
            for epsilon in (1/32,1/128,1/512):
                tadpole = M.tadpole_proper_time(mass,mu2,epsilon)
                bubble,_ = L.bubble_regulated_spacelike(0.0,mass,mu2,epsilon)
                self.assertLess(abs((1-epsilon)*tadpole.tadpole/mass-bubble),3e-9)
            step = mass*1e-5
            derivative = (M.tadpole_finite(mass+step,mu2)-M.tadpole_finite(mass-step,mu2))/(2*step)
            self.assertLess(abs(derivative-L.bubble_closed(0.0,mass,mu2)),5e-9)

    def test_portal_light_mass_tuning_vs_derivative_decoupling(self):
        small = M.mass_renormalization(0.7,1.0,1.0)
        heavy = M.mass_renormalization(0.7,4.0,4.0)
        self.assertGreater(small.tuned_msbar_parameter(0),0)
        self.assertAlmostEqual(heavy.tuned_msbar_parameter(0),4*small.tuned_msbar_parameter(0),places=14)
        self.assertEqual(16*E.dimension_eight_operator(4.0,0.7),E.dimension_eight_operator(1.0,0.7))
        self.assertGreater(abs(small.pole_mass_squared(0,"MSbar")),1e-4)
        self.assertAlmostEqual(small.pole_mass_squared(small.tuned_msbar_parameter(0),"MSbar"),0,places=14)
        # The untuned shift is not a claim of vacuum stability or a new bound.

    def test_domain_guards(self):
        for epsilon in (0.0,1.0,2.0,-0.1,math.nan):
            with self.assertRaises(ValueError):
                M.tadpole_gamma(1.0,1.0,epsilon)
        with self.assertRaises(ValueError):
            M.tadpole_proper_time(1.0,1.0,0.01,split=0.001)
        with self.assertRaises(ValueError):
            M.mass_renormalization(0.7,0.0,1.0)
        with self.assertRaises(ValueError):
            M.mass_renormalization(math.nan,1.0,1.0)
        record = M.mass_renormalization(0.7,1.0,1.0)
        with self.assertRaisesRegex(ValueError,"scheme"):
            record.self_energy(0.0,"unknown")
        with self.assertRaises(ValueError):
            record.tuned_msbar_parameter(-1.0)


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
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(ScalarMassTests))
    if not result.wasSuccessful():
        raise SystemExit(1)
    integral_records = []
    for mass in (1.0,2.25):
        for mu2 in (mass,4*mass):
            for epsilon in (1/8,1/32,1/128,1/512,1.5):
                for split in (0.5,1.0,2.0):
                    history = M.tadpole_proper_time(mass,mu2,epsilon,split)
                    integral_records.append({"proper_time_history":history,"gamma_value":M.tadpole_gamma(mass,mu2,epsilon),
                                             "absolute_discrepancy":abs(history.tadpole-M.tadpole_gamma(mass,mu2,epsilon))})
    masses = []
    for name,coupling,loop_mass,target in (("massive phi4",0.7,1.0,1.0),("heavy portal",0.4,2.25,0.0)):
        for mu2 in (loop_mass,4*loop_mass):
            record = M.mass_renormalization(coupling,loop_mass,mu2)
            tuned = record.tuned_msbar_parameter(target)
            masses.append({"model":name,"target_pole_mass_squared":target,"counterterm_record":record,
                           "msbar_mass_parameter":tuned,"msbar_pole":record.pole_mass_squared(tuned,"MSbar"),
                           "on_shell_pole":record.pole_mass_squared(target,"on-shell")})
    report = {"status":"numerical-scalar-mass-renormalization-benchmark-passed",
              "conventions":"inverse=p^2-m_R^2-Sigma_R, insertion=-i Sigma; Sigma_loop=-c T/(32pi^2); Sigma_R=Sigma_loop+delta_m^2",
              "tadpole":"T=M^2[Delta+1-log(M^2/mu^2)]+O(epsilon); gamma and UV-subtracted proper-time continuation compared",
              "coverage":"60 regulated integral comparisons, convergent d=1 anchor, finite-part limit, MSbar/on-shell poles, running, tadpole/bubble derivative and LSZ",
              "lsz":"Sigma has no external momentum dependence at this loop order, so Z=1; no higher-loop claim",
              "portal":"heavy local mass correction requires tuning; derivative decoupling does not remove it",
              "accuracy":"float arithmetic; propagated quadrature estimates not certified; integral comparison tolerance 5e-9",
              "limitations":"one-loop tadpole sector only; no higher-loop self-energy, complete portal renormalization, vacuum-stability result or Agda proof",
              "novel_physical_prediction":False,"integral_records":integral_records,"mass_records":masses,"tests_run":result.testsRun}
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(report,default=encode,indent=2)+"\n",encoding="utf-8")
    print("Scalar mass audit: tadpole continuation, mass subtraction/tuning, running and one-loop LSZ passed")


if __name__=="__main__":
    main()
