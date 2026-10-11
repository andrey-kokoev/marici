"""Exact local harmonic/first-anharmonic audit, not a full cosine spectrum.
Run: uv run --with sympy python THIS_FILE
"""
from pathlib import Path
from hashlib import sha256
import json
import sympy as s

BASE=Path(__file__).resolve().parents[1]


def main():
    raw=(BASE/'results/spinor_hard_flux_parent.json').read_bytes()
    assert json.loads(raw)['verification_passed']
    c=s.Matrix([[0,0,0,1,-1,1],[0,-1,1,0,0,-1],
                [1,0,-1,0,1,0],[-1,1,0,-1,0,0]])
    pc=c.T*c/4
    assert pc*pc==pc and pc.rank()==3
    assert c*c.T==4*s.eye(4)-s.ones(4)
    assert all(pc[i,i]==s.Rational(1,2) for i in range(6))
    beta,kappa,hbar,eps=s.symbols('beta kappa hbar eps',positive=True)
    omega=2*s.sqrt(beta*kappa)
    position=hbar*s.sqrt(beta/kappa)/4
    momentum=hbar*s.sqrt(kappa/beta)
    assert s.simplify(position*momentum-hbar**2/4)==0
    covariance=position*pc
    face_cov=s.simplify(c*covariance*c.T)
    assert all(s.simplify(face_cov[i,i]-3*position)==0 for i in range(4))
    zpe=3*hbar*omega/2
    electric=3*beta*momentum/2
    assert s.simplify(electric-zpe/2)==0
    quartic=s.simplify(-kappa*sum(3*face_cov[i,i]**2 for i in range(4))/24)
    assert quartic==-9*beta*hbar**2/32
    # Gaussian Wilson expectation and edge hopping suppression, frozen matter.
    wilson=s.exp(-3*position/2)
    hopping=s.exp(-position/4)
    bound=9*hbar**2*beta/(16*eps**4)
    assert s.simplify((3*position).subs(kappa,bound)-eps**2)==0
    assert s.simplify(zpe.subs(kappa,bound)-9*hbar**2*beta/(4*eps**2))==0
    rows=[]
    for kval in (1,100,10000):
        sub={beta:s.Rational(3,5),hbar:1,kappa:kval}
        rows.append({'kappa':kval,'harmonic_face_rms':float(s.sqrt(3*position).subs(sub)),
                     'harmonic_zero_point_energy':float(zpe.subs(sub)),
                     'gaussian_relative_Wilson_expectation':float(wilson.subs(sub)),
                     'gaussian_hopping_factor':float(hopping.subs(sub))})
    report={'verification_passed':True,'parent_result_sha256':sha256(raw).hexdigest(),
            'scope':'Local normal-mode harmonic identities and first-order cosine quartic correction. Not a rigorous global strong-coupling convergence bound.',
            'cycle_modes':3,'frequency':str(omega),'mode_position_variance':str(position),
            'mode_momentum_variance':str(momentum),'face_variance':str(3*position),
            'zero_point_energy':str(zpe),'first_quartic_energy_shift':str(quartic),
            'rms_target_stiffness_in_harmonic_model':str(bound),
            'rms_target_zero_point_cost_in_harmonic_model':str(9*hbar**2*beta/(4*eps**2)),
            'fixtures':rows,'exact_flux_at_finite_stiffness':False,
            'limiting_obligations':['Subtract the diverging cycle vacuum energy with a declared common reference','Account for finite anharmonic shift and matter-induced corrections','Control compact global identifications, Gauss reduction and remainder estimates'],
            'next_gate':'Specify a structurally constrained quantum constructor that removes independent cycle modes, or provide a controlled approximation with declared tolerances. Finite cosine stiffness is not an exact implementation.'}
    (BASE/'results/spinor_stiff_flux_limit.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
