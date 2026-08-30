import contextlib, io, json
from fractions import Fraction as F
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    from five_site_disjoint_region_pair_exact_survivor import I


def ka(a,b=(F(0),F(0))): return (a[0]+b[0],a[1]+b[1])
def kn(a): return (-a[0],-a[1])
def km(a,b): return (a[0]*b[0]+5*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def ks(q,a): return (q*a[0],q*a[1])


def pa(a,b):
    n=max(len(a),len(b));return [ka(a[i] if i<len(a) else (F(0),F(0)),b[i] if i<len(b) else (F(0),F(0))) for i in range(n)]
def pm(a,b):
    out=[(F(0),F(0))]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]=ka(out[i+j],km(x,y))
    return out
def ps(q,a): return [ks(q,x) for x in a]


A=(F(70),F(25));B=(F(-170),F(-60));C=(F(85),F(30))
d2=(F(5,8),F(1,8));b2=(F(21,8),F(1,8))
# D=9z-d2, and B^2*b2*D-(A*b2+C*D)^2=0.
D=[kn(d2),(F(9),F(0))]
left=ps(F(1),pm([km(B,B),],[b2]+[])) # scalar B^2*b2
left=pm(left,D)
right_base=pa([km(A,b2)],ps(F(1),pm([C],D)))
poly=pa(left,ps(F(-1),pm(right_base,right_base)))
while poly and poly[-1]==(F(0),F(0)):poly.pop()
assert len(poly)==3

# Rational field norm P(z)P^sigma(z).
conj=[(a,-b) for a,b in poly];norm=pm(poly,conj)
assert all(b==0 for a,b in norm)
norm_q=[a for a,b in norm]
den=1
from math import gcd
for q in norm_q:den=den*q.denominator//gcd(den,q.denominator)
ints=[int(q*den) for q in norm_q];g=0
for n in ints:g=gcd(g,abs(n))
ints=[n//g for n in ints]
if ints[-1]<0:ints=[-n for n in ints]

q=I(F(7067,10000),F(7068,10000));s=I(F(2236067,10**6),F(2236068,10**6))
def kval(x):return I(x[0])+I(x[1])*s
def inv(x):assert x.lo>0 or x.hi<0;return I(min(1/x.lo,1/x.hi),max(1/x.lo,1/x.hi))
z=(kval(d2)+kval(b2)*inv(q.square()))*I(F(1,9))
assert F(7464,10000)<z.lo<z.hi<F(7468,10000)

packet={
 'schema':'marici.five_site_region_pair_threshold_polynomial.v1',
 'representative':['g_123','g_125'],
 'identity':'9*t^2=d2+b2/q^2 from stationarity on the fixed line',
 'quadratic_over_Qsqrt5_coefficients':[[str(a),str(b)] for a,b in poly],
 'rational_norm_coefficients_low_to_high':ints,
 'rational_norm_polynomial':' + '.join(f'({c})*z^{i}' for i,c in enumerate(ints)),
 'physical_root_t_squared_interval':[str(z.lo),str(z.hi)],
 'physical_root_t_interval':'negative square root, because internal energies are positive',
 'classification':'exact homogeneous physical Landau coefficient divisor over the existing region-pair incidence',
 'new_carrier_datum':False,
}
Path('research/benincasa/results/five-site-region-pair-threshold-polynomial.json').write_text(
 json.dumps(packet,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps({k:packet[k] for k in ('rational_norm_coefficients_low_to_high','physical_root_t_squared_interval','new_carrier_datum')},sort_keys=True))
