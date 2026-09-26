"""Heavy portal-loop EFT matching and its forward spectral positivity."""
from __future__ import annotations

import argparse
from dataclasses import asdict, is_dataclass
from fractions import Fraction as Q
from itertools import permutations
import json
import math
from pathlib import Path
import unittest

import scalar_one_loop as L
import scalar_portal_eft as E
from qed_fermion_scattering import dot
import yang_mills_four as Kinematics


class PortalEFTTests(unittest.TestCase):
    def test_exact_taylor_moments(self):
        self.assertEqual(tuple(E.series_coefficient(n) for n in range(1,5)),
                         (Q(1,6),Q(1,60),Q(1,420),Q(1,2520)))
        for n in range(1,13):
            # Independent exact integration of the expanded polynomial,
            # rather than evaluating the factorial/Beta-function formula.
            polynomial_integral = sum((Q((-1)**k*math.comb(n,k),n*(n+k+1)) for k in range(n+1)),Q(0))
            self.assertEqual(E.series_coefficient(n),polynomial_integral)
            numerical = L.integrate(lambda x:(x*(1-x))**n/n,tolerance=1e-14)
            self.assertLess(abs(numerical.value-float(polynomial_integral)),2e-13)

    def test_matching_with_remainder_bounds(self):
        for mass in (Q(1),Q(9,4)):
            for ratio in (Q(1,2),Q(1),Q(2),Q(3)):
                for cosine in (Q(1,3),Q(1)):
                    invariants = E.light_invariants(ratio*mass,cosine)
                    full = E.heavy_amplitude(invariants,float(mass),4*float(mass))
                    prefactor = full.portal_coupling**2/(32*math.pi**2)
                    for order in (2,4,8,12):
                        series = E.expansion(invariants,mass,order)
                        self.assertEqual(series.invariant_terms[0],0)
                        approximation = prefactor*float(series.dimensionless_sum)
                        bound = prefactor*float(series.dimensionless_remainder_bound)
                        self.assertLessEqual(abs(full.derivative_remainder-approximation),bound+3e-12)
                        self.assertEqual(full.derivative_remainder.imag,0)
        inv = E.light_invariants(Q(2),Q(1,3))
        target = E.heavy_amplitude(inv).derivative_remainder
        errors = [abs(target-0.7**2/(32*math.pi**2)*float(E.expansion(inv,Q(1),n).dimensionless_sum))
                  for n in (2,4,8,12)]
        self.assertTrue(all(a>b for a,b in zip(errors,errors[1:])))

    def test_dimension_six_cancellation_and_operator_normalization(self):
        ps = tuple(Kinematics.times(p,-1) for p in Kinematics.kinematics())
        inv = tuple(2*dot(ps[0],ps[i]) for i in (1,2,3))
        self.assertEqual(sum(inv),0)
        mass = Q(16)
        series = E.expansion(inv,mass,2)
        self.assertEqual(series.invariant_terms[0],0)  # on-shell, not off-shell operator absence
        assignments = sum((dot(ps[a],ps[b])*dot(ps[c],ps[d]) for a,b,c,d in permutations(range(4))),Q(0))
        self.assertEqual(assignments,2*sum(s*s for s in inv))
        coefficient = E.dimension_eight_operator(float(mass),0.7)
        contact = coefficient*float(assignments)
        matched = 0.7**2/(32*math.pi**2)*float(series.invariant_terms[1])
        self.assertAlmostEqual(contact,matched,places=15)
        self.assertGreater(abs(contact/24-matched),1e-9)

    def test_forward_spectral_positivity(self):
        for mass in (1.0,2.25,4.0):
            for g in (0.3,0.7,1.2):
                spectral = E.forward_spectral_coefficient(mass,g)
                expected = 4*E.dimension_eight_operator(mass,g)
                self.assertGreater(spectral.value.real,0)
                self.assertEqual(spectral.value.imag,0)
                self.assertLess(abs(spectral.value-expected),2e-12)
                self.assertGreater(abs(spectral.value/2-expected),1e-8)  # missing crossed cut
        self.assertEqual(E.forward_spectral_coefficient(1.0,0.0).value,0j)

    def test_matching_scale_and_portal_running(self):
        inv = E.light_invariants(Q(1),Q(1,3))
        g,quartic = 0.7,0.1
        a = E.heavy_amplitude(inv,1.0,1.0,g,quartic)
        running = 3*g*g/(32*math.pi**2)*math.log(9)
        b = E.heavy_amplitude(inv,1.0,9.0,g,quartic+running)
        self.assertAlmostEqual(a.matched_quartic,b.matched_quartic,places=14)
        self.assertLess(abs(a.tree_plus_heavy_loop-b.tree_plus_heavy_loop),2e-14)
        self.assertLess(abs(a.derivative_remainder-b.derivative_remainder),2e-14)
        zero = E.heavy_amplitude((0,0,0),1.0,9.0,g,quartic+running)
        self.assertLess(abs(zero.tree_plus_heavy_loop+a.matched_quartic),2e-14)
        self.assertEqual(zero.derivative_remainder,0j)

    def test_heavy_production_cut_with_massless_external_states(self):
        for mass in (1.0,2.25):
            for ratio in (5.0,9.0):
                inv = E.light_invariants(Q(str(ratio*mass)),Q(1))
                amplitude = E.heavy_amplitude(inv,mass,4*mass)
                cut = L.optical_cut(ratio*mass,mass,0.7)
                self.assertAlmostEqual(2*amplitude.heavy_loop.imag,cut,places=12)
                # Independent logarithmic quadrature at this light-external point.
                bubbles = sum((L.bubble_parameter(float(x),mass,4*mass).value for x in inv),0j)
                self.assertLess(abs(amplitude.heavy_loop-0.7**2*bubbles/(32*math.pi**2)),1e-11)
                with self.assertRaisesRegex(ValueError,"On-shell"):
                    L.amplitude(tuple(map(float,inv)),mass,4*mass)  # distinct theory's validator

    def test_decoupling_and_crossing(self):
        inv = E.light_invariants(Q(1,4),Q(1,3))
        c = E.dimension_eight_operator(1.0,0.7)
        self.assertEqual(E.dimension_eight_operator(4.0,0.7)*16,c)
        for order in permutations(inv):
            self.assertEqual(E.expansion(order,Q(1),6).dimensionless_sum,E.expansion(inv,Q(1),6).dimensionless_sum)
        errors = []
        for mass in (Q(1),Q(4),Q(16)):
            full = E.heavy_amplitude(inv,float(mass),float(mass))
            leading = 0.7**2/(32*math.pi**2)*float(E.expansion(inv,mass,2).dimensionless_sum)
            errors.append(abs(full.derivative_remainder/leading-1))
        self.assertTrue(all(a>b for a,b in zip(errors,errors[1:])))

    def test_theory_and_expansion_domain_guards(self):
        with self.assertRaisesRegex(ValueError,"Massless"):
            E.heavy_amplitude(L.physical_invariants(9.0,1.0,0.3))
        for inv in ((Q(4),Q(-2),Q(-2)),(Q(5),Q(-2),Q(-3))):
            with self.assertRaisesRegex(ValueError,"Taylor remainder"):
                E.expansion(inv,Q(1),4)
        with self.assertRaisesRegex(ValueError,"integer/Fraction"):
            E.expansion((1.0,-0.5,-0.5),Q(1),4)
        with self.assertRaises(ValueError):
            E.expansion((Q(1),Q(-1,2),Q(-1,2)),Q(0),4)
        with self.assertRaises(ValueError):
            E.series_coefficient(0)


def encode(value):
    if isinstance(value,Q):
        return str(value)
    if isinstance(value,complex):
        return {"real":value.real,"imag":value.imag}
    if is_dataclass(value):
        return asdict(value)
    raise TypeError(type(value).__name__)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output",type=Path)
    args = parser.parse_args()
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(PortalEFTTests))
    if not result.wasSuccessful():
        raise SystemExit(1)
    matches = []
    for mass in (Q(1),Q(9,4)):
        for ratio in (Q(1,2),Q(1),Q(2),Q(3)):
            for cosine in (Q(1,3),Q(1)):
                inv = E.light_invariants(ratio*mass,cosine)
                full = E.heavy_amplitude(inv,float(mass),4*float(mass))
                expansions = []
                for n in (2,4,8,12):
                    series = E.expansion(inv,mass,n)
                    pref = full.portal_coupling**2/(32*math.pi**2)
                    expansions.append({"exact_series":series,"numerical_approximation":pref*float(series.dimensionless_sum),
                                       "numerical_remainder_bound":pref*float(series.dimensionless_remainder_bound),
                                       "absolute_error":abs(full.derivative_remainder-pref*float(series.dimensionless_sum))})
                matches.append({"full_heavy_amplitude":full,"expansions":expansions})
    spectra = [{"heavy_mass_squared":m,"g":g,"operator_coefficient":E.dimension_eight_operator(m,g),
                "forward_s2_from_operator":4*E.dimension_eight_operator(m,g),
                "heavy_state_spectral_history":E.forward_spectral_coefficient(m,g)}
               for m in (1.0,2.25,4.0) for g in (0.3,0.7,1.2)]
    report = {"status":"heavy-portal-EFT-benchmark-passed",
              "theory":"massless external phi, massive internal chi; -g phi^2 chi^2/4 and -lambda_phi phi^4/4!",
              "sector":"tree quartic plus heavy one-loop g^2 correction ONLY; light lambda_phi^2 loops omitted; light pole-mass tuning assumed",
              "matching":"lambda_EFT=lambda_phi+3g^2 log(M_chi^2/mu^2)/(32pi^2)",
              "operator_basis":"L_EFT += c (partial phi . partial phi)^2, c=g^2/(3840pi^2 M_chi^4)",
              "on_shell_dimension_six":"linear s+t+u term cancels; not a claim that every off-shell dimension-six operator vanishes",
              "positivity":"heavy-sector forward s^2 coefficient=4c>0 for nonzero g, from both crossed heavy-state cuts",
              "accuracy":"Taylor coefficients and invariant sums exact rational; full loop/spectral integrals float; analytical tail bound plus 3e-12 numerical allowance in tests",
              "limitations":"no full light-loop IR treatment, general positivity theorem, independently calculated mass tuning, or Agda bridge",
              "novel_physical_prediction":False,"matching_records":matches,"spectral_records":spectra,"tests_run":result.testsRun}
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(report,default=encode,indent=2)+"\n",encoding="utf-8")
    print("Heavy portal EFT: rational matching, derivative-operator normalization and positive heavy-state dispersion passed")


if __name__=="__main__":
    main()
