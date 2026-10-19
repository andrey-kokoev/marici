"""Explicit cross-ray half-power cut modulus within either double-margin factorization-sign sector."""
import argparse
from fractions import Fraction as Q
from itertools import product
import hashlib
import json
from pathlib import Path
import sys

HOME=Path(__file__).resolve().parents[1];ROOT=HOME.parents[1]
sys.path.insert(0,str(HOME/'checkers'))
import check_photon_common_ray_modulus_v1 as ray
box=ray.box;prior=ray.prior;joint=ray.joint;t=ray.t
CONTRACT=HOME/'contracts/photon-branchwise-double-margin-v1.json';PROOF=HOME/'photon-branchwise-double-margin-v1.md'
TEST=HOME/'checkers/test_photon_branchwise_double_margin_v1.py';MANIFEST=HOME/'scc-models/photon-branchwise-double-margin-v1.json'
RESULT=HOME/'results/photon-branchwise-double-margin-v1.json'


def admissible(x,M,sigma,eta,branch):
    if len(x)!=8 or branch not in (-1,1):return False
    if max(map(abs,x))>M:return False
    g,f,p,q=x[:4];r2=g*g+f*f;s2=p*p+q*q;d=g*q-10*f*p
    # Both zero strata are included by homogeneous inequalities; no normalized 0/0 is evaluated.
    return d*d>=sigma*sigma*r2*s2 and branch*d>=0 and (6*g+f)**2>=eta*eta*r2


def constants(sigma,eta):
    sigma=Q(sigma);eta=Q(eta);assert 0<sigma<=Q(1,2) and 0<eta<=1
    K=ray.RADIUS_GAIN;c=ray.COERCIVITY
    L=1+50/sigma;e=2*L;u=e+1;R=(14+u)/eta
    a=c*eta*eta/37;b=1/(eta*eta)
    T=2/(eta*eta)+74/(eta**4);D=2+37*T
    F1=4*K*e*(1+R)*(R*R+1)/a
    F2=28*K*b*u*(1+R)*(R*R+1)/(a*a)
    N=8*e*(Q(400)/a+D/(a*a))
    small=1+(2+e)**2
    A=Q(13,3)+max(K/a,small)/224
    B=max((F1+F2+N)/224,Q(229,4200))
    return {'L':L,'e':e,'u':u,'R':R,'a':a,'b':b,'T':T,'D':D,'F1':F1,'F2':F2,'N':N,'small':small,'A':A,'B':B}


def bound(delta,M,sigma,eta):
    delta=Q(delta);M=Q(M);assert delta>=0 and M>=1
    c=constants(sigma,eta)
    return min(box.diameter(M),c['A']*delta+c['B']*M*ray.axis.sqrt_upper(delta))


def bilinear(x):
    g,f,p,q=x[:4]
    return (g*p,g*q,f*p,f*q)


def auxiliary_den(direction,x):
    g,f=direction;r2=g*g+f*f;assert r2>0 and 6*g+f!=0
    pp=(Q(7,256)*g*g+Q(989,8064)*f*f)/r2
    qq=(Q(49,7680)*g*g+Q(5,256)*f*f)/r2
    pq=-g*f/(192*r2)
    hh=(Q(49,640)*g*g-Q(11,40)*g*f+Q(203,720)*f*f)/r2
    a,b,c,d=bilinear(x);z=x[4]*(6*x[0]+x[1]);trace2=(6*g+f)**2/r2
    return pp*(a*a+c*c)+qq*(b*b+d*d)+2*pq*(a*b+c*d)+hh*z*z/trace2


def pair_algebra(x,y,delta,sigma,eta,C):
    vx,vy=bilinear(x),bilinear(y)
    dx=x[0]*x[3]-10*x[1]*x[2];dy=y[0]*y[3]-10*y[1]*y[2]
    assert abs(dx-dy)<=50*delta/sigma
    E2=sum((a-b)**2 for a,b in zip(vx,vy))
    assert E2<=(C['e']*delta)**2
    zx=x[4]*(6*x[0]+x[1]);zy=y[4]*(6*y[0]+y[1])
    assert E2+(zx-zy)**2<=(C['u']*delta)**2
    rx2=sum(v*v for v in x[:2]);ry2=sum(v*v for v in y[:2])
    if rx2 and ry2:
        sin2=1-(x[0]*y[0]+x[1]*y[1])**2/(rx2*ry2)
        tx2=rx2*sum(v*v for v in x[2:4]);ty2=ry2*sum(v*v for v in y[2:4])
        assert max(tx2,ty2)*sin2<=E2
    for own_source in (x,y):
        direction=own_source[:2]
        if not any(direction):continue
        for source in (x,y):
            r2=sum(v*v for v in source[:2]);c2=sum(v*v for v in source[2:5])
            den=auxiliary_den(direction,source)
            assert den>=C['a']*r2*c2
        source=own_source
        if sum(v*v for v in source[2:5]):
            B=box.equal.previous.transport(source);den=auxiliary_den(direction,source)
            colp=bilinear(source)[::2]
            assert ray.radius(direction,B)*sum(v*v for v in colp)/den==source[2]**2


def check_pair(x,y,M,sigma,eta,branch):
    x=tuple(map(Q,x));y=tuple(map(Q,y));M=Q(M);sigma=Q(sigma);eta=Q(eta)
    C=constants(sigma,eta);assert M>=1
    if not admissible(x,M,sigma,eta,branch) or not admissible(y,M,sigma,eta,branch):
        raise ValueError('sources do not share the stated box, two margins and weak branch sign')
    delta=box.gap(box.data(x),box.data(y));cut=box.gap(box.cut_vector(x),box.cut_vector(y))
    pair_algebra(x,y,delta,sigma,eta,C)
    assert cut<=bound(delta,M,sigma,eta)
    return delta,cut


def certificate():
    # Uniform coefficient bounds for direction-dependent radius and auxiliary quadratic denominator.
    assert 2*sum(sum(map(abs,row),Q()) for row in (ray.WG,ray.WF,ray.WC))<400
    assert 2*(Q(7,256)+Q(989,8064)+Q(1,192))<2
    assert 2*(Q(49,7680)+Q(5,256)+Q(1,192))<2
    assert 2*(Q(49,640)+Q(11,40)+Q(203,720))<2
    assert max(sum(map(abs,row[:6]),Q()) for row in t.FLOW)==Q(9,10)
    assert max(sum(map(abs,row[6:]),Q()) for row in t.FLOW)==Q(1,16)
    assert 37<7**2
    return {'radius_weight_direction_gain':'400','metric_direction_gain':'2','trace_square_direction_gain':'74',
            'quartic_transport_row_gain':'9/10','cubic_transport_row_gain':'1/16',
            'outer_product_entry_gain':'L=1+50/sigma','outer_product_Frobenius_gain':'e=2*L',
            'auxiliary_data_gain':'u=e+1','cubic_norm_comparability':'R=(14+u)/eta',
            'auxiliary_denominator_coercivity':'a=c0*eta^2/37','auxiliary_denominator_norm':'b=eta^(-2)',
            'auxiliary_denominator_direction_gain':'D=2+37*(2/eta^2+74/eta^4)'}


def validate(c):
    assert c['schema']=='marici.photon-branchwise-double-margin.v1' and c['owner']=='marici.Nima'
    for k in ('cross_ray_same_branch_double_margin_half_power','no_common_ray_assumption',
              'independent_h3_and_all_quartics_retained','zero_strata_by_homogeneous_inequalities',
              'half_power_sharp_on_stated_margin_range'):
        assert c[k] is True,k
    for k in ('opposite_branch_pairs_classified','physical_branch_margin_box_or_noise_licensed',
              'cubic_single_minus_margin_assumed','physical_matching_selected','native_or_UV_dynamics_derived','C12_budget_renewed'):
        assert c[k] is False,k


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate(c);parent=ray.build();cert=certificate()
    sigma=Q(1,4);eta=Q(1,10);M=Q(1);counts={};cross=0
    points=[tuple(map(Q,x)) for x in product((-1,0,1),repeat=8)]
    for branch in (-1,1):
        eligible=[x for x in points if admissible(x,M,sigma,eta,branch)]
        pairs=0
        for i in range(0,len(eligible),29):
            x=eligible[i];y=eligible[(113*i+19)%len(eligible)]
            check_pair(x,y,M,sigma,eta,branch);pairs+=1
            cross+=int(x[0]*y[1]!=x[1]*y[0])
        counts[str(branch)]={'eligible_controls':len(eligible),'two_point_controls':pairs}
    assert cross>0
    # Explicit fractional cross-ray pair with nonzero h3 and three nonzero quartic inputs.
    x=(Q(1),Q(),Q(1,4),Q(3,4),Q(1,2),Q(1),Q(-1),Q(1,2))
    y=(Q(1),Q(1,10),Q(13,50),Q(4,5),Q(2,5),Q(-1),Q(1),Q(-1,2))
    check_pair(x,y,M,sigma,eta,1)
    assert x[0]*y[1]!=x[1]*y[0]
    x=(Q(1),Q(),Q(1,10),Q(-1),Q(1),Q(1),Q(-1),Q(1))
    y=(Q(1),Q(1,10),Q(1,10),Q(-1),Q(-1),Q(-1),Q(1),Q(-1))
    assert 10*x[2]+x[3]==10*y[2]+y[3]==0
    check_pair(x,y,M,sigma,eta,-1)
    witnesses=[]
    for branch in (-1,1):
        for n in (10,100,1000):
            x,y=box.bounded_pair(Q(1,n))
            if branch==1:
                flip=lambda z:z[:2]+tuple(-v for v in z[2:5])+z[5:]
                x,y=flip(x),flip(y)
            delta,cut=check_pair(x,y,Q(1),Q(1,2),Q(1),branch)
            witnesses.append({'branch':branch,'r':str(Q(1,n)),'joint_data_gap':str(delta),'cut_gap':str(cut)})
    # Opposite roots are not relabeled by convention, even if both satisfy the absolute margins.
    x=(Q(1),Q(),Q(1),Q(1),Q(),Q(),Q(),Q())
    y=x[:3]+(-x[3],)+x[4:]
    assert admissible(x,M,Q(1,2),Q(1),1) and admissible(y,M,Q(1,2),Q(1),-1)
    try:check_pair(x,y,M,Q(1,2),Q(1),1)
    except ValueError:pass
    else:raise AssertionError('opposite branch silently identified')
    # The large constants are exact/conservative, not empirically optimized from controls.
    constants_record={k:str(v) for k,v in constants(sigma,eta).items()}
    refused=['hold_radius_weights_fixed_across_different_rays','use_unrealizable_intermediate_ratio_as_source',
             'select_factorization_branch_from_noise_by_convention','erase_small_cubic_pair_or_zero_leading_strata']
    for key in ('opposite_branch_pairs_classified','physical_branch_margin_box_or_noise_licensed',
                'cubic_single_minus_margin_assumed','physical_matching_selected','native_or_UV_dynamics_derived','C12_budget_renewed'):
        try:validate({**c,key:True})
        except AssertionError:refused.append(key)
        else:raise AssertionError('unearned branchwise margin promotion: '+key)
    paths={ROOT/path for path in parent['source_sha256']};paths.update((CONTRACT,PROOF,TEST,MANIFEST,Path(__file__).resolve()))
    return {'schema':'marici.photon-branchwise-double-margin-receipt.v1','status':'pass',
        'scope':'arbitrary_leading_rays_with_two_margins_within_each_weak_branch_sign_sector_not_across_labels',
        'source_sha256':{path.relative_to(ROOT).as_posix():hashlib.sha256(path.read_bytes()).hexdigest() for path in sorted(paths)},
        'certificate':cert,'constant_example_sigma_quarter_eta_tenth':constants_record,
        'control_counts_by_branch':counts,'cross_ray_comparisons':cross,'explicit_fractional_h3_cross_ray_control':True,'explicit_cubic_trace_zero_control':True,'pairwise_projection_and_auxiliary_ratio_controls':True,
        'sharpness_controls':witnesses,'uniform_cut_exponent':'1/2','compatible_single_branch_cut_diameter':'omega(2*epsilon)',
        'general_branchwise_geometry_proof_machine_formalized':False,
        **{k:v for k,v in c.items() if isinstance(v,bool)},'hostile_controls_refused':refused}


def main():
    q=argparse.ArgumentParser(description=__doc__);q.add_argument('--check',action='store_true');a=q.parse_args();r=build()
    if a.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale branchwise double-margin receipt'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','uniform_cut_exponent','cross_ray_comparisons','no_common_ray_assumption','opposite_branch_pairs_classified')}))

if __name__=='__main__':main()
