"""Exact certificates for positive-diagonal real observations with an l1 budget."""
from fractions import Fraction as F
import hashlib
import json
import sys

MODEL='positive-diagonal-real-l1-v1'


def digest(p):return hashlib.sha256(json.dumps(p,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def rational(x):
    if not isinstance(x,str):raise ValueError('Rationals must be strings')
    return F(x)


def parse(p):
    if p['model']!=MODEL or not 1<=len(p['rows'])<=64:raise ValueError('Unsupported model or size')
    rows=[]
    for row in p['rows']:
        dl,dh=map(rational,row['data']);el,eh=map(rational,row['calibration']);w=rational(row['weight'])
        if not(dl<=dh and 0<el<=eh and w>0):raise ValueError('Invalid row')
        rows.append((dl,dh,el,eh,w))
    B=rational(p['budget']);target=list(map(rational,p['target']['coefficients']))
    if B<0 or len(target)!=len(rows):raise ValueError('Invalid budget or target')
    return rows,B,target,rational(p['target']['threshold'])


def zero(lo,hi):return F(0) if lo<=0<=hi else min((lo,hi),key=abs)


def dual(boxes,weights,target,B):
    best=None
    for lam in {F(0)}|{abs(a)/w for a,w in zip(target,weights)}:
        value=-lam*B
        for (lo,hi),w,a in zip(boxes,weights,target):
            points=[lo,hi]+([F(0)] if lo<=0<=hi else [])
            value+=min(a*x+lam*w*abs(x) for x in points)
        if best is None or value>best[0]:best=value,lam
    return {'bound':str(best[0]),'lambda':str(best[1])}


def maximize(boxes,weights,target,B):
    x=[zero(*b) for b in boxes]
    left=B-sum(w*abs(a) for w,a in zip(weights,x))
    if left<0:return None
    for i in sorted(range(len(x)),key=lambda i:abs(target[i])/weights[i],reverse=True):
        if target[i]==0:continue
        endpoint=boxes[i][1] if target[i]>0 else boxes[i][0]
        distance=min(abs(endpoint-x[i]),left/weights[i])
        x[i]+=distance if endpoint>x[i] else -distance
        left-=distance*weights[i]
    return x


def solve_fixed(p):
    rows,B,target,threshold=parse(p)
    outer=[];inner=[];weights=[]
    for dl,dh,el,eh,w in rows:
        corners=(dl/el,dl/eh,dh/el,dh/eh)
        outer.append((min(corners),max(corners)))
        inner.append((max(dl/el,dl/eh),min(dh/el,dh/eh)));weights.append(w)
    cert={'version':1,'problem_sha256':digest(p),'status':'UNRESOLVED'}
    lower_cost=sum(w*abs(zero(*b)) for w,b in zip(weights,outer))
    if lower_cost>B:
        cert.update(status='INFEASIBLE',minimum_cost_lower_bound=str(lower_cost));return cert
    ld=dual(outer,weights,target,B);ud=dual(outer,weights,[-a for a in target],B)
    if any(lo>hi for lo,hi in inner):return cert
    maximum=maximize(inner,weights,target,B)
    minimum=maximize(inner,weights,[-a for a in target],B)
    if maximum is None:return cert
    if F(ld['bound'])>threshold:
        cert.update(status='TARGET_TRUE',witness=list(map(str,maximum)),dual=ld)
    elif -F(ud['bound'])<=threshold:
        cert.update(status='TARGET_FALSE',witness=list(map(str,minimum)),dual=ud)
    elif sum(a*x for a,x in zip(target,minimum))<=threshold<sum(a*x for a,x in zip(target,maximum)):
        cert.update(status='AMBIGUOUS',false_witness=list(map(str,minimum)),true_witness=list(map(str,maximum)))
    return cert


def solve(p):
    """Preserve v1 certificates; try constant-numerator parametric witnesses last."""
    previous=solve_fixed(p)
    if previous['status']!='UNRESOLVED':return previous
    rows,B,target,threshold=parse(p)
    data=[(l,u) for l,u,e,f,w in rows]
    costs=[w/e for l,u,e,f,w in rows]
    numerators=[zero(*box) for box in data]
    if sum(w*abs(d) for w,d in zip(costs,numerators))>B:return previous
    candidates=[numerators]
    for endpoint in (2,3):
        scores=[a/row[endpoint] for a,row in zip(target,rows)]
        for sign in (1,-1):
            candidate=maximize(data,costs,[sign*a for a in scores],B)
            if candidate is not None:candidates.append(candidate)
    outer=[];weights=[]
    for l,u,e,f,w in rows:
        corners=(l/e,l/f,u/e,u/f);outer.append((min(corners),max(corners)));weights.append(w)
    lower=dual(outer,weights,target,B)
    upper=dual(outer,weights,[-a for a in target],B)
    cert={'version':2,'problem_sha256':digest(p),'status':'UNRESOLVED',
          'witness_semantics':'for-every-calibration-there-exists-source'}
    def encode(d):return {'kind':'inverse-calibration','numerators':list(map(str,d))}
    if F(lower['bound'])>threshold:
        cert.update(status='TARGET_TRUE',witness=encode(numerators),dual=lower);return cert
    if -F(upper['bound'])<=threshold:
        cert.update(status='TARGET_FALSE',witness=encode(numerators),dual=upper);return cert
    true=None;false=None
    for d in candidates:
        lo=hi=F(0)
        for a,value,(_,_,e,f,_) in zip(target,d,rows):
            ends=(a*value/e,a*value/f);lo+=min(ends);hi+=max(ends)
        if lo>threshold:true=d
        if hi<=threshold:false=d
    if true is not None and false is not None:
        cert.update(status='AMBIGUOUS',true_witness=encode(true),false_witness=encode(false));return cert
    return previous


if __name__=='__main__':
    with open(sys.argv[1],encoding='utf-8') as stream:problem=json.load(stream)
    print(json.dumps(solve(problem),indent=2))
