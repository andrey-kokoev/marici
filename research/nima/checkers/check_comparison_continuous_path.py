# /// script
# dependencies = ["numpy>=2,<3"]
# ///
"""Continuous orthogonal realization of each retained-record comparison.

One auxiliary coordinate supplies orientation compensation. Its path is a
chosen interpolation, not a physical clock or a canonical Hamiltonian law.
"""
from pathlib import Path
import runpy
import numpy as np

source = runpy.run_path(str(Path(__file__).with_name('check_comparison_energy_spectrum.py')))
rows = np.asarray(source['rows'], dtype=float)
dimension = 160
aux = np.eye(dimension)[-1]


def plane_rotate(X, d, angle):
    """Apply exp(angle*(aux*d^T-d*aux^T)) to columns of X."""
    longitudinal = d @ X
    clock = aux @ X
    return (X + np.outer(d, (np.cos(angle)-1)*longitudinal-np.sin(angle)*clock)
            + np.outer(aux, np.sin(angle)*longitudinal+(np.cos(angle)-1)*clock))


# Compare the continuous endpoint with the lifted discrete sweep.
continuous = np.eye(dimension)
discrete = np.eye(dimension)
for i, r in enumerate(rows):
    u = np.zeros(dimension)
    u[:6] = r/np.linalg.norm(r)
    record = np.eye(dimension)[6+i]
    difference = (u-record)/np.sqrt(2)
    assert abs(difference @ aux) < 1e-14
    # Reflection in difference exchanges carrier longitudinal and record axes.
    half_turn = plane_rotate(np.eye(dimension), difference, np.pi)
    expected = np.eye(dimension)-2*np.outer(difference, difference)-2*np.outer(aux, aux)
    assert np.max(np.abs(half_turn-expected)) < 1e-14
    assert np.max(np.abs(half_turn.T@half_turn-np.eye(dimension))) < 1e-14
    assert np.max(np.abs(plane_rotate(np.eye(dimension), difference, 3*np.pi)-half_turn)) < 1e-14
    # Verify a genuine intermediate excursion for unit difference input.
    midpoint = plane_rotate(difference[:, None], difference, np.pi/2)[:, 0]
    assert np.max(np.abs(midpoint-aux)) < 1e-14
    continuous = plane_rotate(continuous, difference, np.pi)
    longitudinal = u @ discrete
    old_record = discrete[6+i, :].copy()
    discrete[:6, :] += np.outer(u[:6], old_record-longitudinal)
    discrete[6+i, :] = longitudinal
    discrete[-1, :] *= -1
assert np.max(np.abs(continuous-discrete)) < 1e-12
assert np.max(np.abs(continuous[-1, :-1])) < 1e-12
assert abs(continuous[-1, -1]+1) < 1e-12
assert np.max(np.abs(continuous.T@continuous-np.eye(dimension))) < 1e-12

# If G is the unit-angle generator, exp(pi*G) is the endpoint.
# For any duration tau>0, B_tau=(pi/tau)*G reaches that endpoint at tau.
# A 3*pi path is another endpoint-compatible branch; the half-turn can
# also run with either orientation and any monotone angular speed profile.
print('All 153 comparisons realized as continuous half-turns with one auxiliary coordinate.')
print('Endpoint map is diag(U,-1); an initially zero auxiliary returns to zero at each comparison.')
print('Mid-update auxiliary excursion verified; norm preserved throughout each plane rotation.')
print('pi and 3*pi paths reproduce identical comparison endpoints.')
print('Every positive comparison duration is compatible with these endpoints.')
print('This constructs a continuous path; its duration, orientation, speed profile, and physical role remain choices.')
