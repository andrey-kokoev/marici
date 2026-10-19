"""Sharp unlabelled double-margin cut modulus: opposite roots controlled by leading Gram data."""
import argparse
from fractions import Fraction as Q
from itertools import product
import hashlib
import json
from pathlib import Path
import sys

HOME=Path(__file__).resolve().parents[1];ROOT=HOME.parents[1]
sys.path.insert(0,str(HOME/'checkers'))
import check_photon_branchwise_double_margin_v1 as branch
ray=branch.ray;box=branch.box;prior=branch.prior;t=branch.t
CONTRACT=HOME/'contracts/photon-double-margin-cut-modulus-v1.json';PROOF=HOME/'photon-double-margin-cut-modulus-v1.md'
TEST=HOME/'checkers/test_photon_double_margin_cut_modulus_v1.py';MANIFEST=HOME/'scc-models/photon-double-margin-cut-modulus-v1.json'
RESULT=HOME/'results/photon-double-margin-cut-modulus-v1.json'
OPPOSITE_A=Q(439,84)


def discriminant(x):return x[0]*x[3]-10*x[1]*x[2]


def margin_box(x,M,sigma):
    if len(x)!=8 or max(map(abs,x))>M:return False
    r2=sum(v*v for v in x[:2]);s2=sum(v*v for v in x[2:4]);d=discriminant(x)
    return d*d>=sigma*sigma*r2*s2


def admissible(x,M,sigma,eta):
    return margin_box(x,M,sigma) and (6*x[0]+x[1])**2>=eta*eta*sum(v*v for v in x[:2])


def constants(sigma,eta):
    c=branch.constants(sigma,eta)
    assert c['A']>=OPPOSITE_A and c['B']>=Q(229,70)/Q(sigma)
    return c


def bound(delta,M,sigma,eta):
    constants(sigma,eta)
    return branch.bound(delta,M,sigma,eta)


def opposite_bound(delta,M,sigma):
    delta=Q(delta);M=Q(M);sigma=Q(sigma)
    assert delta>=0 and M>=1 and 0<sigma<=Q(1,2)
    return min(box.diameter(M),OPPOSITE_A*delta+Q(229,70)*M*ray.axis.sqrt_upper(delta)/sigma)


def opposite_geometry(x,y,delta,sigma):
    """Exact controls for the proof's Gram projection and far-leading small-pair consequence."""
    assert discriminant(x)*discriminant(y)<=0
    rx2=sum(v*v for v in x[:2]);ry2=sum(v*v for v in y[:2]);r2=max(rx2,ry2)
    assert abs(rx2-ry2)<=2*delta
    if rx2 and ry2:
        dot=x[0]*y[0]+x[1]*y[1];sin2=1-dot*dot/(rx2*ry2)
        gram_gap2=(x[0]**2-y[0]**2)**2+(x[1]**2-y[1]**2)**2+2*(x[0]*x[1]-y[0]*y[1])**2
        assert r2*r2*sin2<=gram_gap2<=4*delta*delta
    if delta==0:return 'zero'
    if r2<=(120/sigma)**2*delta:return 'near'
    assert min(rx2,ry2)>=r2/4
    # ||n-m|| <=4 delta/r^2, and this is <=sigma/3320 in this far regime.
    assert 16*delta*delta/(r2*r2)<=(sigma/3320)**2
    assert sum(v*v for v in x[2:4])<=100*delta
    assert sum(v*v for v in y[2:4])<=100*delta
    assert abs(x[2]**2-y[2]**2)<=200*delta
    return 'far'


def check_opposite_pair(x,y,M,sigma):
    x=tuple(map(Q,x));y=tuple(map(Q,y));M=Q(M);sigma=Q(sigma)
    assert M>=1 and 0<sigma<=Q(1,2)
    if not margin_box(x,M,sigma) or not margin_box(y,M,sigma) or discriminant(x)*discriminant(y)>0:
        raise ValueError('opposite-root lemma requires its box, discriminant margin and nonpositive root product')
    delta=box.gap(box.data(x),box.data(y));cut=box.gap(box.cut_vector(x),box.cut_vector(y))
    regime=opposite_geometry(x,y,delta,sigma)
    if regime=='far':assert cut<=OPPOSITE_A*delta
    assert cut<=opposite_bound(delta,M,sigma)
    return delta,cut,regime


def check_pair(x,y,M,sigma,eta):
    x=tuple(map(Q,x));y=tuple(map(Q,y));M=Q(M);sigma=Q(sigma);eta=Q(eta)
    constants(sigma,eta);assert M>=1
    if not admissible(x,M,sigma,eta) or not admissible(y,M,sigma,eta):
        raise ValueError('full theorem requires the stated box and both homogeneous margins')
    dx,dy=discriminant(x),discriminant(y)
    if dx*dy<0:
        delta,cut,_=check_opposite_pair(x,y,M,sigma)
    else:
        label=1 if (dx if dx else dy)>=0 else -1
        delta,cut=branch.check_pair(x,y,M,sigma,eta,label)
    assert cut<=bound(delta,M,sigma,eta)
    return delta,cut


def certificate():
    # Leading Gram Frobenius gain2 and projective alignment gain2 give unit-direction gain4.
    assert 2**2==1+1+2
    assert 15**2>202 and 11**2>102
    assert 10*30==300 and 10*165+10==1660 and 2*1660==3320
    # r>120*sqrt(delta)/sigma and sigma<=1/2 imply direction gap<=sigma/3320.
    assert Q(4,120**2)*Q(1,2)<Q(1,3320)
    assert 1200/ Q(120)==10 and Q(13,3)+Q(200,224)==OPPOSITE_A
    assert Q(229,8400)*120==Q(229,70)
    # Universal domination by the already-published branchwise constants.
    assert ray.RADIUS_GAIN>2 and ray.COERCIVITY/37<1
    assert 1+(2+202)**2>200 and Q(800,224)==Q(25,7)>Q(229,70)
    return {'leading_Gram_Frobenius_gain':'2','unit_leading_direction_gain':'4',
            'pair_sensing_inverse_gain':'15','pair_sensing_direction_gain':'11',
            'discriminant_pair_functional_gain':'10','opposite_root_inequality':'sigma*(||a||+||b||)<=300*delta+1660*||n-m||*||b||',
            'far_leading_threshold':'r>120*sqrt(delta)/sigma',
            'far_pair_square_bound':'s_i^2<=100*delta','far_missing_square_gap':'200*delta',
            'opposite_linear_cut_gain':str(OPPOSITE_A),'opposite_sqrt_cut_gain':'229/(70*sigma)',
            'unlabelled_modulus':'same explicit A(sigma,eta),B(sigma,eta) as branchwise packet, without branch prior',
            'sharp_full_sector_exponent':'1/2'}


def validate(c):
    assert c['schema']=='marici.photon-double-margin-cut-modulus.v1' and c['owner']=='marici.Nima'
    for k in ('unlabelled_double_margin_half_power','opposite_branch_pairs_classified',
              'both_root_signs_and_cross_sign_pairs_included','half_power_sharp_on_stated_margin_range',
              'independent_h3_all_quartics_and_zero_strata_retained','bounded_double_margin_frontier_resolved'):
        assert c[k] is True,k
    for k in ('factorization_label_prior_assumed','common_ray_assumed','cubic_single_minus_margin_assumed',
              'opposite_root_lemma_requires_leading_trace_margin','discriminant_margin_alone_full_sector_half_power',
              'native_source_box_margin_or_noise_licensed','physical_matching_selected','native_or_UV_dynamics_derived',
              'full_physical_programme_complete','C12_budget_renewed'):
        assert c[k] is False,k


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate(c);parent=branch.build();cert=certificate()
    sigma=Q(1,4);eta=Q(1,10);M=Q(1)
    points=[tuple(map(Q,x)) for x in product((-1,0,1),repeat=8)]
    points=[x for x in points if admissible(x,M,sigma,eta)]
    same=opposite=zeros=0
    for i in range(0,len(points),29):
        x=points[i];y=points[(113*i+19)%len(points)]
        check_pair(x,y,M,sigma,eta)
        if discriminant(x)*discriminant(y)<0:opposite+=1
        else:same+=1
        zeros+=int(not any(x[:2]) or not any(y[:2]) or not any(x[2:4]) or not any(y[2:4]))
    assert opposite>0 and same>0 and zeros>0
    # The pair explicitly refused by the branchwise checker is accepted without a branch label.
    x=(Q(1),Q(),Q(1),Q(1),Q(1,2),Q(1),Q(-1),Q(1))
    y=(Q(1),Q(1,10),Q(1),Q(-1),Q(1,2),Q(1),Q(-1),Q(1))
    assert x[0]*y[1]!=x[1]*y[0]
    check_pair(x,y,Q(1),Q(1,2),Q(1))
    far=[]
    for n in (10**8,10**10,10**12):
        v=Q(1,n)
        x=(Q(1),Q(),v,v,Q(1,2),Q(1),Q(-1),Q(1))
        y=(Q(1),v,2*v,-v,Q(1,2),Q(1),Q(-1),Q(1))
        delta,cut,regime=check_opposite_pair(x,y,M,sigma)
        assert regime=='far' and x[0]*y[1]!=x[1]*y[0]
        check_pair(x,y,M,sigma,eta)
        far.append({'scale':str(v),'joint_gap':str(delta),'cut_gap':str(cut),'regime':regime})
    # Opposite-root lemma alone does not require the leading-trace margin; the full theorem still does.
    v=Q(1,10**10)
    x=(Q(1,6),Q(-1),v,v,Q(1,2),Q(1),Q(-1),Q(1))
    y=x[:2]+tuple(-a for a in x[2:5])+x[5:]
    assert check_opposite_pair(x,y,M,sigma)[2]=='far'
    try:check_pair(x,y,M,sigma,eta)
    except ValueError:pass
    else:raise AssertionError('full theorem dropped leading-trace margin')
    refused=['infer_full_sector_half_power_from_discriminant_margin_alone',
             'select_physical_root_to_apply_unlabelled_bound','remove_box_by_zero_transport_coercivity',
             'identify_mathematical_frontier_completion_with_physical_programme_completion']
    for key in ('factorization_label_prior_assumed','common_ray_assumed','cubic_single_minus_margin_assumed',
                'opposite_root_lemma_requires_leading_trace_margin','discriminant_margin_alone_full_sector_half_power',
                'native_source_box_margin_or_noise_licensed','physical_matching_selected','native_or_UV_dynamics_derived',
                'full_physical_programme_complete','C12_budget_renewed'):
        try:validate({**c,key:True})
        except AssertionError:refused.append(key)
        else:raise AssertionError('unearned full double-margin promotion: '+key)
    paths={ROOT/path for path in parent['source_sha256']};paths.update((CONTRACT,PROOF,TEST,MANIFEST,Path(__file__).resolve()))
    return {'schema':'marici.photon-double-margin-cut-modulus-receipt.v1','status':'pass',
        'scope':'all_root_signs_and_arbitrary_rays_on_conditional_two_margin_real_eight_contact_box_not_native_physics',
        'source_sha256':{path.relative_to(ROOT).as_posix():hashlib.sha256(path.read_bytes()).hexdigest() for path in sorted(paths)},
        'certificate':cert,'eligible_grid_controls':len(points),'same_or_zero_sign_comparisons':same,
        'opposite_sign_comparisons':opposite,'zero_stratum_comparisons':zeros,
        'far_opposite_nonzero_h3_all_quartics_controls':far,'cancelled_leading_trace_opposite_lemma_control':True,
        'previously_refused_cross_label_pair_now_admitted':True,
        'sharpness_controls_inherited':parent['sharpness_controls'],'full_double_margin_exponent':'1/2',
        'unlabelled_compatible_cut_diameter':'omega(2*tau)',
        'general_double_margin_geometry_proof_machine_formalized':False,
        **{k:v for k,v in c.items() if isinstance(v,bool)},'hostile_controls_refused':refused}


def main():
    q=argparse.ArgumentParser(description=__doc__);q.add_argument('--check',action='store_true');a=q.parse_args();r=build()
    if a.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale full double-margin receipt'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','full_double_margin_exponent','opposite_sign_comparisons','factorization_label_prior_assumed','full_physical_programme_complete')}))

if __name__=='__main__':main()
