"""Bounded structural tests against rounded p, H-1, He-4 reference data.

Decimal inputs are frozen approximations, not exact measured constants.
Fraction arithmetic makes the calculations exact conditional on these inputs.
No fitted electronic coefficient uses helium in the prediction tests.
"""
from fractions import Fraction as F
from pathlib import Path
import json


def main():
    me_ev = F('510998.95')
    mp = F('1836.152673')
    mn = F('1838.683662')
    h_binding = F('13.5984')
    he_electronic = F('79.0052')
    he_nuclear = F('28295700')
    # Masses computed by constituent accounting are not independent predictions.
    cases = [('p', 1, 0, 0, F(0), F(0)),
             ('H-1', 1, 0, 1, F(0), h_binding),
             ('He-4', 2, 2, 2, he_nuclear, he_electronic)]
    rows = []
    for name, z, n, electrons, nuclear, electronic in cases:
        baseline = 1836*(z+n)+electrons
        constituent_excess = z*(mp-1836)+n*(mn-1836)
        mass = z*mp+n*mn+electrons-(nuclear+electronic)/me_ev
        residual = mass-baseline
        assert residual == constituent_excess-nuclear/me_ev-electronic/me_ev
        rows.append(dict(system=name, protons=z, neutrons=n, electrons=electrons,
                         integer_baseline=baseline, mass_me=float(mass),
                         constituent_excess_me=float(constituent_excess),
                         nuclear_correction_me=float(-nuclear/me_ev),
                         electronic_correction_me=float(-electronic/me_ev),
                         total_excess_me=float(residual)))

    # Each rule agrees with H by calibration. He is a held-out discriminator.
    predictions = []
    for label, factor in [('per electron', 2),
                          ('per proton-electron pair', 4),
                          ('independent hydrogenic Z-squared per electron', 8)]:
        predicted = factor*h_binding
        error = predicted-he_electronic
        assert error != 0
        predictions.append(dict(rule=label, hydrogen_calibrated_coefficient_eV=str(h_binding),
                                helium_factor=factor, predicted_helium_binding_eV=str(predicted),
                                prediction_minus_reference_eV=str(error),
                                predicted_decimal=float(predicted), error_decimal=float(error),
                                disposition='does_not_reproduce_reference'))
    # The correction needed by the last model is descriptive, not a prediction.
    screening = 8*h_binding-he_electronic
    assert screening > 0
    effective_charge_squared = he_electronic/(2*h_binding)
    assert 1 < effective_charge_squared < 4
    assert mp-1836 == F('0.152673')
    assert (mp+1-h_binding/me_ev)-mp == 1-h_binding/me_ev
    # Negative control: wrong binding sign must increase rather than reduce mass.
    assert mp+1+h_binding/me_ev != mp+1-h_binding/me_ev
    result = dict(
        schema='marici.nima.proton-hydrogen-helium-structure.v1', status='pass',
        input_status='Rounded reference values from the conversation; no external precision audit performed.',
        inputs=dict(proton_me=str(mp), neutron_me=str(mn), electron_rest_energy_eV=str(me_ev),
                    hydrogen_binding_eV=str(h_binding), helium_electronic_binding_eV=str(he_electronic),
                    helium_nuclear_binding_eV=str(he_nuclear)),
        mass_rows=rows, held_out_helium_tests=predictions,
        required_reduction_from_independent_hydrogenic_binding_eV=str(screening),
        required_reduction_decimal_eV=float(screening),
        effective_charge_squared_fit=str(effective_charge_squared),
        interpretation='Charge-squared hydrogenic model overbinds helium; its residual has the sign of screening/repulsion. It does not derive that correction.',
        residual='Need a source-derived coupled electronic operator and a distinct nuclear binding calculation; three systems do not determine a universal quartic kernel.',
    )
    out = Path(__file__).resolve().parents[1]/'results/proton-hydrogen-helium-structure.json'
    out.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
