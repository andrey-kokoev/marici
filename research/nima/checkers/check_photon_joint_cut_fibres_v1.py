"""Exact charts for real Born-source fibres of the joint degree-four/five cut map."""
import argparse
from fractions import Fraction as Q
from itertools import product
import hashlib
import json
from pathlib import Path
import sys

HOME=Path(__file__).resolve().parents[1];ROOT=HOME.parents[1]
sys.path.insert(0,str(HOME/'checkers'))
import check_photon_general_degree5_cut_v1 as cut
base=cut.base
CONTRACT=HOME/'contracts/photon-joint-cut-fibres-v1.json';PROOF=HOME/'photon-joint-cut-fibres-v1.md'
TEST=HOME/'checkers/test_photon_joint_cut_fibres_v1.py';MANIFEST=HOME/'scc-models/photon-joint-cut-fibres-v1.json'
RESULT=HOME/'results/photon-joint-cut-fibres-v1.json'


def observe(source):
    g,f,p,q,h=map(Q,source)
    return g*g,f*f,g*f,g*p,f*q,g*q+10*f*p,h*(6*g+f)


def chart(data):
    """Exact Q chart for real fibres. Coordinates represent sqrt(root_square)*coefficients."""
    a,b,c,u,v,w,t=map(Q,data)
    if a<0 or b<0 or a*b!=c*c:raise ValueError('leading Gram is not real rank-one PSD')
    if a==b==0:
        if any((u,v,w,t)):raise ValueError('nonzero cut with zero leading source')
        return {'stratum':'zero-leading','chart':'unit-root','root_square':Q(1),'base':(Q(),)*5,'free_indices':(2,3,4)}
    if a>0:
        if a*v-c*w+10*b*u:raise ValueError('degree-five data violates source factorization')
        values=(Q(1),c/a,u/a,w/a-10*c*u/(a*a),Q())
        if 6*a+c==0:
            if t:raise ValueError('single-minus response on cancellation stratum')
            return {'stratum':'single-minus-cancellation','chart':'g2-positive','root_square':a,'base':values,'free_indices':(4,)}
        values=values[:4]+(t/(6*a+c),)
        return {'stratum':'ordinary','chart':'g2-positive','root_square':a,'base':values,'free_indices':()}
    if u:raise ValueError('nonzero g2*g3 with g2=0')
    return {'stratum':'ordinary','chart':'f2-positive','root_square':b,
            'base':(Q(),Q(1),w/(10*b),v/b,t/b),'free_indices':()}


def instantiate(c,parameters=(),sign=1):
    assert sign in (-1,1) and len(parameters)==len(c['free_indices'])
    values=list(c['base'])
    for i,x in zip(c['free_indices'],parameters):values[i]=Q(x)
    return c['root_square'],tuple(sign*x for x in values)


def observe_scaled(root_square,coefficients):
    # J is quadratic, so no square root, float or restricted radical field is required.
    assert root_square>0
    return tuple(root_square*x for x in observe(coefficients))


def calibrated_data(source,betas,cases):
    g,f,p,q,h=map(Q,source)
    fourth=(-80*base.primary.evaluate(betas['beta13'],g,f),
            240*base.primary.evaluate(betas['beta12'],g,f),
            -Q(48,5)*base.primary.evaluate(betas['beta2'],g,f))
    fifth=cut.combine(cases,(g*p,g*q,g*h,f*p,f*q,f*h))
    get=lambda poly,i:poly[i] if i<len(poly) else Q()
    return fourth+(-48*get(fifth[2],0),-240*get(fifth[0],2),96*get(fifth[1],0),480*get(fifth[3],1))


def jacobian(source):
    g,f,p,q,h=map(Q,source)
    return ((2*g,0,0,0,0),(0,2*f,0,0,0),(f,g,0,0,0),
            (p,0,g,0,0),(0,q,0,f,0),(q,10*p,10*f,g,0),(6*h,h,0,0,6*g+f))


def check_source(source):
    source=tuple(map(Q,source));data=observe(source);c=chart(data)
    g,f=source[:2];normalizer=abs(g) if g else abs(f) if f else Q(1)
    sign=1 if (g if g else f if f else Q(1))>0 else -1
    parameters=tuple(sign*source[i]/normalizer for i in c['free_indices'])
    d,coeff=instantiate(c,parameters,sign)
    assert d==normalizer*normalizer and coeff==tuple(x/normalizer for x in source)
    assert observe_scaled(d,coeff)==data
    assert observe(tuple(-x for x in source))==data
    return c


def validate(c):
    assert c['schema']=='marici.photon-joint-cut-fibres.v1' and c['owner']=='marici.Nima'
    assert c['domain']=='five_real_leading_Born_couplings;realizable_joint_degree4_degree5_cut_data;fixed_amplitude_frames'
    for k in ('real_image_conditions_and_fibre_charts_derived','generic_two_sheet_sign_fibre_verified',
              'cancellation_and_zero_leading_fibres_retained','square_root_free_executable_chart_encoding'):
        assert c[k] is True,k
    for k in ('global_inverse_without_strata_derived','physical_Born_sign_selected','actual_couplings_or_matching_selected',
              'degree_six_cut_inventory_constructed','native_or_UV_dynamics_derived','C12_budget_renewed'):
        assert c[k] is False,k


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate(c);parent=cut.build()
    _,_,cases=cut.inventory();betas=base.primary.parse_primary_betas(base.primary.load_primary()[2])
    counts={'ordinary':0,'single-minus-cancellation':0,'zero-leading':0};calibrations=0
    for source in product(map(Q,(-2,-1,0,1,2)),repeat=5):counts[check_source(source)['stratum']]+=1
    for g in (Q(-1),Q(1)):
        for p,q,h in product(map(Q,(-1,0,1)),repeat=3):counts[check_source((g,-6*g,p,q,h))['stratum']]+=1
    for source in product(map(Q,(-1,0,1)),repeat=5):
        assert calibrated_data(source,betas,cases)==observe(source);calibrations+=1
    # Nonsquare leading norm: exact algebraic representation, no float or Q(sqrt2,sqrt3,...) restriction.
    irrational_data=observe_scaled(Q(7),(Q(1),Q(2),Q(3),Q(5),Q(7)))
    ir=chart(irrational_data);assert ir['root_square']==7 and ir['base']==(Q(1),Q(2),Q(3),Q(5),Q(7))
    assert observe_scaled(*instantiate(ir))==irrational_data
    # Full one-dimensional cancellation fibre; fixing h3=0 would delete real sources.
    x=(Q(1),Q(-6),Q(2),Q(3),Q());y=x[:4]+(Q(7),)
    assert observe(x)==observe(y) and x!=y and x!=tuple(-v for v in y)
    assert chart(observe(x))['free_indices']==(4,)
    single_minus_Born_difference=7*base.amplitude_rows(Q(3,5),Q(4,5))[4][4]
    assert single_minus_Born_difference==Q(1008,625)
    z=(Q(),Q(),Q(1),Q(2),Q(3));zz=(Q(),Q(),Q(4),Q(5),Q(6))
    assert observe(z)==observe(zz)==(Q(),)*7 and z!=zz and z!=tuple(-v for v in zz)
    assert chart(observe(z))['free_indices']==(2,3,4)
    # Jacobian rank is not a fibre dimension oracle on singular zero-leading data.
    samples={'ordinary':(1,2,3,4,5),'cancellation':(1,-6,2,3,7),
             'zero-leading-g3':(0,0,1,0,0),'zero-leading-h3':(0,0,0,0,1),'origin':(0,0,0,0,0)}
    ranks={name:len(base.reduced_rows(jacobian(x))[1]) for name,x in samples.items()}
    assert ranks=={'ordinary':5,'cancellation':4,'zero-leading-g3':2,'zero-leading-h3':1,'origin':0}
    assert observe((Q(1,10),0,0,0,0))!=(Q(),)*7 # infinitesimal zero at origin is not an actual same-data curve
    conditioning={}
    for n in (10,100,1000):
        eps=Q(1,n);left=(Q(1),-6+eps,Q(2),Q(3),Q());right=left[:4]+(Q(1),)
        assert chart(observe(left))['stratum']==chart(observe(right))['stratum']=='ordinary'
        difference=max(abs(a-b) for a,b in zip(observe(left),observe(right)))
        assert difference==eps and abs(right[4]-left[4])/difference==n
        conditioning[str(n)]=str(1/difference)
    # Each inadmissible datum violates a separate necessary image condition.
    invalid=[(-1,0,0,0,0,0,0),(1,1,0,0,0,0,0),(1,1,1,0,1,0,0),
             (1,36,-6,2,-18,-117,1),(0,1,0,1,0,0,0),(0,0,0,0,0,1,0)]
    for data in invalid:
        try:chart(data)
        except ValueError:pass
        else:raise AssertionError('nonrealizable cut datum accepted')
    refused=['one_chart_divides_by_zero_g2','set_h3_zero_from_cancelled_response','infer_fibre_from_singular_Jacobian','require_rational_square_root_of_rational_data']
    for key in ('global_inverse_without_strata_derived','physical_Born_sign_selected','actual_couplings_or_matching_selected',
                'degree_six_cut_inventory_constructed','native_or_UV_dynamics_derived','C12_budget_renewed'):
        try:validate({**c,key:True})
        except AssertionError:refused.append(key)
        else:raise AssertionError('unsupported fibre promotion: '+key)
    paths={ROOT/p for p in parent['source_sha256']};paths.update((CONTRACT,PROOF,TEST,MANIFEST,Path(__file__).resolve()))
    return {'schema':'marici.photon-joint-cut-fibres-receipt.v1','status':'pass',
        'scope':'real_joint_cut_image_and_stratified_source_fibres_not_physical_measurement_or_matching',
        'source_sha256':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
        'source_chart_checks':counts,'calibrations_against_independent_cut_coefficients':calibrations,
        'nonsquare_root_chart':{'root_square':'7','coefficients':list(map(str,ir['base']))},
        'fibre_dimensions_before_sign_quotient':{'ordinary':0,'single-minus-cancellation':1,'zero-leading':3},
        'ordinary_fibre_cardinality':2,'zero_leading_sign_action':'antipodal_on_R3_with_fixed_origin',
        'cancellation_witness':{'source1':list(map(str,x)),'source2':list(map(str,y)),
                                'single_minus_Born_difference':str(single_minus_Born_difference)},
        'Jacobian_ranks':ranks,'near_cancellation_inverse_lower_bounds':conditioning,'nonrealizable_data_refused':len(invalid),
        'real_fibre_proof_machine_formalized':False,**{k:v for k,v in c.items() if isinstance(v,bool)},'hostile_controls_refused':refused}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');a=p.parse_args();r=build()
    if a.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale joint fibre receipt'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','source_chart_checks','ordinary_fibre_cardinality','fibre_dimensions_before_sign_quotient','actual_couplings_or_matching_selected')}))

if __name__=='__main__':main()
