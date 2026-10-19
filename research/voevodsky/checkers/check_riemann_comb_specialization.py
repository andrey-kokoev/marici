# /// script
# dependencies = ["sympy"]
# ///
"""Exact specialization ranks and endpoint algebra; imports Poisson/Mellin analysis."""
from pathlib import Path
import hashlib,json
import sympy as S
ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'research/voevodsky'


def main():
    inputs=[BASE/'results/carrier-fourier-orbit-bridge-v1.json',
            BASE/'results/full-endpoint-fourier-bridge-v1.json',
            BASE/'results/fourier-six-step-descent-v1.json']
    receipts=[]
    for p in inputs:
        r=json.loads(p.read_text());assert r['passed'];receipts.append(r)
        for source,digest in r['source_hashes'].items():
            assert hashlib.sha256(Path(source).read_bytes()).hexdigest()==digest,source
    F=S.zeros(4)
    for j in range(4):F[(j+1)%4,j]=1
    collapse=S.ones(1,4)
    assert collapse*F==collapse and collapse*(F-F.T)==S.zeros(1,4)
    assert collapse.rank()==1 and len(collapse.nullspace())==3
    top=S.Matrix(receipts[0]['projection_then_attachment'])
    riemann_row=collapse*top
    assert riemann_row.rank()==1 and len(riemann_row.nullspace())==11
    J=S.Matrix(receipts[1]['full_analytic_attachment']);M=S.Matrix(receipts[1]['endpoint_matrix'])
    history_row=S.simplify(collapse*J)
    assert history_row.rank()==1 and S.simplify(history_row*M-history_row)!=S.zeros(1,4)
    # Complete distribution basis (integer comb Delta, delta_0, constant 1).
    # These distributions are independent; Fourier fixes Delta and exchanges
    # delta_0 with the constant distribution in the self-dual convention.
    Fboundary=S.Matrix([[1,0,0],[0,0,1],[0,1,0]])
    removed=S.Matrix([1,-1,0])
    assert Fboundary*removed==S.Matrix([1,0,-1])
    assert Fboundary*removed!=removed
    assert Fboundary**2==S.eye(3)
    # Endpoint-dilation complex, derived from monomials 1 and t^(-1/2).
    s=S.symbols('s');Ds=S.diag(s,s-1);orientation=S.diag(-1,1)
    swap=S.Matrix([[0,1],[1,0]])
    polar=S.trace(orientation*Ds.inv())
    assert S.simplify(polar-1/(s*(s-1)))==0
    assert S.factor(Ds.det())==s*(s-1)
    assert swap*Ds.subs(s,1-s)*swap==-Ds
    assert swap*orientation*swap==-orientation
    assert S.simplify(polar.subs(s,1-s)-polar)==0
    assert Ds.subs(s,0).rank()==Ds.subs(s,1).rank()==1
    assert S.residue(polar,s,0)==-1 and S.residue(polar,s,1)==1
    assert S.simplify(s*(s-1)*polar/2)==S.Rational(1,2)
    # Half-theta normalization at s=2, using the known zeta(2) identity.
    assert S.simplify(S.pi**(-1)*S.gamma(1)*S.zeta(2)-S.pi/6)==0
    result={'schema':'marici.riemann-comb-specialization.v1','iteration':5,'passed':True,
      'unshifted_fourier_orbit_dimension':1,'generic_four_port_kernel_dimension':3,
      'twelve_coefficient_to_unshifted_distribution_kernel_dimension':11,
      'riemann_source_row':[[str(v) for v in riemann_row.row(0)]],
      'native_endpoint_riemann_row':[[str(v) for v in history_row.row(0)]],
      'riemann_row_invariant_under_native_history_tick':False,
      'zero_removed_comb_is_Fourier_fixed':False,
      'endpoint_completed_distribution_dimension':3,
      'endpoint_determinant':str(Ds.det()),'endpoint_polar_current':str(S.factor(polar)),
      'xi_endpoint_constant':'1/2',
      'theta_Mellin_continuation':'Imported analytic theorem with stated Gaussian and Haar input',
      'five_scalar_factors_derived_from_finite_carrier_alone':False,'RH_proved':False}
    files=[Path(__file__),*inputs,BASE/'riemann-comb-specialization-v1.md',
      ROOT/'research/grothendieck/archimedean-theta-completion-gate.md',
      ROOT/'research/grothendieck/theta-endpoint-dilation-complex-derives-both-the-pole-packet-and-completion-polynomial.md',
      ROOT/'research/grothendieck/fourier-self-sewing-uniquely-selects-the-unit-unshifted-affine-lattice.md']
    result['source_hashes']={str(p.resolve()):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
    (BASE/'results/riemann-comb-specialization-v1.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='source_hashes'},indent=2))


if __name__=='__main__':main()
