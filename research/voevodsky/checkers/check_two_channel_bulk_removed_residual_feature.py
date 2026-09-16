"""Exact finite regular-carrier model of the two-channel bulk projection and residual."""
import json,sys
from pathlib import Path
try:
 import sympy as s
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import sympy as s
N=4;Vin=2;Vann=2
def shift(k):
 M=s.zeros(N)
 for j in range(N):M[(j+k)%N,j]=1
 return M
basis=[shift(k) for k in range(N)]
Pin=s.diag(1,1,0,0);Pann=s.diag(0,0,1,1);Q=s.diag(1,0,1,0)
def vec(M):return s.Matrix(list(M))
# Each shift has normalized Plancherel norm one; right compression has HS norm sqrt(V).
def embed(B,P,V):return vec(B*P)/s.sqrt(V)
# Orthogonal two-copy bulk embedding into a two-channel matrix target.
cols=[]
for B in basis:cols.append(embed(B,Pin,Vin).col_join(s.zeros(N*N,1)))
for B in basis:cols.append(s.zeros(N*N,1).col_join(embed(B,Pann,Vann)))
J=s.Matrix.hstack(*cols);Pi=s.simplify(J*J.T)
A1=basis[0]+2*basis[1]-basis[3];A2=2*basis[0]-basis[2]
def feature(A):return vec(Q*Pin*A).col_join(vec(Q*Pann*A))
T1=feature(A1);T2=feature(A2);Y1=s.simplify((s.eye(2*N*N)-Pi)*T1);Y2=s.simplify((s.eye(2*N*N)-Pi)*T2)
G=s.Matrix([[Y1.dot(Y1),Y1.dot(Y2)],[Y2.dot(Y1),Y2.dot(Y2)]])
checks={'bulk_embedding_isometry':s.simplify(J.T*J)==s.eye(2*N),'bulk_projection_idempotent':s.simplify(Pi*Pi)==Pi,'residual_orthogonal_to_bulk_1':s.simplify(J.T*Y1)==s.zeros(2*N,1),'residual_orthogonal_to_bulk_2':s.simplify(J.T*Y2)==s.zeros(2*N,1),'pythagoras_1':s.simplify(T1.dot(T1)-(Pi*T1).dot(Pi*T1)-Y1.dot(Y1))==0,'pythagoras_2':s.simplify(T2.dot(T2)-(Pi*T2).dot(Pi*T2)-Y2.dot(Y2))==0,'residual_gram_positive':all(x>=0 for x in [G[0,0],G.det()])}
out={'schema':'marici.voevodsky.two-channel-bulk-removed-residual-feature.v1','group':'cyclic regular carrier C4','inner_volume':Vin,'annular_volume':Vann,'bulk_domain_dimension':2*N,'target_dimension':2*N*N,'residual_gram':[[str(x) for x in row] for row in G.tolist()],'residual_ranks':{'feature_span':s.Matrix.hstack(Y1,Y2).rank(),'gram':G.rank()},'checks':checks,'all_exact':all(checks.values()),'meaning':'The channelwise right-compression isometry defines an explicit orthogonal projection, and Y=(I-Pi)T is a positive packet-independent residual feature on the finite regular carrier.','claim_boundary':'Finite cyclic regular model. Semilocal transport through spectral multiplicity and regulator-limit estimates remain analytic.'}
if __name__=='__main__':
 p=Path(__file__).parents[1]/'results'/'two-channel-bulk-removed-residual-feature.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
