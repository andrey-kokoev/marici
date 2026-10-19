"""Common exact L/G -> N protocol assembler and projector-defect energy.

Particle-neutral input: coordinate labels, diagonal positive metric, two
commuting metric-orthogonal projections L,G. Derives N=GL and Hhat=2I-L-G.
Energy convention: H=(pi/4) Hhat, using defects L-I and G-I. This is a
protocol constraint energy, not native triangle dynamics or a rest mass.
Coefficients use Q(sqrt(2),sqrt(3),sqrt(5),i), masks 1,2,4,8.
"""
from pathlib import Path
from fractions import Fraction as F
import sys
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/voevodsky/checkers'))
from check_pentachoron_spin_interfaces import A,ZERO,ONE


def decode(value):return A(tuple(F(value.get(str(i),'0')) for i in range(16)))
def clean(m):return {k:v for k,v in m.items() if v!=ZERO}
def plus(*matrices):
    out={}
    for m in matrices:
        for k,v in m.items():out[k]=out.get(k,ZERO)+v
    return clean(out)
def scaled(s,m):return clean({k:s*v for k,v in m.items()})
def product(a,b):
    rows={};out={}
    for (i,j),x in a.items():rows.setdefault(j,[]).append((i,x))
    for (j,k),y in b.items():
        for i,x in rows.get(j,[]):out[i,k]=out.get((i,k),ZERO)+x*y
    return clean(out)
def sharp(m,metric):return {(j,i):x.flip(8)*(metric[i]/metric[j]) for (i,j),x in m.items()}
def tr(m):return sum((v for (i,j),v in m.items() if i==j),ZERO)
def integer_trace(m):
    t=tr(m)
    if any(t.c[1:]) or t.c[0].denominator!=1:raise ValueError('Expected integer projector trace')
    return int(t.c[0])
def encode(m):return [{'target':i,'source':j,'coefficient':v.record()} for (i,j),v in sorted(m.items())]
def read_operator(rows,n):
    m={}
    for r in rows:
        i,j=r['target'],r['source']
        if not isinstance(i,int) or not isinstance(j,int) or not 0<=i<n or not 0<=j<n:raise ValueError('Invalid operator endpoint')
        if (i,j) in m:raise ValueError('Duplicate operator endpoint')
        v=decode(r['coefficient'])
        if v==ZERO:raise ValueError('Zero is not a transfer')
        m[i,j]=v
    return m


def assemble(source):
    if set(source)!={'schema','coordinates','metric','local','alignment','provenance'} or source['schema']!='marici.metric-coefficient-source.v1':raise ValueError('Unexpected coefficient source fields')
    labels=source['coordinates'];n=len(labels);metric=tuple(map(F,source['metric']))
    if n==0 or len(set(labels))!=n or len(metric)!=n or any(x<=0 for x in metric):raise ValueError('Invalid coordinate metric')
    L=read_operator(source['local'],n);G=read_operator(source['alignment'],n);I={(i,i):ONE for i in range(n)}
    for m in (L,G):
        if sharp(m,metric)!=m or product(m,m)!=m:raise ValueError('Operation is not a metric-orthogonal projector')
    N=product(G,L)
    if product(L,G)!=N:raise ValueError('Local and alignment operations do not commute')
    # Commuting projector theorem gives N*=N=N²; verify product independently.
    if sharp(N,metric)!=N or product(N,N)!=N:raise AssertionError('Return projector failure')
    H=plus(scaled(A(2),I),scaled(A(-1),L),scaled(A(-1),G))
    defect=plus(L,scaled(A(-1),I));other=plus(G,scaled(A(-1),I))
    if plus(product(sharp(defect,metric),defect),product(sharp(other,metric),other))!=H:raise AssertionError('Defect-energy identity')
    if product(H,N):raise AssertionError('Nonzero return constraint energy')
    # Four orthogonal joint sectors, from the proven commuting projections.
    joint=[N,plus(L,scaled(A(-1),N)),plus(G,scaled(A(-1),N)),plus(I,scaled(A(-1),L),scaled(A(-1),G),N)]
    ranks=list(map(integer_trace,joint))
    if any(r<0 for r in ranks) or sum(ranks)!=n:raise AssertionError('Invalid joint dimensions')
    supports=list(map(len,(L,G,N)))
    result={'schema':'marici.metric-coefficient-assembly.v1','source':source,
            'operators':{'L':encode(L),'G':encode(G),'N':encode(N),'H_in_pi_over_four_units':encode(H)},
            'measures':{'raw_complex_coordinates':n,'local_rank':integer_trace(L),'alignment_rank':integer_trace(G),'return_rank':ranks[0],
                        'stage_transfer_supports':supports,'protocol_transfer_count':sum(supports),
                        'constraint_energy_on_return':'0','constraint_spectrum_in_pi_over_four_units':{'0':ranks[0],'1':ranks[1]+ranks[2],'2':ranks[3]},
                        'constraint_energy_trace_in_pi_over_four_units':tr(H).record(),
                        'physical_mass':None,'physical_energy_scale':None},
            'energy_rule':'H=(pi/4)[(L-I)^sharp(L-I)+(G-I)^sharp(G-I)]; N is derived feedback, not a third energy defect',
            'scope':'One exact protocol constructor on declared local/alignment projections. No particle-dependent weights, rest-energy offset or mass conversion.'}
    assert read_operator(result['operators']['N'],n)==N
    return result
