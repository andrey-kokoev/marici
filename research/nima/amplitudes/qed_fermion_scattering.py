"""Exact tree e- mu- -> e- mu- benchmarks with arbitrary declared masses.

Distinct Dirac flavours, metric +---, vertex -i e gamma^mu, photon
propagator -i[g_mu_nu-(1-xi)q_mu q_nu/t]/t. Delta-stripped contribution i M.
Canonical spin basis (not helicity). Rational complex arithmetic, no loops.
"""
from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass, is_dataclass
from fractions import Fraction as Q
from itertools import product
import json
from math import isqrt
from pathlib import Path
import unittest


@dataclass(frozen=True)
class C:
    real: Q = Q(0)
    imag: Q = Q(0)

    @staticmethod
    def of(x):
        return x if isinstance(x, C) else C(Q(x))

    def __add__(self, x):
        x = C.of(x)
        return C(self.real + x.real, self.imag + x.imag)

    __radd__ = __add__

    def __neg__(self):
        return C(-self.real, -self.imag)

    def __sub__(self, x):
        return self + -C.of(x)

    def __rsub__(self, x):
        return C.of(x) + -self

    def __mul__(self, x):
        x = C.of(x)
        return C(self.real*x.real - self.imag*x.imag,
                 self.real*x.imag + self.imag*x.real)

    __rmul__ = __mul__

    def __truediv__(self, x):
        x = C.of(x)
        norm = x.abs2()
        if norm == 0:
            raise ZeroDivisionError("Exact complex division by zero")
        y = self * x.conjugate()
        return C(y.real/norm, y.imag/norm)

    def conjugate(self):
        return C(self.real, -self.imag)

    def abs2(self):
        return self.real**2 + self.imag**2


ZERO = C()
I = C(Q(0), Q(1))
SIGNS = (1, -1, -1, -1)


def matrix(rows):
    return tuple(tuple(C.of(x) for x in row) for row in rows)


def eye(n=4):
    return matrix([[int(i == j) for j in range(n)] for i in range(n)])


def add(a, b):
    return tuple(tuple(x+y for x, y in zip(ar, br)) for ar, br in zip(a, b))


def scale(a, scalar):
    return tuple(tuple(x*scalar for x in row) for row in a)


def multiply(a, b):
    return tuple(tuple(sum((a[i][k]*b[k][j] for k in range(len(b))), ZERO)
                       for j in range(len(b[0]))) for i in range(len(a)))


def apply(a, v):
    return tuple(sum((x*y for x, y in zip(row, v)), ZERO) for row in a)


def dagger(a):
    return tuple(tuple(a[j][i].conjugate() for j in range(len(a))) for i in range(len(a[0])))


def trace(a):
    return sum((a[i][i] for i in range(len(a))), ZERO)


def outer(v, row):
    return tuple(tuple(x*y for y in row) for x in v)


PAULI = (matrix(((0, 1), (1, 0))), matrix(((0, -I), (I, 0))), matrix(((1, 0), (0, -1))))
GAMMA = (matrix(((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, -1, 0), (0, 0, 0, -1))),) + tuple(
    matrix([[s[i][j-2] if i < 2 <= j else -s[i-2][j] if j < 2 <= i else 0
             for j in range(4)] for i in range(4)]) for s in PAULI)


def dot(p, q):
    return sum((sign*x*y for sign, x, y in zip(SIGNS, p, q)), Q(0))


def plus(p, q):
    return tuple(x+y for x, y in zip(p, q))


def minus(p, q):
    return tuple(x-y for x, y in zip(p, q))


def slash(p):
    result = scale(eye(), 0)
    for mu in range(4):
        result = add(result, scale(GAMMA[mu], SIGNS[mu]*p[mu]))
    return result


def rational_sqrt(x):
    x = Q(x)
    if x <= 0:
        raise ValueError("Spinor normalization requires E+m > 0")
    a, b = isqrt(x.numerator), isqrt(x.denominator)
    if a*a != x.numerator or b*b != x.denominator:
        raise ValueError("E+m needs an algebraic square root outside this rational backend")
    return Q(a, b)


def spinor(p, mass, spin):
    if len(p) != 4 or mass < 0 or p[0] <= 0 or dot(p, p) != mass**2:
        raise ValueError("Positive-energy on-shell four-momentum required")
    if spin not in (0, 1):
        raise ValueError("Spin label must be 0 or 1")
    r = rational_sqrt(p[0]+mass)
    chi = tuple(C.of(int(i == spin)) for i in range(2))
    sigma_p = scale(eye(2), 0)
    for axis in range(3):
        sigma_p = add(sigma_p, scale(PAULI[axis], p[axis+1]))
    return tuple(x*r for x in chi) + tuple(x/r for x in apply(sigma_p, chi))


def adjoint(u):
    return tuple(x.conjugate()*s for x, s in zip(u, (1, 1, -1, -1)))


def current(outgoing, incoming):
    row = adjoint(outgoing)
    return tuple(sum((x*y for x, y in zip(row, apply(g, incoming))), ZERO) for g in GAMMA)


def amplitude_currents(j, k, q, charge, xi=Q(1)):
    t = dot(q, q)
    if t == 0:
        raise ValueError("Photon propagator pole t=0")
    return charge**2 / t * (dot(j, k) - (1-xi)*dot(j, q)*dot(k, q)/t)


def validate(ps, masses):
    if len(ps) != 4 or len(masses) != 2:
        raise ValueError("Four momenta and two flavour masses required")
    for p, mass in zip(ps, (masses[0], masses[1], masses[0], masses[1])):
        if len(p) != 4 or mass < 0 or p[0] <= 0 or dot(p, p) != mass**2:
            raise ValueError("Positive-energy on-shell four-momenta required")
    if plus(ps[0], ps[1]) != plus(ps[2], ps[3]):
        raise ValueError("Incoming and outgoing momenta do not conserve energy-momentum")
    if dot(minus(ps[0], ps[2]), minus(ps[0], ps[2])) == 0:
        raise ValueError("Photon propagator pole t=0")


def amplitudes(ps, masses, charge, xi=Q(1)):
    validate(ps, masses)
    us = tuple(tuple(spinor(p, m, s) for s in (0, 1))
               for p, m in zip(ps, (masses[0], masses[1], masses[0], masses[1])))
    q = minus(ps[0], ps[2])
    records = []
    for s1, s2, s3, s4 in product((0, 1), repeat=4):
        j = current(us[2][s3], us[0][s1])
        k = current(us[3][s4], us[1][s2])
        records.append({"spins": (s1, s2, s3, s4),
                        "external_spinors": (us[0][s1], us[1][s2], us[2][s3], us[3][s4]),
                        "electron_current": j, "muon_current": k,
                        "ward_contractions": (dot(j, q), dot(k, q)),
                        "amplitude": amplitude_currents(j, k, q, charge, xi)})
    return records


def spin_average(records):
    return sum((r["amplitude"].abs2() for r in records), Q(0))/4


def trace_average(ps, masses, charge):
    """Spin sum using Dirac traces; no explicit spinor basis or square roots."""
    validate(ps, masses)
    return trace_expression(ps, masses, charge)


def trace_expression(ps, masses, charge):
    """Algebraic trace expression for analytic crossing, NOT a physical API.

    Does not enforce positive external energies or mass-shell constraints.
    Use trace_average for physical elastic-scattering inputs.
    """
    rho = tuple(add(slash(p), scale(eye(), m)) for p, m in zip(ps, (masses[0], masses[1])*2))
    answer = ZERO
    for mu, nu in product(range(4), repeat=2):
        lepton = trace(multiply(multiply(multiply(rho[2], GAMMA[mu]), rho[0]), GAMMA[nu]))
        muon = trace(multiply(multiply(multiply(rho[3], GAMMA[mu]), rho[1]), GAMMA[nu]))
        answer += SIGNS[mu]*SIGNS[nu]*lepton*muon
    t = dot(minus(ps[0], ps[2]), minus(ps[0], ps[2]))
    return answer * (charge**4/(4*t**2))


def invariant_average(ps, masses, charge):
    validate(ps, masses)
    return invariant_expression(ps, masses, charge)


def invariant_expression(ps, masses, charge):
    """Algebraic invariant expression; physical validation is in the wrapper."""
    s = dot(plus(ps[0], ps[1]), plus(ps[0], ps[1]))
    t = dot(minus(ps[0], ps[2]), minus(ps[0], ps[2]))
    u = dot(minus(ps[0], ps[3]), minus(ps[0], ps[3]))
    msum = sum((m*m for m in masses), Q(0))
    return 2*charge**4/t**2*((s-msum)**2+(u-msum)**2+2*t*msum)


MASSES = (Q(7, 32), Q(143, 32))
CHARGE = Q(1, 3)
DIRECTIONS = ((Q(1), Q(0), Q(0)), (Q(3, 5), Q(4, 5), Q(0)),
              (Q(2, 3), Q(1, 3), Q(2, 3)), (Q(0), Q(0), Q(-1)))


def kinematics(direction=DIRECTIONS[0]):
    if sum((x*x for x in direction), Q(0)) != 1:
        raise ValueError("Unit outgoing direction required")
    p, ee, em = Q(3, 4), Q(25, 32), Q(145, 32)
    return ((ee, Q(0), Q(0), p), (em, Q(0), Q(0), -p),
            (ee,) + tuple(p*x for x in direction), (em,) + tuple(-p*x for x in direction))


class QEDTests(unittest.TestCase):
    def test_clifford_and_adjoint(self):
        for mu, nu in product(range(4), repeat=2):
            self.assertEqual(add(multiply(GAMMA[mu], GAMMA[nu]), multiply(GAMMA[nu], GAMMA[mu])),
                             scale(eye(), 2*SIGNS[mu] if mu == nu else 0))
        for mu in range(4):
            self.assertEqual(dagger(GAMMA[mu]), multiply(multiply(GAMMA[0], GAMMA[mu]), GAMMA[0]))

    def test_spinor_equations_and_completeness(self):
        for direction in DIRECTIONS:
            for p, m in zip(kinematics(direction), MASSES*2):
                us = tuple(spinor(p, m, s) for s in (0, 1))
                for a, b in product((0, 1), repeat=2):
                    self.assertEqual(sum((x*y for x, y in zip(adjoint(us[a]), us[b])), ZERO),
                                     C.of(2*m if a == b else 0))
                for u in us:
                    self.assertEqual(apply(add(slash(p), scale(eye(), -m)), u), (ZERO,)*4)
                    self.assertEqual(sum((x.abs2() for x in u), Q(0)), 2*p[0])
                self.assertEqual(add(outer(us[0], adjoint(us[0])), outer(us[1], adjoint(us[1]))),
                                 add(slash(p), scale(eye(), m)))

    def test_fixed_spin_amplitude_sign(self):
        # For four spin-up labels at the first point, J.K=153/16,
        # t=-9/8 and e^2=1/9. Unlike |M|^2 this detects an overall sign error
        # relative to the declared vertex, propagator and spinor conventions.
        first = amplitudes(kinematics(), MASSES, CHARGE)[0]
        self.assertEqual(first["spins"], (0, 0, 0, 0))
        self.assertEqual(dot(first["electron_current"], first["muon_current"]), C.of(Q(153, 16)))
        self.assertEqual(first["amplitude"], C.of(Q(-17, 18)))

    def test_three_independent_spin_sums(self):
        for direction in DIRECTIONS:
            ps = kinematics(direction)
            value = spin_average(amplitudes(ps, MASSES, CHARGE))
            self.assertEqual(trace_average(ps, MASSES, CHARGE), C.of(value))
            self.assertEqual(invariant_average(ps, MASSES, CHARGE), value)
            self.assertGreater(value, 0)

    def test_ward_and_gauge_parameter(self):
        for direction in DIRECTIONS:
            ps = kinematics(direction)
            baseline = amplitudes(ps, MASSES, CHARGE)
            for r in baseline:
                self.assertEqual(r["ward_contractions"], (ZERO, ZERO))
            for xi in (Q(0), Q(-2), Q(7, 3)):
                self.assertEqual([r["amplitude"] for r in amplitudes(ps, MASSES, CHARGE, xi)],
                                 [r["amplitude"] for r in baseline])

    def test_gauge_hostile_and_complex_amplitudes(self):
        ps = kinematics(DIRECTIONS[1])
        records = amplitudes(ps, MASSES, CHARGE)
        self.assertTrue(any(r["amplitude"].imag != 0 for r in records))
        q = minus(ps[0], ps[2])
        r = records[0]
        j = plus(r["electron_current"], q)
        k = plus(r["muon_current"], q)
        self.assertNotEqual(dot(j, q), ZERO)
        self.assertNotEqual(amplitude_currents(j, k, q, CHARGE, Q(0)),
                            amplitude_currents(j, k, q, CHARGE, Q(1)))

    def test_scaling_and_azimuth(self):
        ps = kinematics()
        baseline = spin_average(amplitudes(ps, MASSES, CHARGE))
        # A square scale retains rational sqrt(E+m) for these test spinors.
        scale_factor = Q(4)
        scaled = tuple(tuple(scale_factor*x for x in p) for p in ps)
        scaled_masses = tuple(scale_factor*m for m in MASSES)
        self.assertEqual(spin_average(amplitudes(scaled, scaled_masses, CHARGE)), baseline)
        self.assertEqual(spin_average(amplitudes(ps, MASSES, 2*CHARGE)), 16*baseline)
        self.assertEqual(spin_average(amplitudes(kinematics(DIRECTIONS[1]), MASSES, CHARGE)), baseline)

    def test_invalid_inputs(self):
        with self.assertRaisesRegex(ValueError, "pole"):
            amplitudes(kinematics((Q(0), Q(0), Q(1))), MASSES, CHARGE)
        with self.assertRaisesRegex(ValueError, "on-shell"):
            amplitudes(kinematics(), (Q(1), Q(1)), CHARGE)
        with self.assertRaisesRegex(ValueError, "algebraic square root"):
            rational_sqrt(Q(2))
        ps = kinematics()
        with self.assertRaisesRegex(ValueError, "conserve"):
            amplitudes((ps[0], ps[1], ps[0], ps[3]), MASSES, CHARGE)


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
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(QEDTests))
    if not result.wasSuccessful():
        raise SystemExit(1)
    samples = []
    for direction in DIRECTIONS:
        ps = kinematics(direction)
        records = amplitudes(ps, MASSES, CHARGE)
        samples.append({"momenta": ps, "momentum_transfer": minus(ps[0], ps[2]),
                        "spin_amplitudes": records, "averaged_squared_amplitude": spin_average(records),
                        "trace_result": trace_average(ps, MASSES, CHARGE),
                        "invariant_result": invariant_average(ps, MASSES, CHARGE)})
    report = {"status": "exact-computational-benchmark-passed",
              "process": "distinct-flavour negative-charge Dirac fermion elastic scattering, tree level",
              "masses": MASSES, "charge_magnitude": CHARGE,
              "physical_parameters": "rational benchmark parameters, not measured electron/muon masses or charge",
              "spin_basis": "canonical rest-frame z spin boosted to external momentum; not helicity",
              "conventions": "metric +---; incoming p1,p2; outgoing p3,p4; vertex -i e gamma; delta-stripped i M",
              "gauge_parameters_checked": (Q(1), Q(0), Q(-2), Q(7, 3)),
              "formal_agda_bridge": "not implemented", "novel_physical_prediction": False,
              "samples": samples, "tests_run": result.testsRun}
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, default=encode, indent=2)+"\n", encoding="utf-8")
    print(f"16 spin amplitudes per point; 4 angles; average |M|^2 at first point = {samples[0]['averaged_squared_amplitude']}")


if __name__ == "__main__":
    main()
