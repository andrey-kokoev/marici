"""Exactly solvable degenerate-qubit control, not a gapped-emitter solution.

For a real conserved current j and conserved source operator X, the interaction
is X times a linear free-field observable. Its time-ordered exponential is a
conditional displacement, up to a common phase. Source-flip heralding selects
odd photon number. All probability tails below are infinite-series bounds.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from math import factorial

from photon_local_current import LocalDipoleCurrent
from photon_maxwell_adapter import ZERO


@dataclass(frozen=True)
class CoherentHeraldModel:
    current: LocalDipoleCurrent
    mean_photon_number: F  # mu=lambda^2 * radiation norm; supplied gain calibration

    def __post_init__(self):
        if not isinstance(self.current, LocalDipoleCurrent):
            raise ValueError('Retained local source current required')
        if (all(d == ZERO for d in self.current.dipole)
                or any(d.conjugate() != d for d in self.current.dipole)):
            raise ValueError('This exact X-current model requires a nonzero real dipole; circular complex transitions are different')
        mu = self.mean_photon_number
        if not isinstance(mu, (int, F)) or mu <= 0:
            raise ValueError('Positive exact mean photon number required')
        object.__setattr__(self, 'mean_photon_number', F(mu))

    @property
    def source_gap(self):
        # The commuting-source solution does NOT silently approximate Omega>0.
        return F(0)

    def number_weight(self, number, source_flip=False):
        """Probability with the common factor exp(-mu) omitted, NOT normalized."""
        if type(number) is not int or number < 0:
            raise ValueError('Nonnegative integer photon count required')
        if source_flip and number % 2 == 0:
            return F(0)
        return self.mean_photon_number ** number / factorial(number)

    def infidelity_upper_bound(self):
        """Bound 1-mu/sinh(mu) using the entire odd-photon tail, not a cutoff."""
        x = self.mean_photon_number ** 2
        if x >= 20:
            raise ValueError('This geometric certificate requires mu^2<20')
        # sinh(mu)/mu=1+sum_{m>=1} mu^(2m)/(2m+1)!.
        # Ratios within the tail are <=mu^2/20.
        tail_bound = (x / 6) / (1 - x / 20)
        return tail_bound / (1 + tail_bound)

    def herald_probability_bounds(self):
        # P_flip=(1-exp(-2mu))/2. Convexity and the second-degree exponential
        # remainder bound give these global (occasionally weak) inequalities.
        mu = self.mean_photon_number
        return max(F(0), mu - mu * mu), min(F(1, 2), mu)

    def certification(self, max_infidelity, minimum_success):
        if (not isinstance(max_infidelity, (int, F)) or not 0 <= max_infidelity < 1
                or not isinstance(minimum_success, (int, F)) or not 0 < minimum_success <= 1):
            raise ValueError('Exact probability targets required')
        error = self.infidelity_upper_bound()
        lower, upper = self.herald_probability_bounds()
        if error > max_infidelity or lower < minimum_success:
            raise ValueError('Requested fidelity/success not certified by this source setting')
        return {'infidelity_upper_bound': error, 'herald_probability_lower_bound': lower,
                'herald_probability_upper_bound': upper,
                'exact_single_photon': False, 'source_gap': self.source_gap}
