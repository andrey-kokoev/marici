#!/usr/bin/env python3
"""Source-incidence derivation of the projective history6 coefficient."""
import json
from hashlib import sha256
from pathlib import Path
from check_history6_projection_descent import s, EPS, twistors, ratio, adjugate2
from momentum_twistor_constructors import four_bracket, line_plane_point
ROOT=Path(__file__).resolve().parents[3]
PROJECTION='research/benincasa/results/history6_projection_descent.json'


def cross_ratio(Z):
    def br(*labels):return four_bracket(*(Z[j] for j in labels))
    return s.factor(1-br(6,8,1,2)*br(5,1,2,3)/(br(5,8,1,2)*br(6,1,2,3)))


def symbolic_incidence():
    # On <12> != 0, translate x2 to zero and change the spinor basis to
    # lambda1=e1, lambda2=e2. Z3,Z5,Z6,Z8 remain unrestricted 4-vectors.
    # Translation leaves x differences invariant; Lorentz/spinor changes
    # multiply each A or S endpoint functional by common canceling factors.
    Z={1:s.Matrix([1,0,0,0]),2:s.Matrix([0,1,0,0])}
    for j in (3,5,6,8):Z[j]=s.Matrix(s.symbols(f'z{j}_0:4'))
    lam={j:Z[j][:2,0] for j in Z};mu={j:Z[j][2:4,0] for j in Z}
    def line_x(a,b):
        return (s.Matrix.hstack(mu[a],mu[b])*s.Matrix.hstack(EPS*lam[a],EPS*lam[b]).inv()).T
    x3=line_x(2,3);x6=line_x(5,6)
    # Incidence gives <8|x8=-mu8^T, so x8 and Z7 disappear exactly.
    ut=mu[8].T*adjugate2(x6)
    xi=(-mu[8].T-lam[8].T*EPS*x6)*adjugate2(x6)
    kt=EPS*ut.T
    L=xi*(-x3)*adjugate2(x3-x6)
    W=line_plane_point(Z[5],Z[6],Z[8],Z[1],Z[2])
    endpoint_identity=s.factor(s.Matrix.hstack(kt,W[:2,0]).det())
    assert endpoint_identity==0
    S5=s.factor((L*lam[5])[0]);S6=s.factor((L*lam[6])[0])
    B5=four_bracket(Z[5],Z[1],Z[2],Z[3]);B6=four_bracket(Z[6],Z[1],Z[2],Z[3])
    functional_identity=s.factor(S5*B6-S6*B5);assert functional_identity==0
    A0=s.factor(s.Matrix.hstack(lam[6],lam[5]).det());At=s.factor(s.Matrix.hstack(kt,lam[5]).det())
    St=s.factor((L*kt)[0]);source=s.factor(A0*St/(At*S6));intrinsic=cross_ratio(Z)
    assert s.factor(source-intrinsic)==0
    return {'normalization_patch':'<12> nonzero; x2=0; lambda1=e1,lambda2=e2',
        'free_twistor_components':16,'W':'(56) intersect (812)',
        'projected_updated_endpoint_identity':'det[epsilon*ut^T, P(W)]=0',
        'restricted_endpoint_functional_identity':'S(lambda5)*<6123> - S(lambda6)*<5123> = 0',
        'symbolic_source_minus_intrinsic':'0','symbolic_intrinsic_expression_in_patch':str(intrinsic),
        'localization':'Adjacent incidence lines and At*S0 nonzero; equality of rational functions does not restore singular source points.'}


def main():
    prior=json.loads((ROOT/PROJECTION).read_text());assert prior['passed']
    for p,h in prior['source_sha256'].items():assert sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    symbolic=symbolic_incidence()
    fixtures=[]
    for shift in (0,1,2):
        Z,lam,x=twistors(shift);c=cross_ratio(Z);old,_=ratio(lam,x);assert c==old
        W=line_plane_point(Z[5],Z[6],Z[8],Z[1],Z[2]);b=-four_bracket(Z[5],Z[8],Z[1],Z[2])
        viaW=s.factor(four_bracket(W,Z[1],Z[2],Z[3])/(b*four_bracket(Z[6],Z[1],Z[2],Z[3])))
        assert viaW==c
        fixtures.append({'shift':shift,'intrinsic_c6':str(c),'source_c6':str(old),'intersection_c6':str(viaW)})
    paths=[PROJECTION,'research/benincasa/checkers/check_history6_projection_descent.py',
        'research/nima/momentum_twistor_constructors.py','research/nima/dual_spinor_kinematics.py','research/nima/dual_r_invariant.py']
    out={'schema':'marici.benincasa.history6-twistor-cross-ratio.v1','history_index':6,
        'formula':'c6 = 1 - <6812>*<5123>/(<5812>*<6123>)',
        'derivation':symbolic,'fixtures':fixtures,'passed':True,
        'projective_descent':'Each four-bracket acquires det(G); each label has equal numerator/denominator scaling in the cross-ratio term, so c6 is GL4 and individually projectively invariant on its localization. Source incidence identities prove agreement on the normalized <12> open, not just sampled projection invariance.',
        'bosonized_quotient_candidate':'c6(Y,Z)=1-<Y6812>*<Y5123>/(<Y5812>*<Y6123>), since quotient four-brackets are six-brackets with Y. This target-dependent rational extension is specified, not yet a physical extraction theorem.',
        'next_action':'Pull this actual Y-dependent quotient coefficient back to the F6 chart; classify its value, pole orders and possible indeterminacy on b2=b4=0. Compute Laurent residue corrections rather than use external-fixed multiplication.',
        'scope':'Projective endpoint identity and specified quotient rational function; no ordinary canonical admission or boundary-supercomponent map.',
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (ROOT/'research/benincasa/results/history6_twistor_cross_ratio.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'formula':out['formula'],'symbolic_free_components':16,'fixtures':fixtures,
        'quotient_candidate':out['bosonized_quotient_candidate']},indent=2))

if __name__=='__main__':main()
