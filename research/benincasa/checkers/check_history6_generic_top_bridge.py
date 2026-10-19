#!/usr/bin/env python3
"""Generic normalized-incidence full top bridge, not a boundary Berezin map."""
import json
import itertools
from hashlib import sha256
from pathlib import Path
from check_history6_full_component_bridge import s, EPS, wedge_coefficients
from check_history6_bosonization_bridge import normalization, LABELS, PAIRS
from momentum_twistor_constructors import four_bracket
from dual_spinor_kinematics import adjugate2
ROOT=Path(__file__).resolve().parents[3]
PRIOR='research/benincasa/results/history6_full_component_bridge.json'


def proof():
    # <12> != 0 permits a spinor basis change and dual translation x2=0.
    # An independent theta translation sets theta2=0 (chi1=chi2=0);
    # source theta differences and Schur residuals are invariant under it.
    Z={1:s.Matrix([1,0,0,0]),2:s.Matrix([0,1,0,0])}
    for j in (3,5,6,8):Z[j]=s.Matrix(s.symbols(f'z{j}_0:4'))
    lam={j:Z[j][:2,0] for j in Z};mu={j:Z[j][2:4,0] for j in Z}
    chi_labels=[3,5,6,8];chi={j:s.zeros(1,4) for j in Z}
    for k,j in enumerate(chi_labels):chi[j][0,k]=1
    def region(a,b):
        P=s.Matrix.hstack(EPS*lam[a],EPS*lam[b])
        xx=(s.Matrix.hstack(mu[a],mu[b])*P.inv()).T.applyfunc(s.factor)
        theta=(P.T.inv()*s.Matrix.vstack(chi[a],chi[b])).applyfunc(s.factor)
        return xx,theta
    x3,theta3=region(2,3);x6,theta6=region(5,6)
    det6=s.factor(x6.det())
    ut=(mu[8].T*adjugate2(x6)).applyfunc(s.factor)
    xi=((-mu[8].T-lam[8].T*EPS*x6)*adjugate2(x6)).applyfunc(s.factor)
    L=(xi*(-x3)*adjugate2(x3-x6)).applyfunc(s.factor)
    K=(xi*(-x6)*adjugate2(x6-x3)).applyfunc(s.factor)
    kt=EPS*ut.T
    # <8|theta8=-chi8, and ut+xi=-<8|det(x6), so region8/chi7
    # cancels from the outer numerator, exactly as x8 cancels from transport.
    qo=(ut*theta6-det6*chi[8]).applyfunc(s.factor)
    qi=(L*theta6+K*theta3).applyfunc(s.factor)
    A=qo.col_join(qi)
    outer_den=[det6]+[s.factor(v) for v in ((ut*lam[6])[0],(ut*lam[5])[0],(xi*lam[2])[0],(xi*lam[1])[0])]
    inner_den=[s.factor((x3-x6).det())]+[s.factor(v) for v in ((L*kt)[0],(L*lam[5])[0],(K*lam[3])[0],(K*lam[2])[0])]
    assert all(v!=0 for v in outer_den+inner_den)
    po=s.factor(s.Matrix.hstack(lam[2],lam[1]).det()*s.Matrix.hstack(lam[6],lam[5]).det()/s.prod(outer_den))
    pi=s.factor(s.Matrix.hstack(lam[3],lam[2]).det()*s.Matrix.hstack(kt,lam[5]).det()/s.prod(inner_den))
    pi0=s.factor(s.Matrix.hstack(lam[3],lam[2]).det()*s.Matrix.hstack(lam[6],lam[5]).det()/
        (s.prod(inner_den)/inner_den[1]*(L*lam[6])[0]))
    M=s.Matrix.hstack(*(Z[j] for j in LABELS[:4]));d=s.factor(M.det());assert d!=0
    weights=M.inv()*s.Matrix.hstack(Z[6],Z[8])
    B=s.Matrix.vstack(*[(chi[label]-sum((weights[i,k]*chi[LABELS[i]] for i in range(4)),s.zeros(1,4))).applyfunc(s.factor)
        for k,label in enumerate((6,8))])
    aa=wedge_coefficients(A);bb=wedge_coefficients(B)
    pivot=next(p for p,v in bb.items() if v!=0)
    scale=s.factor(aa[pivot]/bb[pivot]);assert scale!=0
    for pair in bb:assert s.factor(aa[pair]-scale*bb[pair])==0,pair
    den=s.prod(four_bracket(*(Z[LABELS[k]] for k in range(6) if k not in pair)) for pair in PAIRS)
    bosonic=s.factor(d**4/den)
    assert s.factor(po*pi*scale**4-bosonic)==0
    def br(*labels):return four_bracket(*(Z[j] for j in labels))
    c=s.factor(1-br(6,8,1,2)*br(5,1,2,3)/(br(5,8,1,2)*br(6,1,2,3)))
    assert s.factor(pi0/pi-c)==0
    assert s.factor(po*pi0*scale**4-c*bosonic)==0
    assert s.factor(po*(pi-pi0)*scale**4-(1-c)*bosonic)==0
    return {'free_bosonic_components':16,'fermionic_gauge':'theta2=0,chi1=chi2=0; other active chi3,chi5,chi6,chi8 arbitrary in each SU4 sector',
        'source_R_two_form_rows':[[str(q) for q in row] for row in A.tolist()],
        'Schur_two_form_rows':[[str(q) for q in row] for row in B.tolist()],
        'all_six_generic_sector_coefficients_equal_up_to_scale':True,'scale':str(scale),
        'outer_prefactor':str(po),'transported_inner_prefactor':str(pi),'unupdated_inner_prefactor':str(pi0),
        'bosonized_prefactor':str(bosonic),'c6':str(c),
        'original_denominator_factors':{'outer':list(map(str,outer_den)),'transported_inner':list(map(str,inner_den)),
            'unupdated_changed_factor':str(s.factor((L*lam[6])[0]))},
        'full_four_sector_identity':'Each two-form scales by the same scalar; po*pi*scale^4 equals the Schur prefactor. Therefore every mixed SU4 component agrees as a generic rational identity on this gauge open.',
        'gauge_scope':'Bosonic normalization uses only dual translation/spinor frame and <12> nonzero. Theta translation leaves source theta differences unchanged and shifts chi by a lambda linear functional annihilated by the Schur residual. Inactive labels4,7 drop from the displayed source incidence circuits; no values for their chi are imposed.'}


def main():
    prior=json.loads((ROOT/PRIOR).read_text());assert prior['passed']
    for p,h in prior['source_sha256'].items():assert sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    assert prior['checker_sha256']==sha256((ROOT/'research/benincasa/checkers/check_history6_full_component_bridge.py').read_bytes()).hexdigest()
    assert normalization()==2880
    result=proof()
    paths=[PRIOR,'research/benincasa/checkers/check_history6_full_component_bridge.py',
        'research/benincasa/checkers/check_history6_bosonization_bridge.py','research/nima/dual_r_invariant.py',
        'research/nima/dual_spinor_kinematics.py','research/nima/momentum_twistor_constructors.py']
    out={'schema':'marici.benincasa.history6-generic-top-bridge.v1','history_index':6,'symbolic_proof':result,
        'passed':True,'disposition':'generic_normalized_incidence_full_top_bridge_constructed',
        'scope':'Universal Berezin identity plus generic16-component source-incidence full polynomial/prefactor identity. Original localization retained. Not a lower-degree boundary Berezin map, ordinary canonical admission or global weighted-chain theorem.',
        'boundary_gate':'Degree7_6 extraction still requires an authorized boundary normal/delta measure and direction-retaining supercomponent codomain; generic top equality cannot supply these by fiat.',
        'next_action':'Read the owning Grassmannian delta-integral/source boundary prescription and formulate its boundary extraction with actual form degree, normal measure and retained direction before computing a physical residue square.',
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (ROOT/'research/benincasa/results/history6_generic_top_bridge.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'free_components':16,'all_generic_sector_coefficients':6,
        'full_mixed_SU4_identity':True,'boundary_gate':out['boundary_gate']},indent=2))

if __name__=='__main__':main()
