"""Exact packet transport for declared same-slot reference composition.

The context policy is an input. Mean plus centered retained records is a
coordinate change, not a quotient and not a new physical measurement law.
"""
from contextlib import redirect_stdout
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import io
import json
import runpy

ROOT=Path(__file__).resolve().parents[3]
with redirect_stdout(io.StringIO()):
    base=runpy.run_path(str(Path(__file__).with_name('check_shared_leg_dg_realization.py')))
add,scale,mul,Z,I,H,K=(base[k] for k in ('add','scale','mul','Z','I','H','K'))
d=scale(2,I); r=scale(F(1,2),I)
assert mul(d,r)==mul(r,d)==I


def sub(a,b): return add(a,scale(-1,b))
def bridge(b,a): return mul(mul(b,r),a)
def total(items):
    out=Z
    for item in items: out=add(out,item)
    return out


def mean(items,weights):
    assert len(items)==len(weights) and sum(weights)==1
    return total(scale(w,item) for w,item in zip(weights,items))


def split(items,weights):
    m=mean(items,weights)
    delta=tuple(sub(item,m) for item in items)
    assert mean(delta,weights)==Z
    return m,delta


def restore(packet):
    m,delta=packet
    return tuple(add(m,item) for item in delta)


def covariance(b,a,weights):
    _,db=split(b,weights); _,da=split(a,weights)
    return mean(tuple(bridge(y,x) for y,x in zip(db,da)),weights)


def join(b,a):
    assert len(b)==len(a)
    return tuple(add(add(x,y),bridge(y,x)) for y,x in zip(b,a))


def packet_join(pb,pa,weights):
    mb,db=pb; ma,da=pa
    terms=tuple(bridge(y,x) for y,x in zip(db,da))
    correction=mean(terms,weights)
    m=add(add(add(ma,mb),bridge(mb,ma)),correction)
    delta=tuple(sub(total((x,y,bridge(mb,x),bridge(y,ma),cross)),correction)
                for y,x,cross in zip(db,da,terms))
    assert mean(delta,weights)==Z
    return m,delta


labels=tuple((tag,i,j) for tag,n in (('a',11),('s',4)) for i,j in product(range(n),repeat=2))
assert len(labels)==137

def fixture(seed):
    result=[]
    for tag,i,j in labels:
        if tag=='a':
            x=add(I,scale(F(i+seed,3),H)); y=add(I,scale(F(j-seed,5),K))
        else:
            x=add(I,scale(F(i-seed,7),K)); y=add(I,scale(F(j+seed,11),H))
        result.append(sub(mul(y,x),d))
    return tuple(result)


A,B,C=(fixture(k) for k in range(3))
partitions=[]
for axis in (1,2):
    groups={}
    for index,label in enumerate(labels): groups.setdefault((label[0],label[axis]),[]).append(index)
    partitions.append(tuple(groups.values()))

for weights in (tuple([F(1,137)]*137),tuple(F(i+1,137*138//2) for i in range(137))):
    pa,pb,pc=(split(x,weights) for x in (A,B,C))
    assert restore(pa)==A
    assert packet_join(pb,pa,weights)==split(join(B,A),weights)
    assert packet_join(pc,packet_join(pb,pa,weights),weights)==packet_join(packet_join(pc,pb,weights),pa,weights)
    assert join(C,join(B,A))==join(join(C,B),A)
    zero=(Z,)*137
    assert packet_join(split(zero,weights),pa,weights)==pa
    assert packet_join(pa,split(zero,weights),weights)==pa

    # Associativity compatibility of the multiplicativity defect. This is an
    # identity of matrices, not a claim that the defect is null-homotopic.
    BA=tuple(bridge(b,a) for b,a in zip(B,A))
    CB=tuple(bridge(c,b) for c,b in zip(C,B))
    lhs=add(covariance(CB,A,weights),bridge(covariance(C,B,weights),mean(A,weights)))
    rhs=add(covariance(C,BA,weights),bridge(mean(C,weights),covariance(B,A,weights)))
    assert lhs==rhs
    assert covariance((d,)*137,A,weights)==covariance(A,(d,)*137,weights)==Z

    # Both indexed presentations retain all members. Within-family plus
    # between-family covariance equals the full correction (total covariance).
    for groups in partitions:
        masses=[]; means_a=[]; means_b=[]; local_cov=[]; rebuilt={}; joined_means=[]
        for members in groups:
            mass=sum(weights[i] for i in members); masses.append(mass)
            local_weights=tuple(weights[i]/mass for i in members)
            fa=tuple(A[i] for i in members); fb=tuple(B[i] for i in members)
            qa=split(fa,local_weights); qb=split(fb,local_weights)
            means_a.append(qa[0]); means_b.append(qb[0])
            local_cov.append(covariance(fb,fa,local_weights))
            joined_means.append(packet_join(qb,qa,local_weights)[0])
            rebuilt.update(zip(members,restore(qa)))
        assert tuple(rebuilt[i] for i in range(137))==A
        assert mean(tuple(joined_means),tuple(masses))==mean(join(B,A),weights)
        assert covariance(B,A,weights)==add(mean(tuple(local_cov),tuple(masses)),
                    covariance(tuple(means_b),tuple(means_a),tuple(masses)))

# A genuine shared-leg control: reflected scalar row perturbations have equal
# means and second moments but unequal third iterated reference responses.
def scalar_rows(sign):
    shifts=(1,1,-2)+(0,)*8
    out=[]
    for tag,i,j in labels:
        x=scale(1+F(sign*shifts[i],2),I) if tag=='a' else I
        out.append(sub(mul(d,x),d))
    return tuple(out)

w=(F(1,137),)*137
positive,negative=scalar_rows(1),scalar_rows(-1)
assert mean(positive,w)==mean(negative,w)==Z
assert covariance(positive,positive,w)==covariance(negative,negative,w)!=Z
assert mean(join(positive,positive),w)==mean(join(negative,negative),w)
triple_positive=mean(join(positive,join(positive,positive)),w)
triple_negative=mean(join(negative,join(negative,negative)),w)
assert triple_positive==scale(F(165,274),I)
assert triple_negative==scale(F(231,274),I)

# No nontrivial normalized averaging character for same-context multiplication:
# e_i*d is a bridge-idempotent, but its mean w_i*d is not unless w_i^2=w_i.
e=(d,)+(Z,)*136
assert tuple(bridge(v,v) for v in e)==e
assert mean(e,w)!=bridge(mean(e,w),mean(e,w))
assert w[0]!=w[0]**2

# Correlated and independent context policies have the same input means and
# different outputs. Both are legitimate source operations; coherence cannot
# select between them. Constant source weights and index alignment are inputs.
xs=(H,scale(-1,H)); ys=(K,scale(-1,K)); half=(F(1,2),)*2
correlated=mean(tuple(bridge(y,x) for y,x in zip(ys,xs)),half)
independent=mean(tuple(bridge(y,x) for y,x in product(ys,xs)),(F(1,4),)*4)
assert correlated==bridge(K,H)!=Z and independent==Z
zs=(I,add(H,K))
# Flattening the retained context triples identifies both parenthesizations.
left=tuple(join((zs[k],),join((ys[j],),(xs[i],)))[0]
           for i,j,k in product(range(2),repeat=3))
right=tuple(join(join((zs[k],),(ys[j],)),(xs[i],))[0]
            for i,j,k in product(range(2),repeat=3))
assert left==right
assert mean(left,(F(1,8),)*8)==join((mean(zs,half),),join((mean(ys,half),),(mean(xs,half),)))[0]

result={
    'status':'passed',
    'classification':'full_packet_associative_transport_with_derived_covariance',
    'obligation':'route/coherencer compatibility before mean-only readout descent',
    'stratum':'137 retained matrix slots; fixed invertible reference; declared same-slot composition; uniform and nonuniform positive weights',
    'checks':{
        'packet_reconstruction':True,'associativity_and_units':True,
        'source_and_target_grouping_transport':True,'total_covariance':True,
        'defect_associativity_identity':True,'mean_only_multiplicativity_falsified':True,
        'mean_plus_second_moment_closure_falsified':True,
        'triple_readouts':[str(F(165,274)),str(F(231,274))],
        'independent_context_associativity':True,
        'context_policy_not_selected_by_coherence':True},
    'unsupported':['physical context-incidence selection','marked-probe multiplication adapter',
                   'full intended rung transport','weak-return extension of this packet law',
                   'physical metric or coupling normalization'],
    'next_constructor':'source-defined joint context incidence, transported with retained members and masses'
}
output=ROOT/'research/nima/results/mean-fluctuation-transport.json'
output.parent.mkdir(parents=True,exist_ok=True)
output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
