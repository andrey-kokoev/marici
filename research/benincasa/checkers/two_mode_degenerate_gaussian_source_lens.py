"""Exact two-mode degenerate-frequency Gaussian source-lens audit."""
import json
from fractions import Fraction as Q
from pathlib import Path

def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def tr(a):return [list(x) for x in zip(*a)]
def add(a,b):return [[a[i][j]+b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
def scale(q,a):return [[q*x for x in row] for row in a]
def diag(x):return [[x[i] if i==j else Q(0) for j in range(len(x))] for i in range(len(x))]
def inv_diag(x):return diag([1/q for q in x])

j2=[[Q(0),Q(1)],[Q(-1),Q(0)]]
omega=[[Q(0) for _ in range(4)] for _ in range(4)]
for block in (0,2):
    for i in range(2):
        for j in range(2):omega[block+i][block+j]=j2[i][j]

s=diag([Q(2),Q(1,2),Q(3),Q(1,3)])
si=inv_diag([Q(2),Q(1,2),Q(3),Q(1,3)])
freq=Q(7)
h=mm(tr(si),mm(scale(freq,diag([Q(1)]*4)),si))
v=scale(Q(1,2),mm(s,tr(s)))

# Rational U(2) stabilizer: a mode rotation tensored with the phase-space I_2.
co,ss=Q(3,5),Q(4,5)
k=[[Q(0) for _ in range(4)] for _ in range(4)]
for i in range(2):
    k[i][i]=co;k[i][i+2]=ss;k[i+2][i]=-ss;k[i+2][i+2]=co
sp=mm(s,k)
hp=mm(tr(mm(tr(k),si)),mm(scale(freq,diag([Q(1)]*4)),mm(tr(k),si)))
vp=scale(Q(1,2),mm(sp,tr(sp)))

assert mm(tr(k),k)==diag([Q(1)]*4)
assert mm(tr(k),mm(omega,k))==omega
assert hp==h and vp==v and sp!=s
a=mm(omega,h)
assert add(mm(a,v),mm(v,tr(a)))==[[Q(0)]*4 for _ in range(4)]

packet={'schema':'marici.two-mode-degenerate-gaussian-source-lens.v1','degenerate_frequency':str(freq),'source_h':[[str(x) for x in row] for row in h],'frame_s':[[str(x) for x in row] for row in s],'stabilizer_k':[[str(x) for x in row] for row in k],'alternate_frame_sk':[[str(x) for x in row] for row in sp],'same_hamiltonian':hp==h,'same_covariance':vp==v,'selected_covariance':[[str(x) for x in row] for row in v],'stationarity':True,'conclusion':'Degenerate Williamson frames form a U(2) gauge orbit, but the source-selected covariance is unique and frame-independent.'}
out=Path(__file__).parent/'results'/'two-mode-degenerate-gaussian-source-lens.json';out.write_text(json.dumps(packet,indent=2)+'\n')
print(json.dumps(packet,indent=2))
