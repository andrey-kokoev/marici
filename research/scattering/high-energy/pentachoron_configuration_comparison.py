"""Nearest-admissible, retained-vertex comparison for a pentachoron pair.

NEW CONDITIONAL MODEL, NOT AN ELECTRON/POSITRON SCATTERING THEORY.

Retained input: the five labelled vertices of the regular 4-simplex used in
marici/research/voevodsky/electron-pentachoron-attachment.md.
New postulates: mirrored head-on pair; only its 3D projection excludes overlap;
contact energy equals E_* times the minimum squared labelled-vertex displacement
to a non-overlapping pair, with translations and common internal rotation allowed.
This is a nonlinear geometric comparison, NOT the native spinor defect operator.
Neither quantum amplitudes nor a physical speed/length scale are supplied.

All lengths below are in ell units, energy in E_* units. For simulations m=1,
I=8/5, and time is ell*sqrt(m/E_*); speed is sqrt(E_*/m), NOT c.
No alignment potential is added.

Run with Python 3: python pentachoron_configuration_comparison.py
Dependencies: numpy, scipy, sympy. Default writes a JSON receipt beside this file.
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
import argparse
import hashlib
import json
from math import sin, cos, sqrt, atan, atan2, acos, pi
from pathlib import Path
import time
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import minimize_scalar, linprog
from scipy.spatial import ConvexHull

H = 1/sqrt(5)
DC = atan(H)
I_BODY = 8/5
BRANCHES = ((-pi, -pi/2, -1., -H),
            (-pi/2, DC, 1., -H),
            (DC, pi-DC, 0., 4*H),
            (pi-DC, pi, -1., -H))
RAW = np.array([[1,1,1,0],[1,-1,-1,0],[-1,1,-1,0],[-1,-1,1,0],
                [0,0,0,sqrt(5)]], dtype=float)
Q = RAW-RAW.mean(axis=0)


def wrap(x: float) -> float:
    return (x+pi) % (2*pi)-pi


def support(x: float) -> float:
    return max(abs(cos(x))-H*sin(x), 4*H*sin(x))


def pair_vertices(distance: float, angle: float) -> np.ndarray:
    """Both full 4D vertex arrays, mirrored across the spatial midplane."""
    c,s=cos(angle),sin(angle)
    R=np.array([[c,0,0,s],[0,1,0,0],[0,0,1,0],[-s,0,0,c]])
    left=Q@R.T
    right=left.copy(); right[:,0]*=-1
    left[:,0]-=distance/2; right[:,0]+=distance/2
    return np.stack([left,right])


@dataclass
class Comparison:
    energy: float
    corrected_angle: float
    corrected_distance: float
    separating_force: float
    per_body_torque: float
    stationarity_or_cusp_residual: float


def cost(distance: float, angle: float, target: float) -> float:
    dq=max(0.,2*support(target)-distance)
    return 2.5*dq*dq+32*(1-cos(target-angle))


def compare(distance: float, angle: float) -> Comparison:
    """Global minimization on the angle circle by enumerating branch candidates.

    The finite candidate list includes all real stationary quartic roots in
    overlap branches, branch endpoints, zero-overlap roots, and stationary
    points of the pure angular cost. A cost bound skips distant branches.
    Labels are retained, not quotiented by an unrecorded vertex permutation.
    """
    if not np.isfinite(distance+angle) or distance < 0:
        raise ValueError('Finite angle and nonnegative center distance required.')
    delta=wrap(angle)
    if distance >= 2*support(delta):
        return Comparison(0.,angle,distance,0.,0.,0.)
    best_theta=delta
    best_cost=cost(distance,delta,delta)
    def consider(theta: float):
        nonlocal best_theta,best_cost
        f=cost(distance,delta,theta)
        if f<best_cost:
            best_cost,best_theta=f,theta
    for lo,hi,A,B in BRANCHES:
        # Minimum angular cost on this branch is a rigorous branch lower bound.
        near=[lo,hi]
        if lo<=delta<=hi: near.append(delta)
        lower=min(32*(1-cos(t-delta)) for t in near)
        if lower>best_cost+1e-12: continue
        consider(lo); consider(hi)
        # f' = S2 sin(2t)+C2 cos(2t)+S1 sin(t)+C1 cos(t)
        S2=10*(B*B-A*A); C2=20*A*B
        S1=10*distance*A+32*cos(delta)
        C1=-10*distance*B-32*sin(delta)
        poly=np.array([C2-C1, -4*S2+2*S1, -6*C2,
                       4*S2+2*S1, C2+C1])
        for root in np.roots(poly):
            if abs(root.imag)<2e-7:
                theta=2*atan(float(root.real))
                if lo-1e-10<=theta<=hi+1e-10:
                    if 2*(A*cos(theta)+B*sin(theta))-distance >= -1e-9:
                        consider(theta)
        radius=sqrt(A*A+B*B)
        if distance<=2*radius:
            phase=atan2(B,A); offset=acos(min(1.,distance/(2*radius)))
            for theta in (wrap(phase-offset),wrap(phase+offset)):
                if lo-1e-10<=theta<=hi+1e-10: consider(theta)
        for theta in (delta,wrap(delta+pi)):
            if lo<=theta<=hi: consider(theta)
    theta=best_theta
    dq=max(0.,2*support(theta)-distance)
    force=5*dq
    torque=16*sin(theta-delta)
    residuals=[]
    # At a cusp the derivative interval must contain zero.
    for lo,hi,A,B in BRANCHES:
        if lo-1e-9<=theta<=hi+1e-9:
            ap=-A*sin(theta)+B*cos(theta)
            residuals.append(10*dq*ap+32*sin(theta-delta))
    if residuals and min(residuals)<=0<=max(residuals):
        residual=0.
    else:
        residual=min(map(abs,residuals), default=0.)
    theta_unwrapped=angle+wrap(theta-delta)
    return Comparison(float(best_cost),float(theta_unwrapped),
                      float(max(distance,2*support(theta))),float(force),
                      float(torque),float(residual))


def independent_minimum(distance: float, angle: float) -> float:
    """Independent dense-bracketing + bounded minimization control."""
    grid=np.linspace(-pi,pi,4097)
    vals=np.array([cost(distance,angle,float(x)) for x in grid])
    candidates=[float(vals.min())]
    for k in np.flatnonzero((vals[1:-1]<=vals[:-2]) & (vals[1:-1]<=vals[2:]))+1:
        r=minimize_scalar(lambda x:cost(distance,angle,x), bounds=(grid[k-1],grid[k+1]),
                          method='bounded', options={'xatol':1e-14})
        candidates.append(float(r.fun))
    for x in [-pi,-pi/2,DC,pi-DC,pi]: candidates.append(cost(distance,angle,x))
    return min(candidates)


def intersection_margin(distance: float, angle: float, lateral: float=0.) -> float:
    """3D hull feasibility control using all five projected vertices per body.

    Maximizes the common inscribed-ball radius. Positive means common interior;
    zero is touching; negative means separated. No support-overlap formula is used.
    """
    pair=pair_vertices(distance,angle)[:,:,:3].copy()
    pair[1,:,1]+=lateral
    inequalities=[]
    for body in pair:
        hull=ConvexHull(body)
        inequalities.extend(hull.equations)
    eq=np.asarray(inequalities)
    A=np.column_stack([eq[:,:3],np.linalg.norm(eq[:,:3],axis=1)])
    r=linprog([0,0,0,-1],A_ub=A,b_ub=-eq[:,3],bounds=[(None,None)]*4,method='highs')
    if not r.success: raise RuntimeError(r.message)
    return float(r.x[3])


def verify() -> dict:
    """Exact geometric coefficients plus independent numerical controls."""
    import sympy as sp
    l,d,t=sp.symbols('ell d t', real=True)
    centered=sp.Matrix([[1,1,1,-1/sp.sqrt(5)], [1,-1,-1,-1/sp.sqrt(5)],
                       [-1,1,-1,-1/sp.sqrt(5)],[-1,-1,1,-1/sp.sqrt(5)],
                       [0,0,0,4/sp.sqrt(5)]])
    assert centered.T*centered==4*sp.eye(4)
    R=sp.Matrix([[sp.cos(t),0,0,sp.sin(t)],[0,1,0,0],[0,0,1,0],
                 [-sp.sin(t),0,0,sp.cos(t)]])
    displacement=l*(centered*R.T-centered)
    displacement[:,0]+=sp.ones(5,1)*d/2
    twice=sp.trigsimp(2*sum(z*z for z in displacement))
    expected=sp.Rational(5,2)*d*d+32*l*l*(1-sp.cos(t))
    assert sp.trigsimp(twice-expected)==0
    # Small-penetration projection in the induced vertex metric.
    q,u,e=sp.symbols('q u e', real=True)
    objective=sp.Rational(5,2)*(q-2*l/sp.sqrt(5)*e)**2+16*l*l*e*e
    e_star=sp.solve(sp.diff(objective,e),e)[0]
    localcost=sp.simplify(objective.subs(e,e_star))
    assert localcost==sp.Rational(20,9)*q*q
    assert sp.simplify(e_star-sp.sqrt(5)*q/(18*l))==0
    rng=np.random.default_rng(51403)
    vertex_errors=[]
    for _ in range(30):
        distance,target_d=rng.uniform(.4,3.8,2)
        angle,target_a=rng.uniform(-pi,pi,2)
        actual=np.sum((pair_vertices(target_d,target_a)-pair_vertices(distance,angle))**2)
        formula=2.5*(target_d-distance)**2+32*(1-cos(target_a-angle))
        vertex_errors.append(abs(actual-formula))
    hull_cases=[]
    for angle in [0.,.2,DC,.6,1.,-pi/2,2.5]:
        for offset in [-.03,0.,.03]:
            distance=2*support(angle)+offset
            margin=intersection_margin(distance,angle)
            expected_sign=-np.sign(offset)
            if expected_sign==0: assert abs(margin)<1e-8
            else: assert expected_sign*margin>1e-5
            hull_cases.append({'angle':angle,'distance_offset':offset,'margin':margin})
    # The exact head-on criterion must not be extended to transverse offsets.
    lateral_margin=intersection_margin(1.9,0.,lateral=4.)
    assert 2*support(0.)-1.9>0 and lateral_margin<0
    global_errors=[]; stationarity=[]; gradient_errors=[]; recovery_errors=[]
    fixtures=[(1.9,0.),(1.5,0.),(1.,.2),(1.2,DC),(2.,1.)]
    fixtures.extend((float(rng.uniform(.05,3.6)),float(rng.uniform(-pi,pi))) for _ in range(35))
    for distance,angle in fixtures:
        out=compare(distance,angle)
        independent=independent_minimum(distance,angle)
        global_errors.append(abs(out.energy-independent))
        stationarity.append(out.stationarity_or_cusp_residual)
        original=pair_vertices(distance,angle)
        target=pair_vertices(out.corrected_distance,out.corrected_angle)
        residual=original-target
        recovery_errors.append(float(np.max(np.abs((target+residual)-original))))
        assert abs(np.sum(residual**2)-out.energy)<2e-9
        if out.energy>1e-6:
            h=2e-6
            dD=(compare(distance+h,angle).energy-compare(distance-h,angle).energy)/(2*h)
            dt=(compare(distance,angle+h).energy-compare(distance,angle-h).energy)/(2*h)
            gradient_errors.extend([abs(dD+out.separating_force),abs(dt+2*out.per_body_torque)])
    assert max(global_errors)<2e-7, max(global_errors)
    assert max(vertex_errors)<1e-10
    assert max(gradient_errors)<2e-6, max(gradient_errors)
    small=[]
    for qn in [.01,.001,.0001]:
        out=compare(2-qn,0.)
        small.append({'penetration':qn,'energy_over_q_squared':out.energy/qn**2,
                      'force_over_q':out.separating_force/qn,
                      'correction_angle_over_q':out.corrected_angle/qn})
    return {'exact_pair_displacement_cost':str(expected),
            'exact_initial_energy_coefficient':'20/9',
            'exact_initial_force_coefficient':'40/9',
            'exact_initial_rotation_correction':'sqrt(5) q/(18 ell) + O(q^2/ell^2)',
            'max_vertex_formula_error':max(vertex_errors),
            'max_global_minimum_control_error':max(global_errors),
            'max_gradient_control_error':max(gradient_errors),
            'max_stationarity_or_cusp_residual':max(stationarity),
            'max_record_recovery_error':max(recovery_errors),
            'hull_checks':hull_cases,
            'off_axis_negative_control':{'support_penetration':.1,'actual_intersection_margin':lateral_margin},
            'small_penetration_limit':small,
            'no_exclusion_control':'Without the non-overlap constraint, target=current gives zero cost for every pair.'}


def simulate(speed: float, method: str='DOP853', max_step: float=.012) -> dict:
    if speed<=0: raise ValueError('Positive incoming speed is required.')
    def rhs(t,y):
        D,p,delta,j=y
        c=compare(D,delta)
        return [2*p,c.separating_force,j/I_BODY,c.per_body_torque]
    def contact(t,y): return 2*support(y[2])-y[0]
    def exposure(t,y): return y[2]-DC
    def escape(t,y): return y[0]-8*H-1e-4
    escape.direction=1; escape.terminal=True
    def crossing(t,y): return y[0]-.00001
    crossing.direction=-1; crossing.terminal=True
    sol=solve_ivp(rhs,(0,30),[2.,-speed,0.,0.],method=method,
                  rtol=2e-10,atol=2e-12,max_step=max_step,dense_output=True,
                  events=[contact,exposure,escape,crossing])
    if not sol.success or len(sol.t_events[3]):
        raise RuntimeError('Solution left the positive-distance head-on chart.')
    if not len(sol.t_events[2]): raise RuntimeError('No final escape in integration window.')
    samples=sol.sol(np.linspace(0,sol.t[-1],1200))
    energies=np.array([p*p+j*j/I_BODY+compare(D,de).energy for D,p,de,j in samples.T])
    drift=float(np.max(np.abs(energies-speed*speed))/(speed*speed))
    if drift>2e-7: raise RuntimeError(f'Energy drift too large: {drift}')
    return {'incident_speed':speed,'speed_unit':'sqrt(E_*/m)',
            'contact_boundary_times':sol.t_events[0].tolist(),
            'exposure_times':sol.t_events[1].tolist(),
            'relative_energy_drift':drift,'final_escape_time':float(sol.t[-1]),
            'smallest_center_distance':float(np.min(samples[0])),
            'largest_rotation':float(np.max(samples[2])),
            'force_at_first_exposure':(compare(*sol.sol(sol.t_events[1][0])[[0,2]]).separating_force
                                      if len(sol.t_events[1]) else None)}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--quick',action='store_true',help='Exact/static checks only.')
    parser.add_argument('--speeds',nargs='*',type=float,default=[.7*sqrt(2),.9*sqrt(2),1.2*sqrt(2)])
    args=parser.parse_args()
    started=time.monotonic()
    result={'status':'New conditional geometric comparison; not native spinor dynamics or physical scattering.',
            'geometry_source':'andrey-kokoev/marici/research/voevodsky/electron-pentachoron-attachment.md',
            'geometry_blob_sha':'68bd9714ad40b5ebc0512ab69f7de873714014a2',
            'new_assumptions':['Symmetric mirrored 3D projected contact, common x-w rotation.',
                               'Contact energy = E_*/ell^2 times least squared labelled-vertex correction.',
                               'Non-overlap is the declared admissibility constraint.',
                               'The closest target configuration is a variational comparator, not an actual second state.'],
            'not_derived':['choice of exclusion law','microscopic complex/quantum arrows',
                           'physical E_*, ell or clock','positron transformation','relativistic motion',
                           'recombination/output particles','scattering amplitudes'],
            'checks':verify()}
    result['static_examples']=[{'distance':D,'angle':a,**asdict(compare(D,a))} for D,a in
                               [(2.,0.),(1.99,0.),(1.9,0.),(1.7,0.),(1.5,.2),(1.3,DC),(1.3,.5)]]
    if not args.quick:
        result['runs']=[simulate(v) for v in args.speeds]
        controls=[]
        for run in result['runs']:
            independent=simulate(run['incident_speed'], method='RK45', max_step=.006)
            a=np.array(run['contact_boundary_times'])
            b=np.array(independent['contact_boundary_times'])
            if a.shape!=b.shape: raise RuntimeError('Contact count disagreement.')
            error=float(np.max(np.abs(a-b)))
            if error>2e-6: raise RuntimeError('Contact timing disagreement.')
            run['speed_in_previous_v0_units']=run['incident_speed']/sqrt(2)
            run['time_unit']='ell sqrt(m/E_*) = sqrt(2) times previous t0'
            controls.append({'speed':run['incident_speed'],
                             'max_contact_time_difference':error,
                             'RK45_relative_energy_drift':independent['relative_energy_drift']})
        result['independent_solver_controls']=controls
    result['runtime_seconds']=time.monotonic()-started
    path=Path(__file__).with_name('pentachoron_configuration_comparison_results.json')
    result['script_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__': main()
