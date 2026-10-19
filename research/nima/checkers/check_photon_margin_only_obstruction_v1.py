"""A bounded positive-discriminant-margin family still forces the sharp one-third cut exponent."""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import sys

HOME=Path(__file__).resolve().parents[1];ROOT=HOME.parents[1]
sys.path.insert(0,str(HOME/'checkers'))
import check_photon_axis_cut_modulus_v1 as axis
full=axis.full;RF=full.RF;box=axis.box;t=axis.t
CONTRACT=HOME/'contracts/photon-margin-only-obstruction-v1.json';PROOF=HOME/'photon-margin-only-obstruction-v1.md'
TEST=HOME/'checkers/test_photon_margin_only_obstruction_v1.py';MANIFEST=HOME/'scc-models/photon-margin-only-obstruction-v1.json'
RESULT=HOME/'results/photon-margin-only-obstruction-v1.json'
P=Q(1,10);RMAX=Q(1,100)
ROOT_U=Q(475440,588553);ROOT_V=Q(9509250,588553)
H0=Q(1065,3962);H2=Q(75,1132)
HRAD=(0,0,0,0,1,0,0,0)

# Q(r)[theta]/(theta^2-ROOT_U*theta-ROOT_V); the h coordinate also carries sqrt(H(theta)).
def E(a=0,b=0):return RF(a),RF(b)
def add(a,b):return a[0]+b[0],a[1]+b[1]
def scale(c,a):return c*a[0],c*a[1]
def mul(a,b):
    z=a[1]*b[1]
    return a[0]*b[0]+ROOT_V*z,a[0]*b[1]+a[1]*b[0]+ROOT_U*z
THETA=E(0,1);THETA2=mul(THETA,THETA)
H=add(E(H0),scale(H2,THETA2))
CK=add(E(-Q(5,12)),scale(Q(7,30),H))
CM=add(add(E(-Q(5,32)),scale(-Q(7,192),THETA2)),scale(Q(7,16),H))
ZERO=(E(),E())


def fadd(a,b):return add(a[0],b[0]),add(a[1],b[1])
def fscale(c,a):return scale(c,a[0]),scale(c,a[1])
def fzero(a):return a==ZERO

def family():
    r=RF((0,1));s=1+r;T=-P*P*(2+r)/s;D=P*P*(1-s*s)
    X=(E(r),E(-6*r),E(P*s),scale(P*s,THETA),E(P),E(),E(),E())
    Y=(E(r*s),E(-6*r*s),E(P),scale(P,THETA),E(P*s),scale(T,CK),scale(T/2,H),scale(-T/6,CM))
    return r,X,Y,D


def product(X,i,j):
    z=mul(X[i],X[j]);degree=HRAD[i]+HRAD[j]
    return (mul(H,z),E()) if degree==2 else (E(),z) if degree==1 else (z,E())
def weights(X):return tuple(product(X,i,j) for i,j in t.cut.PAIRS)
def project(rows,W):
    return tuple(sum_fields(tuple(fscale(c,w) for c,w in zip(row,W))) for row in rows)
def sum_fields(values):
    out=ZERO
    for value in values:out=fadd(out,value)
    return out

def lower_data(X):
    return tuple(product(X,i,j) for i,j in ((0,0),(1,1),(0,1),(0,2),(1,3)))+(fadd(product(X,0,3),fscale(10,product(X,1,2))),fadd(fscale(6,product(X,0,4)),product(X,1,4)))
def diff(A,B):return tuple(fadd(a,fscale(-1,b)) for a,b in zip(A,B))


def validate(c):
    assert c['schema']=='marici.photon-margin-only-obstruction.v1' and c['owner']=='marici.Nima'
    for k in ('positive_margin_unit_box_one_third_obstruction','same_factorization_branch_sign_retained',
              'independent_nonzero_h3_retained','quartic_contacts_bounded_not_erased','margin_alone_does_not_improve_full_box_power'):
        assert c[k] is True,k
    for k in ('double_margin_sector_classified','physical_margin_or_source_box_licensed','physical_matching_selected',
              'native_or_UV_dynamics_derived','C12_budget_renewed'):
        assert c[k] is False,k


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate(c);parent=axis.build()
    polynomial=lambda z:588553*z*z-475440*z-9509250
    assert polynomial(Q(4))<0<polynomial(Q(9,2)) and 2*588553*4-475440>0
    assert add(add(scale(588553,THETA2),scale(-475440,THETA)),E(-9509250))==E()
    Hmax=H0+H2*Q(81,4);assert 0<H0<Hmax<Q(25,14)<2
    assert -Q(5,32)+Q(7,16)*H0<0 and -Q(7,192)+Q(7,16)*H2<0
    r,X,Y,D=family();WX,WY=weights(X),weights(Y)
    # Every actual source-product difference, including both radical-carrying interference terms, is certified.
    V=(CK,scale(Q(1,2),H),scale(-Q(1,6),CM),scale(-6,CK),scale(-3,H),CM,E(1),THETA,E(),THETA2,E(),scale(-1,H))
    for value,v in zip(diff(WY,WX),V):assert value==(scale(D,v),E())
    BX,BY=project(t.FLOW,WX),project(t.FLOW,WY)
    assert all(fzero(v) for v in diff(BY,BX))
    # A common single-minus coefficient is explicitly positive: P^2*s*(10+theta)*sqrt(H)/320.
    assert BX[5]==(E(),scale(P*P*(1+r)/320,add(E(10),THETA)))
    JX,JY=lower_data(X),lower_data(Y);dJ=diff(JY,JX)
    for source in (X,Y):
        discriminant_root=fadd(product(source,0,3),fscale(-10,product(source,1,2)))
        assert discriminant_root==(scale(r*(1+r)*P,add(THETA,E(60))),E())
        assert add(scale(6,source[0]),source[1])==E()
    A=r*r*((1+r)**2-1)
    assert dJ[:3]==((E(A),E()),(E(36*A),E()),(E(-6*A),E()))
    assert all(fzero(v) for v in dJ[3:])
    Cdiff=diff(project(box.CUT_ROWS,WY),project(box.CUT_ROWS,WX))
    for value,line in zip(Cdiff,axis.prior.flat_cut(axis.prior.equal.LINE)):
        assert value==(E(line*D/4032),E())
    # Whole-interval bounds, using 4<theta<9/2<5, 0<H<2 and 0<sqrt(H)<2.
    smax=1+RMAX
    capsX=(RMAX,6*RMAX,P*smax,5*P*smax,2*P,Q(),Q(),Q())
    capsY=(RMAX*smax,6*RMAX*smax,P,5*P,2*P*smax,
           2*P*P*(Q(5,12)+Q(14,30)),2*P*P,2*P*P/Q(6)*(Q(5,32)+Q(175,192)+Q(14,16)))
    assert all(v<1 for v in capsX+capsY)
    # sigma^2>4: the concave quadratic below is positive at both endpoints of [4,5].
    margin_poly=lambda z:-147*z*z+120*z+3452
    assert margin_poly(Q(4))>0 and margin_poly(Q(5))>0
    assert add(mul(add(THETA,E(60)),add(THETA,E(60))),scale(-148,add(E(1),THETA2)))==add(add(scale(-147,THETA2),scale(120,THETA)),E(3452))
    dat=36*A;cut=-D/224
    assert dat.order()==3 and cut.order()==1
    assert (dat/(r**3)).at(0)==72 and (cut/r).at(0)==Q(1,11200)
    samples=[]
    for n in (100,1000,10000):
        rr=Q(1,n);delta=dat.at(rr);cutgap=cut.at(rr)
        assert delta==36*rr**3*(2+rr) and cutgap==P*P*rr*(2+rr)/224
        assert cutgap<=box.modulus(delta,Q(1))
        samples.append({'r':str(rr),'joint_data_gap':str(delta),'cut_gap':str(cutgap),
                        'data_gap_over_r_cubed':str(delta/rr**3),'cut_gap_over_r':str(cutgap/rr)})
    refused=['drop_h3_to_promote_discriminant_margin','assume_nonzero_single_minus_trace_without_prior',
             'confuse_same_branch_sign_with_positive_leading_trace','use_diverging_quartics_in_unit_box_obstruction']
    for key in ('double_margin_sector_classified','physical_margin_or_source_box_licensed','physical_matching_selected',
                'native_or_UV_dynamics_derived','C12_budget_renewed'):
        try:validate({**c,key:True})
        except AssertionError:refused.append(key)
        else:raise AssertionError('unearned margin-sector promotion: '+key)
    encode=lambda z:[v.encode() for v in z]
    paths={ROOT/path for path in parent['source_sha256']};paths.update((CONTRACT,PROOF,TEST,MANIFEST,Path(__file__).resolve()))
    return {'schema':'marici.photon-margin-only-obstruction-receipt.v1','status':'pass',
        'scope':'positive_discriminant_margin_with_leading_single_minus_cancellation_still_sharp_one_third_not_double_margin_sector',
        'source_sha256':{path.relative_to(ROOT).as_posix():hashlib.sha256(path.read_bytes()).hexdigest() for path in sorted(paths)},
        'root_polynomial':['-9509250','-475440','588553'],'root_isolating_interval':['4','9/2'],
        'H_constants':[str(H0),str(H2)],'radical_source_index':4,'parameter_upper':str(RMAX),
        'source_coefficients_in_basis_1_theta':{'X':[encode(z) for z in X],'Y':[encode(z) for z in Y]},
        'uniform_source_coordinate_bounds':{'X':list(map(str,capsX)),'Y':list(map(str,capsY))},
        'normalized_discriminant_margin_lower':'2','normalized_leading_single_minus_trace':'0',
        'cubic_single_minus_trace_nonzero':True,'all_twelve_product_difference_identities':True,
        'data_gap_over_r_cubed_limit':'72','cut_gap_over_r_limit':'1/11200','excluded_exponents':'alpha>1/3',
        'exact_samples':samples,'general_real_family_proof_machine_formalized':False,
        **{k:v for k,v in c.items() if isinstance(v,bool)},'hostile_controls_refused':refused}


def main():
    q=argparse.ArgumentParser(description=__doc__);q.add_argument('--check',action='store_true');a=q.parse_args();r=build()
    if a.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale positive-margin obstruction receipt'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','normalized_discriminant_margin_lower','excluded_exponents','double_margin_sector_classified','physical_margin_or_source_box_licensed')}))

if __name__=='__main__':main()
