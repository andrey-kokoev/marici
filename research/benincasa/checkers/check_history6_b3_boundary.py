#!/usr/bin/env python3
"""Regular b3=0 quotient split square; retain singular adjacent corners."""
import json
import itertools
from hashlib import sha256
from pathlib import Path
from check_three_composite_internal_gluings import s, normalize, target_jac, gradient
from check_paired_composite_corner_residues import raw_bracket, sign
ROOT=Path(__file__).resolve().parents[3]
PRIOR='research/benincasa/results/history6_quotient_boundary.json'
CHART='research/benincasa/results/history6_common_corner.json'
QUAD=(1,2,3,8)


def main():
    prior=json.loads((ROOT/PRIOR).read_text());chart=json.loads((ROOT/CHART).read_text())
    assert prior['passed'] and chart['passed']
    for r in (prior,chart):
        for p,h in r['source_sha256'].items():assert sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    assert prior['checker_sha256']==sha256((ROOT/'research/benincasa/checkers/check_history6_quotient_boundary.py').read_bytes()).hexdigest()
    b=s.symbols('b1:9');b1,b2,b3,b4,b5,b6,b7,b8=b
    C=s.Matrix([[s.sympify(x,locals={str(z):z for z in b}) for x in row] for row in chart['source_chart']])
    g=s.sympify(prior['source_c6'],locals={str(z):z for z in b});h=s.factor(1-g)
    assert g.subs(b3,0)==0 and h.subs(b3,0)==1
    e=2;free=[j for j in range(8) if j!=e];parity=(-1)**e
    assert parity==1
    # Exact ordinary source-normal Laurent coefficients, prior to any target
    # pushforward: quotient K0 has canceled its b3 pole rather than contracted.
    assert s.factor(g/b3).subs(b3,0)==(b2+b4)/(b2*b4)
    assert s.residue(g/b3,b3,0)==0 and s.residue(h/b3,b3,0)==1
    runs=[]
    for shift,values in enumerate(([2,3,5,7,11,13,17,19],[3,5,7,11,13,17,19,23])):
        sample=dict(zip(b,map(s.Integer,values)));v=sample|{b3:s.Integer(0)}
        Z=s.Matrix([[s.Integer(j+shift)**k for k in range(6)] for j in range(1,9)])
        raw=s.factor(raw_bracket(C,Z,QUAD));factor=s.factor(raw/b3)
        assert raw.subs(b3,0)==0 and factor.subs(v)!=0
        assert s.factor(raw/(3628800*b3*b6*b7))==1
        original_den=[raw_bracket(C,Z,q) for q in ((5,8,1,2),(6,1,2,3))]
        assert all(q.subs(v)!=0 for q in original_den)
        Cn=C.subs(v);Y=Cn*Z;N=normalize(Y,[0,1])
        assert all(Cn[:,list(I)].det()>=0 for I in itertools.combinations(range(8),2))
        J,coords=target_jac(Y,[C.diff(z).subs(v)*Z for z in b],[0,1]);assert J.det()!=0
        tangent=J[:,free]*s.diag(*[v[b[j]] for j in free]);assert tangent.rank()==7
        selected=next(list(I) for I in itertools.combinations(range(8),7) if tangent[list(I),:].det()!=0)
        grad=gradient(N,Z,QUAD,coords);B=grad*J
        assert B[0,e]!=0 and all(B[0,j]==0 for j in free)
        pivot=s.factor((C*Z)[:,[0,1]].det());assert pivot.subs(v)!=0
        slope=s.factor(factor.subs(v)/pivot.subs(v));assert slope==B[0,e]
        det7=s.factor(tangent[selected,:].det())
        D=s.factor(parity/det7)
        det8=s.factor(s.Matrix.vstack(B,J[selected,:]).det());assert det8!=0
        targetD=s.factor(slope/(s.prod(v[b[j]] for j in free)*det8));assert targetD==D
        # Invertibility of the ambient germ makes the quotient coefficient
        # analytic in this target normal, with value0 and linear zero.
        derivative=s.factor(s.diff(g,b3).subs(v));assert derivative!=0
        target_weight_slope=s.factor(derivative/slope);assert target_weight_slope!=0
        top0finite=s.factor(derivative/(s.prod(v[b[j]] for j in free)*det8))
        assert top0finite!=0
        split0=s.factor(g.subs(v)*D);splitB=s.factor(h.subs(v)*D)
        assert split0==0 and splitB==D
        assert -2*splitB!=0
        # The minor56 merger is a regular rank7 image, not a contraction.
        # Y1238 comprises physical adjacent pairs23 and81.
        assert {2,3,8,1}==set(QUAD)
        runs.append({'positive_Z_moment_shift':shift,'boundary_parameters':{str(z):str(q) for z,q in v.items()},
            'source_minor56':str(s.factor(C[:,[4,5]].det())),
            'raw_target_Y1238':str(raw),'normalized_normal_slope':str(slope),
            'source_quotient_denominator_values':[str(q.subs(v)) for q in original_den],
            'ambient_target_rank':8,'target_boundary_rank':7,'chosen_target_coordinate_indices':selected,
            'transported_source_residue_then_pushforward':str(D),'transported_top_then_target_residue':str(targetD),
            'K0_source_residue_then_pushforward':'0','K0_top_then_target_residue':'0',
            'B22_source_residue_then_pushforward':str(splitB),'B22_top_then_target_residue':str(targetD),
            'K0_target_coefficient_first_normal_derivative':str(target_weight_slope),
            'K0_finite_top_density_on_boundary_normal_chart':str(top0finite),
            'split_recombination_defect':'0','B22_orientation_flip_defect':str(-2*splitB),
            'disposition':'regular_rank7_physical_bracket_branch_K0_zero_from_pole_cancellation_not_contraction'})
    # At the excluded intersection b2=b3=0, g is not regular: two positive
    # approaches give different limits. Normal crossings for omegaF alone
    # do not imply normal crossings for its coefficient-weighted summands.
    t,rho=s.symbols('t rho',positive=True)
    approach=s.factor(s.limit(g.subs({b2:rho*t,b3:t}),t,0));assert approach==1/(rho+1)
    orders=[]
    for indices in ([1,2],[2,1]):
        first,second=[b[j] for j in indices];sgn,_=sign(indices)
        r0=s.factor(sgn*s.residue(s.residue(g/(first*second),first,0),second,0))
        rB=s.factor(sgn*s.residue(s.residue(h/(first*second),first,0),second,0))
        assert r0+rB==sgn
        orders.append({'deleted_order':[str(first),str(second)],'parity':sgn,
            'K0_coefficient':str(r0),'B22_coefficient':str(rB),'transported_total':str(sgn)})
    assert [q['K0_coefficient'] for q in orders]==['1','0']
    assert [q['B22_coefficient'] for q in orders]==['0','-1']
    paths=[PRIOR,CHART,'research/benincasa/checkers/check_history6_quotient_boundary.py',
        'research/benincasa/checkers/check_three_composite_internal_gluings.py','research/benincasa/checkers/check_paired_composite_corner_residues.py']
    out={'schema':'marici.benincasa.history6-b3-boundary.v1','history_index':6,
        'source_equation':'b3=0; other b positive','target_normal':'normalized <Y1238>',
        'source_orientation':'increasing b1..b8 dlog order; delete b3 with parity+1',
        'runs':runs,'singular_intersection':{'equations':['b2=0','b3=0'],'positive_approach':'b2=rho*t,b3=t,t->0+',
            'coefficient_limit':str(approach),'iterated_source_extractions':orders,
            'disposition':'coefficient_indeterminate_corner; added pole b2+b3 passes through it. Individual K0/B22 order extractions do not anticommute; combined transported form does. No regular target corner square claimed here.'},
        'passed':True,'scope':'Actual quotient-weighted differential extraction on one regular physical bracket boundary; source-only excluded-intersection diagnostics, not full physical supercomponent extraction or weighted-chain closure.',
        'next_action':'Resolve the b2=b3=0 coefficient indeterminacy using a positive radial/blowup chart and construct its target image/rank and localized residue routes. Keep extra meromorphic pole accounting and the boundary-supercomponent compatibility map separate.',
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (ROOT/'research/benincasa/results/history6_b3_boundary.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'normal':'Y1238','split_boundary_densities':[[r['K0_source_residue_then_pushforward'],r['B22_source_residue_then_pushforward']] for r in runs],
        'excluded_corner_limit':str(approach),'ordered_source_diagnostics':orders},indent=2))

if __name__=='__main__':main()
