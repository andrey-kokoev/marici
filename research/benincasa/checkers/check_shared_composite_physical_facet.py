#!/usr/bin/env python3
"""Common Y1234 divisor: algebraic overlap versus positive branch nonoverlap."""
import json
import sys
import itertools
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(Path(__file__).resolve().parent))
from check_three_composite_inverse_normals import (s,rational,normalize,target_jac,setup_A,setup_H,inverse_A,inverse_H,extract)
PRIOR='research/benincasa/results/three_composite_normalizations.json'
INVERSES='research/benincasa/results/three_composite_inverse_normals.json'


def parameters(sample):
    a=s.symbols('a1:9');C=s.Matrix([[s.sympify(v) for v in rr] for rr in sample['source_chart_matrix']])
    vals={z:s.Integer(sample['source_parameters'][str(z)]) for z in a}
    return a,C,vals


def symbolic_nonoverlap(rows,Z):
    a,C,_=parameters(rows[5]['target_runs'][0]);Y=C.subs(a[1],0)*Z
    emb=rows[8]['superfunction_runs'][0]['matches'][0];data=setup_A(Z,emb);source_rows=[]
    for allowed,M,h,piv,lift in data:
        yh=Y*h;g=s.Matrix([[-yh[1],yh[0]]]);coeff=(g*Y)[:,piv]*lift
        row=s.zeros(1,8)
        for j,label in enumerate(allowed):row[label]=s.factor(coeff[j])
        source_rows.append(row)
    S=s.Matrix.vstack(*source_rows)
    # A extraction ratios are GL invariant, so the common G^{-1} cancels.
    b1=rational(S[:,[1,3]].det()/S[:,[1,2]].det())
    b5=rational(S[:,[2,6]].det()/S[:,[2,5]].det())
    positive_num=3*(4*a[0]+5);positive_den=(30*a[0]+25)*a[4]+27*a[0]+30
    assert rational(b1-a[0])==0 and rational(b5+positive_num/positive_den)==0
    assert all(q>0 for q in s.Poly(positive_num,a[0],a[4]).coeffs())
    assert all(q>0 for q in s.Poly(positive_den,a[0],a[4]).coeffs())
    return {'forward_a1_identity':'b1=a1','forward_a5_identity':str(s.factor(b5)),
        'negative_sign_certificate':{'positive_numerator':str(positive_num),'positive_denominator':str(positive_den),
            'domain':'all donor alpha1,alpha5 positive on alpha2=0, within the rational inverse localization'},
        'reverse_a5_rule':'a5= -((27*b1+30)*b5+12*b1+15)/((30*b1+25)*b5)',
        'disposition':'positive_chart_interiors_do_not_overlap_on_this_selected_divisor_within_inverse_localization',
        'scope':'Both fixed moment-curve external Z fixtures; not arbitrary external Z or every boundary atlas chart.'}


def compare(rows,Z,shift,donor,receiver):
    source=rows[donor]['target_runs'][shift];other=rows[receiver]['target_runs'][shift]
    a,C,vals=parameters(source);vals[a[1]]=0;e=1
    N=normalize(C.subs(vals)*Z,[0,1]);emb=rows[receiver]['superfunction_runs'][0]['matches'][0]
    R,loc=inverse_A(N,setup_A(Z,emb)) if receiver==8 else inverse_H(N,setup_H(Z,emb))
    pars,gauge,_=extract(R,emb);assert pars[e]==0 and all(q!=0 for q in loc+gauge)
    assert all(pars[j]!=0 for j in range(8) if j!=e)
    _,D,_=parameters(other);rv=dict(zip(a,pars));assert normalize(D.subs(rv)*Z,[0,1])==N
    coords=[(i,j) for i in range(2) for j in range(6) if j not in (0,1)];free=[j for j in range(8) if j!=e]
    Js=[];LJs=[]
    for chart,values in [(C,vals),(D,rv)]:
        Y=chart.subs(values)*Z;J,actual=target_jac(Y,[chart.diff(z).subs(values)*Z for z in a],[0,1]);assert actual==coords and J.det()!=0
        Js.append(J);LJs.append(J[:,free]*s.diag(*[values[a[j]] for j in free]))
    selected=next(I for I in itertools.combinations(range(8),7) if all(J[list(I),:].det()!=0 for J in LJs))
    quad=[0,1,2,3];assert s.Matrix.vstack(N,Z[quad,:]).det()==0
    grad=[]
    for i,j in coords:
        E=s.zeros(2,6);E[i,j]=1
        grad.append(s.Matrix.vstack(E[0,:],N[1,:],Z[quad,:]).det()+s.Matrix.vstack(N[0,:],E[1,:],Z[quad,:]).det())
    grad=s.Matrix(1,8,grad);routes=[]
    for J,LJ,values in zip(Js,LJs,[vals,rv]):
        normals=grad*J;slope=normals[e]
        assert slope!=0 and all(normals[j]==0 for j in free)
        det=s.factor(LJ[list(selected),:].det());detD=s.factor(s.Matrix.vstack(normals,J[list(selected),:]).det())
        routeA=s.factor((-1)**e/det);routeB=s.factor(slope/(s.prod(values[a[j]] for j in free)*detD))
        assert routeA==routeB and -routeA!=routeB
        routes.append({'boundary_log_jacobian':str(det),'normal_slope':str(slope),
            'source_residue_then_pushforward':str(routeA),'top_pushforward_then_shared_bracket_residue':str(routeB),
            'orientation_failure_residual':str(-routeA-routeB)})
    rho=[s.Rational(r['source_residue_then_pushforward']) for r in routes]
    difference=s.factor(rho[0]-rho[1]);total=s.factor(rho[0]+rho[1]);assert difference!=0 and total!=0
    donor_minors=[s.factor(C.subs(vals)[:,list(pair)].det()) for pair in itertools.combinations(range(8),2)]
    receiver_minors={','.join(str(j+1) for j in pair):s.factor(D.subs(rv)[:,list(pair)].det()) for pair in itertools.combinations(range(8),2)}
    assert all(v>=0 for v in donor_minors) and any(v<0 for v in receiver_minors.values())
    a5_forward=-3*(4*vals[a[0]]+5)/((30*vals[a[0]]+25)*vals[a[4]]+27*vals[a[0]]+30)
    if donor==5:assert pars[0]==vals[a[0]] and pars[4]==a5_forward
    else:
        assert pars[0]==vals[a[0]]
        assert pars[4]==-((27*vals[a[0]]+30)*vals[a[4]]+12*vals[a[0]]+15)/((30*vals[a[0]]+25)*vals[a[4]])
    return {'positive_Z_moment_shift':shift,'donor_history':donor,'receiver_history':receiver,
        'shared_divisor':'Y1234=0','source_boundary':'alpha2=0 in both charts',
        'donor_parameters':{str(z):str(vals[z]) for z in a},'receiver_parameters':{str(z):str(rv[z]) for z in a},
        'receiver_localization_values':[str(v) for v in loc+gauge],
        'receiver_negative_source_minors':{k:str(v) for k,v in receiver_minors.items() if v<0},
        'algebraic_overlap':'regular inverse and forward target reconstruction verified',
        'positive_overlap':False,'positive_overlap_disposition':'receiver_alpha5_and_some_ordered_source_minors_negative',
        'target_coordinate_order':[[i+1,j+1] for i,j in coords],
        'selected_common_target_coordinate_indices':list(selected),
        'target_boundary_point':[str(N[i,j]) for i,j in coords],'routes':routes,
        'receiver_over_donor_density_ratio':str(s.factor(rho[1]/rho[0])),
        'density_difference':str(difference),'density_sum':str(total),
        'residual_disposition':'nonzero algebraic continuation residuals retained; not a positive shared-branch or weighted cancellation counterexample'}


def main():
    prior=json.loads((ROOT/PRIOR).read_text());inv=json.loads((ROOT/INVERSES).read_text())
    for r,checker in [(prior,'research/benincasa/checkers/check_three_composite_normalizations.py'),
                      (inv,'research/benincasa/checkers/check_three_composite_inverse_normals.py')]:
        for p,h in r['source_sha256'].items():assert sha256((ROOT/p).read_bytes()).hexdigest()==h,p
        assert r['checker_sha256']==sha256((ROOT/checker).read_bytes()).hexdigest()
    rows={r['history_index']:r for r in prior['rows']};certificates=[];runs=[]
    for shift in (0,1):
        Z=s.Matrix([[s.Integer(j+shift)**k for k in range(6)] for j in range(1,9)])
        certificates.append({'positive_Z_moment_shift':shift,**symbolic_nonoverlap(rows,Z)})
        for donor,receiver in [(5,8),(8,5)]:runs.append(compare(rows,Z,shift,donor,receiver))
    checks={'four_regular_algebraic_overlap_reconstructions':True,'eight_shared_normal_local_residue_squares':True,
        'four_positive_overlap_candidates_rejected_by_negative_parameters_and_minors':True,
        'two_symbolic_forward_sign_certificates_for_positive_boundary_chart_interiors':True,
        'four_density_differences_and_sums_nonzero_retained':True,'eight_orientation_hostiles_nonzero':True}
    paths=[PRIOR,INVERSES,'research/benincasa/checkers/check_three_composite_normalizations.py',
        'research/benincasa/checkers/check_three_composite_inverse_normals.py',
        'research/benincasa/checkers/check_composite_nonlinear_target_normal.py',
        'research/benincasa/checkers/check_composite_root_normalization.py']
    out={'schema':'marici.benincasa.shared-composite-physical-facet.v1','histories':[5,8],'runs':runs,
        'symbolic_nonoverlap_certificates':certificates,'checks':checks,'passed':True,
        'disposition':'regular_algebraic_common_divisor_but_selected_positive_branches_nonoverlapping',
        'claim_boundary':'Same Y1234 target points, source-derived inverse charts, fixed source dlog orientation and common tangent entries. No positive cancellation/refutation asserted; no weighted coefficients fitted. Sign certificate covers this localized boundary chart at two fixed Z, not the full external/BCFW atlas.',
        'next_action':'Test a different physical shared branch (histories8 and9 alpha6=0 on Y1267) with the same inverse/localization/positivity criteria; if nonoverlap, retain it and search actual shared codimension-two strata rather than pairing equal divisor labels.',
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    path=ROOT/'research/benincasa/results/shared_composite_physical_facet.json';path.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'checks':checks,'disposition':out['disposition'],
        'density_ratios':[r['receiver_over_donor_density_ratio'] for r in runs]},indent=2))


if __name__=='__main__':main()
