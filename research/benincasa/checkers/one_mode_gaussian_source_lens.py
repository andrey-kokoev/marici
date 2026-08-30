"""Exact smallest-rank Gaussian source-lens selector audit."""
import json
from fractions import Fraction as Q
from pathlib import Path

def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def tr(a):return [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]
def add(a,b):return [[a[i][j]+b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
def det2(a):return a[0][0]*a[1][1]-a[0][1]*a[1][0]

omega=[[Q(0),Q(1)],[Q(-1),Q(0)]]
h=[[Q(5),Q(1)],[Q(1),Q(2)]]
delta=det2(h);sqrt_delta=Q(3)
hinv=[[h[1][1]/delta,-h[0][1]/delta],[-h[1][0]/delta,h[0][0]/delta]]
v=[[sqrt_delta*x/2 for x in row] for row in hinv]
a=mm(omega,h)
stationarity=add(mm(a,v),mm(v,tr(a)))
j=[[x/sqrt_delta for x in row] for row in a]
assert mm(j,j)==[[Q(-1),Q(0)],[Q(0),Q(-1)]]
assert stationarity==[[Q(0),Q(0)],[Q(0),Q(0)]]
assert det2(v)==Q(1,4)

# Two distinct pure positive covariances show nonselection before h is frozen.
v1=[[Q(1,2),Q(0)],[Q(0),Q(1,2)]]
v2=[[Q(1),Q(0)],[Q(0),Q(1,4)]]
assert det2(v1)==det2(v2)==Q(1,4) and v1!=v2

packet={'schema':'marici.one-mode-gaussian-source-lens.v1','unselected_pure_packets':[[[str(x) for x in row] for row in w] for w in (v1,v2)],'source_h':[[str(x) for x in row] for row in h],'det_h':str(delta),'selected_complex_structure':[[str(x) for x in row] for row in j],'selected_covariance':[[str(x) for x in row] for row in v],'stationarity_residual':[[str(x) for x in row] for row in stationarity],'purity_det':str(det2(v)),'uniqueness_derivation':['c*x+b*z=0','a*z+c*y=0','b*y-a*x=0','det(V)=1/4 and V>0 fixes the positive scale'],'scale_invariance':'V_{lambda h}=V_h for lambda>0','conclusion':'Symplectic Carrier data leaves compatible-complex-structure moduli; a positive quadratic source Hamiltonian uniquely selects the vacuum covariance lens up to its irrelevant positive scale.'}
out=Path(__file__).parent/'results'/'one-mode-gaussian-source-lens.json';out.write_text(json.dumps(packet,indent=2)+'\n')
print(json.dumps(packet,indent=2))
