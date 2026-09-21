"""Exact cross-grade and adjoint requirements on the arithmetic Jordan algebra."""
from pathlib import Path
import json
import sympy as sp

ROOT = Path(__file__).resolve().parents[3]


def main():
    a,L,h = sp.symbols('a L h', real=True)
    U = sp.Matrix([[1,0,0],[1,1,0],[0,1,1]])
    # B=C[d]/d^3; r=1+d. Its required adjoint r^*=r^-1 gives
    # d^*=-d+d^2 and (d^2)^*=d^2.
    star = sp.Matrix([[1,0,0],[0,-1,0],[0,1,1]])
    assert star**2 == sp.eye(3)
    def multiply(x,y):
        return sp.Matrix([sum(x[i]*y[n-i] for i in range(n+1)) for n in range(3)])
    basis = [sp.eye(3)[:,i] for i in range(3)]
    adjoint = lambda x: star*x.conjugate()
    r = sp.Matrix([1,1,0])
    assert multiply(adjoint(r),r) == basis[0]
    for x in basis:
        for y in basis:
            assert adjoint(multiply(x,y)) == multiply(adjoint(y),adjoint(x))
    functional = sp.Matrix([[a,L/2+sp.I*h,L]])
    Q = sp.Matrix(3,3,lambda i,j:(functional*multiply(adjoint(basis[i]),basis[j]))[0])
    assert Q == Q.conjugate().T
    assert U.T*Q*U == Q
    assert sp.factor(Q.det()) == L**3
    assert Q[0,2] == L and Q[1,1] == -L
    # Orthogonality of vacuum to all positive history degrees sets these
    # two entries to zero, hence L=h=0 and both history modes are radical.
    assert Q.subs({L:0,h:0}) == sp.diag(a,0,0)
    # One-event inverse in the full four-jet formal algebra.
    t = sp.symbols('t')
    inverse_event = 1-t+t**2-t**3+t**4
    event_star_increment = inverse_event-1
    truncated = lambda f: sp.series(f,t,0,5).removeO().expand()
    assert truncated((1+t)*inverse_event) == 1
    assert truncated(event_star_increment.subs(t,event_star_increment)) == t
    # A degree-preserving involution taking v to -v misses quadratic return.
    assert truncated((1-t)*(1+t)) == 1-t**2
    result = {
        'schema':'marici.voevodsky.history-clark-cross-grade-requirement.v1',
        'passed':True,
        'relative_algebra':'C[d]/(d^3)',
        'required_adjoint':'d^*=-d+d^2, provided r=1+d is isometric',
        'functional':{'lambda(1)':'a','lambda(d)':'L/2+i h','lambda(d^2)':'L'},
        'form':[[str(v) for v in Q.row(i)] for i in range(3)],
        'determinant':'L^3',
        'degreewise_orthogonal_clark_assembly':'Invariant restriction has L=h=0 and annihilates d,d^2.',
        'event_adjoint_increment':'-v+v^2-v^3+v^4 if each event 1+v is required to be isometric',
        'source_clark_functional_constructed':False,
        'scope':'Necessary algebraic conditions under specified isometry assumptions; no selected physical metric or arithmetic spectral representation.',
    }
    out=ROOT/'research/voevodsky/results/history-clark-cross-grade-requirement.json'
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
