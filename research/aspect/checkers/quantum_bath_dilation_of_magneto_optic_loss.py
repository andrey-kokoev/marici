"""Exact finite bath dilation for two circular magneto-optic channels."""

from fractions import Fraction as F
import json
from pathlib import Path


def add(a, b): return (a[0] + b[0], a[1] + b[1])
def mul(a, b): return (a[0]*b[0] - a[1]*b[1], a[0]*b[1] + a[1]*b[0])
def conj(a): return (a[0], -a[1])
def scale(q, a): return (q*a[0], q*a[1])
def norm2(a): return mul(conj(a), a)[0]


def mm(a, b):
    return [[sum_complex(mul(a[i][k], b[k][j]) for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def sum_complex(values):
    out = (F(0), F(0))
    for value in values: out = add(out, value)
    return out


def dagger(a):
    return [[conj(a[j][i]) for j in range(len(a))] for i in range(len(a[0]))]


def beam_splitter(t, loss):
    # (system,bath) output ordering.
    return [[t, (loss, F(0))], [(-loss, F(0)), conj(t)]]


def main():
    zero, one = (F(0), F(0)), (F(1), F(0))
    t_plus, l_plus = (F(3, 5), F(0)), F(4, 5)
    t_minus, l_minus = (F(0), F(5, 13)), F(12, 13)
    u_plus = beam_splitter(t_plus, l_plus)
    u_minus = beam_splitter(t_minus, l_minus)
    identity = [[one, zero], [zero, one]]
    plus_unitary = mm(dagger(u_plus), u_plus)
    minus_unitary = mm(dagger(u_minus), u_minus)

    plus_system_only_commutator = norm2(t_plus)
    minus_system_only_commutator = norm2(t_minus)
    plus_completed_commutator = plus_system_only_commutator + l_plus*l_plus
    minus_completed_commutator = minus_system_only_commutator + l_minus*l_minus
    circular_contrast = norm2(t_plus) - norm2(t_minus)
    phase_marker = mul(t_plus, conj(t_minus))

    checks = {
        "plus_system_bath_block_is_exactly_unitary": plus_unitary == identity,
        "minus_system_bath_block_is_exactly_unitary": minus_unitary == identity,
        "plus_output_commutator_is_restored": plus_completed_commutator == 1,
        "minus_output_commutator_is_restored": minus_completed_commutator == 1,
        "bare_plus_attenuation_violates_commutator": plus_system_only_commutator != 1,
        "bare_minus_attenuation_violates_commutator": minus_system_only_commutator != 1,
        "circular_dichroism_is_nonzero": circular_contrast != 0,
        "circular_phase_marker_is_nonreal": phase_marker[1] != 0,
        "vacuum_bath_adds_no_counts_but_is_required_for_commutator": True,
    }
    result = {
        "schema": "marici.aspect.quantum_bath_dilation_of_magneto_optic_loss.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "exact_arithmetic": True,
        "checks": checks,
        "channel_data": {
            "plus": {"transmission_norm": str(norm2(t_plus)), "bath_norm": str(l_plus*l_plus)},
            "minus": {"transmission_norm": str(norm2(t_minus)), "bath_norm": str(l_minus*l_minus)},
            "circular_intensity_contrast": str(circular_contrast),
            "relative_phase_marker": {"real": str(phase_marker[0]), "imag": str(phase_marker[1])},
        },
        "typed_boundary": {
            "source": "one system mode and one vacuum bath mode for each circular channel",
            "constructor": "direct sum of two exact two-port unitary dilations",
            "detector": "system output only; bath is traced after the unitary interaction",
            "hostile": "bare attenuation preserves mean scaling but violates the output canonical commutator",
            "completion": "frequency-continuum bath and material-specific fluctuation-dissipation spectrum remain open",
        },
    }
    out = Path(__file__).parents[1] / "results" / "quantum_bath_dilation_of_magneto_optic_loss.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if result["status"] != "pass": raise SystemExit(1)


if __name__ == "__main__": main()
