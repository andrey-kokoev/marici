"""Finite graph-lift fixtures; completion bounds are in the companion proof."""
from pathlib import Path
import json
import sympy as s
I=s.I
E=s.Matrix([[1,0],[0,1],[0,0],[0,0]])
A=s.Matrix([[2,I,1,2*I],[-I,3,1-I,2],[1,1+I,4,I],[-2*I,2,-I,5]])
assert A==A.H
B=s.Matrix([[1,I],[2,1]])
J=s.Matrix([[0,1],[1,0]])
C=-E.H*A*E+B.H*J*B
K=s.Matrix([[I,2],[-2,-I]])
L=C/2+K
assert L+L.H==C
# Coordinates are u(2),v(2),full Tate response(4),endpoint(2).
G=s.zeros(10,4)
G[:4,:4]=s.eye(4)
G[4:8,:2]=A*E
G[8:10,:2]=B
R=s.zeros(4,10);R[:4,:4]=s.eye(4)
assert R*G==s.eye(4)
Q=s.zeros(10)
Q[:2,2:4]=s.eye(2);Q[2:4,:2]=s.eye(2)
Q[:2,4:8]=-E.H/2;Q[4:8,:2]=-E/2
Q[8:10,8:10]=J
Qres=s.zeros(4);Qres[:2,:2]=C
Qres[:2,2:4]=s.eye(2);Qres[2:4,:2]=s.eye(2)
assert G.H*Q*G==Qres
# The old even/moment data are only changed triangularly, not refitted.
Tri=s.eye(4);Tri[2:4,:2]=-L
Swap=s.zeros(4);Swap[:2,2:4]=s.eye(2);Swap[2:4,:2]=s.eye(2)
assert Tri.H*Qres*Tri==Swap
GG=s.kronecker_product(G,G)
tensor_defect=GG.H*s.kronecker_product(Q,Q)*GG-s.kronecker_product(Qres,Qres)
assert tensor_defect.applyfunc(s.simplify)==s.zeros(16)
# The negative response is nonzero and retained, though positive pairing
# sees only the compressed part. No assertion of invariance is made.
leak=(A*E)[2:4,:]
assert leak.rank()==2
# Linear source diamond and cut telescoping survive the actual graph map.
a=s.Matrix([1,I,2,0]);b=s.Matrix([0,1,I,3]);c=s.Matrix([2,0,1,-I])
assert (G*a+G*(b+c)-G*(a+b)-G*c).applyfunc(s.simplify)==s.zeros(10,1)
assert (G*(a-b)+G*(b-c)-G*(a-c)).applyfunc(s.simplify)==s.zeros(10,1)
# A graph isomorphism preserves any selected two-sector observation.
x1=Tri*a;x2=Tri*b;o=s.Matrix([1,I,2,-1])
old=(x2.H*Qres*o-x1.H*Qres*o)[0]
new=((G*x2).H*Q*(G*o)-(G*x1).H*Q*(G*o))[0]
assert s.simplify(old-new)==0
result={'passed':True,'checks':{'nonreal_hermitian_graph_pullback':True,
 'retained_input_retraction':True,'even_moment_triangular_identity':True,
 'two_slot_paired_tensor_identity':True,'nonzero_leakage_retained':True,
 'source_diamond_and_refinement':True,'two_sector_observer_transport':True},
 'scope':'Finite rigged-response graph algebra. Actual balanced source descent and nonzero witness are transported by the proved coefficient-complex graph isomorphism; their owning checkers are rerun separately. No unweighted L2 or output-only equivalence.'}
ROOT=Path(__file__).resolve().parents[3]
out=ROOT/'research/voevodsky/results/rigged-residual-attachment-lift.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
