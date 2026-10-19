#!/usr/bin/env python3
"""Canonical versus split Plucker divisors, pivot charts and cycle-lift ambiguity."""
import itertools
import json
from hashlib import sha256
from pathlib import Path
from check_history6_boundary_berezin_current import s, normalize
ROOT=Path(__file__).resolve().parents[3]
LINK='research/benincasa/results/history6_current_normal_link.json'
CHART='research/benincasa/results/history6_common_corner.json'
LATTICE='research/benincasa/results/history6_current_contour_lattice.json'
SOURCE='research/sources/nima/papers/six-point-nmhv/1212.5605/positive_grassmannian_update.tex'


def main():
    link=json.loads((ROOT/LINK).read_text());chart=json.loads((ROOT/CHART).read_text());lattice=json.loads((ROOT/LATTICE).read_text())
    for receipt in (link,chart,lattice):
        assert receipt['passed']
        for p,h in receipt['source_sha256'].items():assert sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    assert link['checker_sha256']==sha256((ROOT/'research/benincasa/checkers/check_history6_current_normal_link.py').read_bytes()).hexdigest()
    b=s.symbols('b1:9');b1,x,y,B,b5,b6,b7,b8=b;labels=[1,2,3,5,6,8]
    C=s.Matrix([[s.sympify(q,locals={str(z):z for z in b}) for q in row] for row in chart['source_chart']])[:,[0,1,2,4,5,7]]
    D=normalize(C,[0,1]).applyfunc(s.factor)
    pairs=list(itertools.combinations(range(6),2))
    def minors(Q):return {(labels[i],labels[j]):s.factor(Q[:,[i,j]].det()) for i,j in pairs}
    p=minors(D)
    assert p[3,6]==b5*b7*(x+y) and p[5,8]==b6*b8*(y+B)
    assert p[3,5]==b5*b6*x and p[5,6]==b6*b7*y
    assert s.factor(p[3,6]*p[5,8]-p[3,5]*p[6,8]-p[3,8]*p[5,6])==0
    g=s.factor(p[5,6]*p[3,8]/(p[3,6]*p[5,8]))
    h=s.factor(p[3,5]*p[6,8]/(p[3,6]*p[5,8]))
    assert s.factor(g+h-1)==0
    cyclic=[(1,2),(2,3),(3,5),(5,6),(6,8),(1,8)]
    assert (3,6) not in cyclic and (5,8) not in cyclic
    # Closing cyclic minor is p81=-p18. Record this orientation correction,
    # then use increasing-index positive cyclic minors in the frozen source.
    assert D[:,[5,0]].det()==-p[1,8]
    den=s.prod(p[q] for q in cyclic)
    free=[(i,j) for i in range(2) for j in range(2,6)]
    J=s.Matrix([[s.diff(D[i,j],u) for u in b] for i,j in free])
    jac=s.factor(J.det());assert jac==b5*b6*b7*b8
    canonical=s.factor(jac/den);assert canonical==1/s.prod(b)
    # Local defining equations and positive closure: sums of two positive
    # source parameters have no interior zeros. In the nonnegative closure
    # their zeros force BOTH consecutive source-boundary minors to vanish.
    extra=[{'plucker':[3,6],'equation':str(x+y),'adjacent_positive_boundary_parameters':['b2','b3'],
            'positive_closure':'b2=b3=0; codim2 on the declared nonzero base localization'},
           {'plucker':[5,8],'equation':str(y+B),'adjacent_positive_boundary_parameters':['b3','b4'],
            'positive_closure':'b3=b4=0; codim2 on the declared nonzero remaining parameters'}]
    fixtures=[]
    eta=s.Symbol('eta')
    for label,values,normal in [('p36',[2,-1,1,3,5,7,11,13],{x:-y+eta}),
                               ('p58',[2,5,-3,3,5,7,11,13],{y:-B+eta})]:
        v=dict(zip(b,map(s.Integer,values)));pv={q:value.subs(v) for q,value in p.items()}
        assert all(pv[q]!=0 for q in cyclic)
        vanishing=[q for q,value in pv.items() if value==0]
        assert vanishing==([(3,6)] if label=='p36' else [(5,8)])
        assert jac.subs(v)!=0
        # Canonical source has no residue there; both split weights have a
        # genuine simple pole with opposite nonzero residues.
        canonical_res=s.factor(s.residue(canonical.subs(normal,simultaneous=True),eta,0).subs(v));assert canonical_res==0
        weights_res=[s.factor(s.residue(F.subs(normal,simultaneous=True),eta,0).subs(v)) for F in (g,h)]
        assert weights_res[0]!=0 and weights_res[1]==-weights_res[0]
        admitted=[];excluded=[]
        for pivot in pairs:
            pivot_labels=(labels[pivot[0]],labels[pivot[1]])
            if pv[pivot_labels]==0:
                excluded.append(list(pivot_labels));continue
            H=D[:,list(pivot)].inv();P=(H*D).applyfunc(s.factor);pm=minors(P)
            # Exact invariant Plucker cross-ratio expressions, not pole
            # positions chosen anew in each gauge.
            gp=s.factor(pm[5,6]*pm[3,8]/(pm[3,6]*pm[5,8]))
            hp=s.factor(pm[3,5]*pm[6,8]/(pm[3,6]*pm[5,8]))
            assert s.factor(gp-g)==s.factor(hp-h)==0
            remaining=[j for j in range(6) if j not in pivot]
            chartJac=s.Matrix([[s.diff(P[i,j],u).subs(v) for u in b] for i in range(2) for j in remaining])
            chartdet=s.factor(chartJac.det());dh=s.factor(H.subs(v).det())
            assert chartdet==dh**6*jac.subs(v)
            cyclicden=s.prod(pm[q].subs(v) for q in cyclic)
            assert s.factor(chartdet/cyclicden-canonical.subs(v))==0
            admitted.append({'pivot':list(pivot_labels),'source_chart_volume_factor':str(dh**6),
                'canonical_density':str(s.factor(chartdet/cyclicden)),
                'split_weight_cross_ratios_preserved':True})
        assert len(admitted)==14 and len(excluded)==1
        fixtures.append({'divisor':label,'parameters':{str(u):str(value) for u,value in v.items()},
            'all_canonical_cyclic_minors_nonzero':True,'vanishing_plucker_minors':[list(q) for q in vanishing],
            'canonical_residue':'0','split_weight_residues':[str(q) for q in weights_res],
            'positive_locus_excluded_by_opposite_adjacent_minor_signs':True,
            'regular_pivot_chart_tests':admitted,'singular_pivot_excluded':excluded})
        assert pv[3,5]*pv[5,6]<0 if label=='p36' else pv[5,6]*pv[6,8]<0
    # Forgetting the additional central puncture gives the undecorated
    # direction complement P1 minus {0,infinity}. The kernel of induced
    # H1 map is the central-loop Z; lifts of C0 form a Z-torsor.
    R=s.Matrix(lattice['residue_matrix']);reduced=s.Matrix(lattice['quotient_period_matrix'])
    forget=s.Matrix([[1,0]]);assert forget.nullspace()==[s.Matrix([0,1])]
    n=s.Symbol('central_winding',integer=True);lift=s.Matrix([1,n])
    exceptional=reduced*lift;source=-exceptional
    assert source==s.Matrix([1-n,n]) and sum(source)==1
    assert reduced*s.Matrix([0,1])==s.Matrix([1,-1])
    # Total period descends to undecorated source homology, neither split
    # does. This is the extra physical datum, not a failed covariance law.
    assert (s.ones(1,2)*reduced)*s.Matrix([0,1])==s.zeros(1,1)
    assert all(q!=0 for q in reduced*s.Matrix([0,1]))
    text=(ROOT/SOURCE).read_text(encoding='utf-8')
    assert r'\label{cyclic_minor_top_form}' in text
    assert 'any non-consecutive minors appearing as factors' in text
    assert 'new, unwanted singularities for the top-cell' in text
    paths=[LINK,CHART,LATTICE,SOURCE,'research/benincasa/checkers/check_history6_current_normal_link.py']
    out={'schema':'marici.benincasa.history6-current-split-divisors.v1','history_index':6,
        'active_cell':'Local active six-label G(2,6) source canonical chart inside the fixed n8 history; not an uncomputed ambient n8 top-form residue certificate.',
        'source_authority':{'path':SOURCE,'section':'invariant_top_form_section','equation':'cyclic_minor_top_form',
            'scope':'Source explicitly excludes extra non-consecutive-minor poles from the canonical top-cell form; our split weights introduce such poles, not new canonical source boundaries.'},
        'active_labels':labels,'all_plucker_minors':{f'{q[0]},{q[1]}':str(value) for q,value in p.items()},
        'orientation_normalized_canonical_cyclic_minors':[list(q) for q in cyclic],
        'closing_minor_orientation':'p81=-p18; increasing-index closing p18 used consistently with the frozen positive source orientation.',
        'source_coordinate_Jacobian':str(jac),'canonical_pullback':str(canonical),
        'invariant_split_weights':{'K0':'p56*p38/(p36*p58)','B22':'p35*p68/(p36*p58)',
            'Plucker_relation':'p36*p58=p35*p68+p38*p56'},
        'extra_split_divisors':extra,'complex_divisor_fixtures':fixtures,
        'source_chart_transition':'In every regular tested pivot chart, d8Xprime/d8X=det(H)^6 and the active six cyclic-minor product scales by det(H)^6. Canonical source forms agree; both split cross-ratios agree as rational functions.',
        'normal_cycle_exact_sequence':'0 -> Z[Cminus1] -> H1(P1 minus {0,-1,infinity},Z) -> H1(P1 minus {0,infinity},Z) -> 0.',
        'local_cycle_lift_datum':{'undecorated_source_class':'C0 with positive normal-link source total period1',
            'all_decorated_lifts':'C0+n*Cminus1, n integer; source fixed-normal-orientation periods (1-n,n).',
            'source_periods':[str(q) for q in source],
            'two_product_torus_chambers':'n0 for radius_b2<radius_b3, n1 for radius_b2>radius_b3',
            'admission_condition':'Specify an owning-source-compatible oriented lift (central winding n) avoiding the weighted divisor, together with external current/contour compatibility. Canonical cell, total period and pivot covariance alone do not specify n.',
            'no_physical_choice_made':True},
        'descent_obstruction':'Each split period is nonzero on the central-loop kernel of the forgetful homology map, so neither descends to undecorated source contour homology without extra lift data. Their sum does descend.',
        'passed':True,'claim_boundary':'Exact local canonical-versus-decoration divisor classification, 28 actual regular pivot-coordinate/Jacobian tests, and contour-lift Z-torsor. No physical contour, global current gluing or weighted-sector admission inferred.',
        'next_action':'Compare the now explicit central-winding lift datum with the owning history boundary/residue word and prescribed normal orders: construct conditional ordered-residue lifts and test their compatibility under exchange of deletion order and the second split divisor p58. Do not infer a physical lift merely from source orientation or fit n to cancellation.',
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (ROOT/'research/benincasa/results/history6_current_split_divisors.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'extra_plucker_divisors':['p36','p58'],'canonical_source_residues':[0,0],
        'regular_chart_tests':sum(len(f['regular_pivot_chart_tests']) for f in fixtures),
        'source_lift_periods':out['local_cycle_lift_datum']['source_periods'],
        'split_descent_to_undecorated_contour':False,'physical_admission':False},indent=2))

if __name__=='__main__':main()
