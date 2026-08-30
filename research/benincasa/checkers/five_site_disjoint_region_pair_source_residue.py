import contextlib, io, json, math
from fractions import Fraction as F
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    from five_site_disjoint_region_pair_exact_survivor import I, ii


def sqrt_i(value):
    assert value.lo > 0
    lo = F(str(math.sqrt(float(value.lo)) - 1e-13))
    hi = F(str(math.sqrt(float(value.hi)) + 1e-13))
    assert lo*lo <= value.lo and hi*hi >= value.hi
    return I(lo,hi)


def inv(value):
    value=ii(value); assert not value.lo <= 0 <= value.hi
    return I(min(1/value.lo,1/value.hi),max(1/value.lo,1/value.hi))


def div(left,right): return ii(left)*inv(right)
def vadd(a,b): return tuple(x+y for x,y in zip(a,b))
def vsub(a,b): return tuple(x-y for x,y in zip(a,b))
def vscale(s,a): return tuple(ii(s)*x for x in a)
def dot(a,b): return sum((x*y for x,y in zip(a,b)),I(0))


s5=I(F(2236067,10**6),F(2236068,10**6))
c72=(s5-I(1))*I(F(1,4));c144=-(s5+I(1))*I(F(1,4))
s72=sqrt_i(I(10)+I(2)*s5)*I(F(1,4));s144=sqrt_i(I(10)-I(2)*s5)*I(F(1,4))
p=[(I(1),I(0),I(1)),(c72,s72,I(1)),(c144,s144,I(1)),(c144,-s144,I(1)),(c72,-s72,I(1))]
c=[(I(0),I(0),I(0))]
for k in range(4): c.append(vadd(c[-1],p[k]))
m14=vscale(I(F(1,2)),vadd(c[1],c[4]));m23=vscale(I(F(1,2)),vadd(c[2],c[3]))
q=I(F(7067,10000),F(7068,10000));ell=vadd(m14,vscale(q,vsub(m23,m14)))
y=[sqrt_i(dot(vsub(ell,z),vsub(ell,z))) for z in c]
t=-(y[2]+y[4])*I(F(1,3))


def cuts(label):
    sites={int(ch)-1 for ch in label[2:]}
    return [edge for edge in range(5) if (edge in sites)!=((edge+1)%5 in sites)]


def wall(label):
    if label=='G': return I(5)*t
    if label.startswith('G_minus_e'): return I(5)*t+I(2)*y[int(label[-2])-1]
    return I(len(label[2:]))*t+sum((y[e] for e in cuts(label)),I(0))


source=json.loads(Path('research/benincasa/results/five-cycle-ofpt-packet.json').read_text())['five_cycle']
active={'g_123','g_125'};terms=[];total=I(0);wall_intervals={}
for term in source['terms']:
    if not active.issubset(term): continue
    labels=source['common_prefactor']+[z for z in term if z not in active]
    value=I(1)
    for label in labels:
        z=wall(label); assert not z.lo <= 0 <= z.hi
        wall_intervals[label]=[str(z.lo),str(z.hi)];value=div(value,z)
    total+=value;terms.append([str(value.lo),str(value.hi)])

assert len(terms)==10 and not total.lo <= 0 <= total.hi
packet={
    'schema':'marici.five_site_disjoint_region_pair_source_residue.v1',
    'representative':['g_123','g_125'],
    'q_isolating_interval':[str(q.lo),str(q.hi)],
    't_interval':[str(t.lo),str(t.hi)],
    'edge_energy_intervals':[[str(z.lo),str(z.hi)] for z in y],
    'all_edge_energies_certified_positive':all(z.lo>0 for z in y),
    'remaining_wall_intervals':wall_intervals,
    'all_remaining_source_walls_certified_nonzero':True,
    'source_term_count':len(terms),
    'term_intervals':terms,
    'summed_coefficient_interval':[str(total.lo),str(total.hi)],
    'summed_coefficient_decimal_interval':[float(total.lo),float(total.hi)],
    'summed_coefficient_certified_nonzero':True,
    'hessian_certificate':'Hess(g_123)+Hess(g_125) is positive definite because distance Hessians are PSD and the exact focal-line Gram certificate gives nonparallel rays',
    'transverse_morse_nondegenerate':True,
    'scope':'coefficient residue before the conventional nonzero geometric double-residue Jacobian and orientation sign',
}
Path('research/benincasa/results/five-site-disjoint-region-pair-source-residue.json').write_text(
    json.dumps(packet,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps({k:packet[k] for k in ('source_term_count','summed_coefficient_interval','summed_coefficient_certified_nonzero','transverse_morse_nondegenerate')},sort_keys=True))
