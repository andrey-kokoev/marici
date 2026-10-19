# /// script
# dependencies = ["sympy"]
# ///
"""Exact coefficient part of the source-cycle to Fourier-comb bridge.
Poisson summation and Mellin continuation are imported analytic statements.
"""
from pathlib import Path
import hashlib,json,sys
import sympy as S
ROOT=Path(__file__).resolve().parents[3]
ST=ROOT/'research/strominger'
sys.path.insert(0,str(ST/'checkers'))
from source_arrow_hamiltonian import construct


def main():
    rp=ST/'results/source-arrow-hamiltonian-descent.json'
    receipt=json.loads(rp.read_text());assert receipt['status']=='pass'
    for p,h in receipt['input_sha256'].items():
        assert hashlib.sha256((ROOT/'research'/p).read_bytes()).hexdigest()==h,p
    source,C12,edges=construct(tuple('ABCD'),receipt['vertex_permutation'],
                              {'A':0,'C':1,'D':2,'B':3},S.Rational(1,2))
    E=S.eye(12)[:,:4];P=(E.T*source.G*E).inv()*E.T*source.G
    N=S.eye(12)-E*P;C4=P*C12*E;D4=P*source.D*E
    # Fourier orbit ordered P_a,C_-a,P_(1-a),C_a. Source orbit AD,DB,BC,CA.
    port={'AD':0,'DB':1,'BC':2,'CA':3}
    J=S.zeros(4)
    for j,e in enumerate(edges[:4]):J[port[e],j]=1
    F=S.zeros(4)
    for j in range(4):F[(j+1)%4,j]=1
    K=J*P
    assert P*C12==C4*P and C12*E==E*C4
    assert J*C4==F*J and K*C12==F*K
    assert K*source.D==(F-F.inv())*K
    assert K.rank()==4 and K*N==S.zeros(4,12)
    assert E*J.inv()*K+N==S.eye(12)
    for k in range(9):assert K*C12**k==F**k*K
    assert N*C12==C12*N # retained hidden representation remains autonomous
    # All four characters, especially the alternating character, are retained.
    char_ranks={}
    for name,l in [('1',S.Integer(1)),('-1',S.Integer(-1)),('i',S.I),('-i',-S.I)]:
        Q12=sum((l**(-k)*C12**k for k in range(4)),S.zeros(12))/4
        Q4=sum((l**(-k)*F**k for k in range(4)),S.zeros(4))/4
        assert S.simplify(K*Q12-Q4*K)==S.zeros(4,12)
        assert Q12.rank()==3 and Q4.rank()==1
        char_ranks[name]={'source':3,'analytic_orbit':1}
    A=-D4**2/4;minus=(S.eye(4)-C4+C4**2-C4**3)/4
    quarter=S.eye(4)-A+D4/2
    assert quarter-C4==2*minus and minus.rank()==1
    assert J*quarter!=F*J
    # At a=1/3, localized test probes isolate the comb atoms at these points.
    # Columns are the four actual distribution ports in the order above.
    w=-S.Rational(1,2)+S.I*S.sqrt(3)/2
    probes=S.Matrix([[1,0,0,0],[0,0,1,0],[0,1,0,1],[0,S.conjugate(w),0,w]])
    assert probes.det()!=0 and probes.rank()==4
    endpoint=S.Matrix([[0,1,0,1]])
    assert endpoint==probes[2,:]
    # A coefficient metric transported to the orbit, not a comb L2 norm.
    G4=E.T*source.G*E
    orbit_gram=J.inv().T*G4*J.inv()
    assert F.T*orbit_gram*F==orbit_gram
    assert K.T*orbit_gram*K+N.T*source.G*N==source.G
    result={'schema':'marici.carrier-fourier-orbit-bridge.v1','passed':True,
      'iteration':1,'arrow_order':list(edges),'analytic_orbit_order':['P_a','C_-a','P_(1-a)','C_a'],
      'visible_attachment':port,'projection_then_attachment':[[str(v) for v in K.row(i)] for i in range(4)],
      'full_permutation_intertwines':True,'skew_generator_intertwines':True,
      'retained_reconstruction':True,'hidden_dimension':8,'character_ranks':char_ranks,
      'a_one_third_atom_probe_rank':4,'endpoint_atom_retained':True,
      'angular_quarter_step_equals_full_Fourier_step':False,
      'coefficient_gram_transport_verified':True,'independent_analytic_Hilbert_Gram_verified':False,
      'Mellin_gamma_identity':'Imported prior analytic identity; not numerically inferred',
      'triangle_history_interface_identified':False,
      'five_scalar_completion_arrows_identified_with_Fourier_steps':False,
      'RH_proved':False}
    files=[Path(__file__),rp,ST/'checkers/source_arrow_hamiltonian.py',
      ROOT/'research/voevodsky/carrier-fourier-orbit-bridge-v1.md',
      ROOT/'research/voevodsky/mellin-diagonalization-of-the-oriented-radial-fourier-kernel-recovers-the-tate-gamma-matrix.md',
      ROOT/'research/voevodsky/the-oriented-hurwitz-polylogarithm-pair-closes-the-source-comb-fourier-intertwiner.md',
      ROOT/'research/nima/checkers/check_triangle_coherent_generator_transport.py']
    result['source_hashes']={str(p.resolve()):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
    (ROOT/'research/voevodsky/results/carrier-fourier-orbit-bridge-v1.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('source_hashes','projection_then_attachment')},indent=2))


if __name__=='__main__':main()
