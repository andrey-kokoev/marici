"""Exact zero-frequency Gaussian source-lens obstruction."""
import json
from fractions import Fraction as Q
from pathlib import Path

def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def tr(a):return [list(x) for x in zip(*a)]
def add(a,b):return [[a[i][j]+b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

omega=[[Q(0),Q(1)],[Q(-1),Q(0)]]
h0=[[Q(0),Q(0)],[Q(0),Q(1)]]
a0=mm(omega,h0)
# For V=[[x,z],[z,y]], stationarity gives [[2z,y],[y,0]]=0.
# Hence z=y=0 and det(V)=0: no finite positive pure stationary covariance.
stationarity_coefficients={'(1,1)':'2 z','(1,2)':'y','(2,1)':'y','(2,2)':'0'}

def regulated(eps,c=Q(1)):
    # h=diag((c eps)^2,1), sqrt(det h)=c eps.
    return [[Q(1)/(2*c*eps),Q(0)],[Q(0),c*eps/2]]

rows=[]
for eps in (Q(1,10),Q(1,100),Q(1,1000)):
    v=regulated(eps)
    assert v[0][0]*v[1][1]==Q(1,4)
    rows.append({'epsilon':str(eps),'V':[[str(x) for x in row] for row in v]})
v_c1=regulated(Q(1,100),Q(1));v_c2=regulated(Q(1,100),Q(2))
assert v_c1!=v_c2

packet={'schema':'marici.zero-mode-gaussian-source-lens.v1','semidefinite_h':[[str(x) for x in row] for row in h0],'stationarity_equations':stationarity_coefficients,'finite_stationary_pure_covariance_exists':False,'regulated_family':rows,'two_regulator_normalizations':{'c=1':[[str(x) for x in row] for row in v_c1],'c=2':[[str(x) for x in row] for row in v_c2]},'projective_boundary_ray':'[V_qq:V_pp]=[1:0] after compactification','affine_normalization_is_regulator_dependent':True,'support_classification':'existing zero-frequency/soft support; boundary coefficient object required; no new Carrier incidence','conclusion':'The source Hamiltonian selects no finite vacuum lens on its zero-mode kernel. It selects only a projective infinite-squeezing boundary direction; an affine covariance requires independent infrared source data.'}
out=Path(__file__).parent/'results'/'zero-mode-gaussian-source-lens.json';out.write_text(json.dumps(packet,indent=2)+'\n')
print(json.dumps(packet,indent=2))
