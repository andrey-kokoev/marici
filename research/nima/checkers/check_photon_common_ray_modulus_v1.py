"""General positive cubic-radius observable and sharp half-power cut bound for common-ray pairs."""
import argparse
from fractions import Fraction as Q
from itertools import product
import hashlib
import json
from pathlib import Path
import sys

HOME=Path(__file__).resolve().parents[1];ROOT=HOME.parents[1]
sys.path.insert(0,str(HOME/'checkers'))
import check_photon_margin_only_obstruction_v1 as margin
axis=margin.axis;box=axis.box;prior=axis.prior;joint=axis.joint;t=axis.t
CONTRACT=HOME/'contracts/photon-common-ray-modulus-v1.json';PROOF=HOME/'photon-common-ray-modulus-v1.md'
TEST=HOME/'checkers/test_photon_common_ray_modulus_v1.py';MANIFEST=HOME/'scc-models/photon-common-ray-modulus-v1.json'
RESULT=HOME/'results/photon-common-ray-modulus-v1.json'
WG=(Q(),Q(49,8),Q(49,4),Q(),Q(),Q())
WF=(Q(2),Q(83,4),Q(409,12),Q(),Q(),Q())
WC=(Q(),Q(),Q(),Q(274,3),-Q(131,18),Q())
COERCIVITY=Q(49,7680);RADIUS_GAIN=Q(3821,36)


def radius(ray,B):
    g,f=map(Q,ray);r2=g*g+f*f;assert r2>0
    return (g*g*t.dot(WG,B)+f*f*t.dot(WF,B)+g*f*t.dot(WC,B))/r2


def cubic_form(ray,cubic):
    g,f=map(Q,ray);p,q,h=map(Q,cubic);r2=g*g+f*f;assert r2>0
    return ((Q(7,256)*g*g+Q(989,8064)*f*f)*p*p
           +(Q(49,7680)*g*g+Q(5,256)*f*f)*q*q-g*f*p*q/96
           +(Q(49,640)*g*g-Q(11,40)*g*f+Q(203,720)*f*f)*h*h)/r2


def constants(M,eta):
    M=Q(M);eta=Q(eta);assert M>=1 and 0<eta<=1
    m=min(eta,Q(1,15))
    return Q(13,3)+RADIUS_GAIN/(224*COERCIVITY),M/(14*COERCIVITY*m)


def bound(delta,M,eta):
    delta=Q(delta);assert delta>=0;A,B=constants(M,eta)
    return min(box.diameter(M),A*delta+B*axis.sqrt_upper(delta))


def check_pair(x,y,M,eta):
    x=tuple(map(Q,x));y=tuple(map(Q,y));M=Q(M);eta=Q(eta)
    assert len(x)==len(y)==8 and M>=1 and max(map(abs,x+y))<=M and 0<eta<=1
    if x[0]*y[1]!=x[1]*y[0]:raise ValueError('pair does not have an exact common leading ray')
    g,f=x[:2] if any(x[:2]) else y[:2]
    if (g or f) and (6*g+f)**2<eta*eta*(g*g+f*f):raise ValueError('common leading ray violates the trace margin')
    delta=box.gap(box.data(x),box.data(y));cut=box.gap(box.cut_vector(x),box.cut_vector(y))
    assert cut<=bound(delta,M,eta)
    return delta,cut


def certificate():
    U=tuple(t.combine(row,t.FLOW) for row in (WG,WF,WC));Ug,Uf,Uc=U
    # The three quartic columns, after multiplication by a ray component, vanish as cubic polynomials in n.
    for i in range(3):assert (Ug[i],Uc[i]+Ug[i+3],Uf[i]+Uc[i+3],Uf[i+3])==(Q(),)*4
    expected=((Q(7,256),Q(989,8064),Q()),(Q(),Q(),-Q(1,96)),(Q(),)*3,
              (Q(49,7680),Q(5,256),Q()),(Q(),)*3,(Q(49,640),Q(203,720),-Q(11,40)))
    assert tuple(tuple(row[i] for row in U) for i in range(6,12))==expected
    assert max(sum(map(abs,row),Q()) for row in (WG,WF))+sum(map(abs,WC),Q())/2==RADIUS_GAIN
    # p/q lower bound after |ng*nf*p*q|/96 <=(ng²p²+nf²q²)/192.
    pq_surplus=(Q(7,256)-Q(1,192)-COERCIVITY,Q(989,8064)-COERCIVITY,
                Q(49,7680)-COERCIVITY,Q(5,256)-Q(1,192)-COERCIVITY)
    assert all(v>=0 for v in pq_surplus)
    det=Q(49,640)*Q(203,720)-Q(11,80)**2;trace=Q(49,640)+Q(203,720)
    assert det/trace>COERCIVITY and trace<1
    assert max(Q(7,256)+Q(49,7680),Q(989,8064)+Q(5,256))<1
    assert 1/(14*COERCIVITY*Q(1,15))>Q(229,4200)
    return {'radius_rows_ng2_nf2_ngnf':[list(map(str,row)) for row in (WG,WF,WC)],
            'quartic_polynomial_cancellation_constraints':12,'cubic_coefficient_constraints':18,
            'metric_eigenvalue_lower':str(COERCIVITY),'metric_eigenvalue_upper':'1',
            'h_block_determinant':str(det),'h_block_trace':str(trace),
            'radius_data_gain':str(RADIUS_GAIN),
            'bound':'min(diameter,A*delta+B*sqrt(delta)); A=13/3+K/(224*c); B=M/(14*c*min(eta,1/15))',
            'positive_margin_obstruction':'axis family: discriminant margin>=23/37, leading trace margin=6'}


def validate(c):
    assert c['schema']=='marici.photon-common-ray-modulus.v1' and c['owner']=='marici.Nima'
    for k in ('general_quartic_free_positive_cubic_radius','universal_single_source_zero_transport_coercivity','common_ray_trace_separated_half_power_bound',
              'sharp_common_ray_half_power_exponent','nonzero_h3_and_all_quartics_retained','zero_strata_included'):
        assert c[k] is True,k
    for k in ('general_cross_ray_double_margin_sector_classified','common_ray_or_margin_physically_licensed',
              'near_ray_projection_licensed','physical_matching_selected','native_or_UV_dynamics_derived','C12_budget_renewed'):
        assert c[k] is False,k


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate(c);parent=margin.build();cert=certificate()
    rays=((Q(1),Q()),(Q(),Q(1)),(Q(1),Q(1)),(Q(1),Q(-6)),(Q(2),Q(-3)))
    identities=pairs=0
    for ray in rays:
        scale=max(map(abs,ray));points=[]
        for a in (Q(-1),Q(),Q(1)):
            for cubic in product((Q(-1),Q(),Q(1)),repeat=3):
                for quartic in product((Q(-1),Q(1)),repeat=3):
                    x=tuple(a*v/scale for v in ray)+cubic+quartic;points.append(x)
                    B=box.equal.previous.transport(x);value=radius(ray,B)
                    assert value==cubic_form(ray,cubic)
                    length=sum(v*v for v in cubic)
                    assert COERCIVITY*length<=value<=length
                    A,_=constants(Q(1),Q(1,10))
                    assert prior.norm(box.cut_vector(x))<=A*prior.norm(B)
                    identities+=1
        if 6*ray[0]+ray[1]:
            for i in range(0,len(points),43):
                check_pair(points[i],points[(113*i+19)%len(points)],Q(1),Q(1,10));pairs+=1
    # Cubic single-minus trace cancellation is permitted: no extra |10p+q| margin is assumed.
    x=(Q(2,3),Q(-1),Q(1,10),Q(-1),Q(1),Q(1),Q(-1),Q(1))
    y=x[:2]+(Q(-1,10),Q(1),Q(-1),Q(-1),Q(1),Q(-1))
    check_pair(x,y,Q(1),Q(1,10))
    # Sharp exponent on a positive-discriminant-margin subset of common rays.
    witnesses=[]
    for n in (10,100,1000,10000):
        x,y=box.bounded_pair(Q(1,n));delta,cut=check_pair(x,y,Q(1),Q(1))
        assert axis.separation_squared(x)>=Q(1,4) and axis.separation_squared(y)>=Q(1,4)
        witnesses.append({'r':str(Q(1,n)),'joint_gap':str(delta),'cut_gap':str(cut)})
    for x,y in (((Q(1),Q(),Q(),Q(),Q(),Q(),Q(),Q()),(Q(1),Q(1,10**12),Q(),Q(),Q(),Q(),Q(),Q())),
                ((Q(1,6),Q(-1),Q(),Q(),Q(),Q(),Q(),Q()),(Q(),)*8)):
        try:check_pair(x,y,Q(1),Q(1,10))
        except ValueError:pass
        else:raise AssertionError('unearned near-ray or cancelled-trace pair admitted')
    refused=['infer_cross_ray_modulus_from_common_ray_pairs','replace_near_collinearity_by_exact_prior',
             'discard_h3_for_positive_radius','infer_native_positive_coupling_bound_from_radius_identity']
    for key in ('general_cross_ray_double_margin_sector_classified','common_ray_or_margin_physically_licensed',
                'near_ray_projection_licensed','physical_matching_selected','native_or_UV_dynamics_derived','C12_budget_renewed'):
        try:validate({**c,key:True})
        except AssertionError:refused.append(key)
        else:raise AssertionError('unearned common-ray promotion: '+key)
    paths={ROOT/path for path in parent['source_sha256']};paths.update((CONTRACT,PROOF,TEST,MANIFEST,Path(__file__).resolve()))
    return {'schema':'marici.photon-common-ray-modulus-receipt.v1','status':'pass',
        'scope':'general_positive_radius_and_paired_common_ray_half_power_not_arbitrary_double_margin_pair',
        'source_sha256':{path.relative_to(ROOT).as_posix():hashlib.sha256(path.read_bytes()).hexdigest() for path in sorted(paths)},
        'certificate':cert,'radius_identity_controls':identities,'two_data_common_ray_controls':pairs,
        'single_source_cut_coercivity_gain':str(constants(Q(1),Q(1))[0]),
        'cubic_trace_zero_control':True,'sharpness_controls':witnesses,'sharp_common_ray_exponent':'1/2',
        'general_radius_geometry_proof_machine_formalized':False,
        **{k:v for k,v in c.items() if isinstance(v,bool)},'hostile_controls_refused':refused}


def main():
    q=argparse.ArgumentParser(description=__doc__);q.add_argument('--check',action='store_true');a=q.parse_args();r=build()
    if a.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale common-ray cut-modulus receipt'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','sharp_common_ray_exponent','radius_identity_controls','two_data_common_ray_controls','general_cross_ray_double_margin_sector_classified')}))

if __name__=='__main__':main()
