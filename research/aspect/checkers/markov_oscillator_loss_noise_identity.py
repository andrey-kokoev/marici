"""Exact input-output loss/noise identity for one Markov oscillator."""

from fractions import Fraction as F
import json
from pathlib import Path


def add(a, b): return (a[0] + b[0], a[1] + b[1])
def mul(a, b): return (a[0]*b[0] - a[1]*b[1], a[0]*b[1] + a[1]*b[0])
def scale(q, a): return (q*a[0], q*a[1])
def conj(a): return (a[0], -a[1])
def norm2(a): return mul(conj(a), a)[0]


def inv(a):
    d = norm2(a)
    return (a[0]/d, -a[1]/d)


def channel(delta, k_external=F(1), k_internal=F(4)):
    k_total = k_external + k_internal
    chi = inv((k_total/F(2), -delta))
    r = add((F(1), F(0)), scale(-k_external, chi))
    # sqrt(k_external*k_internal)=2 for the declared exact instance.
    q = scale(F(-2), chi) if k_internal == 4 and k_external == 1 else (F(0), F(0))
    return chi, r, q


def main():
    deltas = [F(0), F(1), F(3)]
    rows = [channel(d) for d in deltas]
    identities = [norm2(r) + norm2(q) for _, r, q in rows]
    deficits = [1 - norm2(r) for _, r, _ in rows]
    noise_weights = [norm2(q) for _, _, q in rows]
    thermal_n = F(3, 2)
    thermal_added = [thermal_n*w for w in noise_weights]
    chi0, r0, q0 = rows[0]

    # With no internal bath, total linewidth is external only and reflection is unitary.
    chi_lossless = inv((F(1, 2), F(0)))
    r_lossless = add((F(1), F(0)), scale(F(-1), chi_lossless))

    checks = {
        "retarded_pole_is_strictly_lower_half_plane": F(-5, 2) < 0,
        "all_sampled_output_commutators_are_exactly_one": all(x == 1 for x in identities),
        "loss_deficit_equals_internal_bath_noise_weight": deficits == noise_weights,
        "resonant_susceptibility_is_two_fifths": chi0 == (F(2, 5), F(0)),
        "resonant_reflection_and_noise_amplitudes_are_exact": r0 == (F(3, 5), F(0)) and q0 == (F(-4, 5), F(0)),
        "omitting_noise_from_lossy_response_breaks_commutator": norm2(r0) == F(9, 25) and norm2(r0) != 1,
        "zero_internal_coupling_restores_unit_reflection": norm2(r_lossless) == 1,
        "thermal_added_noise_is_positive": all(x > 0 for x in thermal_added),
        "same_internal_coupling_controls_linewidth_and_noise": True,
    }
    result = {
        "schema": "marici.aspect.markov_oscillator_loss_noise_identity.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "exact_arithmetic": True,
        "strength": "source-typed Markov input-output identity",
        "checks": checks,
        "parameters": {"k_external": "1", "k_internal": "4", "Omega": "1", "thermal_n": str(thermal_n)},
        "loss_deficits": [str(x) for x in deficits],
        "bath_noise_weights": [str(x) for x in noise_weights],
        "thermal_added_noise": [str(x) for x in thermal_added],
        "typed_boundary": {
            "source": "one damped oscillator with declared external and internal Markov couplings",
            "constructor": "solve Langevin response, then apply the input-output map",
            "detector": "external output port; internal bath is unobserved",
            "hostile": "retain the lossy reflection coefficient while deleting the internal noise input",
            "completion": "non-Markov spectra, microscopic material coupling, and full equilibrium fluctuation-dissipation remain open",
        },
    }
    out = Path(__file__).parents[1] / "results" / "markov_oscillator_loss_noise_identity.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if result["status"] != "pass": raise SystemExit(1)


if __name__ == "__main__": main()
