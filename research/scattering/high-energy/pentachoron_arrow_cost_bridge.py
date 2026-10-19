"""Arrow-cost bridge to the symmetric pentachoron collision toy.

This is a NEW conditional nonrelativistic geometric model, not an electron
scattering prediction and not an implementation of the full native spinor graph.

New dynamical postulates:
  * Equal squared displacement cost on each of five retained vertex records.
  * A common energy coefficient E_* and an unspecified physical step time tau.
  * Positive projected-overlap residual q/ell as the single contact defect.
  * No free alignment potential for rigid co-rotation of all retained records.

These give m=10 E_* tau^2/ell^2, I=16 E_* tau^2,
k=2 E_*/ell^2, I/(m ell^2)=8/5, and t0=sqrt(5)*tau.
The input speed is v/(ell*sqrt(k/m)); it is NOT v/c.

The source five-cycle remains a geometric symmetry, NOT the physical clock.
No elementary configuration-arrow amplitude law is claimed to be derived.

Run: python pentachoron_arrow_cost_bridge.py
Dependencies: numpy, scipy, sympy. Prints a JSON verification receipt.
The numerical solver is retained from pentachoron_collision.py, with K=0.
"""
from __future__ import annotations
import json
from math import atan, sqrt
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq, root
import sympy as sp

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



def exact_geometric_checks() -> dict:
    """Exact source geometry and kinetic-metric checks; no fitted parameters."""
    ell = sp.symbols('ell', positive=True)
    x, angle = sp.symbols('x angle', real=True)
    raw = sp.Matrix([[1,1,1,0], [1,-1,-1,0], [-1,1,-1,0],
                     [-1,-1,1,0], [0,0,0,sp.sqrt(5)]])
    centroid = sum((raw.row(i) for i in range(5)), sp.zeros(1,4))/5
    q = raw - sp.ones(5,1)*centroid
    assert q.T*q == 4*sp.eye(4)
    assert sum((q.row(i) for i in range(5)), sp.zeros(1,4)) == sp.zeros(1,4)
    B = sp.Matrix.hstack(*[(raw.row(i)-raw.row(4)).T for i in range(4)])
    Gsource = sp.Matrix([[8,4,4,4],[4,8,4,4],[4,4,8,4],[4,4,4,8]])
    assert B.T*B == Gsource
    source_M=sp.Matrix([[-1,-1,-1,-1],[1,0,0,0],[0,1,0,0],[0,0,1,0]])
    source_t=sp.Matrix([1,0,0,0])
    Rsource=B*source_M*B.inv()
    assert Rsource.T*Rsource == sp.eye(4)
    assert Rsource**5 == sp.eye(4)
    assert B*source_t == (raw.row(0)-raw.row(4)).T
    for i in range(5):
        assert sp.simplify(Rsource*q.row(i).T-q.row((i+1)%5).T)==sp.zeros(4,1)
    c, s = sp.cos(angle), sp.sin(angle)
    R = sp.Matrix([[c,0,0,s],[0,1,0,0],[0,0,1,0],[-s,0,0,c]])
    transformed = ell*q*R.T + sp.ones(5,1)*sp.Matrix([[x,0,0,0]])
    difference = transformed-ell*q
    cost = sp.trigsimp(sum(z*z for z in difference))
    wanted = 5*x*x + 16*ell**2*(1-sp.cos(angle))
    assert sp.trigsimp(cost-wanted) == 0
    tx=transformed.diff(x)
    ta=transformed.diff(angle)
    translation=sp.trigsimp(sum(z*z for z in tx))
    rotation=sp.trigsimp(sum(z*z for z in ta))
    cross=sp.trigsimp(sum(a*b for a,b in zip(tx,ta)))
    assert translation==5 and rotation==8*ell**2 and cross==0
    # Every intrinsic pair length is invariant under rigid rotation.
    for i in range(5):
        for j in range(i):
            dif=transformed.row(i)-transformed.row(j)
            assert sp.trigsimp(sum(z*z for z in dif)-8*ell**2)==0
    dc=sp.atan(1/sp.sqrt(5))
    assert sp.trigsimp((sp.cos(angle)-sp.sin(angle)/sp.sqrt(5)
                       -4*sp.sin(angle)/sp.sqrt(5)).subs(angle,dc))==0
    # A symmetry-compatible extra center-motion term changes the inertia ratio.
    # T_extra=(lambda*mu/10)*|sum_i dot(r_i)|^2.
    # Thus symmetry alone, without per-vertex locality, does not fix the ratio.
    lam=sp.symbols('lambda', nonnegative=True)
    ratio=sp.Rational(8,5)/(1+lam)
    return {
      'exact_checks_passed': True,
      'centered_vertex_covariance':'sum_i q_i q_i^T = 4 ell^2 I_4',
      'source_metric_recovered': True,
      'source_five_cycle_preserves_vertex_set': True,
      'source_cycle_is_not_assumed_to_be_a_time_step': True,
      'configuration_displacement_cost':str(wanted),
      'motion_metric':{'translation':str(translation),'rotation':str(rotation),'cross':str(cross)},
      'inertia_ratio_under_local_uniform_rule':'8/5',
      'symmetry_alone_countermodel_ratio':str(ratio),
      'intrinsic_edge_lengths_do_not_supply_alignment': True,
      'exposure_angle_exact':'atan(1/sqrt(5))',
      'new_cost_extension':{
        'kinetic':'E_* tau^2/ell^2 sum_i |dot(r_i)|^2 per body',
        'contact':'E_* (q/ell)^2',
        'mass':'10 E_* tau^2/ell^2',
        'inertia':'16 E_* tau^2',
        'contact_stiffness':'2 E_*/ell^2',
        'time_unit':'sqrt(5) tau',
        'speed_unit':'ell/(sqrt(5) tau)'},
      'same_support_different_force_control':{
        'residual_1':'q/ell', 'residual_2':'(q/ell)^2',
        'both_active':'q>0',
        'force_1':'2 E_* q/ell^2',
        'force_2':'4 E_* q^3/ell^4',
        'conclusion':'Arrow presence/count alone does not choose the overlap-force law.'}
    }


def main() -> None:
    exact=exact_geometric_checks()
    th=thresholds(alignment=0.0)
    dop=[simulate(v, alignment=0.0, method='DOP853') for v in [.7,.8,.9]]
    rk=[simulate(v, alignment=0.0, method='RK45') for v in [.7,.8,.9]]
    comparisons=[]
    for a,b in zip(dop,rk):
        if len(a['contact_boundary_times'])!=len(b['contact_boundary_times']):
            raise RuntimeError('Solver contact-event counts disagree.')
        error=float(np.max(np.abs(np.array(a['contact_boundary_times'])-
                                  np.array(b['contact_boundary_times']))))
        if error>1e-6:
            raise RuntimeError('Solver contact-event times disagree.')
        comparisons.append({'incident_speed':a['incident_speed'],
                            'contact_time_difference':error,
                            'RK45_relative_energy_drift':b['relative_energy_drift']})
    # Resolve the two local transitions on both sides, away from grazing ties.
    boundary_controls=[]
    for name,key in [('recontact','local_recontact_onset_speed'),
                     ('during_first_contact','first_contact_exposure_speed')]:
        for shift in [-.002,.002]:
            v=th[key]+shift
            r=simulate(v, alignment=0.0)
            boundary_controls.append({'boundary':name,'offset':shift,
              'incident_speed':v,
              'contact_boundary_times':r['contact_boundary_times'],
              'first_exposure':r['exposure_events'][0] if r['exposure_events'] else None})
    result={
      'model':'conditional arrow-cost extension; nonrelativistic projected contact',
      'source':{'repository':'andrey-kokoev/marici',
        'geometry_file':'research/voevodsky/inputs/relative-electron.json',
        'geometry_git_blob_sha':'e6c919458f5e95a4830d6ef405fda6397ab837a2',
        'operation_energy_file':'research/voevodsky/native-operation-energy-lift.md',
        'operation_energy_git_blob_sha':'846c2a12b537731fafd7e06ceb06f0aaa6dddb95',
        'five_cycle_file':'research/voevodsky/pentachoron-cycle-spin-energy-transport.md',
        'five_cycle_git_blob_sha':'d0bdb86bd2e3ed0399d3f97c69d39235ae3ddbdc'},
      'scope':'The native spinor Hamiltonian checker was not rerun. Its stated covariance is cited, not independently certified here. Geometry and the new mechanical extension are checked here.',
      'exact_geometry_and_postulate_checks':exact,
      'alignment_parameter':0.0,
      'thresholds_in_v0_units':th,
      'thresholds_in_ell_over_tau_units':{
         k:val/sqrt(5) for k,val in th.items() if 'speed' in k},
      'runs':dop,'solver_comparisons':comparisons,
      'local_threshold_controls':boundary_controls,
      'not_derived':['physical ell','physical tau','a physical contact-arrow operator',
                     'relativistic dynamics','electron identification',
                     'photon/recombination channels','complex scattering amplitudes']}
    print(json.dumps(result,indent=2))

if __name__=='__main__':
    main()
