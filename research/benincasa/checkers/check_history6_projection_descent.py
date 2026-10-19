#!/usr/bin/env python3
"""Exact incidence reconstruction and infinity-projection audit of c6."""
import itertools
import json
from hashlib import sha256
from pathlib import Path
from check_history6_endpoint_boundary import s, coefficient, momentum_conserving_kinematics, transport_spinor, x_interval, adjugate2
from dual_r_invariant import generalized_r
ROOT=Path(__file__).resolve().parents[3]
ENDPOINT='research/benincasa/results/history6_endpoint_boundary.json'
EPS=s.Matrix([[0,1],[-1,0]])


def twistors(shift):
    lam,_,x=momentum_conserving_kinematics(
        [(1,j*j+j+1+shift*j) for j in range(1,9)],
        [(1,j**3+2*j+1+shift*j*j) for j in range(1,7)])
    Z={j:lam[j].col_join(x[j].T*EPS*lam[j]) for j in range(1,9)}
    return Z,lam,x


def incidence(Z):
    lam={j:Z[j][:2,0] for j in range(1,9)};x={}
    for j in range(1,9):
        prev=8 if j==1 else j-1
        L=s.Matrix.hstack(EPS*lam[prev],EPS*lam[j])
        assert L.det()!=0
        M=s.Matrix.hstack(Z[prev][2:4,0],Z[j][2:4,0])
        x[j]=(M*L.inv()).T.applyfunc(s.factor)
    x[9]=x[1]
    assert all(s.simplify(x[j].T*EPS*lam[j]-Z[j][2:4,0])==s.zeros(2,1) for j in range(1,9))
    til={}
    for j in range(1,9):
        delta=(x[j]-x[j+1]).applyfunc(s.factor)
        row=next(k for k in range(2) if lam[j][k]!=0)
        til[j]=s.Matrix([s.factor(delta[row,k]/lam[j][row]) for k in range(2)])
        assert (delta-lam[j]*til[j].T).applyfunc(s.factor)==s.zeros(2)
    assert sum((lam[j]*til[j].T for j in range(1,9)),s.zeros(2)).applyfunc(s.factor)==s.zeros(2)
    return lam,x


def ratio(lam,x):
    ut=transport_spinor(lam,x,(8,2,6));u0=lam[6].T*EPS
    xi=transport_spinor(lam,x,(8,6,2))
    L=xi*x_interval(x,2,3)*adjugate2(x_interval(x,3,6))
    kt,k0=EPS*ut.T,EPS*u0.T
    A0=s.factor(s.det(s.Matrix.hstack(k0,lam[5])))
    At=s.factor(s.det(s.Matrix.hstack(kt,lam[5])))
    S0=s.factor((L*k0)[0]);St=s.factor((L*kt)[0])
    assert At!=0 and S0!=0
    return s.factor(A0*St/(At*S0)),{'A0':str(A0),'At':str(At),'S0':str(S0),'St':str(St)}


def localize(lam,x):
    _,o=generalized_r(lam,x,8,(),(2,6),lam[1].T*EPS,lam[6].T*EPS)
    lower=lam[2].T*EPS
    _,t=generalized_r(lam,x,8,(6,2),(3,6),lower,transport_spinor(lam,x,(8,2,6)))
    _,u=generalized_r(lam,x,8,(6,2),(3,6),lower,lam[6].T*EPS)
    assert all(v!=0 for meta in (o,t,u) for v in meta['denominator_factors'])
    assert s.det(s.Matrix.hstack(lam[2],lam[3]))!=0
    return {'outer':[str(q) for q in o['denominator_factors']],
            'transported_inner':[str(q) for q in t['denominator_factors']],
            'untransported_inner':[str(q) for q in u['denominator_factors']]}


def main():
    prior=json.loads((ROOT/ENDPOINT).read_text());assert prior['passed']
    for p,h in prior['source_sha256'].items():assert sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    rho=s.Symbol('rho');G=s.eye(4);G[0,2]=rho;G[1,3]=rho
    assert G.det()==1
    fixtures=[]
    for shift in (0,1,2):
        Z,original_lam,original_x=twistors(shift);lam,x=incidence(Z)
        assert lam==original_lam and x==original_x
        baseline,_=ratio(lam,x);assert baseline==s.Rational(prior['runs'][shift]['c'])
        controls={}
        # Little-group representative changes and determinant-one Lorentz
        # frame change preserve the original infinity projection.
        H=s.diag(2,s.Rational(1,2),1,1)
        for name,zz in [('column_rescaling',{j:(j+1)*Z[j] for j in Z}),
                        ('projection_preserving_frame',{j:H*Z[j] for j in Z})]:
            ll,xx=incidence(zz);v,_=ratio(ll,xx);assert v==baseline;controls[name]=str(v)
        singular_frame={j:G.subs(rho,1)*Z[j] for j in Z}
        singular_labels=[j for j in range(1,9) if s.Matrix.hstack(
            EPS*singular_frame[8 if j==1 else j-1][:2,0],EPS*singular_frame[j][:2,0]).det()==0]
        assert singular_labels==[2]
        changed={j:G.subs(rho,2)*Z[j] for j in Z}
        # All projective four-bracket invariants are identical under this SL4
        # shear. In a fixed twistor vector space this changes P=[I | rho I],
        # hence the infinity projection, not the eight projective points.
        assert all(s.Matrix.hstack(*(changed[j] for j in I)).det()==s.Matrix.hstack(*(Z[j] for j in I)).det()
                   for I in itertools.combinations(range(1,9),4))
        ll,xx=incidence(changed);value,raw=ratio(ll,xx)
        loc=localize(ll,xx)
        defect=s.factor(value-baseline)
        other_projections=[]
        for block in (s.Matrix([[1,2],[3,5]]),s.diag(2,3),s.Matrix([[0,1],[-1,0]])):
            K=s.eye(4);K[:2,2:4]=block
            zz={j:K*Z[j] for j in Z}
            assert K.det()==1
            assert all(s.Matrix.hstack(*(zz[j] for j in I)).det()==s.Matrix.hstack(*(Z[j] for j in I)).det()
                       for I in itertools.combinations(range(1,9),4))
            kl,kx=incidence(zz);kc,_=ratio(kl,kx)
            assert kc==baseline
            other_projections.append({'upper_right_block':[[str(q) for q in row] for row in block.tolist()],
                'coefficient':str(kc),'source_localization':localize(kl,kx)})
        fixtures.append({'shift':shift,'baseline':str(baseline),'shear_rho2':str(value),
            'additional_projection_controls':other_projections,
            'excluded_rho1_incidence_singularity':{'line_endpoint_labels':singular_labels,'disposition':'undefined_not_zero'}, 
            'projection_change_defect':str(defect),'all_70_four_brackets_preserved':True,
            'preserving_controls':controls,'changed_endpoint_factors':raw,'changed_source_localization':loc})
    # A fixed original twistor configuration, with symbolic projection choice.
    Z,_,_=twistors(0);ll,xx=incidence({j:G*Z[j] for j in Z})
    symbolic,raw=ratio(ll,xx);base=s.Rational(fixtures[0]['baseline'])
    assert s.factor(symbolic.subs(rho,0)-base)==0
    derivative=s.factor(s.diff(symbolic,rho).subs(rho,0))
    varying=any(s.Rational(r['projection_change_defect'])!=0 for r in fixtures)
    assert varying==(derivative!=0)
    if not varying: assert s.factor(symbolic-base)==0
    sources=[ENDPOINT,'research/benincasa/checkers/check_history6_endpoint_boundary.py',
        'research/nima/dual_spinor_kinematics.py','research/nima/dual_r_invariant.py']
    out={'schema':'marici.benincasa.history6-projection-descent.v1','history_index':6,
        'incidence_convention':'Z_j=(lambda_j, x_j^T epsilon lambda_j); x_j reconstructed from line (Z_{j-1},Z_j)',
        'projection_family':'P_rho=[I2 | rho I2], Q=[0 | I2]; equivalently coordinates G_rho Z, G determinant1',
        'fixtures':fixtures,'symbolic_fixed_twistor_family':{'coefficient':str(symbolic),'raw_endpoint_factors':raw,
            'derivative_at_rho0':str(derivative)},'passed':True,
        'decision':('c6 does not descend to projective momentum-twistors without infinity-projection data'
                    if varying else 'c6 passes this projection family; full descent not proved'),
        'boundary_implication':('The spinor coefficient cannot be treated as an undecorated GL4-invariant target quotient function. A physical extraction must specify extra projection/infinity data and their boundary behavior; independent-base c6 times CZ remains only a relative module.'
                    if varying else 'A source-derived twistor formula and quotient boundary test remain needed; one invariant family is not a proof.'),
        'next_action':'Derive an intrinsic projective momentum-twistor expression for c6 (for example a four-bracket/intersection cross ratio). The tested projection invariance permits this continuation but is not a GL4 descent theorem. Then apply the explicit bosonized target quotient and audit actual corner localization/poles before physical extraction.',
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in sources},
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (ROOT/'research/benincasa/results/history6_projection_descent.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'decision':out['decision'],'derivative_at_rho0':str(derivative),
        'fixture_values':[{k:r[k] for k in ('shift','baseline','shear_rho2','projection_change_defect')} for r in fixtures]},indent=2))

if __name__=='__main__': main()
