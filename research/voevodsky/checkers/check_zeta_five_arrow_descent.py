# /// script
# dependencies = ["sympy"]
# ///
"""Test supplied zeta completion factors against Strominger's actual 12->4 P.
Symbolic factors are independent parameters; no zeta law is inferred.
"""
from pathlib import Path
import hashlib,json,sys
import sympy as S
ROOT=Path(__file__).resolve().parents[3]
ST=ROOT/'research/strominger'
sys.path.insert(0,str(ST/'checkers'))
from source_arrow_hamiltonian import construct


def main():
    receipt_path=ST/'results/source-arrow-hamiltonian-descent.json'
    receipt=json.loads(receipt_path.read_text())
    assert receipt['status']=='pass'
    for path,digest in receipt['input_sha256'].items():
        assert hashlib.sha256((ROOT/'research'/path).read_bytes()).hexdigest()==digest,path
    source,C,edges=construct(tuple('ABCD'),receipt['vertex_permutation'],
                            {'A':0,'C':1,'D':2,'B':3},S.Rational(1,2))
    assert list(edges)==receipt['arrow_order']
    E=S.eye(12)[:,:4]
    P=(E.T*source.G*E).inv()*E.T*source.G
    N=S.eye(12)-E*P
    assert P*E==S.eye(4) and P*N==S.zeros(4,12)
    assert P==S.eye(4).row_join(S.ones(4,8)/14)
    g,p,q=S.symbols('g p q')
    factors={'AB':g,'BC':p,'AC':p*g,'CD':q,'AD':q*p*g}
    # First interpretation: same scalar multiplier on the whole carrier.
    scalar={}
    for edge,a in factors.items():
        top=a*S.eye(12);bottom=a*S.eye(4)
        assert P*top==bottom*P
        scalar[edge]={'factor':str(a),'exact_intertwining':True}
    assert factors['BC']*factors['AB']==factors['AC']
    assert factors['CD']*factors['AC']==factors['AD']
    # Second interpretation: alter just the coefficient on the named edge.
    # Freeze generic nonidentity multiplier as 2 for an exact falsifier.
    localized={}
    for edge in factors:
        j=edges.index(edge);Q=S.zeros(12);Q[j,j]=1
        U=S.eye(12)+Q
        leak=P*U*N
        assert leak.rank()==1
        k=next(k for k in range(12) if leak[:,k]!=S.zeros(4,1))
        h=N[:,k]
        assert P*h==S.zeros(4,1) and P*U*h!=S.zeros(4,1)
        localized[edge]={'generic_leakage_rank':1,'witness_multiplier':2,
          'hidden_input':[str(x) for x in h],
          'visible_output':[str(x) for x in P*U*h]}
    # Classification: ALL diagonal operations descending through this P.
    d=S.symbols('d0:12');D=S.diag(*d)
    residual=P*D-(P*D*E)*P
    constraints,_=S.linear_eq_to_matrix(list(residual),d)
    assert constraints.rank()==11
    assert constraints.nullspace()==[S.ones(12,1)]
    # Edge-local decorations fail the original triangle composition as well.
    def local(edge,a):
        U=S.eye(12);j=edges.index(edge);U[j,j]=a;return U
    assert local('BC',3)*local('AB',2)!=local('AC',6)
    result={'schema':'marici.zeta-five-arrow-descent.v1','passed':True,
      'projection':'Strominger fixed-Gram four-mode projection, not native retained T9',
      'visible_order':list(edges[:4]),'arrow_order':list(edges),
      'scalar_factor_descent':scalar,'edge_local_descent':localized,
      'descending_diagonal_space_dimension':1,
      'descending_diagonal_space':'scalar multiples of I12',
      'edge_local_assignment_preserves_two_triangle_composition':False,
      'supplied_analytic_factors_derived_from_native_arrows':False,
      'native_T9_intertwiner_constructed':False,'RH_proved':False,
      'scope':'Exact coefficient-map test; scalar meromorphic factors supplied externally. No physical or Postnikov-rung identification.'}
    files=[Path(__file__),receipt_path,ST/'checkers/source_arrow_hamiltonian.py',
           ST/'checkers/hamiltonian_descent_wg.py',
           ROOT/'research/voevodsky/zeta-five-arrow-descent-v1.md']
    result['source_hashes']={str(p.resolve()):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
    out=ROOT/'research/voevodsky/results/zeta-five-arrow-descent-v1.json'
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('source_hashes','edge_local_descent')},indent=2))


if __name__=='__main__':main()
