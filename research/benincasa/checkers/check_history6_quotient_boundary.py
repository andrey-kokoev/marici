#!/usr/bin/env python3
"""Actual quotient coefficient pullback and localized F6 residue extraction."""
import json
import itertools
from hashlib import sha256
from pathlib import Path
from check_three_composite_internal_gluings import s, normalize, target_jac, gradient
from check_paired_composite_corner_residues import raw_bracket, sign
ROOT=Path(__file__).resolve().parents[3]
CROSS='research/benincasa/results/history6_twistor_cross_ratio.json'
CORNER='research/benincasa/results/history6_common_corner.json'
COMPOSITE='research/benincasa/results/three_composite_common_corner.json'
QUADS=[(6,8,1,2),(5,1,2,3),(5,8,1,2),(6,1,2,3)]


def main():
    cross=json.loads((ROOT/CROSS).read_text());prior=json.loads((ROOT/CORNER).read_text())
    for r in (cross,prior):
        assert r['passed']
        for p,h in r['source_sha256'].items():assert sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    b=s.symbols('b1:9');b1,b2,b3,b4,b5,b6,b7,b8=b
    C=s.Matrix([[s.sympify(x,locals={str(z):z for z in b}) for x in row] for row in prior['source_chart']])
    support=[0,1,2,4,5,7]
    # A generic active external basis: by multilinearity every bracket with
    # four active labels is the corresponding complement minor times det Z_S.
    Zbasis=s.zeros(8,6)
    for j,k in enumerate(support):Zbasis[k,j]=1
    generic=[s.factor(raw_bracket(C,Zbasis,q)) for q in QUADS]
    g=s.factor(1-generic[0]*generic[1]/(generic[2]*generic[3]))
    expected=b3*(b2+b3+b4)/((b2+b3)*(b3+b4))
    assert s.factor(g-expected)==0
    difference=s.factor(1-g);assert difference==b2*b4/((b2+b3)*(b3+b4))
    assert s.factor(g.subs(b2,0))==s.factor(g.subs(b4,0))==1
    assert g.subs({b2:0,b4:0})==1 and difference.subs({b2:0,b4:0})==0
    # Ordered coefficient extraction of the relative log forms. On this
    # localization the weights are regular, so Laurent cross terms vanish.
    parity,free=sign([1,3]);assert parity==-1
    six0=s.factor(parity*s.residue(s.residue(g/(b2*b4),b2,0),b4,0))
    sixB=s.factor(parity*s.residue(s.residue(difference/(b2*b4),b2,0),b4,0))
    assert six0==-1 and sixB==0
    full0=s.factor(g/s.prod(b));fullB=s.factor(difference/s.prod(b))
    assert s.factor(full0+fullB-1/s.prod(b))==0
    # Added poles in the rational continuation, outside the positive b chart.
    added=[]
    for z,at in ((b2,-b3),(b4,-b3)):
        deletion=(-1)**b.index(z)
        r0=s.factor(deletion*s.residue(g/z,z,at));rB=s.factor(deletion*s.residue(difference/z,z,at))
        assert r0!=0 and r0+rB==0
        added.append({'normal':str(z+b3),'coordinate':str(z),'K0_log_remaining_coefficient':str(r0),
            'B22_log_remaining_coefficient':str(rB),'sum':'0','domain':'meromorphic continuation; not reached inside strictly positive source chart'})
    b3res0=s.factor(s.residue(g/b3,b3,0));b3resB=s.factor(s.residue(difference/b3,b3,0))
    assert b3res0==0 and b3resB==1
    runs=[]
    composite=json.loads((ROOT/COMPOSITE).read_text())
    for old,comp in zip(prior['runs'],composite['runs']):
        shift=old['positive_Z_moment_shift']
        Z=s.Matrix([[s.Integer(j+shift)**k for k in range(6)] for j in range(1,9)])
        detZ=Z[support,:].det();assert detZ!=0
        pulls=[s.factor(raw_bracket(C,Z,q)) for q in QUADS]
        assert all(s.factor(p-detZ*q)==0 for p,q in zip(pulls,generic))
        actual=s.factor(1-pulls[0]*pulls[1]/(pulls[2]*pulls[3]));assert actual==g
        v={z:s.Rational(old['parameters'][str(z)]) for z in b}
        assert all(v[b[j]]>0 for j in free)
        denominators=[p.subs(v) for p in pulls[2:]];assert all(q!=0 for q in denominators)
        Cn=C.subs(v);Y=Cn*Z;N=normalize(Y,[0,1])
        J,coords=target_jac(Y,[C.diff(z).subs(v)*Z for z in b],[0,1]);assert J.det()!=0
        B=s.Matrix.vstack(*[gradient(N,Z,q,coords) for q in ((1,2,6,8),(1,2,3,5))])*J
        assert B[:,[1,3]].det()!=0
        selected=comp['common_target_coordinate_indices']
        tangent=J[:,free]*s.diag(*[v[b[j]] for j in free]);assert tangent.rank()==6
        D=s.factor(parity/tangent[selected,:].det());assert D==s.Rational(old['source_corner_then_pushforward'])
        prod=s.prod(v[b[j]] for j in free)
        full=s.Matrix.vstack(B,J[selected,:])
        targetD=s.factor(B[:,[1,3]].det()/(prod*full.det()));assert targetD==D
        rem=[j for j in range(8) if j!=1]
        mixedD=s.factor(-B[1,3]/(prod*s.Matrix.vstack(B[1,rem],J[selected,rem]).det()));assert mixedD==D
        # Target coefficient is regular at this actual normal crossing and
        # equals one. Its numerator correction has both normal factors.
        assert actual.subs(v)==1 and difference.subs(v)==0
        corrected_sum=s.factor(D+s.Rational(comp['three_composite_canonical_order_sum']));assert corrected_sum==0
        sample={z:s.Integer(j+2) for j,z in enumerate(b)}
        assert 0<g.subs(sample)<1 and 0<difference.subs(sample)<1
        runs.append({'positive_Z_moment_shift':shift,'raw_quotient_bracket_pullbacks':{str(q):str(p) for q,p in zip(QUADS,pulls)},
            'original_quotient_denominator_values_at_corner':[str(q) for q in denominators],
            'corner_c6':'1','corner_one_minus_c6':'0','ambient_target_rank':8,'corner_tangent_rank':6,
            'K0_source_then_pushforward':str(D),'K0_mixed_route':str(mixedD),'K0_target_iterated_residue':str(targetD),
            'B22_all_three_corner_routes':'0','three_composites_plus_quotient_K0_sum':str(corrected_sum),
            'orientation_flip_defect':str(-2*D)})
    paths=[CROSS,CORNER,COMPOSITE,'research/benincasa/checkers/check_history6_twistor_cross_ratio.py',
        'research/benincasa/checkers/check_history6_common_corner.py','research/benincasa/checkers/check_paired_composite_corner_residues.py']
    out={'schema':'marici.benincasa.history6-quotient-boundary.v1','history_index':6,
        'generic_external_basis_pullbacks':{str(q):str(p) for q,p in zip(QUADS,generic)},
        'source_c6':str(g),'source_one_minus_c6':str(difference),
        'positive_source_localization':'all b positive in the interior; corner b2=b4=0 with b1,b3,b5,b6,b7,b8 positive. Active external det Z_S nonzero. Original quotient denominators require b5*b7*(b2+b3) and b6*b8*(b3+b4) nonzero.',
        'source_corner_extraction':{'deleted_order':['b2','b4'],'deletion_parity':parity,
            'remaining_order':[str(b[j]) for j in free],'K0_coefficient':str(six0),'B22_coefficient':str(sixB),
            'reference_transition_determinant':prior['six_log_transition_determinant'],
            'K0_reference_coefficient':'1','B22_reference_coefficient':'0'},
        'meromorphic_added_pole_residues':added,
        'other_coordinate_boundary':{'equation':'b3=0; b2,b4 nonzero','K0_log_remaining_coefficient':str(b3res0),
            'B22_log_remaining_coefficient':str(b3resB),'disposition':'source calculation only; target differential square not yet constructed'},
        'runs':runs,'passed':True,
        'scope':'Actual Y-dependent quotient rational weight and local differential boundary extraction; not a full bosonized supercomponent theorem, ordinary canonical admission or global weighted comparison.',
        'prior_external_fixed_disposition':'Independent-base c6(t) multiplication remains valid in its relative module but is not the extraction of c6(Y,Z); its nonzero K0-only residuals are preserved, not superseded as identical-data tests.',
        'next_action':'Construct the b3=0 target boundary square for the quotient K0/B22 split, and separately establish a typed bosonized-supercomponent compatibility map; classify the added meromorphic poles rather than omit them from source-domain accounting.',
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (ROOT/'research/benincasa/results/history6_quotient_boundary.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'pullback':str(g),'corner_coefficients':[str(six0),str(sixB)],
        'added_poles':added,'corner_sums':[r['three_composites_plus_quotient_K0_sum'] for r in runs]},indent=2))

if __name__=='__main__':main()
