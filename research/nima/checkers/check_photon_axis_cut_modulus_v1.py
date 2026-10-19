"""Sharp half-power cut modulus on the explicitly restricted f2=0 source face."""
import argparse
from fractions import Fraction as Q
from itertools import product
import hashlib
import json
from pathlib import Path
import sys

HOME=Path(__file__).resolve().parents[1];ROOT=HOME.parents[1]
sys.path.insert(0,str(HOME/'checkers'))
import check_photon_box_cut_sharpness_v1 as full
box=full.previous;prior=box.prior;joint=prior.joint;t=prior.t
CONTRACT=HOME/'contracts/photon-axis-cut-modulus-v1.json';PROOF=HOME/'photon-axis-cut-modulus-v1.md'
TEST=HOME/'checkers/test_photon_axis_cut_modulus_v1.py';MANIFEST=HOME/'scc-models/photon-axis-cut-modulus-v1.json'
RESULT=HOME/'results/photon-axis-cut-modulus-v1.json'
RADIUS_ROW=(Q(),Q(1),Q(2),Q(4),-Q(1,3),Q())
WEIGHT=Q(1,224)+Q(1,960)


def sqrt_upper(q,bits=64):
    q=Q(q);assert q>=0 and type(bits) is int and bits>=1
    if q==0:return Q()
    hi=Q(1)
    while hi*hi<q:hi*=2
    while (hi/2)**2>=q:hi/=2
    lo=hi/2
    for _ in range(bits):
        mid=(lo+hi)/2
        if mid*mid<q:lo=mid
        else:hi=mid
    assert lo*lo<=q<=hi*hi
    return hi


def bound(delta,M,bits=64):
    delta=Q(delta);M=Q(M);assert delta>=0 and M>=1
    return min(box.diameter(M),Q(35,3)*delta+Q(37,700)*M*sqrt_upper(delta,bits))


def radius(B):return t.dot(RADIUS_ROW,tuple(map(Q,B)))

def check_pair(x,y,M):
    x=tuple(map(Q,x));y=tuple(map(Q,y));M=Q(M)
    if len(x)!=8 or len(y)!=8 or x[1] or y[1]:raise ValueError('both sources must lie on the exact f2=0 face')
    assert M>=1 and max(map(abs,x+y))<=M
    delta=box.gap(box.data(x),box.data(y));cut=box.gap(box.cut_vector(x),box.cut_vector(y))
    assert cut<=bound(delta,M)
    return delta,cut


def separation_squared(x):
    g,f,p,q=x[:4]
    if not (g*g+f*f)*(p*p+q*q):return None
    return (g*q-10*f*p)**2/((g*g+f*f)*(p*p+q*q))


def certificate():
    row=t.combine(RADIUS_ROW,t.FLOW)
    expected=tuple(Q(1,240) if i==4 else Q(1,35) if i==5 else Q(1,224) if i==6 else Q(1,960) if i==9 else Q() for i in range(12))
    assert row==expected
    # f2=0 kills columns 3,4,5; h3 and all g2*quartic terms cancel exactly.
    assert all(row[i]==0 for i in (0,1,2,7,8,10,11))
    assert sum(map(abs,RADIUS_ROW),Q())==Q(22,3)
    assert WEIGHT==Q(37,6720) and 8*WEIGHT==Q(37,840)
    assert Q(13,3)+Q(22,3)==Q(35,3)
    assert 36*Q(37,50400)==Q(37,1400)
    assert Q(37,1680)<Q(37,700)
    # Earlier bounded half-power family lies on this face with a uniform positive separation margin.
    assert Q(30,7)>1 and Q(23,37)**2>Q(1,4)
    # p(v),q(v) on [1,2]: q<=-23/37 and p²+q²<=1, hence margin>=23/37>1/2.
    return {'transport_radius_row':list(map(str,RADIUS_ROW)),
            'source_monomial_radius_row':list(map(str,row)),
            'axis_radius':'g3^2/224+f3^2/960',
            'radius_data_gain':'22/3','weighted_pair_sum':'37/6720',
            'far_cut_bound':'(35/3)*delta+(37/840)*M*delta/r',
            'near_cut_bound':'(13/3)*delta+(37/1400)*M*r',
            'global_axis_bound':'min(diameter,(35/3)*delta+(37/700)*M*sqrt(delta))',
            'separated_obstruction_margin_lower':'23/37',
            'obstruction_data_limit':'840/1369','obstruction_cut_limit':'161/202612'}


def validate(c):
    assert c['schema']=='marici.photon-axis-cut-modulus.v1' and c['owner']=='marici.Nima'
    assert c['domain']=='conditional_source_box;both_sources_exact_f2=0;all_other_seven_Born_contacts_retained'
    for k in ('axis_uniform_half_power_cut_modulus','axis_half_power_exponent_sharp',
              'nonzero_h3_and_all_quartics_retained','zero_leading_and_zero_cubic_strata_retained',
              'positive_margin_sharpness_witness'):
        assert c[k] is True,k
    for k in ('general_separation_only_sector_classified','near_axis_projection_licensed','physical_axis_or_box_prior_licensed',
              'physical_matching_selected','native_or_UV_dynamics_derived','C12_budget_renewed'):
        assert c[k] is False,k


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate(c);parent=full.build();cert=certificate()
    controls=0
    points=[]
    for values in product((Q(-1),Q(),Q(1)),repeat=7):
        x=(values[0],Q())+values[1:];points.append(x)
        B=box.equal.previous.transport(x)
        assert radius(B)==x[2]**2/224+x[3]**2/960
    for i in range(0,len(points),31):
        x=points[i];y=points[(113*i+19)%len(points)]
        check_pair(x,y,Q(1));controls+=1
    # Include fractional, signed and scaled sources, including nonzero h3 and all quartics.
    a=(Q(1,100),Q(),Q(1,3),Q(-2,3),Q(3,4),Q(1),Q(-1),Q(1,2))
    b=(Q(),Q(),Q(-1,3),Q(2,3),Q(-3,4),Q(-1),Q(1),Q(-1,2))
    for M in (Q(1),Q(2),Q(3)):
        check_pair(tuple(M*v for v in a),tuple(M*v for v in b),M)
    for x in (points[0],points[-1],(Q(),)*8):check_pair(x,tuple(-v for v in x),Q(1))
    witnesses=[]
    for n in (10,100,1000,10000):
        r=Q(1,n);x,y=box.bounded_pair(r);delta,cut=check_pair(x,y,Q(1))
        assert x[1]==y[1]==0 and separation_squared(x)>=Q(1,4) and separation_squared(y)>=Q(1,4)
        assert box.equal.previous.transport(x)==box.equal.previous.transport(y)
        witnesses.append({'r':str(r),'joint_data_gap':str(delta),'cut_gap':str(cut),
                          'margin_squared_X':str(separation_squared(x)),'margin_squared_Y':str(separation_squared(y))})
    # A small f2 is not the exact axis prior.
    bad=list(a);bad[1]=Q(1,10**12)
    try:check_pair(tuple(bad),b,Q(1))
    except ValueError:pass
    else:raise AssertionError('near-axis source silently projected onto f2=0')
    refused=['infer_general_separation_theorem_from_axis_face','drop_h3_to_get_the_radius_identity',
             'replace_small_f2_by_zero','use_only_unbounded_quartic_sharpness_example','treat_margin_or_axis_as_native_prior']
    for key in ('general_separation_only_sector_classified','near_axis_projection_licensed','physical_axis_or_box_prior_licensed',
                'physical_matching_selected','native_or_UV_dynamics_derived','C12_budget_renewed'):
        try:validate({**c,key:True})
        except AssertionError:refused.append(key)
        else:raise AssertionError('unearned axis-sector promotion: '+key)
    paths={ROOT/path for path in parent['source_sha256']};paths.update((CONTRACT,PROOF,TEST,MANIFEST,Path(__file__).resolve()))
    return {'schema':'marici.photon-axis-cut-modulus-receipt.v1','status':'pass',
        'scope':'sharp_half_power_cut_modulus_on_exact_leading_axis_face_not_general_margin_only_sector',
        'source_sha256':{path.relative_to(ROOT).as_posix():hashlib.sha256(path.read_bytes()).hexdigest() for path in sorted(paths)},
        'certificate':cert,'axis_radius_controls':len(points),'two_point_axis_controls':controls,
        'scaled_h3_controls':3,'separated_sharpness_controls':witnesses,
        'sharp_axis_exponent':'1/2','compatible_axis_noise_diameter':'omega_axis_M(2*epsilon)',
        'general_axis_geometry_proof_machine_formalized':False,
        **{k:v for k,v in c.items() if isinstance(v,bool)},'hostile_controls_refused':refused}


def main():
    q=argparse.ArgumentParser(description=__doc__);q.add_argument('--check',action='store_true');a=q.parse_args();r=build()
    if a.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale leading-axis cut modulus receipt'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','sharp_axis_exponent','axis_radius_controls','general_separation_only_sector_classified','physical_axis_or_box_prior_licensed')}))

if __name__=='__main__':main()
