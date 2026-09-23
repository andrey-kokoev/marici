"""An admitted n=8 CZ fibre has a genuinely curved positive boundary slice."""
from fractions import Fraction as Q
from pathlib import Path
import json,itertools
ROOT=Path(__file__).resolve().parents[3];N=ROOT/'research/nima/results'
Z=[[Q(j**d) for d in range(6)] for j in range(1,9)]
assert all(__import__('math').prod(j-i for i,j in itertools.combinations(ids,2))>0
           for ids in itertools.combinations(range(1,9),6))
k0=(1,-6,15,-20,15,-6,1,0);k1=(0,1,-6,15,-20,15,-6,1)
assert all(sum(k[r]*Z[r][d] for r in range(8))==0 for k in (k0,k1) for d in range(6))
assert k0!=k1
x=[Q(1)]*8;y=list(map(Q,[1,1,2,3,4,5,6,7]))
def matrix(a,b):return [x[i]+a*k0[i] for i in range(8)],[y[i]+b*k1[i] for i in range(8)]
def minor(X,Y,i,j):return X[i]*Y[j]-X[j]*Y[i]
def check(a,b,boundary):
 X,Y=matrix(a,b);m={(i,j):minor(X,Y,i,j) for i,j in itertools.combinations(range(8),2)}
 assert all(v>0 for p,v in m.items() if p!=(0,1))
 assert (m[(0,1)]==0) if boundary else (m[(0,1)]>0)
 assert all(sum(X[i]*Z[i][d] for i in range(8))==sum(x[i]*Z[i][d] for i in range(8)) for d in range(6))
 assert all(sum(Y[i]*Z[i][d] for i in range(8))==sum(y[i]*Z[i][d] for i in range(8)) for d in range(6))
 return min(v for p,v in m.items() if p!=(0,1))
# Delta12(a,b)=7a+b+ab, giving a genuine hyperbola b=-7a/(1+a).
a1,a2=Q(1,10000),Q(2,10000);b1,b2=(-7*a/(1+a) for a in (a1,a2))
assert minor(*matrix(Q(0),Q(0)),0,1)==0
margin1=check(a1,b1,True);margin2=check(a2,b2,True)
strict_margin=check(Q(0),Q(1,10000),False)
am,bm=(a1+a2)/2,(b1+b2)/2
mid=minor(*matrix(am,bm),0,1);assert mid!=0
# Entire neighbourhood has all other minors >0 by strict inequalities at
# (0,0); hence the local boundary is the NONLINEAR hyperbola, not a facet.
# Its second derivative is +14/(1+a)^3, nonzero near zero.
assert min(minor(*matrix(Q(0),Q(0)),i,j) for i,j in itertools.combinations(range(8),2) if (i,j)!=(0,1))>0
result={'schema':'marici.nima.eight-point-fibre-curvature.v1','passed':True,
 'source':'C first row all ones; second row (1,1,2,3,4,5,6,7)',
 'kernel_generators':[list(k0),list(k1)],
 'two_parameter_slice':'C(a,b)=C+[a*k0; b*k1], all other kernel coordinates fixed',
 'ordered_minor_12':'7a+b+ab','boundary_function':'b=-7a/(1+a)',
 'boundary_points':[[str(a1),str(b1)],[str(a2),str(b2)]],
 'strict_other_minor_margins':[str(margin1),str(margin2)],
 'strictly_positive_lift':{'a':'0','b':'1/10000','other_minor_margin':str(strict_margin)},
 'boundary_midpoint_minor_12':str(mid),
 'theorem':'The fixed target is admitted by a strictly positive source, yet its rank-two 8-point positive CZ fibre has a two-dimensional affine slice whose boundary is locally a nonstraight analytic curve; the full fibre is not polyhedral.',
 'scope':'Fixed positive moment-curve Z, n=8 and rank-two source. Does not rule out other nonpolyhedral or semialgebraic arbitrary-n certificate methods.'}
(N/'eight-point-fibre-curvature.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
