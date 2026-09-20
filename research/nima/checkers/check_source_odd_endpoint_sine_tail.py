"""Exact source odd-endpoint coefficients; Schur algebra checked separately.
No identification of a model bulk matrix with the Weil operator is made.
"""
import json
from pathlib import Path
import sympy as s


def z(e):
    return s.simplify(s.expand_trig(e))==0


def main():
    x=s.symbols('x',real=True)
    L=s.symbols('L',positive=True)
    n=s.symbols('n',integer=True,positive=True)
    a=s.Rational(1,2)
    beta=s.pi*n/L
    primitive=(a*s.cosh(a*x)*s.sin(beta*x)-beta*s.sinh(a*x)*s.cos(beta*x))/(a*a+beta*beta)
    coefficient=(-1)**(n+1)*2*s.sqrt(2)*beta*s.sinh(L/2)/(s.sqrt(L)*(s.Rational(1,4)+beta*beta))
    observed=s.sqrt(2)/s.sqrt(L)*(primitive.subs(x,L)-primitive.subs(x,-L))
    t=s.symbols('t',positive=True)
    gap=s.factor(1/t**2-t**2/(a*a+t*t)**2)
    # A polynomial-in-frequency identity for any real wavepacket envelope.
    R,g,gp=s.symbols('R g gp',real=True)
    derivative_square=s.expand((gp+s.I*R*g)*(gp-s.I*R*g))
    # Independent finite fixture verifies the block inverse formula only.
    C=s.Matrix([[3,1,1],[1,2,0],[1,0,2]])
    b=s.Matrix([1,2,3])
    A=C[:1,:1]; B=C[1:,:1]; D=C[1:,1:]
    low=b[:1,:]; tail=b[1:,:]
    schur=A-B.T*D.inv()*B
    effective=low-B.T*D.inv()*tail
    split=(tail.T*D.inv()*tail+effective.T*schur.inv()*effective)[0]
    naive=(low.T*A.inv()*low+tail.T*D.inv()*tail)[0]
    checks={
        'endpoint_antiderivative':z(s.diff(primitive,x)-s.sinh(x/2)*s.sin(beta*x)),
        'all_integer_mode_coefficients':z(observed-coefficient),
        'coefficient_bound_positive_gap':z(gap-a*a*(a*a+2*t*t)/(t*t*(a*a+t*t)**2)),
        'exact_modulated_dirichlet_energy_density':z(derivative_square-(gp*gp+R*R*g*g)),
        'coupled_leverage_block_identity':z(split-(b.T*C.inv()*b)[0]),
        'dropping_bulk_cross_block_changes_leverage':not z(split-naive),
    }
    assert all(checks.values()),checks
    result={
        'schema':'marici.nima.source-odd-endpoint-sine-tail.v1',
        'strength':'exact_endpoint_coordinate_and_conditional_tail_bound',
        'checks':checks,
        'source_vector':'b_L(x)=(exp(x/2)-exp(-x/2))/sqrt(2)',
        'basis':'e_n(x)=sin(n*pi*x/L)/sqrt(L), n>=1, odd subspace',
        'coefficient':'(-1)^(n+1)*2*sqrt(2)*(n*pi/L)*sinh(L/2)/(sqrt(L)*(1/4+(n*pi/L)^2))',
        'squared_tail_bound':'sum_{n>N}|b_n|^2 <= 8*L*sinh(L/2)^2/(pi^2*N), N>=1',
        'conditional_tail_leverage':'if high block D>=c_N I, then b_tail^*D^-1 b_tail <= 8*L*sinh(L/2)^2/(pi^2*N*c_N)',
        'fixture_coupled_leverage':str(split),
        'fixture_uncoupled_leverage':str(naive),
        'fixture_is_source_weil_matrix':False,
        'physical_schur_gate_proved':False,
        'missing_inputs':['certified high-block source bound c_N','actual low-high coupling B','corrected finite Schur block'],
    }
    out=Path(__file__).resolve().parents[1]/'results/source-odd-endpoint-sine-tail.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
