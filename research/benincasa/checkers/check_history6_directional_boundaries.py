#!/usr/bin/env python3
"""Two-chart directional residues and their actual common six-form image."""
import json
import itertools
from hashlib import sha256
from pathlib import Path
from check_three_composite_internal_gluings import s, normalize, target_jac
from check_paired_composite_corner_residues import sign
ROOT=Path(__file__).resolve().parents[3]
BLOWUP='research/benincasa/results/history6_target_blowup.json'
DIAGNOSTIC='research/benincasa/results/history6_b3_boundary.json'
CHART='research/benincasa/results/history6_common_corner.json'


def main():
    blown=json.loads((ROOT/BLOWUP).read_text());old=json.loads((ROOT/DIAGNOSTIC).read_text());chart=json.loads((ROOT/CHART).read_text())
    for receipt in (blown,old,chart):
        assert receipt['passed']
        for p,h in receipt['source_sha256'].items():assert sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    assert blown['checker_sha256']==sha256((ROOT/'research/benincasa/checkers/check_history6_target_blowup.py').read_bytes()).hexdigest()
    T,R,S,V=s.symbols('T R S V');b=s.symbols('b1:9');b1,b2,b3,b4,b5,b6,b7,b8=b
    g=(b4+R*T+T)/((b4+T)*(R+1));h=s.factor(1-g)
    gg=s.factor(g.subs({T:V*S,R:1/V},simultaneous=True));hh=s.factor(1-gg)
    f0=1/(R+1);fB=R/(R+1)
    # Exceptional seven-form coefficients in b1,direction,b4..b8 order.
    # The complementary exceptional coefficients include the transition sign.
    other0=s.factor(-gg.subs(S,0));otherB=s.factor(-hh.subs(S,0))
    assert s.factor(other0+f0.subs(R,1/V))==0
    assert s.factor(otherB+fB.subs(R,1/V))==0
    results=[]
    for name,z,at,A,B in [('R0',R,0,f0,fB),('Rminus1',R,-1,f0,fB),('Rinfinity_V0',V,0,other0,otherB)]:
        # Direction is index1 in the exceptional seven-form, deletion sign-1.
        a=s.factor(-s.residue(A/z,z,at));bb=s.factor(-s.residue(B/z,z,at))
        results.append({'direction':name,'chart_coordinate':str(z),'equation':str(z-at),
            'exceptional_then_direction_K0':str(a),'exceptional_then_direction_B22':str(bb),
            'total':str(a+bb),'positive_direction_boundary':at==0})
    assert [(r['exceptional_then_direction_K0'],r['exceptional_then_direction_B22']) for r in results]==[('-1','0'),('1','-1'),('0','1')]
    assert sum(s.Rational(r['exceptional_then_direction_K0']) for r in results)==0
    assert sum(s.Rational(r['exceptional_then_direction_B22']) for r in results)==0
    # The meromorphic pole R=-1 is also V=-1. Ordinary six-form residues
    # are coordinate-invariant; no seven-form sign is silently discarded.
    alternate=[s.factor(-s.residue(A/V,V,-1)) for A in (other0,otherB)]
    assert alternate==[s.Integer(1),s.Integer(-1)]
    # Full decorated top order b1,T,R,... has coefficient-g; other chart
    # b1,S,V,... has coefficient+gg. Reversing the two residue orders must
    # negate each split at these now-resolved normal crossings.
    for row in results:
        if row['chart_coordinate']=='R':
            first,second=T,R;at=s.Integer(0) if row['direction']=='R0' else s.Integer(-1)
            topA,topB=-g,-h
        else:
            first,second=S,V;at=s.Integer(0);topA,topB=gg,hh
        parity,_=sign([2,1])
        reverse=[]
        for w in (topA,topB):
            reverse.append(s.factor(parity*s.residue(s.residue(w/(first*second),second,at),first,0)))
        assert reverse==[-s.Rational(row['exceptional_then_direction_K0']),-s.Rational(row['exceptional_then_direction_B22'])]
        row['direction_then_exceptional_K0']=str(reverse[0]);row['direction_then_exceptional_B22']=str(reverse[1])
    diagnostics=old['singular_intersection']['iterated_source_extractions']
    assert results[0]['direction_then_exceptional_K0']==diagnostics[0]['K0_coefficient']
    assert results[0]['direction_then_exceptional_B22']==diagnostics[0]['B22_coefficient']
    assert results[2]['direction_then_exceptional_K0']==diagnostics[1]['K0_coefficient']
    assert results[2]['direction_then_exceptional_B22']==diagnostics[1]['B22_coefficient']
    C=s.Matrix([[s.sympify(q,locals={str(z):z for z in b}) for q in row] for row in chart['source_chart']])
    center=C.subs({b2:0,b3:0});six=[b1,b4,b5,b6,b7,b8]
    Cr=C.subs({b2:R*T,b3:T},simultaneous=True)
    Cs=C.subs({b2:S,b3:V*S},simultaneous=True)
    runs=[]
    for shift,vals in enumerate(([2,7,11,13,17,19],[3,11,13,17,19,23])):
        values=dict(zip(six,map(s.Integer,vals)))
        Z=s.Matrix([[s.Integer(j+shift)**k for k in range(6)] for j in range(1,9)])
        N=normalize(center.subs(values)*Z,[0,1])
        J,coords=target_jac(center.subs(values)*Z,[center.diff(z).subs(values)*Z*values[z] for z in six],[0,1]);assert J.rank()==6
        selected=next(list(I) for I in itertools.combinations(range(8),6) if J[list(I),:].det()!=0)
        density=s.factor(1/J[selected,:].det());assert density!=0
        images=[]
        for row in results:
            point=Cr.subs({T:0,R:0 if row['direction']=='R0' else -1}) if row['chart_coordinate']=='R' else Cs.subs({S:0,V:0})
            assert normalize(point.subs(values)*Z,[0,1])==N
            d0=s.factor(s.Rational(row['exceptional_then_direction_K0'])*density)
            dB=s.factor(s.Rational(row['exceptional_then_direction_B22'])*density)
            images.append({'direction':row['direction'],'K0_common_target_density':str(d0),
                'B22_common_target_density':str(dB),'target_image_rank':6,
                'provenance':('positive_direction_endpoint' if row['positive_direction_boundary'] else 'extra_meromorphic_pole_not_positive_direction')})
        assert sum(s.Rational(q['K0_common_target_density']) for q in images)==0
        assert sum(s.Rational(q['B22_common_target_density']) for q in images)==0
        endpoint0=s.factor(s.Rational(images[0]['K0_common_target_density'])+s.Rational(images[2]['K0_common_target_density']))
        endpointB=s.factor(s.Rational(images[0]['B22_common_target_density'])+s.Rational(images[2]['B22_common_target_density']))
        assert endpoint0==-density and endpointB==density and endpoint0+endpointB==0
        runs.append({'positive_Z_moment_shift':shift,'common_target_coordinate_indices':selected,
            'common_target_six_log_reference_density':str(density),'directional_residue_images':images,
            'all_three_direction_K0_sum':'0','all_three_direction_B22_sum':'0',
            'positive_endpoints_only_K0_sum':str(endpoint0),'positive_endpoints_only_B22_sum':str(endpointB),
            'positive_endpoints_transported_total_sum':'0','endpoint_orientation_flip_K0_defect':str(2*density)})
    paths=[BLOWUP,DIAGNOSTIC,CHART,'research/benincasa/checkers/check_history6_target_blowup.py',
        'research/benincasa/checkers/check_three_composite_internal_gluings.py','research/benincasa/checkers/check_paired_composite_corner_residues.py']
    out={'schema':'marici.benincasa.history6-directional-boundaries.v1','history_index':6,
        'residue_reference_order':[str(z) for z in six],'directional_source_and_decorated_target_routes':results,
        'Rminus1_complementary_chart_residues':list(map(str,alternate)),
        'original_order_diagnostics_recovered':True,'runs':runs,'passed':True,
        'scope':'Resolved local two-chart differential residue routes, signed endpoint matching, and common ordinary target six-form images. The extra pole is meromorphic, not a positive BCFW boundary; zero full-projective-direction sums are not weighted A3 chain admission.',
        'not_supplied':['ordinary blowdown exceptional seven-form','physical boundary-supercomponent extraction retaining direction','global BCFW orientation and covering','normalized weighted nine-form sector map'],
        'next_action':'Type the actual coefficient-weighted differential maps and their source/supercomponent bridge explicitly, auditing whether bosonization at a reference Y reproduces the unupdated full superfunction rather than only scalar ratios. Preserve nonzero positive-endpoint split sums and the indispensable meromorphic pole.',
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (ROOT/'research/benincasa/results/history6_directional_boundaries.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'directions':results,'runs':runs},indent=2))

if __name__=='__main__':main()
