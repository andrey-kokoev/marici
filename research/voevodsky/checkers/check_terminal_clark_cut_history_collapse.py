"""Exact terminal collapse of the native affine Clark prime-cut receiver."""
from pathlib import Path
from itertools import permutations
import importlib.util
import json
import sympy as sp

ROOT=Path(__file__).resolve().parents[3]
spec=importlib.util.spec_from_file_location('window_adapter',ROOT/'research/voevodsky/checkers/check_arithmetic_window_signature_adapter.py')
adapter=importlib.util.module_from_spec(spec)
spec.loader.exec_module(adapter)


def main():
    L,M,a=sp.symbols('L M a',real=True)
    def jet(length,degree):
        return sp.Matrix(degree+1,degree+1,lambda j,k:sp.binomial(j,k)*length**(j-k) if j>=k else 0)
    checks={}
    for degree in range(1,7):
        assert sp.simplify(jet(L,degree)*jet(M,degree)-jet(L+M,degree))==sp.zeros(degree+1)
        assert sp.simplify(jet(L,degree)*jet(-L,degree))==sp.eye(degree+1)
        checks[f'moment_order_{degree}_additive_transport']=True
    clark=sp.Matrix([[1,-a]])
    assert clark*jet(L,1)==sp.Matrix([[1-a*L,-a]])
    # Common phase exp(i z L) multiplies the jet matrix; it too composes
    # additively and cancels in a same-terminal comparison.
    relative=sp.simplify((jet(L,2)*jet(M,2)).inv()*jet(M,2)*jet(L,2))
    assert relative==sp.eye(3)
    assert (relative-sp.eye(3))**2==sp.zeros(3)

    routes=list(permutations(adapter.PRIMES))
    one=sp.ones(15,1)
    stage_matrices=[]
    for word in routes:
        n=2
        rows=[]
        for prime in word:
            windows=adapter.event_window(n,prime)
            rows.append([int(i in windows) for i in range(15)])
            n*=prime
        P=sp.Matrix(rows)
        assert n==420 and P.T*sp.ones(4,1)==one
        # Coefficient of any arbitrary shell-pair kernel Q_ij after sewing
        # all event pairs is (P^T 1)(P^T 1)^T, independent of the route.
        coefficients=(P.T*sp.ones(4,1))*(P.T*sp.ones(4,1)).T
        assert coefficients==sp.ones(15,15)
        stage_matrices.append(P)
    assert stage_matrices[0]!=stage_matrices[1]
    # Exact terminal coefficient map has rank one; every zero-mass route
    # combination is invisible, including all six recorded parity modes.
    terminal=sp.ones(15,24)
    prior=json.loads((ROOT/'research/voevodsky/results/theta-hidden-channel-transport.json').read_text())
    parity=sp.Matrix(prior['parity_basis_K']).applyfunc(sp.Rational)
    assert terminal.rank()==1 and terminal*parity==sp.zeros(15,6)
    result={
        'schema':'marici.voevodsky.terminal-clark-cut-history-collapse.v1',
        'passed':True,
        'checks':checks,
        'clark_origin_row':'(1,-a) T_L=(1-a L,-a)',
        'same_terminal_jet_comparison':'identity',
        'route_window_checks':24,
        'all_cross_shell_coefficients_retained':True,
        'terminal_coefficient_rank':1,
        'parity_kernel_dimension_in_test':6,
        'relative_history_d_image':'0',
        'relative_history_d_squared_image':'0',
        'L_for_this_terminal_factoring_candidate':'0',
        'stage_resolved_records_distinct':True,
        'scope':'Exact additive origin transport and full sewn window comparison. The zero L applies to this terminal-factoring receiver, not to every possible labelled or multipoint Clark extension.',
    }
    out=ROOT/'research/voevodsky/results/terminal-clark-cut-history-collapse.json'
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
