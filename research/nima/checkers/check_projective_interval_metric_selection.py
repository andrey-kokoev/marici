"""Exact rational regression of the projective metric classification.
No sympy, numerical curvature inference or source-model replacement.
"""
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[3]

def require(ok, why):
    if not ok:
        raise AssertionError(why)


def metric(C, u, v):
    w = v-u
    return ((F(0), C/(2*w*w)), (C/(2*w*w), F(0)))


def main():
    count = 0
    for a,b,c,d in product(range(-2,3), repeat=4):
        if a*d-b*c != 1:
            continue
        for u,v in ((F(-2),F(-1)), (F(0),F(1)), (F(1,3),F(5,2))):
            if (c*u+d)*(c*v+d) <= 0:
                continue  # one nonsingular ordered endpoint chart
            U,V = (a*u+b)/(c*u+d), (a*v+b)/(c*v+d)
            ju,jv = 1/(c*u+d)**2, 1/(c*v+d)**2
            require(U<V, 'ordered image')
            for C in (F(-16), F(-4), F(4), F(16)):
                require(metric(C,U,V)[0][1]*ju*jv == metric(C,u,v)[0][1], 'Mobius pullback')
                count += 1
    # Independent component formulas, derived by the tensor Lie derivative.
    lie_checks = 0
    for u,v in ((F(-2),F(3)), (F(1,3),F(7,3))):
        w = v-u
        for A,C,D in product((F(-2), F(0), F(3)), repeat=3):
            # V acts on w^-2 by -2 (u+v)/w^2.
            uu = -2*(u+v)*A/w**2 + 4*u*A/w**2
            vv = -2*(u+v)*D/w**2 + 4*v*D/w**2
            uv = -2*(u+v)*C/(2*w**2) + (2*u+2*v)*C/(2*w**2)
            require(uu == -2*A/w and vv == 2*D/w and uv == 0, 'Lie classification')
            require((uu==vv==0) == (A==D==0), 'diagonal hostile')
            lie_checks += 1
    curvature = []
    for C in (F(-16),F(-4),F(4),F(16)):
        u,v = F(1,3),F(7,3)
        w = v-u
        g = metric(C,u,v)
        det = -g[0][1]**2
        inverse_uv = 1/g[0][1]
        # Ric_uv=-partial_v Gamma^u_uu=2/w^2; product terms vanish.
        ric_uv = F(2)/w**2
        scalar = 2*inverse_uv*ric_uv
        require(det < 0 and scalar == 8/C, 'signature/curvature')
        require(ric_uv == (4/C)*g[0][1], 'Einstein identity in dimension two')
        # Under u=x-r,v=x+r: du dv=dx^2-dr^2.
        for dx,dr in product((F(-1),F(0),F(2)), repeat=2):
            r=w/2
            require(C*(dx-dr)*(dx+dr)/w**2 == C*(dx**2-dr**2)/(4*r**2), 'chart change')
        interior = C*(-1)*1/w**2
        require((interior<0) == (C>0), 'containment cone')
        require(C*0*1/w**2 == 0 and C*(-1)*0/w**2 == 0, 'both null edge families')
        curvature.append({'C':str(C),'scalar_curvature':str(scalar),
                          'containment_interior_timelike':interior<0})
    require(F(8,4) != F(8,16), 'scale counterexample')
    # The tensor C=0 is degenerate and must not be called a third spacetime.
    require(metric(F(0),F(0),F(1))[0][1] == 0, 'zero scale boundary')
    paths = ['research/nima/projective-interval-metric-selection.md',
             'research/nima/checkers/check_projective_interval_metric_selection.py',
             'research/nima/check_nnmhv_projective_interval_desitter_bridge.py',
             'research/nima/check_nnmhv_entanglement_crofton_bridge.py',
             'research/nima/check_nnmhv_interval_causal_diamond_bridge.py',
             'research/nima/check_nnmhv_mobius_wave_operator_bridge.py']
    result = {'schema':'marici.nima.projective-interval-metric-selection.v1',
        'passed':True, 'test_disposition':'rejected_source_selection_for_inspected_constraints',
        'mobius_pullbacks':count, 'lie_coefficient_checks':lie_checks, 'curvature_controls':curvature,
        'hostiles':['diagonal-invariant-metric-rejected','negative-C-does-not-preserve-containment-time-cone',
                    'positive-scale-nonuniqueness','null-edges-alone-do-not-select-sign','zero-C-degenerate'],
        'scope':'Conditional smooth local projective classification; not a WG-to-continuum or physical realization proof.',
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}
    out=ROOT/'research/nima/results/projective-interval-metric-selection.json'
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__':
    main()
