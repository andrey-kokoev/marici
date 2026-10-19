"""Finite-duration, symmetric pentachoron contact toy.

This is a nonrelativistic, dimensionless mechanical model, not a physical
prediction for electrons or a quantum scattering model. Time unit: sqrt(m/k).
Length unit: ell. Per-body incident-speed unit: ell*sqrt(k/m).

New assumptions: projected-overlap repulsion W=q_+^2/2, per-body alignment
energy K(1-cos(delta)), and equal inertial weight at the five vertices.
The latter gives I/(m*ell^2)=8/5. No reconnection rule is included.

Run: python pentachoron_collision.py
Requires NumPy and SciPy. Outputs JSON to standard output.
"""
from __future__ import annotations
import json
from math import atan, sqrt
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq, root

HIDDEN_LEVER = 1 / sqrt(5)
EXPOSURE_ANGLE = atan(HIDDEN_LEVER)
INERTIA = 8 / 5


def support(angle: float) -> tuple[float, float]:
    """Forward support and its derivative, including rotations beyond pi/2."""
    c, s = np.cos(angle), np.sin(angle)
    base = abs(c) - HIDDEN_LEVER * s
    apex = 4 * HIDDEN_LEVER * s
    if base >= apex:
        return float(base), float(-np.sign(c) * s - HIDDEN_LEVER * c)
    return float(apex), float(4 * HIDDEN_LEVER * c)


def first_base_separation(speed: float, alignment: float):
    """Continue the original-boundary branch for threshold root finding only."""
    def rhs(t, state):
        d, p, angle, angular_p = state
        a = np.cos(angle) - HIDDEN_LEVER * np.sin(angle)
        ap = -np.sin(angle) - HIDDEN_LEVER * np.cos(angle)
        force = max(0.0, 2*a-d)
        return 2*p, force, angular_p/INERTIA, -alignment*np.sin(angle)-force*ap

    def separation(t, state):
        d, _, angle, _ = state
        return 2*(np.cos(angle)-HIDDEN_LEVER*np.sin(angle))-d
    separation.direction = -1
    separation.terminal = True
    sol = solve_ivp(rhs, (0, 30), [2, -speed, 0, 0], events=separation,
                    method='DOP853', rtol=2e-12, atol=2e-14, max_step=.01)
    if not sol.success or not sol.t_events[0].size:
        raise RuntimeError('Base-branch separation was not resolved.')
    return float(sol.t[-1]), sol.y[:, -1]


def simulate(speed: float, alignment: float = .1, method: str = 'DOP853') -> dict:
    if speed <= 0 or alignment < 0:
        raise ValueError('Speed must be positive and alignment nonnegative.')

    def rhs(t, state):
        distance, momentum, angle, angular_p = state
        a, ap = support(angle)
        force = max(0.0, 2*a-distance)
        return (2*momentum, force, angular_p/INERTIA,
                -alignment*np.sin(angle)-force*ap)

    def contact(t, state):
        return 2*support(state[2])[0]-state[0]
    def exposure(t, state):
        return state[2]-EXPOSURE_ANGLE
    def escaped(t, state):
        # Beyond the maximum possible pair width, with increasing separation,
        # no subsequent internal rotation can cause another contact.
        return state[0]-8*HIDDEN_LEVER-1e-5
    escaped.direction = 1
    escaped.terminal = True

    sol = solve_ivp(rhs, (0, 100), [2, -speed, 0, 0],
                    events=(contact, exposure, escaped), method=method,
                    rtol=2e-11, atol=2e-13, max_step=.003, dense_output=True)
    if not sol.success or not sol.t_events[2].size:
        raise RuntimeError('Final escape was not resolved within the integration window.')
    times = np.linspace(0, sol.t[-1], 10000)
    distance, momentum, angle, angular_p = sol.sol(times)
    a = np.maximum(np.abs(np.cos(angle))-HIDDEN_LEVER*np.sin(angle),
                   4*HIDDEN_LEVER*np.sin(angle))
    overlap = np.maximum(0, 2*a-distance)
    energy = momentum**2 + angular_p**2/INERTIA + 2*alignment*(1-np.cos(angle)) + overlap**2/2
    relative_drift = float(np.max(np.abs(energy-speed**2))/speed**2)
    if relative_drift > 1e-7:
        raise RuntimeError(f'Energy check failed: relative drift {relative_drift}.')
    return {
        'incident_speed': speed,
        'alignment_energy': alignment,
        'contact_boundary_times': sol.t_events[0].tolist(),
        'exposure_events': [
            {'time': float(t),
             'force': float(max(0, 2*support(sol.sol(t)[2])[0]-sol.sol(t)[0])),
             'direction': 'outward' if sol.sol(t)[3] > 0 else 'return'}
            for t in sol.t_events[1]
        ],
        'peak_force': float(overlap.max()),
        'relative_energy_drift': relative_drift,
        'final_escape_time': float(sol.t[-1]),
    }


def thresholds(alignment: float = .1) -> dict:
    direct = brentq(lambda v: first_base_separation(v, alignment)[1][2]-EXPOSURE_ANGLE,
                    .5, 1.5, xtol=2e-11)

    def grazing_equations(unknowns):
        speed, elapsed = unknowns
        if elapsed <= 0:
            raise ValueError('Grazing search requires positive elapsed time.')
        sep_time, state = first_base_separation(speed, alignment)
        distance, momentum, angle, angular_p = state
        def free_rotation(t, y):
            return y[1]/INERTIA, -alignment*np.sin(y[0])
        sol = solve_ivp(free_rotation, (0, elapsed), [angle, angular_p],
                        method='DOP853', rtol=2e-12, atol=2e-14)
        angle, angular_p = sol.y[:, -1]
        gap = 8*HIDDEN_LEVER*np.sin(angle)-(distance+2*momentum*elapsed)
        gap_rate = 8*HIDDEN_LEVER*np.cos(angle)*angular_p/INERTIA-2*momentum
        return [gap, gap_rate]

    grazing = root(grazing_equations, [.755, .8], tol=1e-10)
    if not grazing.success or np.linalg.norm(grazing.fun) > 1e-8:
        raise RuntimeError('Recontact grazing threshold was not resolved.')
    return {'first_contact_exposure_speed': float(direct),
            'local_recontact_onset_speed': float(grazing.x[0]),
            'grazing_elapsed_after_first_separation': float(grazing.x[1])}


if __name__ == '__main__':
    dop = [simulate(v) for v in [.7, .8, .9]]
    rk = [simulate(v, method='RK45') for v in [.7, .8, .9]]
    comparisons = []
    for a, b in zip(dop, rk):
        err = float(np.max(np.abs(np.array(a['contact_boundary_times'])-
                                  np.array(b['contact_boundary_times']))))
        if err > 1e-6:
            raise RuntimeError('Independent solver contact times disagree.')
        comparisons.append({'speed': a['incident_speed'], 'contact_time_difference': err})
    print(json.dumps({'model': 'nonrelativistic symmetric projected-contact toy',
                      'exposure_angle_radians': EXPOSURE_ANGLE,
                      'thresholds': thresholds(), 'runs': dop,
                      'independent_solver_comparisons': comparisons}, indent=2))
