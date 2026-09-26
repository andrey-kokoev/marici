"""Conditional HJ endpoint/phase transport; retain the actual Clifford word data.
Not a derivation of a source Hamiltonian, clock, or source-to-trajectory map.
"""
from itertools import product
from pathlib import Path
import hashlib
import json
import sympy as s
import check_clifford_retained_order as clifford

OWNER = Path(__file__).resolve().parents[1]


def main():
    q, q0, p, t = s.symbols('q q0 p t', real=True)
    m, hbar = s.symbols('m hbar', positive=True)
    S = s.Function('S')(q, t)
    chi = s.Function('chi')(q, t)
    H = s.Function('H')
    shifted = S + hbar*chi
    # Transport a local action branch AND its momentum/energy frame.
    before = s.diff(S,t) + H(q,s.diff(S,q),t)
    after = (s.diff(shifted,t) - hbar*s.diff(chi,t)
             + H(q,s.expand(s.diff(shifted,q)-hbar*s.diff(chi,q)),t))
    assert s.simplify(after-before) == 0
    # A Hamiltonian characteristic carries action phase at L/hbar.
    Hqp = H(q,p,t)
    assert s.expand((-Hqp+p*s.diff(Hqp,p))/hbar
                    -(p*s.diff(Hqp,p)-Hqp)/hbar) == 0

    # Independent classical benchmark, t != 0: fixed initial position q0.
    principal = m*(q-q0)**2/(2*t)
    residual = lambda f: s.simplify(s.diff(f,t)+s.diff(f,q)**2/(2*m))
    assert residual(principal) == 0
    assert residual(principal+s.pi*hbar) == 0
    assert s.exp(s.I*s.pi) == -1
    # Endpoint-dependent rephasing is not free at a fixed Hamiltonian.
    a,b = s.symbols('a b', real=True)
    shifted_principal = principal+hbar*(a*q+b*t)
    false_fixed_H_residual = residual(shifted_principal)
    assert false_fixed_H_residual != 0
    transported = (s.diff(shifted_principal,t)-hbar*b
                   +(s.diff(shifted_principal,q)-hbar*a)**2/(2*m))
    assert s.simplify(transported) == 0

    grades = tuple(product((0,1),repeat=2))
    xor = lambda g,h: (g[0]^h[0],g[1]^h[1])
    log_bit = lambda g,h: g[1]*h[0]
    def carry(g,h,k):
        defect = (log_bit(g,h)+log_bit(xor(g,h),k)
                  -log_bit(h,k)-log_bit(g,xor(h,k)))
        assert defect % 2 == 0
        return defect//2
    carries = {carry(g,h,k) for g,h,k in product(grades,repeat=3)}
    assert carries == {-1,0,1}
    for g,h,k,l in product(grades,repeat=4):
        assert (carry(h,k,l)-carry(xor(g,h),k,l)+carry(g,xor(h,k),l)
                -carry(g,h,xor(k,l))+carry(g,h,k)) == 0
    L,R = (1,0),(0,1)
    assert carry(R,L,L) == 1  # two parenthesizations differ by 2*pi in raw logs

    # Do not replace the matrix lift with a scalar multiplicative selector.
    multiplicative_sections = 0
    for signs in product((1,-1),repeat=4):
        section = {g:(sign,*g) for g,sign in zip(grades,signs)}
        if all(clifford.normal_product(section[g],section[h]) == section[xor(g,h)]
               for g,h in product(grades,repeat=2)):
            multiplicative_sections += 1
    assert multiplicative_sections == 0
    assert clifford.evaluate((1,2)) == (1,1,1)
    assert clifford.evaluate((2,1)) == (-1,1,1)
    assert clifford.evaluate(()) == clifford.evaluate((1,1))
    assert () != (1,1)

    # A presentation-dependent real phase unwrap can use full word counts.
    # It is NOT a physical action or a clock, and is not a faithful history code.
    def inversions(w):
        return sum(w[i] == 2 and w[j] == 1 for i in range(len(w)) for j in range(i+1,len(w)))
    words = [w for n in range(7) for w in product((1,2),repeat=n)]
    for w in words:
        expected = ((-1)**inversions(w), w.count(1)%2, w.count(2)%2)
        assert clifford.evaluate(w) == expected
    short = [w for w in words if len(w) <= 3]
    for u,v in product(short,repeat=2):
        assert inversions(u+v) == inversions(u)+inversions(v)+u.count(2)*v.count(1)
    assert inversions((2,1,1)) == 2

    result = {
        'schema':'marici.nima.retained-hamilton-jacobi.v1',
        'classification':'constant_lift_phases_leave_local_hj_unchanged_and_require_comparison_and_log_branch_data',
        'obligations':['attachment_transport','readout_descent'],
        'symbolic_checks':['general_endpoint_phase_frame_covariance','characteristic_action_phase',
                           'free_particle_principal_action','constant_pi_phase_shift',
                           'fixed_H_rephasing_hostile','transported_H_rephasing_control'],
        'finite_controls':{'cocycle_log_triples':64,'integer_carry_four_tuples':256,
                           'multiplicative_sections':multiplicative_sections,
                           'retained_words':len(words),'concatenation_pairs':len(short)**2},
        'log_carry_values':sorted(carries),
        'scope':'Symbolic smooth local HJ identities and exact finite Clifford word checks. Classical H, reference t, hbar, and any interpretation of source comparisons as action-branch comparisons remain explicit inputs. No full native higher-witness realization, physical Hamiltonian, clock, amplitude law, or quantum HJ correction is derived.',
        'input_sha256':{str(path.relative_to(OWNER)):hashlib.sha256(path.read_bytes()).hexdigest()
                        for path in (Path(__file__),Path(clifford.__file__),OWNER/'phase-selection-from-coherence.md')}
    }
    (OWNER/'results/retained-hamilton-jacobi.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
