"""Zero-leading joint photon-cut fibres: cubic squares and wholly unseen quartic contacts."""
import argparse
from fractions import Fraction as Q
from itertools import product
import hashlib
import json
from pathlib import Path
import sys

HOME=Path(__file__).resolve().parents[1];ROOT=HOME.parents[1]
sys.path.insert(0,str(HOME/'checkers'))
import check_photon_general_degree6_cut_v1 as six
base=six.base;p=six.p
CONTRACT=HOME/'contracts/photon-zero-leading-fibres-v1.json';PROOF=HOME/'photon-zero-leading-fibres-v1.md'
TEST=HOME/'checkers/test_photon_zero_leading_fibres_v1.py';MANIFEST=HOME/'scc-models/photon-zero-leading-fibres-v1.json'
RESULT=HOME/'results/photon-zero-leading-fibres-v1.json'


def invariants(cubic):
    a,b,h=map(Q,cubic)
    return a*a,b*b,a*b,h*h,h*(10*a+b)


def expected_cut(z,cases):
    a,b,c,d,t=map(Q,z)
    out=((Q(),),)*4
    for weight,index in ((a,6),(b,9),(c,7),(d,11)):
        out=tuple(p.add(x,p.scale(weight,y)) for x,y in zip(out,cases[index]))
    return out[:3]+(p.scale(-t/960,six.prev.K),)


def extract(data6):
    get=lambda poly,n:Q(poly[n]) if n<len(poly) else Q()
    D,O,M,H=data6
    a=-672*get(M,3);d=80*get(O,2);b=960*get(D,2)-12*d
    c=96*(get(O,0)-d/480);t=-960*get(H,1)
    return a,b,c,d,t


def classify(data45,data6,cases):
    if len(data45)!=7 or any(map(Q,data45)):raise ValueError('not the complete zero-leading data stratum')
    data6=tuple(p.trim(tuple(map(Q,poly))) for poly in data6)
    a,b,c,d,t=extract(data6)
    if a<0 or b<0 or d<0 or a*b!=c*c:raise ValueError('nonreal cubic Gram/square data')
    delta=100*a+20*c+b
    if delta<0 or t*t!=d*delta:raise ValueError('single-minus square/linear consistency failed')
    if expected_cut((a,b,c,d,t),cases)!=data6:raise ValueError('cut polynomial outside cubic-square image')
    if a or b:
        if a:
            root=a;A=Q(1);B=c/a;denom=10*a+c
            H=t/denom if denom else Q()
        else:
            root=b;A=Q();B=Q(1);H=t/b
        if delta:
            return {'stratum':'pair-ordinary','root_square':root,'cubic_base':(A,B,H),'h_mode':'fixed',
                    'h_square':d/root,'cubic_components':2,'quartic_free_dimension':3,'sign_quotient':'one_R3'}
        branches=4 if d else 2
        return {'stratum':'pair-cancellation','root_square':root,'cubic_base':(A,B,Q()),
                'h_mode':'plus-minus-square-root' if d else 'fixed','h_square':d/root,
                'cubic_components':branches,'quartic_free_dimension':3,'sign_quotient':'two_R3' if d else 'one_R3'}
    if d:
        return {'stratum':'pure-h','root_square':d,'cubic_base':(Q(),Q(),Q(1)),'h_mode':'fixed','h_square':Q(1),
                'cubic_components':2,'quartic_free_dimension':3,'sign_quotient':'one_R3'}
    return {'stratum':'zero-cubic','root_square':Q(1),'cubic_base':(Q(),)*3,'h_mode':'fixed','h_square':Q(),
            'cubic_components':1,'quartic_free_dimension':3,'sign_quotient':'R3_antipodal_fixed_origin'}


def check_source(source,cases):
    source=tuple(map(Q,source));assert source[:2]==(Q(),Q())
    C=six.combine(cases,source);c=classify((Q(),)*7,C,cases)
    assert extract(C)==invariants(source[2:5])
    A,B,H=source[2:5];r=abs(A) if A else abs(B) if B else abs(H) if H else Q(1)
    sign=1 if (A if A else B if B else H if H else Q(1))>0 else -1
    oriented=tuple(sign*x/r for x in (A,B,H));assert c['root_square']==r*r
    if c['h_mode']=='fixed':assert c['cubic_base']==oriented
    else:assert c['cubic_base'][:2]==oriented[:2] and c['h_square']==oriented[2]**2
    # Every quartic triple is independent of these data, including simultaneous sign changes.
    other=source[:5]+tuple(x+Q(7) for x in source[5:])
    assert six.combine(cases,other)==C and six.combine(cases,tuple(-x for x in source))==C
    return c


def validate(c):
    assert c['schema']=='marici.photon-zero-leading-fibres.v1' and c['owner']=='marici.Nima'
    assert c['domain']=='g2=f2=0;eight_real_Born_couplings;full_coherent_cuts_through_degree6'
    for k in ('zero_leading_real_image_and_fibres_classified','cubic_sign_and_cancellation_strata_retained',
              'three_unseen_quartic_contacts_retained','nonfree_zero_source_sign_action_retained'):
        assert c[k] is True,k
    for k in ('quartic_contacts_identified_at_these_cut_orders','actual_physical_source_selected',
              'regular_degree6_tensor_completion_constructed','native_or_UV_dynamics_derived','C12_budget_renewed'):
        assert c[k] is False,k


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate(c);parent=six.build();_,_,cases=six.inventory()
    counts={};total=0
    for cubic in product(map(Q,(-2,-1,0,1,2)),repeat=3):
        for quartic in product((Q(-1),Q(1)),repeat=3):
            result=check_source((Q(),Q())+cubic+quartic,cases)
            counts[result['stratum']]=counts.get(result['stratum'],0)+1;total+=1
    for A in (Q(-1),Q(1)):
        for H in (Q(-1),Q(),Q(1)):
            for quartic in product((Q(-1),Q(1)),repeat=3):
                result=check_source((Q(),Q(),A,-10*A,H)+quartic,cases)
                counts[result['stratum']]=counts.get(result['stratum'],0)+1;total+=1
    # Independent actual evaluation confirms invariant reconstruction, rather than a fitted cut image.
    for cubic in product(map(Q,(-1,0,1)),repeat=3):
        C=six.combine(cases,(Q(),Q())+cubic+(Q(),)*3)
        assert C==expected_cut(invariants(cubic),cases)
    # Algebraic source branches: rational data with nonsquare cubic and single-minus coordinates.
    nonsquare=classify((Q(),)*7,expected_cut((Q(7),Q(28),Q(14),Q(63),Q(252)),cases),cases)
    assert nonsquare['root_square']==7 and nonsquare['cubic_base']==(Q(1),Q(2),Q(3))
    double=classify((Q(),)*7,expected_cut((Q(7),Q(700),Q(-70),Q(2),Q()),cases),cases)
    assert double['h_mode']=='plus-minus-square-root' and double['h_square']==Q(2,7) and double['cubic_components']==4
    # Pure quartic sources are distinct despite every cut through this order vanishing.
    x=(Q(),)*5+(Q(1),Q(2),Q(3));y=(Q(),)*5+(Q(4),Q(5),Q(6))
    assert six.combine(cases,x)==six.combine(cases,y)==((Q(),),)*4
    forward=base.amplitude_rows(Q(1),Q())[0]
    Born_difference=sum(((b-a)*v for a,b,v in zip(x,y,forward)),Q());assert Born_difference==3
    # Discrete cubic branches and free quartic fibres must not be replaced by a two-sheet cover at zero.
    zero=classify((Q(),)*7,((Q(),),)*4,cases)
    assert zero['cubic_components']==1 and zero['sign_quotient']=='R3_antipodal_fixed_origin'
    invalid=[(-1,0,0,0,0),(1,1,0,0,0),(1,1,1,-1,0),(1,1,1,1,0),(0,0,0,1,1)]
    for z in invalid:
        try:classify((Q(),)*7,expected_cut(tuple(map(Q,z)),cases),cases)
        except ValueError:pass
        else:raise AssertionError('nonrealizable zero-leading square data admitted')
    bad=list(expected_cut((Q(1),Q(1),Q(1),Q(1),Q(11)),cases));bad[0]=p.add(bad[0],(Q(),Q(),Q(),Q(1)))
    try:classify((Q(),)*7,tuple(bad),cases)
    except ValueError:pass
    else:raise AssertionError('wrong angular shape accepted')
    refused=['force_unseen_quartic_contacts_to_zero','extend_nonzero_leading_inverse_across_rank_change',
             'erase_cubic_relative_h_sign','treat_zero_sign_action_as_free_cover','discard_irrational_source_from_rational_data']
    for key in ('quartic_contacts_identified_at_these_cut_orders','actual_physical_source_selected',
                'regular_degree6_tensor_completion_constructed','native_or_UV_dynamics_derived','C12_budget_renewed'):
        try:validate({**c,key:True})
        except AssertionError:refused.append(key)
        else:raise AssertionError('unsupported zero-leading promotion: '+key)
    paths={ROOT/v for v in parent['source_sha256']};paths.update((CONTRACT,PROOF,TEST,MANIFEST,Path(__file__).resolve()))
    return {'schema':'marici.photon-zero-leading-fibres-receipt.v1','status':'pass',
        'scope':'zero_leading_joint_cut_fibres_through_degree6_with_wholly_unseen_quartic_contacts_not_physical_matching',
        'source_sha256':{path.relative_to(ROOT).as_posix():hashlib.sha256(path.read_bytes()).hexdigest() for path in sorted(paths)},
        'source_checks':total,'stratum_counts':counts,'quartic_free_dimension':3,
        'cubic_invariant_coordinates':['g3^2','f3^2','g3*f3','h3^2','h3*(10*g3+f3)'],
        'cubic_component_counts':{'pair-ordinary':2,'pair-cancellation-nonzero-h':4,'pair-cancellation-zero-h':2,'pure-h':2,'zero-cubic':1},
        'zero_cubic_sign_quotient':'R3_antipodal_fixed_origin','nonsquare_h3_coefficient_square':'2/7',
        'pure_quartic_same_cut_Born_difference':'3','invalid_data_refused':len(invalid)+1,
        'real_fibre_proof_machine_formalized':False,**{k:v for k,v in c.items() if isinstance(v,bool)},'hostile_controls_refused':refused}


def main():
    q=argparse.ArgumentParser(description=__doc__);q.add_argument('--check',action='store_true');a=q.parse_args();r=build()
    if a.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale zero-leading fibre receipt'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','source_checks','stratum_counts','quartic_free_dimension','quartic_contacts_identified_at_these_cut_orders')}))

if __name__=='__main__':main()
