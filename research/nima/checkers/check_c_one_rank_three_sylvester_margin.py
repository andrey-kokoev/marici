"""Exact interval Sylvester margins around the coherent c=1 rank-three centers."""
from fractions import Fraction as F
import json,itertools
def I(x,e): return (F(x)-F(e),F(x)+F(e))
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def neg(a): return (-a[1],-a[0])
def mul(a,b):
 v=[a[i]*b[j] for i in (0,1) for j in (0,1)];return (min(v),max(v))
def scale(k,a): return mul((F(k),F(k)),a)
def sub(a,b): return add(a,neg(b))
E='0.06101538'; d=I('2.12511463965217217',E); c1=I('-0.846660221734685927',E); c2=I('1.50462976096',E)
minor2=sub(mul(d,d),mul(c1,c1))
# det [[d,c1,c2],[c1,d,c1],[c2,c1,d]] = d^3-2dc1^2+2c1^2c2-dc2^2
c1sq=mul(c1,c1); det3=sub(add(sub(mul(mul(d,d),d),scale(2,mul(d,c1sq))),scale(2,mul(c1sq,c2))),mul(d,mul(c2,c2)))
assert d[0]>0 and minor2[0]>0 and det3[0]>0
# Deliberate failure with N=3 width.
Eb='0.477499157967168'; db=I('2.12511463965217217',Eb); x=I('-0.846660221734685927',Eb); y=I('1.50462976096',Eb); xs=mul(x,x)
det_bad=sub(add(sub(mul(mul(db,db),db),scale(2,mul(db,xs))),scale(2,mul(xs,y))),mul(db,mul(y,y)))
assert det_bad[0]<0
out=lambda a:[float(a[0]),float(a[1])]
print(json.dumps({'schema':'marici.nima.c-one-rank-three-sylvester-margin.v1','status':'passed','N':4,'entry_error':float(F(E)),'diagonal':out(d),'leading_minor_2':out(minor2),'determinant_3':out(det3),'positive_definite_certified_conditional_on_entry_boxes':True,'N3_deliberate_failure_determinant':out(det_bad),'claim_boundary':'exact interval algebra around numerical centers; directed derivation of the entry boxes remains open'},sort_keys=True))
