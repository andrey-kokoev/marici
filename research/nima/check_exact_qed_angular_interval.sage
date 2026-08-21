"""Arb-ball derivative enclosures for the exact one-loop QED Bell readout."""

import hashlib
import json
from pathlib import Path

from sage.all import ComplexBallField, RealBallField

CBF = ComplexBallField(256)
RBF = RealBallField(256)


class Jet:
    def __init__(self, value, derivative=0, second=0):
        self.v = CBF(value)
        self.d = CBF(derivative)
        self.d2 = CBF(second)

    def lift(self, x):
        return x if isinstance(x, type(self)) else type(self)(x)

    def __add__(self, other):
        other = self.lift(other)
        return Jet(self.v + other.v, self.d + other.d, self.d2 + other.d2)

    __radd__ = __add__

    def __neg__(self):
        return Jet(-self.v, -self.d, -self.d2)

    def __sub__(self, other):
        return self + (-self.lift(other))

    def __rsub__(self, other):
        return self.lift(other) - self

    def __mul__(self, other):
        other = self.lift(other)
        return Jet(
            self.v * other.v,
            self.d * other.v + self.v * other.d,
            self.d2 * other.v + 2 * self.d * other.d + self.v * other.d2,
        )

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self.lift(other)
        inverse = Jet(
            1 / other.v,
            -other.d / other.v**2,
            2 * other.d**2 / other.v**3 - other.d2 / other.v**2,
        )
        return self * inverse

    def __rtruediv__(self, other):
        return self.lift(other) / self

    def __pow__(self, n):
        n = int(n)
        if n == 0:
            return Jet(1)
        if n < 0:
            return Jet(1) / (self ** (-n))
        return Jet(
            self.v**n,
            n * self.v ** (n - 1) * self.d,
            n * (n - 1) * self.v ** (n - 2) * self.d**2 + n * self.v ** (n - 1) * self.d2,
        )

    def sqrt(self):
        root = self.v.sqrt()
        return Jet(root, self.d / (2 * root), self.d2 / (2 * root) - self.d**2 / (4 * root**3))

    def log(self):
        return Jet(self.v.log(), self.d / self.v, self.d2 / self.v - self.d**2 / self.v**2)

    def dilog(self):
        first = -(1 - self.v).log() / self.v
        second = (self.v / (1 - self.v) + (1 - self.v).log()) / self.v**2
        return Jet(self.v.polylog(2), first * self.d, second * self.d**2 + first * self.d2)

    def conjugate(self):
        return Jet(self.v.conjugate(), self.d.conjugate(), self.d2.conjugate())

    def real(self):
        return Jet(self.v.real(), self.d.real(), self.d2.real())


class TaylorJet:
    """Truncated ordinary-power-series coefficients through fixed ORDER."""

    ORDER = 8

    def __init__(self, value, derivative=0, second=0, coefficients=None):
        if coefficients is None:
            self.c = [CBF(0) for _ in range(self.ORDER + 1)]
            self.c[0] = CBF(value)
            self.c[1] = CBF(derivative)
            self.c[2] = CBF(second) / 2
        else:
            self.c = [CBF(q) for q in coefficients]

    @property
    def v(self):
        return self.c[0]

    @property
    def d(self):
        return self.c[1]

    @property
    def d2(self):
        return 2 * self.c[2]

    def lift(self, x):
        return x if isinstance(x, TaylorJet) else TaylorJet(x)

    def __add__(self, other):
        other = self.lift(other)
        return TaylorJet(0, coefficients=[a + b for a, b in zip(self.c, other.c)])

    __radd__ = __add__

    def __neg__(self):
        return TaylorJet(0, coefficients=[-a for a in self.c])

    def __sub__(self, other):
        return self + (-self.lift(other))

    def __rsub__(self, other):
        return self.lift(other) - self

    def __mul__(self, other):
        other = self.lift(other)
        out = []
        for n in range(self.ORDER + 1):
            out.append(sum(self.c[k] * other.c[n - k] for k in range(n + 1)))
        return TaylorJet(0, coefficients=out)

    __rmul__ = __mul__

    def inverse(self):
        out = [1 / self.c[0]]
        for n in range(1, self.ORDER + 1):
            out.append(-sum(self.c[k] * out[n - k] for k in range(1, n + 1)) / self.c[0])
        return TaylorJet(0, coefficients=out)

    def __truediv__(self, other):
        return self * self.lift(other).inverse()

    def __rtruediv__(self, other):
        return self.lift(other) / self

    def __pow__(self, n):
        n = int(n)
        if n < 0:
            return (self.inverse()) ** (-n)
        result, base = TaylorJet(1), self
        while n:
            if n & 1:
                result = result * base
            base = base * base
            n //= 2
        return result

    def sqrt(self):
        out = [self.c[0].sqrt()]
        for n in range(1, self.ORDER + 1):
            middle = sum(out[k] * out[n - k] for k in range(1, n))
            out.append((self.c[n] - middle) / (2 * out[0]))
        return TaylorJet(0, coefficients=out)

    def derivative_series(self):
        return TaylorJet(0, coefficients=[(n + 1) * self.c[n + 1] for n in range(self.ORDER)] + [0])

    def integrate_from(self, constant):
        out = [CBF(constant)]
        out.extend(self.c[n - 1] / n for n in range(1, self.ORDER + 1))
        return TaylorJet(0, coefficients=out)

    def log(self):
        quotient = self.derivative_series() / self
        return quotient.integrate_from(self.c[0].log())

    def dilog(self):
        derivative = -((1 - self).log() / self) * self.derivative_series()
        return derivative.integrate_from(self.c[0].polylog(2))

    def conjugate(self):
        return TaylorJet(0, coefficients=[q.conjugate() for q in self.c])

    def real(self):
        return TaylorJet(0, coefficients=[q.real() for q in self.c])


def g1(a, z):
    return z.log() if a == 0 else (1 - z / a).log()


def g2(a, b, z, region):
    if a == 0:
        return -(z / b).dilog()
    if b == 0:
        if region == 2:
            return z.log() * (1 - z / a).log() + (z / a).dilog()
        v = 1 - z / a
        return z.lift(CBF(a).log()) * v.log() - v.dilog() + z.lift(CBF(1).polylog(2))
    if a == b:
        return (1 - z / a).log() ** 2 / 2
    return (
        z.lift(CBF((b - a) / b).log()) * ((z - a).log() - z.lift(CBF(-a).log()))
        - ((z - a) / (b - a)).dilog()
        + z.lift(CBF(-a / (b - a)).polylog(2))
    )


def solve_wz(xi, xj, region):
    linear = -xi * (2 - xj) - 4 * xj
    discriminant = linear**2 - 4 * xi**2
    sqrt_discriminant = discriminant.sqrt()
    p_plus = 2 * xi / (-linear - sqrt_discriminant)
    p_minus = (-linear - sqrt_discriminant) / (2 * xi)
    p = p_plus if region in (1, 2) else p_minus
    sigma = ((4 - xj) * p).sqrt()
    delta = -(-xj * p).sqrt()
    return (sigma + delta) / 2, (sigma - delta) / 2


def masters(xi, xj, xk, region):
    w, z = solve_wz(xi, xj, region)
    f2 = -g1(-1, w) + g1(-1, z) + g1(1, w) - g1(1, z)
    f4 = (g1(1, w) - g1(-1, w)) * (g1(-1, z) - g1(1, z))
    for i in (0, 1):
        for j in (0, 1):
            ai, aj = (-1) ** i, (-1) ** j
            f4 += (-1) ** (i + j) * (g2(ai, aj, w, region) + g2(ai, aj, z, region))
    f6 = (
        g1(0, w) * (g1(1, z) - g1(-1, z))
        + g1(0, z) * (g1(-1, w) - g1(1, w))
        + g2(1, 0, w, region) - g2(-1, 0, w, region)
        + g2(0, -1, w, region) - g2(0, 1, w, region)
        - g2(1, 0, z, region) + g2(-1, 0, z, region)
        - g2(0, -1, z, region) + g2(0, 1, z, region)
    )
    if region in (1, 3):
        f6 = -f6
    return f2, f4, f6


def amplitudes_jet(y_value, x_ball, jet_class=Jet):
    y, x = jet_class(y_value), jet_class(CBF(x_ball), 1)
    xs, xt, xu = y, -y * x, -y * (1 - x)
    triples = ((xs, xt, xu), (xt, xu, xs), (xu, xs, xt))
    data = [masters(*triple, region) for region, triple in enumerate(triples, 1)]

    def root2(q):
        return (q * (q - 4)).sqrt()

    def root3(qi, qj, qk):
        return (qi * qj * (qi * qj + 4 * qk)).sqrt()

    sum_f4 = sum(d[1] for d in data)
    sum_f6 = sum(d[2] / root3(*triple) for d, triple in zip(data, triples))
    m_pppp = 1 - 4 * sum_f6

    def r8(qi, qj, qk):
        return 2 * (qi * qj + 2 * qk) / qk

    m_mppp = 1 + 2 * (1 / xs + 1 / xt + 1 / xu) * sum_f4
    m_mppp -= sum(r8(*triple) * d[2] / root3(*triple) for d, triple in zip(data, triples))
    f2_stu, _, f6_stu = data[0]
    f2_tus, f4_tus, f6_tus = data[1]
    f2_ust, f4_ust, f6_ust = data[2]

    def r9(qi, qj, qk):
        return (qi - 4) * (qi - qj) / qk

    def r10(qi, qj, qk):
        return 1 - 4 / qi - 2 * qj * qk / qi**2

    def r11(qi, qj, qk):
        return 4 - 2 * qi - qj * qk + 2 * qj * qk * (qj * qk + 4 * qi) / qi**2

    m_mmpp = -1
    m_mmpp += r9(xt, xu, xs) * f2_tus / root2(xt)
    m_mmpp += r9(xu, xt, xs) * f2_ust / root2(xu)
    m_mmpp -= r10(xs, xt, xu) * (f4_tus + f4_ust)
    m_mmpp += 2 * (xs - 2) * f6_stu / root3(xs, xt, xu)
    m_mmpp += 2 * (xs - 2) * f6_ust / root3(xu, xs, xt)
    m_mmpp -= r11(xs, xt, xu) * f6_tus / root3(xt, xu, xs)

    return m_mmpp, m_pppp, m_mppp


def bell_jet(y_value, x_ball, centered=True):
    amplitudes = amplitudes_jet(y_value, x_ball)
    if centered and x_ball.rad() != 0:
        center = RBF(x_ball.center())
        delta = CBF(x_ball - center)
        center_amplitudes = amplitudes_jet(y_value, center)
        amplitudes = tuple(
            Jet(
                center_amp.v + interval_amp.d * delta,
                center_amp.d + interval_amp.d2 * delta,
                interval_amp.d2,
            )
            for center_amp, interval_amp in zip(center_amplitudes, amplitudes)
        )
    m_mmpp, m_pppp, m_mppp = amplitudes
    numerator = 4 * RBF(2).sqrt() * (m_mmpp * m_pppp.conjugate()).real()
    denominator = (
        m_mmpp * m_mmpp.conjugate()
        + m_pppp * m_pppp.conjugate()
        + 2 * m_mppp * m_mppp.conjugate()
    ).real()
    return numerator / denominator


def signed_bell_taylor(y_value, x_ball):
    m_mmpp, m_pppp, m_mppp = amplitudes_jet(y_value, x_ball, TaylorJet)
    numerator = 4 * RBF(2).sqrt() * (m_mmpp * m_pppp.conjugate()).real()
    denominator = (
        m_mmpp * m_mmpp.conjugate()
        + m_pppp * m_pppp.conjugate()
        + 2 * m_mppp * m_mppp.conjugate()
    ).real()
    return numerator / denominator


def taylor_derivative_enclosure(y_value, interval):
    center = RBF(interval.center())
    delta = RBF((-interval.rad(), interval.rad()))
    point = signed_bell_taylor(y_value, center)
    over_interval = signed_bell_taylor(y_value, interval)
    order = TaylorJet.ORDER
    signed_derivative = CBF(0)
    for k in range(1, order):
        signed_derivative += k * point.c[k] * CBF(delta) ** (k - 1)
    signed_derivative += order * over_interval.c[order] * CBF(delta) ** (order - 1)
    return -signed_derivative.real()


if __name__ == "__main__":
    y = RBF("0.42015760875460728129837661981582642")
    for c_text in ("0.1", "0.3", "0.48"):
        disk = CBF(RBF(c_text), RBF("0.001"))
        disk_amplitudes = amplitudes_jet(y, disk, Jet)
        print("cauchy-disk", c_text, [q.v for q in disk_amplitudes])
    taylor_rows = []
    for trial_lo in ("0.1", "0.3", "0.48"):
        trial = RBF((RBF(trial_lo), RBF(trial_lo) + RBF("0.0000001")))
        derivative = taylor_derivative_enclosure(y, trial)
        assert not derivative.is_NaN() and derivative.upper() < 0
        taylor_rows.append({"interval": str(trial), "physical_bell_derivative_ball": str(derivative)})
    point_rows = []
    for x_text in ("0.1", "0.3", "0.48", "0.499"):
        result = bell_jet(y, RBF(x_text))
        signed, derivative = result.v.real(), result.d.real()
        assert signed.upper() < 0
        assert derivative.lower() > 0
        point_rows.append(
            {
                "x": x_text,
                "signed_bell_ball": str(signed),
                "physical_bell_derivative_ball": str(-derivative),
            }
        )

    thin_rows = []
    width = RBF("0.0000000001")
    for lo_text in ("0.1", "0.3", "0.48"):
        lo = RBF(lo_text)
        result = bell_jet(y, RBF((lo, lo + width)))
        derivative = -result.d.real()
        assert derivative.upper() < 0
        thin_rows.append(
            {
                "interval": [str(lo), str(lo + width)],
                "physical_bell_derivative_ball": str(derivative),
            }
        )

    payload = {
        "schema": "marici.exact-qed-angular-arb-prototype.v1",
        "energy": str(y),
        "point_derivative_certificates": point_rows,
        "thin_interval_certificates": thin_rows,
        "order_eight_taylor_certificates": taylor_rows,
        "positive_result": "Arb certifies the physical Bell derivative is negative at four interior points and on three nonzero angular boxes.",
        "obstruction": "Natural interval evaluation loses the strong algebraic cancellations in the exact helicity amplitudes. Order-eight Taylor models widen certified boxes from 1e-10 to 1e-7, but their interval remainder becomes indeterminate by width 1e-6.",
        "next_method": "Derive a cancellation-adapted amplitude basis or use complex-disk/Cauchy remainder bounds before attempting full adaptive interval coverage.",
        "scope": "Rigorous local certificates and a rigorous-method diagnostic, not a continuum monotonicity proof.",
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["content_sha256"] = hashlib.sha256(canonical.encode()).hexdigest().upper()
    out = Path(__file__).parent / "results" / "exact-qed-angular-arb-prototype.json"
    out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"point_certificates": len(point_rows), "second_order_certificates": len(thin_rows), "order_eight_certificates": len(taylor_rows)}))
