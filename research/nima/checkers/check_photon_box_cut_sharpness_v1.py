"""Bounded algebraic source family proves the conditional one-third cut exponent sharp."""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import sys

HOME=Path(__file__).resolve().parents[1];ROOT=HOME.parents[1]
sys.path.insert(0,str(HOME/'checkers'))
import check_photon_box_cut_modulus_v1 as previous
p=previous.p;t=previous.t
CONTRACT=HOME/'contracts/photon-box-cut-sharpness-v1.json';PROOF=HOME/'photon-box-cut-sharpness-v1.md'
TEST=HOME/'checkers/test_photon_box_cut_sharpness_v1.py';MANIFEST=HOME/'scc-models/photon-box-cut-sharpness-v1.json'
RESULT=HOME/'results/photon-box-cut-sharpness-v1.json'
K2=Q(175,72);C=Q(142,791);PARITY=(1,0,1,0,0,1,1,0);RMAX=Q(1,100)


def divmod_poly(a,b):
    a=p.trim(a);b=p.trim(b);assert b!=(Q(),)
    out=[Q()]*max(1,len(a)-len(b)+1)
    while a!=(Q(),) and len(a)>=len(b):
        n=len(a)-len(b);v=a[-1]/b[-1];out[n]+=v
        a=p.add(a,p.scale(-v,(Q(),)*n+b))
    return p.trim(tuple(out)),a


class RF:
    """Canonical exact Q(r); no numerical or third-party symbolic dependency."""
    __slots__=('n','d')
    def __init__(self,n=0,d=(Q(1),)):
        if isinstance(n,RF):self.n,self.d=n.n,n.d;return
        n=p.trim(tuple(map(Q,n))) if isinstance(n,(list,tuple)) else (Q(n),)
        d=p.trim(tuple(map(Q,d)));assert d!=(Q(),)
        if n==(Q(),):self.n,self.d=n,(Q(1),);return
        a,b=n,d
        while b!=(Q(),):_,rem=divmod_poly(a,b);a,b=b,rem
        g=p.scale(1/a[-1],a);n,rem=divmod_poly(n,g);assert rem==(Q(),)
        d,rem=divmod_poly(d,g);assert rem==(Q(),)
        self.n=p.scale(1/d[-1],n);self.d=p.scale(1/d[-1],d)
    def __add__(self,b):
        b=RF(b);return RF(p.add(p.mul(self.n,b.d),p.mul(b.n,self.d)),p.mul(self.d,b.d))
    __radd__=__add__
    def __neg__(self):return RF(p.scale(-1,self.n),self.d)
    def __sub__(self,b):return self+-RF(b)
    def __rsub__(self,b):return RF(b)+-self
    def __mul__(self,b):
        b=RF(b);return RF(p.mul(self.n,b.n),p.mul(self.d,b.d))
    __rmul__=__mul__
    def __truediv__(self,b):
        b=RF(b);assert b.n!=(Q(),);return RF(p.mul(self.n,b.d),p.mul(self.d,b.n))
    def __rtruediv__(self,b):return RF(b)/self
    def __pow__(self,n):
        assert type(n) is int and n>=0
        out=RF(1)
        for _ in range(n):out=out*self
        return out
    def __eq__(self,b):
        b=RF(b);return self.n==b.n and self.d==b.d
    def at(self,r):return p.evaluate(self.n,Q(r))/p.evaluate(self.d,Q(r))
    def order(self):
        assert self.d[0]
        return next((i for i,v in enumerate(self.n) if v),None)
    def upper(self,rmax=RMAX):
        tail=sum((abs(v)*rmax**i for i,v in enumerate(self.d) if i),Q())
        lower=abs(self.d[0])-tail;assert lower>0
        return sum((abs(v)*rmax**i for i,v in enumerate(self.n)),Q())/lower
    def lower(self,rmax=RMAX):
        assert self.n[0]
        top=abs(self.n[0])-sum((abs(v)*rmax**i for i,v in enumerate(self.n) if i),Q())
        assert top>0;self.upper(rmax)
        return top/sum((abs(v)*rmax**i for i,v in enumerate(self.d)),Q())
    def encode(self):return {'numerator':list(map(str,self.n)),'denominator':list(map(str,self.d))}


def family():
    r=RF((0,1));v=1+r;a=1-C*r;q0=Q(1,2)
    gx=r*a*v;fx=r*a;px=q0/(10*a*v);qx=q0/a
    gy=r/v;fy=r;py=q0*v/10;qy=RF(q0)
    dp=K2*(py*py-px*px);dq=qy*qy-qx*qx;dz=py*qy-px*qx
    S=Q(355,224)*dp+Q(25,64)*dq
    l=S/(K2*(1/v-v))
    U=-Q(5,12)*dp+Q(7,30)*S;V=-Q(5,32)*dp-Q(7,192)*dq
    Ax=r
    Bx=(-Q(7,40)*V/v-Q(5,48)/K2*((v-1/v)*Ax+U*v)-dz/96)/(Q(7,40)*(1/v-v))
    X=(gx,fx,px,qx,RF(),Ax/(K2*gx),l/fx,Bx/fx)
    Y=(gy,fy,py,qy,RF(),(Ax+U)/(K2*gy),l/fy,(Bx+V)/fy)
    return r,X,Y,dp


def field_add(a,b):return a[0]+b[0],a[1]+b[1]
def field_scale(c,a):return c*a[0],c*a[1]
def field_product(X,i,j):
    value=X[i]*X[j];degree=PARITY[i]+PARITY[j]
    return (K2*value,RF()) if degree==2 else (RF(),value) if degree==1 else (value,RF())
def weights(X):return tuple(field_product(X,i,j) for i,j in t.cut.PAIRS)
def project(rows,W):
    out=[]
    for row in rows:
        value=(RF(),RF())
        for c,w in zip(row,W):value=field_add(value,field_scale(c,w))
        out.append(value)
    return tuple(out)
def lower_data(X):
    pairs=((0,0),(1,1),(0,1),(0,2),(1,3))
    return tuple(field_product(X,i,j) for i,j in pairs)+(field_add(field_product(X,0,3),field_scale(10,field_product(X,1,2))),(RF(),RF()))
def field_difference(A,B):return tuple((a[0]-b[0],a[1]-b[1]) for a,b in zip(A,B))
def field_zero(a):return a[0]==0 and a[1]==0


def validate(c):
    assert c['schema']=='marici.photon-box-cut-sharpness.v1' and c['owner']=='marici.Nima'
    for k in ('unit_box_actual_source_obstruction_above_one_third','one_third_cut_exponent_sharp',
              'equal_degree5_data_and_transport_certified','quartic_bounds_uniformly_certified'):
        assert c[k] is True,k
    for k in ('uniform_half_power_cut_modulus_derived','optimal_modulus_prefactor_derived','physical_source_box_licensed',
              'physical_matching_selected','native_or_UV_dynamics_derived','C12_budget_renewed'):
        assert c[k] is False,k


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate(c);parent=previous.build()
    r,X,Y,dp=family();WX,WY=weights(X),weights(Y)
    BJ=project(t.FLOW,WX);BY=project(t.FLOW,WY)
    assert all(field_zero(v) for v in field_difference(BY,BJ))
    JX,JY=lower_data(X),lower_data(Y);dJ=field_difference(JY,JX)
    assert all(field_zero(v) for v in dJ[3:])
    assert all((a.order()==3 if a!=0 else b.order()==3) for a,b in dJ[:3])
    RX=project(previous.prior.equal.previous.RESP,WX);RY=project(previous.prior.equal.previous.RESP,WY)
    for value,line in zip(field_difference(RY,RX),previous.prior.equal.LINE):
        assert value[0]==line*dp/4032 and value[1]==0
    assert dp.order()==1
    full_cut_difference=field_difference(project(previous.CUT_ROWS,WY),project(previous.CUT_ROWS,WX))
    for value,line in zip(full_cut_difference,previous.prior.flat_cut(previous.prior.equal.LINE)):
        assert value[0]==line*dp/4032 and value[1]==0
    # Canonical cancellations leave no pole at r=0; absolute rational-function bounds certify the whole interval.
    caps=tuple(tuple(z.upper()* (2 if parity else 1) for z,parity in zip(S,PARITY)) for S in (X,Y))
    assert all(v<1 for row in caps for v in row) and 1<K2<4
    quotient=tuple((a/r**3,b/r**3) for a,b in dJ[:3])
    data_upper=max(a.upper()+2*b.upper() for a,b in quotient)
    b_lower=quotient[0][0].lower();cut_lower=(dp/(224*r)).lower()
    assert b_lower>max(quotient[1][0].upper(),2*quotient[2][1].upper())
    assert data_upper>0 and b_lower>0 and cut_lower>0
    data_limit=K2*(4-2*C);cut_limit=data_limit/89600
    assert abs(quotient[0][0].at(0))==data_limit and dp.at(0)==0
    assert (dp/r/224).at(0)==cut_limit
    assert data_limit>abs(quotient[1][0].at(0)) and data_limit>2*abs(quotient[2][1].at(0))
    # The real-source zero-transport theorem and a nonzero cubic coefficient certify nonzero transport.
    assert X[3].lower()>0
    samples=[]
    for n in (100,1000,10000):
        rr=Q(1,n);dat=abs(dJ[0][0].at(rr))
        assert dat==max(abs(a.at(rr))+2*abs(b.at(rr)) for a,b in dJ)
        cut=abs(dp.at(rr))/224
        assert b_lower*rr**3<=dat<=data_upper*rr**3 and cut>=cut_lower*rr
        # The rational leading-Gram component dominates even the 2*k-coefficient bound, so this is the actual gap.
        assert cut<=previous.modulus(dat,Q(1))
        samples.append({'r':str(rr),'joint_data_gap':str(dat),'cut_gap':str(cut),
                        'data_gap_over_r_cubed':str(dat/rr**3),'cut_gap_over_r':str(cut/rr)})
    refused=['infer_half_power_from_prior_half_power_ceiling','hide_quartic_poles_in_asymptotic_witness',
             'use_equal_transport_without_equal_lower_degree5_data','equate_algebraic_source_to_physically_matched_source']
    for key in ('uniform_half_power_cut_modulus_derived','optimal_modulus_prefactor_derived','physical_source_box_licensed',
                'physical_matching_selected','native_or_UV_dynamics_derived','C12_budget_renewed'):
        try:validate({**c,key:True})
        except AssertionError:refused.append(key)
        else:raise AssertionError('unearned sharp-exponent promotion: '+key)
    paths={ROOT/path for path in parent['source_sha256']};paths.update((CONTRACT,PROOF,TEST,MANIFEST,Path(__file__).resolve()))
    return {'schema':'marici.photon-box-cut-sharpness-receipt.v1','status':'pass',
        'scope':'conditional_unit_box_algebraic_two_source_family_sharp_one_third_cut_exponent_not_physical_prior',
        'source_sha256':{path.relative_to(ROOT).as_posix():hashlib.sha256(path.read_bytes()).hexdigest() for path in sorted(paths)},
        'algebraic_leading_ratio_square':str(K2),'scale_slope':str(C),'parameter_upper':str(RMAX),
        'source_coefficients_in_basis_1_k':{'parity':list(PARITY),'X':[v.encode() for v in X],'Y':[v.encode() for v in Y]},
        'uniform_source_coordinate_bounds':[[str(v) for v in row] for row in caps],
        'data_gap_upper_coefficient':str(data_upper),'data_gap_positive_lower_coefficient':str(b_lower),
        'cut_gap_positive_lower_coefficient':str(cut_lower),'data_gap_over_r_cubed_limit':str(data_limit),
        'cut_gap_over_r_limit':str(cut_limit),'exact_samples':samples,
        'sharp_exponent':'1/3','excluded_exponents':'alpha>1/3',
        'general_real_asymptotic_proof_machine_formalized':False,
        **{k:v for k,v in c.items() if isinstance(v,bool)},'hostile_controls_refused':refused}


def main():
    q=argparse.ArgumentParser(description=__doc__);q.add_argument('--check',action='store_true');a=q.parse_args();r=build()
    if a.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale source-box exponent-sharpness receipt'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','sharp_exponent','excluded_exponents','equal_degree5_data_and_transport_certified','physical_source_box_licensed')}))

if __name__=='__main__':main()
