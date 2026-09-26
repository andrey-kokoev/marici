"""Exact tree Compton amplitudes, with both s/u electron-exchange diagrams.

Metric +---; physical p,k incoming and p',k' outgoing; delta-stripped i M.
M=-e^2 ubar(p') [eps'*/ (p/+k/+m)/(s-m^2) eps/
                  + eps/ (p/-k'/+m)/(u-m^2) eps'*/] u(p).
Uses canonical electron spins and two real transverse photon polarizations.
"""
from __future__ import annotations

import argparse
from dataclasses import asdict, is_dataclass
from fractions import Fraction as Q
from itertools import product
import json
from pathlib import Path
import unittest

from qed_fermion_scattering import (
    C, ZERO, I, SIGNS, GAMMA, eye, add, scale, multiply, apply, dagger, trace,
    dot, plus, minus, slash, spinor, adjoint,
)

CHARGE = Q(1, 3)
DIRECTIONS = ((Q(1), Q(0), Q(0)), (Q(3, 5), Q(4, 5), Q(0)),
              (Q(2, 3), Q(1, 3), Q(2, 3)), (Q(0), Q(0), Q(-1)),
              (Q(0), Q(0), Q(1)))


def transverse(k):
    if len(k) != 4 or k[0] <= 0 or dot(k, k) != 0:
        raise ValueError("Positive-energy null photon required")
    x, y, z = (component/k[0] for component in k[1:])
    if z == -1:
        return ((Q(0), Q(1), Q(0), Q(0)), (Q(0), Q(0), Q(-1), Q(0)))
    return ((Q(0), 1-x*x/(1+z), -x*y/(1+z), -x),
            (Q(0), -x*y/(1+z), 1-y*y/(1+z), -y))


def kinematics(direction=DIRECTIONS[0], ratio=Q(2), mass=Q(1)):
    if mass <= 0 or ratio <= 1 or sum((x*x for x in direction), Q(0)) != 1:
        raise ValueError("Positive mass, ratio>1 and unit direction required")
    energy = mass*(ratio+1/ratio)/2
    omega = mass*(ratio-1/ratio)/2
    return ((energy, Q(0), Q(0), -omega), (omega, Q(0), Q(0), omega),
            (energy,) + tuple(-omega*x for x in direction),
            (omega,) + tuple(omega*x for x in direction))


def validate(ps, mass):
    if len(ps) != 4 or mass <= 0:
        raise ValueError("Four momenta and positive electron mass required")
    p, k, out, kout = ps
    for v, m2 in ((p, mass**2), (k, Q(0)), (out, mass**2), (kout, Q(0))):
        if len(v) != 4 or v[0] <= 0 or dot(v, v) != m2:
            raise ValueError("Positive-energy on-shell momenta required")
    if plus(p, k) != plus(out, kout):
        raise ValueError("Energy-momentum conservation failed")
    if dot(plus(p, k), plus(p, k))-mass**2 == 0 or dot(minus(p, kout), minus(p, kout))-mass**2 == 0:
        raise ValueError("Electron propagator pole")


def kernels(ps, mass, eps, eps_out):
    validate(ps, mass)
    p, k, _, kout = ps
    qs, qu = plus(p, k), minus(p, kout)
    ds, du = dot(qs, qs)-mass**2, dot(qu, qu)-mass**2
    incoming = slash(eps)
    outgoing = slash(tuple(C.of(x).conjugate() for x in eps_out))
    ns, nu = add(slash(qs), scale(eye(), mass)), add(slash(qu), scale(eye(), mass))
    return (scale(multiply(multiply(outgoing, ns), incoming), 1/ds),
            scale(multiply(multiply(incoming, nu), outgoing), 1/du))


def diagrams(ps, mass, charge, incoming_spin, outgoing_spin, eps, eps_out):
    ks = kernels(ps, mass, eps, eps_out)
    u = spinor(ps[0], mass, incoming_spin)
    row = adjoint(spinor(ps[2], mass, outgoing_spin))
    return tuple(-charge**2 * sum((x*y for x, y in zip(row, apply(kernel, u))), ZERO) for kernel in ks)


def amplitudes(ps, mass, charge):
    validate(ps, mass)
    pols, out_pols = transverse(ps[1]), transverse(ps[3])
    records = []
    for s, sout, pol, pout in product((0, 1), repeat=4):
        eps, eps_out = pols[pol], out_pols[pout]
        terms = diagrams(ps, mass, charge, s, sout, eps, eps_out)
        records.append({"electron_spins": (s, sout), "photon_polarizations": (pol, pout),
                        "external_spinors": (spinor(ps[0], mass, s), spinor(ps[2], mass, sout)),
                        "polarization_vectors": (eps, eps_out),
                        "diagram_amplitudes": terms, "amplitude": sum(terms, ZERO),
                        "incoming_ward_diagrams": diagrams(ps, mass, charge, s, sout, ps[1], eps_out),
                        "outgoing_ward_diagrams": diagrams(ps, mass, charge, s, sout, eps, ps[3])})
    return records


def spin_average(records):
    # Average over initial electron spin and initial photon polarization.
    return sum((r["amplitude"].abs2() for r in records), Q(0))/4


def covariant_trace_average(ps, mass, charge):
    """Use both covariant photon sums -g, not a physical polarization basis.

    Valid here for the SUM of diagrams by the Ward identities. The Dirac
    trace also avoids explicit spinors or their rational-square-root domain.
    """
    validate(ps, mass)
    rho_in = add(slash(ps[0]), scale(eye(), mass))
    rho_out = add(slash(ps[2]), scale(eye(), mass))
    result = ZERO
    for mu, nu in product(range(4), repeat=2):
        eps = tuple(Q(int(i == mu)) for i in range(4))
        eps_out = tuple(Q(int(i == nu)) for i in range(4))
        gs, gu = kernels(ps, mass, eps, eps_out)
        g = add(gs, gu)
        gbar = multiply(multiply(GAMMA[0], dagger(g)), GAMMA[0])
        result += SIGNS[mu]*SIGNS[nu]*trace(multiply(multiply(multiply(rho_out, g), rho_in), gbar))
    return result * (charge**4/4)


def invariant_average(ps, mass, charge):
    """Invariant form of the unpolarized tree result underlying Klein-Nishina."""
    validate(ps, mass)
    a, b = dot(ps[0], ps[1]), dot(ps[0], ps[3])
    difference = 1/a-1/b
    return 2*charge**4*(a/b+b/a+2*mass**2*difference+mass**4*difference**2)


class ComptonTests(unittest.TestCase):
    def test_polarizations(self):
        for direction in DIRECTIONS:
            ps = kinematics(direction)
            for k in (ps[1], ps[3]):
                pols = transverse(k)
                for i, j in product((0, 1), repeat=2):
                    self.assertEqual(dot(pols[i], pols[j]), -int(i == j))
                for eps in pols:
                    self.assertEqual(dot(k, eps), 0)

    def test_three_evaluations(self):
        for direction in DIRECTIONS:
            ps = kinematics(direction)
            value = spin_average(amplitudes(ps, Q(1), CHARGE))
            self.assertEqual(covariant_trace_average(ps, Q(1), CHARGE), C.of(value))
            self.assertEqual(invariant_average(ps, Q(1), CHARGE), value)
        self.assertEqual(spin_average(amplitudes(kinematics(), Q(1), CHARGE)), Q(317, 8100))

    def test_ward_cancellation_and_missing_diagram_hostile(self):
        nonzero = {"incoming_ward_diagrams": False, "outgoing_ward_diagrams": False}
        for direction in DIRECTIONS:
            for record in amplitudes(kinematics(direction), Q(1), CHARGE):
                for key in nonzero:
                    s, u = record[key]
                    self.assertEqual(s+u, ZERO)
                    if s != ZERO:
                        nonzero[key] = True
                        # Omitting a diagram, or reversing its relative sign,
                        # really breaks the Ward test rather than passing vacuously.
                        self.assertNotEqual(s-u, ZERO)
        self.assertTrue(all(nonzero.values()))

    def test_gauge_shifts_and_complex_conjugation(self):
        ps = kinematics(DIRECTIONS[2])
        records = amplitudes(ps, Q(1), CHARGE)
        for r in records:
            s, sout = r["electron_spins"]
            eps, eps_out = r["polarization_vectors"]
            shifted = plus(eps, tuple(Q(2, 5)*x for x in ps[1]))
            shifted_out = plus(eps_out, tuple(Q(-3, 7)*x for x in ps[3]))
            self.assertEqual(sum(diagrams(ps, Q(1), CHARGE, s, sout, shifted, shifted_out), ZERO), r["amplitude"])
            incoming_phase = tuple(I*x for x in eps)
            outgoing_phase = tuple(I*x for x in eps_out)
            self.assertEqual(sum(diagrams(ps, Q(1), CHARGE, s, sout, incoming_phase, eps_out), ZERO), I*r["amplitude"])
            self.assertEqual(sum(diagrams(ps, Q(1), CHARGE, s, sout, eps, outgoing_phase), ZERO), -I*r["amplitude"])

    def test_forward_amplitude_sign(self):
        # Exact forward identity, not a soft-energy extrapolation. Fixes the
        # amplitude sign as well as the spin/polarization normalization.
        for r in amplitudes(kinematics(DIRECTIONS[-1]), Q(1), CHARGE):
            s, sout = r["electron_spins"]
            pol, pout = r["photon_polarizations"]
            self.assertEqual(r["amplitude"], C.of(-2*CHARGE**2 if s == sout and pol == pout else 0))

    def test_energy_scaling_and_azimuth(self):
        ps = kinematics()
        value = spin_average(amplitudes(ps, Q(1), CHARGE))
        self.assertEqual(spin_average(amplitudes(kinematics(DIRECTIONS[1]), Q(1), CHARGE)), value)
        scaled = tuple(tuple(4*x for x in p) for p in ps)
        self.assertEqual(spin_average(amplitudes(scaled, Q(4), CHARGE)), value)
        self.assertEqual(spin_average(amplitudes(ps, Q(1), 2*CHARGE)), 16*value)
        for ratio in (Q(8), Q(9, 2)):
            ps = kinematics(DIRECTIONS[2], ratio)
            value = spin_average(amplitudes(ps, Q(1), CHARGE))
            self.assertEqual(covariant_trace_average(ps, Q(1), CHARGE), C.of(value))
            self.assertEqual(invariant_average(ps, Q(1), CHARGE), value)

    def test_invalid_inputs(self):
        ps = kinematics()
        with self.assertRaisesRegex(ValueError, "on-shell"):
            amplitudes(ps, Q(2), CHARGE)
        with self.assertRaisesRegex(ValueError, "conservation"):
            amplitudes((ps[0], ps[1], ps[2], ps[1]), Q(1), CHARGE)
        with self.assertRaisesRegex(ValueError, "Positive-energy"):
            amplitudes((ps[0], (Q(0),)*4, ps[2], ps[3]), Q(1), CHARGE)
        with self.assertRaisesRegex(ValueError, "null photon"):
            transverse(ps[0])


def encode(value):
    if isinstance(value, Q):
        return str(value)
    if is_dataclass(value):
        return asdict(value)
    raise TypeError(type(value).__name__)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(ComptonTests))
    if not result.wasSuccessful():
        raise SystemExit(1)
    samples = []
    for direction in DIRECTIONS:
        ps = kinematics(direction)
        records = amplitudes(ps, Q(1), CHARGE)
        qs, qu = plus(ps[0], ps[1]), minus(ps[0], ps[3])
        samples.append({"momenta_p_k_pout_kout": ps,
                        "internal_momenta": {"s": qs, "u": qu},
                        "denominators": {"s": dot(qs, qs)-1, "u": dot(qu, qu)-1},
                        "amplitudes": records,
                        "averaged_squared_amplitude": spin_average(records),
                        "covariant_trace_result": covariant_trace_average(ps, Q(1), CHARGE),
                        "invariant_result": invariant_average(ps, Q(1), CHARGE)})
    report = {"status": "exact-computational-benchmark-passed", "process": "tree e- gamma -> e- gamma",
              "mass": Q(1), "charge_magnitude": CHARGE,
              "parameters": "rational benchmark units, not fitted physical constants",
              "conventions": "metric +---; physical incoming/outgoing; delta-stripped i M; M=-e^2 times s+u spinor kernels",
              "bases": "canonical electron spin, two real transverse photon polarizations",
              "formal_agda_bridge": "not implemented", "novel_physical_prediction": False,
              "samples": samples, "tests_run": result.testsRun,
              "scope": "finite exact points, not a general Ward theorem or a differential cross section"}
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, default=encode, indent=2)+"\n", encoding="utf-8")
    print(f"Compton: both diagrams, 16 spin/polarization amplitudes per point; first average |M|^2 = {samples[0]['averaged_squared_amplitude']}")


if __name__ == "__main__":
    main()
