#!/usr/bin/env python3
"""Full quotient Grassmann top bridge via universal Berezin/Schur identity.

Factorized identities certify every mixed SU4 component; no boundary Berezin
codomain is inferred from the top-degree map.
"""
import itertools
import json
from hashlib import sha256
from pathlib import Path
from check_history6_bosonization_bridge import normalization, LABELS, PAIRS
from check_history6_projection_descent import s, twistors, EPS
from check_history6_endpoint_boundary import coefficient
from dual_r_invariant import theta_coefficients, generalized_r
from dual_spinor_kinematics import transport_spinor
from momentum_twistor_constructors import four_bracket
ROOT=Path(__file__).resolve().parents[3]
PRIOR='research/benincasa/results/history6_bosonization_bridge.json'


def quotient_row(row,lam):
    # For each SU4 sector impose sum lambda_j eta_j=0, eliminating eta7,8.
    L=s.Matrix.hstack(lam[7],lam[8]);assert L.det()!=0
    elimination=-L.inv()*s.Matrix.hstack(*(lam[j] for j in range(1,7)))
    out=s.Matrix([[row.get(j,0) for j in range(1,7)]])
    out+=s.Matrix([[row.get(7,0),row.get(8,0)]])*elimination
    return out.applyfunc(s.factor)


def wedge_coefficients(Q):
    return {pair:s.factor(Q[:,list(pair)].det()) for pair in itertools.combinations(range(Q.cols),2)}


def evaluate(shift):
    Z,lam,x=twistors(shift);theta=theta_coefficients(lam,8)
    chi={}
    for j in range(1,9):
        lj=EPS*lam[j]
        chi[j]={k:s.factor((lj.T*value)[0]) for k,value in theta[j].items() if (lj.T*value)[0]!=0}
    pivot=LABELS[:4];last=LABELS[4:]
    M=s.Matrix.hstack(*(Z[j] for j in pivot));d=s.factor(M.det());assert d!=0
    bosonic_weights=M.inv()*s.Matrix.hstack(*(Z[j] for j in last))
    effective=[]
    for k,label in enumerate(last):
        row={j:s.factor(chi[label].get(j,0)-sum(bosonic_weights[i,k]*chi[pivot[i]].get(j,0) for i in range(4))) for j in range(1,9)}
        effective.append({j:v for j,v in row.items() if v!=0})
    B=s.Matrix.vstack(*(quotient_row(row,lam) for row in effective))
    _,outer=generalized_r(lam,x,8,(),(2,6),lam[1].T*EPS,lam[6].T*EPS)
    _,inner=generalized_r(lam,x,8,(6,2),(3,6),lam[2].T*EPS,transport_spinor(lam,x,(8,2,6)))
    _,unupdated=generalized_r(lam,x,8,(6,2),(3,6),lam[2].T*EPS,lam[6].T*EPS)
    A=s.Matrix.vstack(quotient_row(outer['xi_coefficients'],lam),quotient_row(inner['xi_coefficients'],lam))
    assert inner['xi_coefficients']==unupdated['xi_coefficients']
    a=wedge_coefficients(A);bb=wedge_coefficients(B)
    p=next(pair for pair,v in bb.items() if v!=0);scale=s.factor(a[p]/bb[p]);assert scale!=0
    assert all(s.factor(a[pair]-scale*bb[pair])==0 for pair in bb)
    denominator=s.prod(four_bracket(*(Z[LABELS[k]] for k in range(6) if k not in pair)) for pair in PAIRS)
    assert denominator!=0
    bosonic_prefactor=s.factor(d**4/denominator)
    source_prefactor=s.factor(outer['prefactor']*inner['prefactor'])
    assert s.factor(source_prefactor*scale**4-bosonic_prefactor)==0
    c=s.factor(unupdated['prefactor']/inner['prefactor'])
    assert s.factor(outer['prefactor']*unupdated['prefactor']*scale**4-c*bosonic_prefactor)==0
    # Independent all70 quotient-numerator checks in unreduced eight eta
    # coordinates, with the lambda rows explicitly retained.
    rawB=s.Matrix([[row.get(j,0) for j in range(1,9)] for row in effective])
    rawA=s.Matrix([[outer['xi_coefficients'].get(j,0) for j in range(1,9)],
                   [inner['xi_coefficients'].get(j,0) for j in range(1,9)]])
    lambdas=s.Matrix([[lam[j][k] for j in range(1,9)] for k in range(2)])
    HA=lambdas.col_join(rawA);HB=lambdas.col_join(rawB)
    assert all(s.factor(HA[:,list(I)].det()-scale*HB[:,list(I)].det())==0 for I in itertools.combinations(range(8),4))
    # Mixed components genuinely use independently chosen pairs in all four
    # sectors. Certify by tensor-factor identity, with corner products as
    # non-diagonal explicit controls rather than claiming an enumeration.
    nonzero=[pair for pair,v in bb.items() if v!=0]
    controls=[]
    for shift_pair in range(min(4,len(nonzero))):
        pairs=[nonzero[(shift_pair+j)%len(nonzero)] for j in range(4)]
        source=s.factor(source_prefactor*s.prod(a[pair] for pair in pairs))
        extracted=s.factor(bosonic_prefactor*s.prod(bb[pair] for pair in pairs));assert source==extracted
        assert s.factor(c*source-outer['prefactor']*unupdated['prefactor']*s.prod(a[pair] for pair in pairs))==0
        controls.append({'eta_pairs_by_SU4':[[i+1,j+1] for i,j in pairs],'transported_coefficient':str(source),
            'untransported_coefficient':str(s.factor(c*source)),'difference_coefficient':str(s.factor((1-c)*source))})
    return {'shift':shift,'bosonic_schur_pivot_labels':pivot,'residual_fermion_labels':last,
        'bosonic_pivot_determinant':str(d),'quotient_eliminated_eta_labels':[7,8],
        'reduced_berezin_fermion_rows':[[str(v) for v in row] for row in B.tolist()],
        'reduced_generalized_R_fermion_rows':[[str(v) for v in row] for row in A.tolist()],
        'all_15_sector_two_form_coefficients_checked':True,'sector_proportionality':str(scale),
        'all_70_lambda_augmented_numerator_coefficients_checked':True,
        'bosonized_prefactor':str(bosonic_prefactor),'source_prefactor':str(source_prefactor),
        'full_tensor_components_certified':15**4,'certification':'factorized four-sector polynomial identity, not brute-force component enumeration',
        'mixed_component_controls':controls,'c6':str(c)}


def main():
    prior=json.loads((ROOT/PRIOR).read_text());assert prior['passed']
    for p,h in prior['source_sha256'].items():assert sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    assert prior['checker_sha256']==sha256((ROOT/'research/benincasa/checkers/check_history6_bosonization_bridge.py').read_bytes()).hexdigest()
    norm=normalization();assert norm==2880
    runs=[evaluate(j) for j in (0,1,2)]
    paths=[PRIOR,'research/benincasa/checkers/check_history6_bosonization_bridge.py',
        'research/benincasa/checkers/check_history6_projection_descent.py',
        'research/nima/dual_r_invariant.py','research/nima/dual_spinor_kinematics.py','research/nima/momentum_twistor_super.py']
    out={'schema':'marici.benincasa.history6-full-component-bridge.v1','history_index':6,
        'universal_berezin_identity':{'formula':'[phi_top] det_{r,s=1,2}(sum_A phi_rA q_s^A)^4 / 2880 = product_A(q_1^A wedge q_2^A)',
            'proof':'The determinant is homogeneous degree2 in the eight phi and degree2 in the eight independent odd q generators. Its fourth power has phi degree8 and q degree8. There is exactly one top monomial in each; the independent Grassmann 2x2 calculation fixes its coefficient2880. Substitution of arbitrary odd linear forms q proves the identity for every component, including mixed SU4 pair choices.',
            'normalization':str(norm)},
        'schur_bridge':'Choose four independent bosonic active columns M. Subtract their bosonic combinations from the other two columns; det(Z_bosonized)=det(M)*det_2(phi*q) with q the two residual chi forms. At Y0 all six cyclic complementary denominators are phi-independent.',
        'runs':runs,'passed':True,
        'top_map':'Normalized referenceY0 top phi extraction of Omega_F gives transported Ft in the per-sector supermomentum quotient. Multiplication by phi-independent c6 gives F0, and by1-c6 gives Ft-F0, as full factorized degree-eight quotient polynomials at three fixtures.',
        'scope':'Universal algebraic Berezin/Schur identity plus fresh full quotient comparison at three nonsingular spinor fixtures. Not a generic symbolic generalized-R identity in all external kinematics, ordinary canonical-cell admission, or a degree7_6 boundary extraction theorem.',
        'boundary_gate':'No lower-degree boundary Berezin/delta measure or direction-retaining physical supercomponent codomain is yet defined. The top quotient map cannot be applied to the exceptional seven-form by changing its degree silently.',
        'next_action':'Derive a degree-preserving boundary extraction from the source Grassmannian delta-integral or an explicitly authorized super boundary distribution, including its normal/delta measure and direction data; alternatively extend the external-kinematic comparison from fixtures to a generic rational identity.',
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (ROOT/'research/benincasa/results/history6_full_component_bridge.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'universal_Berezin_factor':str(norm),
        'full_quotient_components_per_fixture':15**4,'fixture_scales':[r['sector_proportionality'] for r in runs],
        'boundary_gate':out['boundary_gate']},indent=2))

if __name__=='__main__':main()
