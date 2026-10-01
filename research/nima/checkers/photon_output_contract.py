"""Output instruments: counting one photon is not the same as retaining one.

The number-QND instrument is an explicitly additional mathematical assumption,
not an apparatus derived from the seed. Finite polynomials test operator
identities without an occupation cutoff; continuum extension is stated in the
accompanying note.
"""
from dataclasses import dataclass
from fractions import Fraction as F

from photon_maxwell_adapter import Q, ZERO, ONE
from photon_creation_state import FockPolynomial, VACUUM
from photon_coherent_herald import CoherentHeraldModel


@dataclass(frozen=True)
class InstrumentOutcome:
    # Distinct Kraus/environment branches are summed INCOHERENTLY.
    branches: tuple
    description: str

    def weight(self):
        return sum((p.inner(p) for p in self.branches), ZERO)

    def photon_number_numerator(self):
        return sum((p.inner(p.number()) for p in self.branches), ZERO)

    def retains_exactly_one(self):
        return self.weight() != ZERO and all(p.number() == p for p in self.branches)


def one_photon_component(state):
    return FockPolynomial(tuple((n, c) for n, c in state.terms if sum(n) == 1))


def ideal_total_number_qnd(state):
    accepted = one_photon_component(state)
    return (InstrumentOutcome((accepted,), 'additional ideal Lueders total-number-one QND assumption'),
            InstrumentOutcome((state - accepted,), 'number is not one'))


def destructive_exact_one(state):
    # L_h=|vac><1_h|, so sum L_h^dagger L_h=P_1 but the output is vacuum.
    # The two branches are environmental mode records, not a coherent sum.
    table = dict(state.terms)
    return InstrumentOutcome(tuple(VACUUM.scaled(table.get(n, ZERO)) for n in ((1, 0), (0, 1))),
                             'one photon absorbed; no output photon remains')


def one_count_in_tap(state, transmission_amplitude, reflection_amplitude):
    # Exactly one photon absorbed in the reflected arm of a uniform lossless
    # beamsplitter. K_h=r*t^N*a_h; N acts AFTER the annihilation.
    t, r = transmission_amplitude, reflection_amplitude
    if (not isinstance(t, (int, F)) or not isinstance(r, (int, F))
            or not 0 <= t <= 1 or not 0 <= r <= 1 or t * t + r * r != 1):
        raise ValueError('Nonnegative exact lossless beamsplitter amplitudes required')
    t, r = F(t), F(r)
    branches = []
    for h in (1, -1):
        removed = state.annihilate(h)
        branches.append(FockPolynomial(tuple((n, c * r * t ** sum(n)) for n, c in removed.terms)))
    return InstrumentOutcome(tuple(branches), 'one reflected count; transmitted field has one fewer photon')


def production_contract(model, route, *, assume_ideal_total_number_qnd=False):
    if not isinstance(model, CoherentHeraldModel):
        raise ValueError('Checked real-current control model required')
    if type(assume_ideal_total_number_qnd) is not bool:
        raise ValueError('An explicit Boolean mathematical-instrument assumption is required')
    mu = model.mean_photon_number
    common = {'seed_coefficients': model.current.seed_coefficients,
              'assumptions': ('declared Maxwell/Fock model', 'real conserved current',
                              'degenerate driven control qubit', 'supplied gain and ideal readout'),
              'apparatus_derived': False}
    if route == 'source_only':
        lower, upper = model.herald_probability_bounds()
        return {**common, 'exact_available_one_photon': False,
                'infidelity_upper_bound': model.infidelity_upper_bound(),
                'success_lower_bound': lower, 'success_upper_bound': upper,
                'output': 'odd coherent superposition, with nonzero three-photon weight'}
    if route == 'ideal_total_number_qnd':
        if not assume_ideal_total_number_qnd:
            raise ValueError('Exact retained photon needs the additional ideal total-number QND instrument')
        # Overall success, including source production: P_1=mu*exp(-mu).
        # Convexity gives exp(-mu)>=1-mu; exp(mu)>=1+mu gives the upper bound.
        return {**common, 'exact_available_one_photon': True,
                'infidelity_upper_bound': F(0), 'success_formula': 'mu*exp(-mu)',
                'success_lower_bound': max(F(0), mu * (1 - mu)),
                'success_upper_bound': mu / (1 + mu),
                'extra_assumption': 'ideal total-field-number Lueders instrument; no loss or mode disclosure',
                'output': 'a_dagger(psi)|vacuum>, with the radiative wavepacket psi preserved'}
    if route == 'destructive_counter':
        return {**common, 'exact_available_one_photon': False,
                'count_one_probability_formula': 'mu*exp(-mu)',
                'available_photons_after_count': 0,
                'output': 'vacuum in the counted field'}
    raise ValueError('Unknown production/readout route')
