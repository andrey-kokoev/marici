"""Independent exact consumer of the fixed-precision c=1 rank-three certificate artifact."""
from fractions import Fraction as F
import json,re
p=json.load(open('research/grothendieck/results/c-one-rank-three-iv-certificate.json'))
assert p['passed'] is True and p['schema']=='marici.grothendieck.c-one-rank-three-iv-certificate.v1'
def number(s):
 m=re.search(r'[-+]?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?',s);assert m;return F(m.group())
def cell(name):
 v=p['cells'][name];return(number(v[0]),number(v[1]))
def add(a,b):return(a[0]+b[0],a[1]+b[1])
def neg(a):return(-a[1],-a[0])
def mul(a,b):
 v=[x*y for x in a for y in b];return(min(v),max(v))
def sub(a,b):return add(a,neg(b))
def sc(k,a):return mul((F(k),F(k)),a)
d,x,y=cell('baseline'),cell('lag1'),cell('lag2');x2=mul(x,x);m2=sub(mul(d,d),x2)
det=sub(add(sub(mul(mul(d,d),d),sc(2,mul(d,x2))),sc(2,mul(x2,y))),mul(d,mul(y,y)))
assert d[0]>0 and m2[0]>0 and det[0]>0
fl=lambda z:[float(z[0]),float(z[1])]
print(json.dumps({'schema':'marici.nima.c-one-rank-three-certificate-consumer.v1','status':'passed','cells':{'baseline':fl(d),'lag1':fl(x),'lag2':fl(y)},'recomputed_minor2':fl(m2),'recomputed_determinant3':fl(det),'positive_definite_rank_three':True,'claim_boundary':'exact consumer of materialized coherent c=1 certificate; external Weil identification remains absent'},sort_keys=True))
