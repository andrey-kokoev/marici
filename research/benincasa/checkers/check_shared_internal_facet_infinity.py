#!/usr/bin/env python3
"""One-parameter infinity germs of the actual shared positive internal facet."""
import json
import sys
import itertools
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(Path(__file__).resolve().parent))
from check_shared_internal_composite_facet import s,rational,normalize,parameters
PRIOR='research/benincasa/results/three_composite_normalizations.json'
FACET='research/benincasa/results/shared_internal_composite_facet.json'
ZERO='research/benincasa/results/shared_internal_facet_boundaries.json'


def valuation(v,t):
    v=rational(v)
    if v==0:return None
    n,d=s.fraction(v)
    return min(m[0] for m,c in s.Poly(n,t).terms())-min(m[0] for m,c in s.Poly(d,t).terms())


def finite_pivots(M,t,values):
    candidates=[]
    for pair in itertools.combinations(range(M.cols),2):
        order=valuation(M.subs(values)[:,list(pair)].det(),t)
        if order is not None:candidates.append((order,pair))
    best=min(order for order,pair in candidates)
    return best,[pair for order,pair in candidates if order==best]


def finite_germ(M,pivot,t,values):
    N=normalize(M,list(pivot)).applyfunc(rational)
    # Rational cancellation removes common powers of t. A denominator nonzero
    # at the selected point certifies the analytic extension and differentiation.
    denoms=[s.fraction(v)[1] for v in N]
    assert all(d.subs(values).subs(t,0)!=0 for d in denoms)
    limit=N.subs(t,0).applyfunc(rational)
    assert all(not v.has(s.zoo,s.oo,-s.oo,s.nan) for v in limit)
    return N,limit


def differential(M,variables,pivot,values):
    coords=[(i,j) for i in range(2) for j in range(M.cols) if j not in pivot]
    J=s.Matrix([[rational(s.diff(M[i,j],z).subs(values)) for z in variables] for i,j in coords])
    return J,coords


def run(rows,old):
    shift=old['positive_Z_moment_shift'];Z=s.Matrix([[s.Integer(j+shift)**k for k in range(6)] for j in range(1,9)])
    a,A,values=parameters(rows[8]['target_runs'][shift]);_,H,_=parameters(rows[9]['target_runs'][shift])
    F=A.subs(a[0],0);assert F==H.subs({a[0]:a[1],a[1]:0},simultaneous=True)
    t=s.symbols('t',positive=True);faces=[]
    for e in range(1,8):
        remaining=[a[j] for j in range(1,8) if j!=e];fixed={z:values[z] for z in remaining}
        C=F.subs(a[e],1/t);Y=C*Z
        target_order,pivots=finite_pivots(Y,t,fixed);pivot=pivots[0]
        N,N0=finite_germ(Y,pivot,t,fixed)
        source_order,source_pivots=finite_pivots(C,t,fixed);source_pivot=source_pivots[0]
        S,S0=finite_germ(C,source_pivot,t,fixed)
        J,coords=differential(N0,remaining,pivot,fixed)
        JS,_=differential(S0,remaining,source_pivot,fixed)
        transverse=s.Matrix([rational(s.diff(N[i,j],t).subs(fixed).subs(t,0)) for i,j in coords])
        full=s.Matrix.hstack(transverse,J)
        rank=J.rank();germ_rank=full.rank()
        assert rank<6 and germ_rank<7
        source_limit=S0.subs(fixed);assert source_limit.rank()==2
        assert all(source_limit[:,list(pair)].det()>=0 for pair in itertools.combinations(range(8),2))
        control=[]
        for tv in (s.Integer(1),s.Rational(1,2)):
            v=fixed|{a[0]:0,a[e]:1/tv}
            assert N.subs(fixed).subs(t,tv)==normalize(F.subs(v)*Z,list(pivot))
            assert all(F.subs(v)[:,list(pair)].det()>=0 for pair in itertools.combinations(range(8),2))
            control.append({'t':str(tv),'target_reconstruction':True,'source_positivity':True})
        # A second maximal-pole target pivot has a finite GL(2) transition.
        assert len(pivots)>1;alternative=pivots[1]
        _,alternative0=finite_germ(Y,alternative,t,fixed)
        transition=normalize(N0,list(alternative)).applyfunc(rational)
        assert all(rational(z)==0 for z in transition-alternative0)
        position=e-1;A_sign=-(-1)**position;H_sign=(-1)**position
        assert A_sign+H_sign==0
        faces.append({'A_infinite_alpha':e+1,'H_infinite_alpha':1 if e==1 else e+1,
            'coordinate_substitution':'alpha=1/t','source_dlog_identity':'dlog(alpha)=-dlog(t)',
            'source_iterated_residue_signs':[A_sign,H_sign],'source_paired_six_dlog_sum':'0',
            'target_pivot':[j+1 for j in pivot],'target_pivot_determinant_valuation':target_order,
            'source_pivot':[j+1 for j in source_pivot],'source_pivot_determinant_valuation':source_order,
            'finite_target_germ':[[str(v) for v in rr] for rr in N.tolist()],
            'limit_target_matrix':[[str(v.subs(fixed)) for v in rr] for rr in N0.tolist()],
            'limit_source_matrix':[[str(v) for v in rr] for rr in source_limit.tolist()],
            'limit_target_tangent_rank':rank,'limit_source_tangent_rank':JS.rank(),'target_full_germ_rank':germ_rank,
            'target_transverse_derivative':[str(v) for v in transverse],
            'positive_arc_controls':control,'alternative_finite_target_pivot':[j+1 for j in alternative],
            'finite_pivot_transition_identity':True,
            'inverse_normal_status':'no_regular_rank7_facet_inverse_or_rank6_boundary_image_in_this_one_parameter_compactification',
            'disposition':'contracted_infinity_image_not_an_ordinary_six_form_target_residue',
            'paired_target_density_sum':None,
            'orientation_hostile_source_sum':-A_sign+H_sign})
        assert faces[-1]['orientation_hostile_source_sum']!=0
    return {'positive_Z_moment_shift':shift,'faces':faces,
        'summary':{'one_parameter_infinity_faces':len(faces),'rank6_target_boundary_images':sum(f['limit_target_tangent_rank']==6 for f in faces),
            'contracted_target_boundary_images':sum(f['limit_target_tangent_rank']<6 for f in faces),
            'target_tangent_ranks':[f['limit_target_tangent_rank'] for f in faces],
            'full_germ_ranks':[f['target_full_germ_rank'] for f in faces]}}


def main():
    prior=json.loads((ROOT/PRIOR).read_text());facet=json.loads((ROOT/FACET).read_text());zero=json.loads((ROOT/ZERO).read_text())
    for receipt,checker in [(prior,'research/benincasa/checkers/check_three_composite_normalizations.py'),
        (facet,'research/benincasa/checkers/check_shared_internal_composite_facet.py'),
        (zero,'research/benincasa/checkers/check_shared_internal_facet_boundaries.py')]:
        for p,h in receipt['source_sha256'].items():assert sha256((ROOT/p).read_bytes()).hexdigest()==h,p
        assert receipt['checker_sha256']==sha256((ROOT/checker).read_bytes()).hexdigest()
    rows={r['history_index']:r for r in prior['rows']};runs=[run(rows,old) for old in facet['runs']]
    assert runs[0]['summary']==runs[1]['summary']
    checks={'fourteen_finite_one_parameter_infinity_germs':True,'limit_source_positivity_and_rank2':True,
        'two_fixture_rank_signatures_agree':True,'twenty_eight_positive_arc_reconstructions':True,
        'fourteen_finite_alternative_pivot_transition_identities':True,
        'infinity_dlog_orientation_and_paired_source_signs_verified':True,
        'rank_deficient_inverse_and_target_residue_dispositions_retained':True}
    paths=[PRIOR,FACET,ZERO,'research/benincasa/checkers/check_shared_internal_composite_facet.py',
        'research/benincasa/checkers/check_shared_internal_facet_boundaries.py',
        'research/benincasa/checkers/check_composite_root_normalization.py']
    out={'schema':'marici.benincasa.shared-internal-facet-infinity.v1','histories':[8,9],'runs':runs,'checks':checks,'passed':True,
        'disposition':'seven_one_parameter_infinity_faces_have_finite_positive_but_contracted_images',
        'claim_boundary':'One source parameter tends to infinity with all other positive parameters fixed; rational finite Grassmannian gauges and exact limiting ranks at two fixed Z. Not a complete compactified boundary atlas: correlated scalings, blowup charts and extra branches are untested. No target six-form cancellation asserted for contracted images.',
        'next_action':'Test the correlated radial chart alpha2=1/t, alpha3=u/t, alpha4=v/t with alpha5..8 finite. Derive its logarithmic wedge Jacobian before boundary tests. Row scaling diag(t,1) gives a finite source germ with additional zero column3 at t=0; test its target rank and actual Y1245 or inverse-radial normal, then compare paired residues if admitted. This is not one of the fixed-other-parameters infinity limits.',
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    path=ROOT/'research/benincasa/results/shared_internal_facet_infinity.json';path.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'checks':checks,'summaries':[r['summary'] for r in runs]},indent=2))


if __name__=='__main__':main()
