"""One endpoint-rotor charging rule on metric source hopping graphs.

G_i=n_i+(S ell)_i-q N_i; physical n=q e_i-S ell, sum ell=q.
Use graph-derived internal resistance L^+, retained leads, and zero vacuum.
No species dispatch or independently assigned rest offsets.
"""
from fractions import Fraction as F
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/voevodsky/checkers'))
from check_belt_interface_response import inverse


def matmul(a,b):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def quadratic(R,x):return sum(x[i]*R[i][j]*x[j] for i in range(len(x)) for j in range(len(x)))


def geometry(count,edges,ports):
    if count<2 or not ports or any(not 0<=a<count for a in ports):raise ValueError('Invalid endpoint graph')
    L=[[F(0) for _ in range(count)] for _ in range(count)]
    for a,b in edges:
        if a==b or not 0<=a<count or not 0<=b<count:raise ValueError('Invalid internal edge')
        L[a][a]+=1;L[b][b]+=1;L[a][b]-=1;L[b][a]-=1
    # Invertibility here requires connectedness, not added hidden links.
    J=[[F(1,count) for _ in range(count)] for _ in range(count)]
    inv=inverse([[L[i][j]+J[i][j] for j in range(count)] for i in range(count)])
    R=[[inv[i][j]-J[i][j] for j in range(count)] for i in range(count)]
    P=[[F(i==j)-J[i][j] for j in range(count)] for i in range(count)]
    assert matmul(L,R)==matmul(R,L)==P
    assert all(sum(row)==0 for row in R)
    return {'dimension':count,'edges':edges,'ports':ports,'laplacian':L,'resistance':R}


def block_diagonal(graph,charge,flux,beta,eta):
    q=F(charge);beta,eta=F(beta),F(eta)
    if q.denominator!=1 or beta<=0 or eta<0:raise ValueError('Invalid charge or shared coefficients')
    if len(flux)!=len(graph['ports']) or any(F(x).denominator!=1 for x in flux) or sum(flux)!=q:raise ValueError('Flux violates signed charge sector')
    count=graph['dimension'];attached=[F(0)]*count
    for port,value in zip(graph['ports'],flux):attached[port]+=value
    shifts=[]
    for i in range(count):
        n=[q*int(i==j)-attached[j] for j in range(count)]
        assert sum(n)==0
        # Internal electric field is the zero-circulation gradient solution.
        potential=[sum(R*x for R,x in zip(row,n)) for row in graph['resistance']]
        electric=[potential[b]-potential[a] for a,b in graph['edges']]
        divergence=[F(0)]*count
        for (a,b),value in zip(graph['edges'],electric):divergence[a]-=value;divergence[b]+=value
        assert divergence==n
        assert sum(x*x for x in electric)==quadratic(graph['resistance'],n)
        for j in range(count):
            moved=[n[k]+q*(int(k==j)-int(k==i)) for k in range(count)]
            assert moved==[q*int(k==j)-attached[k] for k in range(count)]
        shifts.append(beta*quadratic(graph['resistance'],n)/2+beta*sum(F(x)**2 for x in flux)/2+eta*q*q/2)
    return shifts
