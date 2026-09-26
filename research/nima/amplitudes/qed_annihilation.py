"""Exact e- e+ -> mu- mu+ tree benchmarks and spin-summed analytic crossing.

Physical positive-energy incoming p1,p2 and outgoing p3,p4; metric +---.
M=e^2/s [vbar(p2) gamma^mu u(p1)] [ubar(p3) gamma_mu v(p4)].
Fixed Pauli-spinor phases are declared explicitly; full amplitude-level
crossing phases and physical fitted parameters are NOT implemented.
"""
from __future__ import annotations

import argparse
from dataclasses import asdict, is_dataclass
from fractions import Fraction as Q
from itertools import product
import json
from pathlib import Path
import unittest

import qed_fermion_scattering as Elastic
from qed_fermion_scattering import (
    C, ZERO, I, GAMMA, SIGNS, eye, add, scale, multiply, apply, outer, trace,
    dot, plus, minus, slash, spinor, adjoint, current, amplitude_currents,
)

MASSES = (Q(19, 36), Q(1))
CHARGE = Q(1, 3)
DIRECTIONS = ((Q(1), Q(0), Q(0)), (Q(3, 5), Q(4, 5), Q(0)),
              (Q(2, 3), Q(1, 3), Q(2, 3)), (Q(0), Q(0), Q(-1)),
              (Q(0), Q(0), Q(1)))


def vspinor(p, mass, spin):
    # eta_s is the SAME fixed Pauli basis used for u; no implicit flip or
    # charge-conjugation phase. v=(sigma.p eta/r, r eta), r=sqrt(E+m).
    u = spinor(p, mass, spin)
    return u[2:] + u[:2]


def kinematics(direction=DIRECTIONS[0]):
    if sum((x*x for x in direction), Q(0)) != 1:
        raise ValueError("Unit direction required")
    energy = Q(5, 4)
    pe, pm = (Q(10, 9), Q(2, 9), Q(0)), Q(3, 4)
    return ((energy,) + pe, (energy,) + tuple(-x for x in pe),
            (energy,) + tuple(pm*x for x in direction),
            (energy,) + tuple(-pm*x for x in direction))


def massless_kinematics(direction):
    return ((Q(1), Q(0), Q(0), Q(1)), (Q(1), Q(0), Q(0), Q(-1)),
            (Q(1),) + direction, (Q(1),) + tuple(-x for x in direction))


def validate(ps, masses):
    if len(ps) != 4 or len(masses) != 2:
        raise ValueError("Four momenta and two flavour masses required")
    for p, mass in zip(ps, (masses[0], masses[0], masses[1], masses[1])):
        if len(p) != 4 or mass < 0 or p[0] <= 0 or dot(p, p) != mass**2:
            raise ValueError("Positive-energy on-shell momenta required")
    if plus(ps[0], ps[1]) != plus(ps[2], ps[3]):
        raise ValueError("Energy-momentum conservation failed")
    q = plus(ps[0], ps[1])
    if dot(q, q) == 0:
        raise ValueError("Photon propagator pole s=0")


def amplitudes(ps, masses, charge, xi=Q(1)):
    validate(ps, masses)
    fs = (spinor, vspinor, spinor, vspinor)
    ms = (masses[0], masses[0], masses[1], masses[1])
    us = tuple(tuple(f(p, m, s) for s in (0, 1)) for f, p, m in zip(fs, ps, ms))
    q = plus(ps[0], ps[1])
    records = []
    for spins in product((0, 1), repeat=4):
        selected = tuple(u[s] for u, s in zip(us, spins))
        j = current(selected[1], selected[0])
        k = current(selected[2], selected[3])
        records.append({"spins_e_minus_e_plus_mu_minus_mu_plus": spins,
                        "external_spinors_u_v_u_v": selected,
                        "incoming_current": j, "outgoing_current": k,
                        "ward_contractions": (dot(j, q), dot(k, q)),
                        "amplitude": amplitude_currents(j, k, q, charge, xi)})
    return records


def spin_average(records):
    return sum((r["amplitude"].abs2() for r in records), Q(0))/4


def trace_average(ps, masses, charge):
    validate(ps, masses)
    me, mm = masses
    rho = tuple(add(slash(p), scale(eye(), m)) for p, m in zip(ps, (me, -me, mm, -mm)))
    result = ZERO
    for mu, nu in product(range(4), repeat=2):
        left = trace(multiply(multiply(multiply(rho[1], GAMMA[mu]), rho[0]), GAMMA[nu]))
        right = trace(multiply(multiply(multiply(rho[2], GAMMA[mu]), rho[3]), GAMMA[nu]))
        result += SIGNS[mu]*SIGNS[nu]*left*right
    q = plus(ps[0], ps[1])
    return result * (charge**4/(4*dot(q, q)**2))


def invariants(ps):
    return tuple(dot(q, q) for q in (plus(ps[0], ps[1]), minus(ps[0], ps[2]), minus(ps[0], ps[3])))


def invariant_average(ps, masses, charge):
    validate(ps, masses)
    s, t, u = invariants(ps)
    msum = sum((m*m for m in masses), Q(0))
    return 2*charge**4/s**2*((t-msum)**2+(u-msum)**2+2*s*msum)


def crossed_elastic_momenta(ps):
    # Analytic substitution, not four physical positive-energy particles:
    # elastic (p1,p2,p3,p4) = annihilation (a1,-a4,-a2,a3).
    return (ps[0], tuple(-x for x in ps[3]), tuple(-x for x in ps[1]), ps[2])


class AnnihilationTests(unittest.TestCase):
    def test_antiparticle_dirac_norm_and_completeness(self):
        for ps, masses in ((kinematics(DIRECTIONS[2]), MASSES),
                           (massless_kinematics(DIRECTIONS[2]), (Q(0), Q(0)))):
            for p, m in ((ps[1], masses[0]), (ps[3], masses[1])):
                vs = tuple(vspinor(p, m, s) for s in (0, 1))
                for a, b in product((0, 1), repeat=2):
                    self.assertEqual(sum((x*y for x, y in zip(adjoint(vs[a]), vs[b])), ZERO),
                                     C.of(-2*m if a == b else 0))
                    self.assertEqual(sum((x.conjugate()*y for x, y in zip(vs[a], vs[b])), ZERO),
                                     C.of(2*p[0] if a == b else 0))
                for v in vs:
                    self.assertEqual(apply(add(slash(p), scale(eye(), m)), v), (ZERO,)*4)
                self.assertEqual(add(outer(vs[0], adjoint(vs[0])), outer(vs[1], adjoint(vs[1]))),
                                 add(slash(p), scale(eye(), -m)))

    def test_three_evaluations_and_mandelstam(self):
        for direction in DIRECTIONS:
            ps = kinematics(direction)
            value = spin_average(amplitudes(ps, MASSES, CHARGE))
            self.assertEqual(trace_average(ps, MASSES, CHARGE), C.of(value))
            self.assertEqual(invariant_average(ps, MASSES, CHARGE), value)
            self.assertEqual(sum(invariants(ps)), 2*sum(m*m for m in MASSES))
            self.assertGreater(value, 0)

    def test_ward_and_gauge(self):
        for direction in DIRECTIONS:
            ps = kinematics(direction)
            records = amplitudes(ps, MASSES, CHARGE)
            for r in records:
                self.assertEqual(r["ward_contractions"], (ZERO, ZERO))
            for xi in (Q(0), Q(-2), Q(7, 3)):
                self.assertEqual([r["amplitude"] for r in amplitudes(ps, MASSES, CHARGE, xi)],
                                 [r["amplitude"] for r in records])
        self.assertTrue(any(r["amplitude"].imag != 0 for r in amplitudes(kinematics(DIRECTIONS[2]), MASSES, CHARGE)))

    def test_crossing_of_spin_summed_expressions(self):
        for ps, masses in [(kinematics(d), MASSES) for d in DIRECTIONS] + [
                (massless_kinematics(d), (Q(0), Q(0))) for d in DIRECTIONS]:
            crossed = crossed_elastic_momenta(ps)
            s, t, u = invariants(ps)
            self.assertEqual(invariants(crossed), (u, s, t))
            self.assertEqual(plus(crossed[0], crossed[1]), plus(crossed[2], crossed[3]))
            # Both crossed spin densities acquire a minus sign. These cancel
            # in the product of traces; they must not be silently discarded.
            for anti_p, crossed_p, m in ((ps[1], crossed[2], masses[0]),
                                         (ps[3], crossed[1], masses[1])):
                self.assertEqual(add(slash(crossed_p), scale(eye(), m)),
                                 scale(add(slash(anti_p), scale(eye(), -m)), -1))
            expected = invariant_average(ps, masses, CHARGE)
            self.assertEqual(Elastic.trace_expression(crossed, masses, CHARGE), C.of(expected))
            self.assertEqual(Elastic.invariant_expression(crossed, masses, CHARGE), expected)
            with self.assertRaisesRegex(ValueError, "Positive-energy"):
                Elastic.trace_average(crossed, masses, CHARGE)

    def test_massless_angular_law_and_phase_convention(self):
        for direction in DIRECTIONS:
            ps = massless_kinematics(direction)
            records = amplitudes(ps, (Q(0), Q(0)), CHARGE)
            expected = CHARGE**4*(1+direction[2]**2)
            self.assertEqual(spin_average(records), expected)
            self.assertEqual(trace_average(ps, (Q(0), Q(0)), CHARGE), C.of(expected))
        selected = next(r for r in amplitudes(massless_kinematics(DIRECTIONS[0]), (Q(0), Q(0)), CHARGE)
                        if r["spins_e_minus_e_plus_mu_minus_mu_plus"] == (0, 1, 0, 1))
        self.assertEqual(selected["amplitude"], C.of(-CHARGE**2))

    def test_antiparticle_rephasing_and_scaling(self):
        ps = kinematics(DIRECTIONS[2])
        r = amplitudes(ps, MASSES, CHARGE)[0]
        u1, v2, u3, v4 = r["external_spinors_u_v_u_v"]
        q = plus(ps[0], ps[1])
        # Incoming v occurs barred, outgoing v unbarred: opposite phases.
        for v_in, v_out, factor in ((tuple(I*x for x in v2), v4, -I),
                                   (v2, tuple(I*x for x in v4), I)):
            value = amplitude_currents(current(v_in, u1), current(u3, v_out), q, CHARGE)
            self.assertEqual(value, factor*r["amplitude"])
        self.assertNotEqual(r["amplitude"], ZERO)
        base = spin_average(amplitudes(ps, MASSES, CHARGE))
        scaled_ps = tuple(tuple(4*x for x in p) for p in ps)
        self.assertEqual(spin_average(amplitudes(scaled_ps, tuple(4*m for m in MASSES), CHARGE)), base)
        self.assertEqual(spin_average(amplitudes(ps, MASSES, 2*CHARGE)), 16*base)

    def test_invalid_inputs(self):
        ps = kinematics()
        with self.assertRaisesRegex(ValueError, "on-shell"):
            amplitudes(ps, (Q(1), Q(1)), CHARGE)
        with self.assertRaisesRegex(ValueError, "conservation"):
            amplitudes((ps[0], ps[1], ps[2], ps[2]), MASSES, CHARGE)
        with self.assertRaisesRegex(ValueError, "on-shell"):
            vspinor(tuple(-x for x in ps[1]), MASSES[0], 0)


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
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(AnnihilationTests))
    if not result.wasSuccessful():
        raise SystemExit(1)
    samples = []
    for direction in DIRECTIONS:
        ps = kinematics(direction)
        records = amplitudes(ps, MASSES, CHARGE)
        crossed = crossed_elastic_momenta(ps)
        samples.append({"momenta": ps, "invariants_s_t_u": invariants(ps),
                        "spin_amplitudes": records, "averaged_squared_amplitude": spin_average(records),
                        "trace_result": trace_average(ps, MASSES, CHARGE),
                        "invariant_result": invariant_average(ps, MASSES, CHARGE),
                        "crossed_elastic_algebraic_momenta": crossed,
                        "crossed_trace": Elastic.trace_expression(crossed, MASSES, CHARGE)})
    report = {"status": "exact-computational-benchmark-passed", "process": "tree e- e+ -> mu- mu+",
              "masses": MASSES, "charge_magnitude": CHARGE,
              "parameters": "rational benchmark values, not measured electron/muon constants",
              "spinor_convention": "u=(r chi,sigma.p chi/r); v=(sigma.p chi/r,r chi); fixed Pauli basis",
              "conventions": "metric +---; physical positive-energy incoming/outgoing; delta-stripped i M",
              "crossing_scope": "spin-summed analytic expressions; NOT full amplitude crossing with spinor phases",
              "formal_agda_bridge": "not implemented", "novel_physical_prediction": False,
              "samples": samples, "tests_run": result.testsRun}
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, default=encode, indent=2)+"\n", encoding="utf-8")
    print(f"Annihilation: 16 spin amplitudes per point; first average |M|^2 = {samples[0]['averaged_squared_amplitude']}")


if __name__ == "__main__":
    main()
