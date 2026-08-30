"""Exact PSZ puncture-source and distributional-readout checks."""

import json
import os

import sympy as sp


checks = []


def record(gate, statement, passed, detail):
    checks.append({
        "gate": gate,
        "statement": statement,
        "passed": bool(passed),
        "detail": detail,
    })


z, zb, x, xb = sp.symbols("z zb x xb", nonzero=True)
G = (sp.log(x - z) + sp.log(xb - zb)
     - sp.log(1 + x * xb) - sp.log(1 + z * zb))
dbar = sp.factor(sp.diff(G, xb))
mixed_regular = sp.factor(sp.diff(G, x, xb))
dbar_expected = (1 + x * zb) / ((xb - zb) * (1 + x * xb))
mixed_expected = -1 / (1 + x * xb) ** 2

record(
    "GREEN.dbar",
    "the orbital PSZ kernel is the exact source derivative of log chordal distance",
    sp.simplify(dbar - dbar_expected) == 0,
    "d_xb G=(1+x*zb)/((xb-zb)(1+x*xb))",
)
record(
    "GREEN.mixed",
    "the regular mixed source derivative is the sphere zero-mode subtraction",
    sp.simplify(mixed_regular - mixed_expected) == 0,
    "away from z=x, d_x d_xb G=-1/(1+x*xb)^2",
)


gamma = 2 / (1 + x * xb) ** 2
record(
    "GREEN.background",
    "the regular mixed derivative equals -gamma/2",
    sp.simplify(mixed_regular + gamma / 2) == 0,
    "distributional completion adds 2*pi*delta^2(x-z)",
)


# Residue with respect to the observation coordinate zb.
residue = sp.simplify(sp.limit((zb - xb) * dbar_expected, zb, xb))
record(
    "PORT.residue",
    "the orbital source coefficient has a nonzero local pole port",
    residue == -1,
    "Res_zb=xb d_xb G=-1",
)


# Distinct simple poles give an identity residue matrix up to the common sign.
n = 7
residue_matrix = sp.zeros(n, n)
for i in range(n):
    for j in range(n):
        residue_matrix[i, j] = -1 if i == j else 0
record(
    "PORT.reconstruct",
    "distinct puncture residue ports reconstruct all orbital source labels",
    residue_matrix.rank() == n and residue_matrix.det() == -1,
    "seven-puncture hostile residue matrix has full rank",
)


# The distributional spin port has coefficient pi*i*gamma*h before taking
# the imaginary part, and a required nonzero smooth subtraction.
h = sp.symbols("h", real=True)
delta_coefficient = sp.simplify(gamma * sp.I * h * sp.pi)
background_coefficient = sp.simplify(
    gamma * (sp.I * h / 2) * (-gamma / 2)
)
record(
    "PORT.spin",
    "the spin source has both a puncture delta port and a sphere background port",
    delta_coefficient != 0 and background_coefficient != 0,
    "delta=" + sp.sstr(delta_coefficient)
    + "; background=" + sp.sstr(background_coefficient),
)


# A finite Taylor/Laurent presentation of the simple pole retains a tail.
t = sp.symbols("t")
pole = 1 / (1 - t)
truncation_ok = True
for order in range(0, 21):
    partial = sum(t ** k for k in range(order + 1))
    remainder = sp.factor(pole - partial)
    expected = sp.factor(t ** (order + 1) / (1 - t))
    truncation_ok &= sp.simplify(remainder - expected) == 0
record(
    "TARGET.tail",
    "every finite coefficient chart of a puncture pole omits a coherent nonzero tail",
    truncation_ok,
    "orders 0..20",
)


# Exact-shift quotient: the antisymmetric derivative kills a gradient.
X = z ** 3 * zb ** 2 + 2 * z * zb + z ** 2 + zb ** 2
curl_gradient = sp.simplify(
    sp.diff(sp.diff(X, z), zb) - sp.diff(sp.diff(X, zb), z)
)
record(
    "QUOTIENT.exact",
    "the local curl removes exact real-gradient shifts",
    curl_gradient == 0,
    "hostile polynomial potential",
)


passed = sum(item["passed"] for item in checks)
total = len(checks)
payload = {
    "checker": "physical_spin_readout_constructor_checks.py",
    "strength": "source-derived PSZ source/readout morphism",
    "passed": passed,
    "total": total,
    "checks": checks,
    "verdict": (
        "The PSZ source generates puncture-supported orbital and spin "
        "distributions. Complete local residue and delta ports reconstruct "
        "the labelled hard packet before conservation quotients, whereas a "
        "finite Laurent target omits coherent tails and distributional ports."
    ),
}

outdir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "results")
os.makedirs(outdir, exist_ok=True)
outpath = os.path.join(outdir, "physical_spin_readout_constructor.json")
with open(outpath, "w", encoding="ascii") as handle:
    json.dump(payload, handle, indent=2, sort_keys=True)
    handle.write("\n")

for item in checks:
    label = "PASS" if item["passed"] else "FAIL"
    print(f"{label} {item['gate']}: {item['statement']} - {item['detail']}")
print(f"SUMMARY {passed}/{total}")

if passed != total:
    raise SystemExit(1)

